import numpy as np
from math import ceil

# format:
#       x1  x2  x3
# (x1)  m11 m12 m13
# (x2)  m21 k22 m23
# (x3)  m31 m32 m33

# x y z
# 0 1 1
# 1 0 0
# 1 1 0

adj_matrix = """
x y z
0 1 0
1 0 0
1 1 0
""".split('\n')[1:-1]
max_iter = 100 - 1
dps = 3

names = adj_matrix[0].split()
count = len(names)
M = np.array([list(map(float, x.split())) for x in adj_matrix[1:]])
a = h = np.ones((count, 1))

output_md = ''

def formatNumber(x, precision=dps):

    if type(x) == type(1):
        return x
    else:
        if round(float(x), precision) == 0:
            return 0
        if int(x) == round(float(x), precision):
            return int(x)
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

def writeColumnStart():
    write('<table border="0"><tr><td style="vertical-align:center;text-align:center;">\n')
def writeColumnNext():
    write('</td>\n<td style="vertical-align:center;text-align:center;">\n')
def writeRowNext():
    write('</td>\n</tr>\n<tr>\n<td>\n')
def writeColumnEnd():
    write('</td>\n</tr>\n</table>\n\n')

top = ""
top += "\\begin{matrix}"
top += "".join(["\\text{"+name+"}&" for name in names])[:-1]+"\\\\"
top += "\\end{matrix}"

side = ""
side += "\\begin{matrix}"
for name in names:
    side += "\\text{"+name+"}\\\\"
side += "\\end{matrix}"

array = ""
array += "\\begin{matrix}"
array += "&"
array += "\\!\\!\\!\\!\\!\\!&" + top + "\\\\"
array += "&" + side
array += "\\!\\!\\!\\!\\!\\!&" + writeMatrix(M) + "\\\\"
array += "\\end{matrix}"
write("The adjacency matrix $M$ is\n\\")
writeEq(array)

#!h
write("  \n")
write(f"The hub scores are given by $h=MM^Th={writeMatrix(M@M.T)}h$. Initializing h by ${writeMatrix(h)}$ and by iteration, we obtain")

h_iter = [h] # ignore 0
h_prime_iter = [h]

h_iter_count = 0
while True:
    h_iter.append(M @ M.T @ h_prime_iter[-1])
    h_prime_iter.append(count / np.sum(h_iter[-1]) * h_iter[-1])
    h_iter_count += 1
    if h_iter_count >= max_iter or np.max(h_prime_iter[-1] - h_prime_iter[-2]) < 0.1**(dps+1):
        break
print(h_iter)
print(h_prime_iter)
print(h_iter_count)

n = [i for i in range(h_iter_count+1)]
n = [n[i*8:(i+1)*8] for i in range(ceil(len(n)/8))]

for section in n:
    writeColumnStart()
    write("Iteration")
    for i in section:
        writeColumnNext()
        write(f"{i+1}")
    writeRowNext()
    hside = ""
    hside += "\\begin{pmatrix}"
    for name in names:
        hside += "h(\\text{"+name+"})\\\\"
    hside += "\\end{pmatrix}"
    writeEq(hside)
    for i in section:
        writeColumnNext()
        writeEq(writeMatrix(h_iter[i]))
    writeRowNext()
    write("\n$h$   \n")
    write("Normalized")
    for i in section:
        writeColumnNext()
        writeEq(writeMatrix(h_prime_iter[i]))
    writeColumnEnd()

# ! a
write("  \n")
write(f"The authority scores are given by $a=M^TMa={writeMatrix(M.T@M)}a$. Initializing a by ${writeMatrix(h)}$ and by iteration, we obtain")

a_iter = [h] # ignore 0
a_prime_iter = [h]

a_iter_count = 0
while True:
    a_iter.append(M.T @ M @ a_prime_iter[-1])
    a_prime_iter.append(count / np.sum(a_iter[-1]) * a_iter[-1])
    a_iter_count += 1
    if a_iter_count >= max_iter or np.max(a_prime_iter[-1] - a_prime_iter[-2]) < 0.1**(dps+1):
        break
print(a_iter)
print(a_prime_iter)
print(a_iter_count)

n = [i for i in range(a_iter_count+1)]
n = [n[i*8:(i+1)*8] for i in range(ceil(len(n)/8))]

for section in n:
    writeColumnStart()
    write("Iteration")
    for i in section:
        writeColumnNext()
        write(f"{i+1}")
    writeRowNext()
    aside = ""
    aside += "\\begin{pmatrix}"
    for name in names:
        aside += "a(\\text{"+name+"})\\\\"
    aside += "\\end{pmatrix}"
    writeEq(aside)
    for i in section:
        writeColumnNext()
        writeEq(writeMatrix(a_iter[i]))
    writeRowNext()
    write("\n$a$   \n")
    write("Normalized")
    for i in section:
        writeColumnNext()
        writeEq(writeMatrix(a_prime_iter[i]))
    writeColumnEnd()


write("Summarizing, the hub scores are $" + hside + "=" + writeMatrix(h_prime_iter[-1]) + 
        "$ and the authority scores are $" + aside + "=" + writeMatrix(a_prime_iter[-1]) + 
        "$.")

f = open('HITS.md', 'w')
f.write(output_md)
f.close()


