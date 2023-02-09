import numpy as np
from fractions import Fraction

# !----------
X = [(6, 6), (9, 10), (4, 11), (10, 5)]
float_threshold = 0             # all float
# float_threshold = 2             # controlled fractions
# float_threshold = 1000000000    # normal mode (with fractions)

# !------------


L = len(X[0])
K = 1
pt_count = len(X)

output_md = ''
def formatNumber(x, precision=4, asFloat=False, brackNeg=False):

    # precision = 4

    if type(x) == type(1):
        if x < 0 and brackNeg:
            return f"({x})"
        return x
    elif type(x) == type(Fraction(1,2)) and not asFloat:
        if x.denominator == 1:
            if x.numerator < 0 and brackNeg:
                return f"({x.numerator})"
            return x.numerator
        elif abs(x.numerator) <= float_threshold:
            if x.numerator < 0:
                        return f"-\\dfrac"+"{"+f"{-x.numerator}"+"}{"+f"{x.denominator}"+"}"
            return f"\\dfrac"+"{"+f"{x.numerator}"+"}{"+f"{x.denominator}"+"}"
    if round(float(x), precision) == 0:
        return 0
    if round(float(x), precision) < 0 and brackNeg:
        return f"({round(float(x), precision)})"
    return round(float(x), precision)
        
def write(x):
    global output_md
    output_md += x
def writeSection(x):
    write("\n"+"#"*2+f" **{x}**\n")
def writeEq(x, newline=False):
    global output_md
    temp = "$\\begin{aligned}"+x+"\\end{aligned}$"
    temp = temp.replace("\n", "")
    if newline:
        output_md += "\n" + temp + "\\\n" 
    else:
        output_md += "\n" + temp + "\n"
def writeMatrix(matrix, brackets="p", **kwargs):
    temp = ""
    temp += "\\begin{" + brackets +"matrix}"
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    for row in range(rows):
        temp += "".join([f"{formatNumber(matrix[row,column], **kwargs)}&" for column in range(columns)])[:-1]+"\\\\"
    temp += "\\end{" +brackets +"matrix}"
    return temp
def writePoint(x,**kwargs):
    return f"({formatNumber(x[0],**kwargs)},{formatNumber(x[1],**kwargs)})"
def writePointVert(x,**kwargs):
    x_vert = x.reshape(2,1)
    return writeMatrix(x_vert,"p",**kwargs)
def writePointTextVert(x1, x2):
    temp = ""
    temp += "\\begin{pmatrix}"
    for row in [x1, x2]:
        temp += row+"\\\\"
    temp += "\\end{pmatrix}"
    return temp


def writeColumnStart():
    write('<table border="0"><tr><td style="vertical-align:top">\n')
def writeColumnNext():
    write('</td>\n<td style="vertical-align:top">\n')
def writeColumnEnd():
    write('</td>\n</tr>\n</table>\n\n')

def writeMatrixStretch(stretch=2.0, renew=False):
    return "\\"+f"{'re' if renew else ''}"+"newcommand\\arraystretch{"+f"{stretch}"+"}"
# step 1
X = [tuple(map(lambda x: Fraction(x,1), x)) for x in X]
X = list(map(np.array, X))
X_mean = sum(X)/pt_count
X_prime = [x - X_mean for x in X]

formula_x_sum = "{" + "".join([f"{formatNumber(x[0], brackNeg=True)}+" for x in X])[:-1] + "}"
formula_y_sum = "{" + "".join([f"{formatNumber(x[1], brackNeg=True)}+" for x in X])[:-1] + "}"
writeSection("Step 1:")
writeEq(writeMatrixStretch()+"\\text{Mean vector} = "+ 
    writePointTextVert(f"\\dfrac{formula_x_sum}{pt_count}",f"\\dfrac{formula_y_sum}{pt_count}")
    +"="+writeMatrixStretch(1, True)+writePointVert(X_mean))
write("\n")
for x, x_prime in zip(X, X_prime):
    write(f"""For data ${writePoint(x)}$, difference from mean vector 
    $={writePointTextVert(f'{formatNumber(x[0],brackNeg=True)}-{formatNumber(X_mean[0],brackNeg=True)}',f'{formatNumber(x[1],brackNeg=True)}-{formatNumber(X_mean[1],brackNeg=True)}')} = {writePointVert(x_prime)}$  
        """)

# step 2
writeSection("Step 2:")
X_reshaped = [x.reshape(2,1) for x in X_prime]
X_big = np.concatenate(X_reshaped, axis=1)
covar = X_big @ X_big.T / pt_count

writeEq(f"Y={writeMatrix(X_big)}")
write("\n")
write(f"$\\Sigma={formatNumber(Fraction(1, pt_count))}YY^T={formatNumber(Fraction(1, pt_count))}{writeMatrix(X_big)}{writeMatrix(X_big.T)}"
    +writeMatrixStretch()+f"={writeMatrix(covar)}$")

# Step 3
def npmap(func, array):
    try:
        my_list = list(array)
        if type(my_list[0]) == np.ndarray:
            my_list = list(map(lambda x: npmap(func, x), my_list))
        else:
            my_list = list(map(func, my_list))
        return np.array(my_list)
    except Exception as e:
        print(e)
        return func(array)

einvalues, einvectors = np.linalg.eig(npmap(float, covar))
einvalues = npmap(lambda x: Fraction(x).limit_denominator(1000), einvalues)
print(einvalues)
print(einvectors)

print(einvalues[0], type(einvalues[0]))
writeSection("Step 3:")
temp = ""
temp += "\\begin{vmatrix}"
temp += f"{formatNumber(covar[0,0])}-\\lambda" +"&" +f"{formatNumber(covar[0,1])}" + "\\\\"
temp += f"{formatNumber(covar[1,0])}" +"&" +f"{formatNumber(covar[1,1])}-\\lambda" + "\\\\"
temp += "\\end{vmatrix}"
write("\n")
writeEq(writeMatrixStretch()+temp+"=0")
writeEq(f"""
\\left({formatNumber(covar[0,0])}-\\lambda\\right)\\left({formatNumber(covar[1,1])}-\\lambda\\right)
-\\left({formatNumber(covar[0,1])}\\right)\\left({formatNumber(covar[1,0])}\\right)=0
""")
write(f"\nSolving, we obtain the eigenvalues " +
    f"$\\lambda = {formatNumber(einvalues[0])}$ and "+
    f"$\\lambda = {formatNumber(einvalues[1])}$.")


einvecs = []
write("\n")
writeColumnStart()
for i, value in enumerate(einvalues):
    if i > 0:
        writeColumnNext()
    vec = einvectors[:, i]
    einvecs.append(vec)
    x2_ratio = Fraction(vec[0]/vec[1]).limit_denominator(10000)
    temp = ""
    temp += "\\begin{pmatrix}"
    temp += f"{formatNumber(covar[0,0])}-{formatNumber(value)}" +"&" +f"{formatNumber(covar[0,1])}" + "\\\\"
    temp += f"{formatNumber(covar[1,0])}" +"&" +f"{formatNumber(covar[1,1])}-{formatNumber(value)}" + "\\\\"
    temp += "\\end{pmatrix}"
    minus_matrix = npmap(Fraction, covar-value*np.identity(2))
    write(f"\nFor $\\lambda = {formatNumber(value)}$,  \n  ")
    writeEq(f"""
    {writeMatrixStretch()}{temp}{writeMatrixStretch(1, True)}{writePointTextVert("x_1", "x_2")}={writePointTextVert("0", "0")}\\\\
    {writeMatrixStretch(2.4)}{writeMatrix(minus_matrix)}{writeMatrixStretch(1, True)}{writePointTextVert("x_1", "x_2")}={writePointTextVert("0", "0")}\\\\
    {writeMatrixStretch(1)}{writeMatrix(minus_matrix/minus_matrix[0,0])}{writeMatrixStretch(1, True)}{writePointTextVert("x_1", "x_2")}={writePointTextVert("0", "0")}\\\\
    x_1={"-" if x2_ratio == -1 else "" if x2_ratio == 1 else formatNumber(x2_ratio)}x_2
    """
    )
    write(f"\nChoosing the eigenvector with unit length, we have ${writePointTextVert('x_1', 'x_2')}={writePointVert(vec)}$.")
writeColumnEnd()

einvec_sorted = [x for _, x in sorted(zip(list(einvalues), list(einvecs)))][::-1]
einvec_sorted = [x.reshape(2, 1) for x in einvec_sorted]
phi = np.concatenate(einvec_sorted, axis=1)
writeSection("Step 4:")
writeEq(f"\\Phi={writeMatrix(phi)}")

writeSection("Step 5:")
writeEq(f"Y=\\Phi^TX={writeMatrix(phi.T)}X")

write("\n")
Y = []
for x, x_prime in zip(X, X_prime):
    y = (phi.T @ x)
    Y.append(y)
    write(f"""For data ${writePoint(x)}$, 
    $Y=\\Phi^TX={writeMatrix(phi.T)}{writePointVert(x)}={writePointVert(y)}$  
        """)
    

Y_mean = sum(Y)/pt_count
Y_prime = [y - Y_mean for y in Y]
formula_x_sum = "{" + "".join([f"{formatNumber(x[0], brackNeg=True)}+" for x in Y])[:-1] + "}"
formula_y_sum = "{" + "".join([f"{formatNumber(x[1], brackNeg=True)}+" for x in Y])[:-1] + "}"
writeEq(writeMatrixStretch()+"\\text{Mean vector} = "+ 
    writePointTextVert(f"\\dfrac{formula_x_sum}{pt_count}",f"\\dfrac{formula_y_sum}{pt_count}")
    +"="+writeMatrixStretch(1, True)+writePointVert(Y_mean))
write("\n")
for x, y, y_prime in zip(X, Y, Y_prime):
    write(f"""For data ${writePoint(x)}$, final transformed vector
    $={writePointTextVert(f'{formatNumber(y[0])}-{formatNumber(Y_mean[0],brackNeg=True)}',f'{formatNumber(y[1])}-{formatNumber(Y_mean[1],brackNeg=True)}')} = {writePointVert(y_prime)}$  
        """)

writeSection("Step 6:")
write(f"Thus,    \n  ")
for x, x_prime in zip(X, Y_prime):
    write(f"""${writePoint(x)}$ is reduced to $({formatNumber(x_prime[0])})${';' if x is not Y[-1] else '.'}   \n   """)
# print(X_big)
# print(X_big.T)
# print(covar)

# step 3




f = open('PCA.md', 'w')
f.write(output_md)
f.close()









