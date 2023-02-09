import math

records = """
1 170 90 Yes
2 190 95 No
3 160 50 No
4 180 70 No 
""".split('\n')[1:-1]
newRecord = ""
training_order = "1 2 3 4 1" # refers to list index + 1
recordID = True
# output_0, output_1 = "0", "1"
output_0, output_1 = "No", "Yes"
output_value_0, output_value_1 = -1, 1
# output_value_0, output_value_1 = 0, 1
activation_func_name = "tanh" # "threshold", "linear", "ReLU", "sigmoid", "tanh"
weights = [0.7, 0.7, 0.7]
learning_rate = 0.3
record_type = int

if recordID:
    records = [record.split()[1:] for record in records]
    newRecord = newRecord.split()
else:
    records = [record.split() for record in records]
    newRecord = newRecord.split()
records_attr = [list(map(record_type, record[:-1])) for record in records]
records_target = [(output_value_0 if record[-1]==output_0 else output_value_1 if record[-1]==output_1 else None) for record in records]
if None in records_target:
    raise Exception("wrong target attribute")
newRecord = list(map(record_type, newRecord))
attrCount = len(records_attr[0])
# check
newRecordFlag = 1
if (len(newRecord) != attrCount):
    print(f"new record has wrong no. of attributes! expected {attrCount} got {len(newRecord)}")
    newRecordFlag = 0
training_order = list(map(lambda x: int(x)-1, training_order.split()))
print(training_order)
# check
if (len(weights) != attrCount + 1):
    raise Exception(f"no. of weights incorrect! expected {attrCount + 1} got {len(weights)}")

def evaluate(record):
    return sum([rec_attr*weight for rec_attr, weight in zip(record, weights[:-1])]) + weights[-1]
    # calculates net

output_md = ''
def write(x):
    global output_md
    output_md += x
def writeEq(x, newline=False):
    global output_md
    temp = "$\\begin{aligned}"+x+"\\end{aligned}$"
    temp = temp.replace("\n", "")
    if newline:
        output_md += "\n" + temp + "\\\n" 
    else:
        output_md += "\n" + temp + "\n"

def writeColumnStart():
    write('<table border="0"><tr><td style="vertical-align:top">\n')
def writeColumnNext():
    write('</td>\n<td style="vertical-align:top">\n')
def writeColumnEnd():
    write('</td>\n</tr>\n</table>\n\n')

activation_func = {
    "threshold": lambda net: 1 if net>=0 else 0,
    "linear": lambda net: net,
    "ReLU": lambda net: 0 if net<0 else net,
    "sigmoid": lambda net: 1/(1+math.exp(-net)),
    "tanh": lambda net: math.tanh(net)
}[activation_func_name]

def formula_direct(net, y):
    writeEq(f"y={y}")
def formula_sigmoid(net, y):
    writeEq("y&=\\dfrac{1}{1+e^{-\\text{net}}}\\\\&=\\dfrac{1}{1+e^{"+f"{round(-net, 4)}"+"}}\\\\"+f"&={round(y,4)}")
def formula_tanh(net, y):
     writeEq("y&=\\tanh{(\\text{net})}\\\\"+f"&=\\tanh({round(net,4)})\\\\&={round(y,4)}")
formula_activation = {
    "threshold": formula_direct,
    "linear": formula_direct,
    "ReLU": formula_direct,
    "sigmoid": formula_sigmoid,
    "tanh": formula_tanh
}[activation_func_name]

formula_net = "".join([f"w_{i+1}x_{i+1}+" for i in range(attrCount)])+"b"
def formula_weight(i):
    return  f"w_{i}&\\leftarrow w_{i}+\\alpha(d-y)x_{i}"
formula_bias = f"b&\leftarrow b+\\alpha(d-y)"

print(weights)
write("Initially,  \n")
write(
    "".join([f"|$w_{i+1}$" for i in range(attrCount)])+"|$b$|\n"+
    "|:-:"*attrCount+"|:-:|\n"+
    "".join([f"|${round(weight, 4)}$" for weight in weights])+"|\n"
)
for iteration, record_id in enumerate(training_order):
    net = evaluate(records_attr[record_id])
    y = activation_func(net)
    prevWeights = weights
    weights = [weight + 
        learning_rate*(records_target[record_id] - y)*x
        for weight, x in zip(weights, records_attr[record_id] + [1])]
    
    write("#"*2+f" **Iteration {iteration + 1}**\n")
    writeColumnStart()
    writeEq(f"""
    ({"".join([f"x_{i+1}," for i in range(attrCount)])}d) = ({"".join([f"{i}," for i in records_attr[record_id]])}{records_target[record_id]})
    """)
    writeEq(f"""
    \\text""" + "{net}" + f""" &=  {formula_net} \\\\
                 &=  """ + "".join([f"{round(weight, 4)}"+"\\"+f"times{attr}+" for weight,attr in zip(prevWeights[:-1], records_attr[record_id])]) + f""" {round(prevWeights[-1], 4)} \\\\
                 &=  {round(net, 4)}
    """)
    formula_activation(net, y)
    if (records_target[record_id] == 1 and y >= 0.5) or (records_target[record_id] == 0 and y < 0.5):
        write("\nCorrect!\n")
    else:
        write("\nIncorrect!\n")
    writeColumnNext()
    for i in range(attrCount):
        writeEq(
            formula_weight(i+1)
            +f""" \\\\
            &={round(prevWeights[i], 4)}+{learning_rate}\\times({records_target[record_id]}-
            {y if type(y)==type(1) else round(y, 4)})\\times{records_attr[record_id][i]} \\\\
            &={round(weights[i], 4)}
            """
        )
    writeEq(
        formula_bias
        +f""" \\\\
        &={round(prevWeights[-1], 4)}+{learning_rate}\\times({records_target[record_id]}-
        {y if type(y)==type(1) else round(y, 4)}) \\\\
        &={round(weights[-1], 4)}
        """
    )
    writeColumnEnd()
    write(
        "".join([f"|$w_{i+1}$" for i in range(attrCount)])+"|$b$|\n"+
        "|:-:"*attrCount+"|:-:|\n"+
        "".join([f"|${round(weight, 4)}$" for weight in weights])+"|\n"
    )


    print(net)
    print(y)
    print(weights)

if newRecordFlag:
    print(evaluate(newRecord))
    y = evaluate(newRecord)
    net = activation_func(y)
    write("#"*2+f" **New Record**\n")
    writeEq(f"""
    ({"".join([f"x_{i+1}," for i in range(attrCount)])[:-1]}) = ({"".join([f"{i}," for i in newRecord])[:-1]})
    """)
    writeEq(f"""
    \\text""" + "{net}" + f""" &=  {formula_net} \\\\
                    &=  """ + "".join([f"{round(weight, 4)}"+"\\"+f"times{attr}+" for weight,attr in zip(weights[:-1], newRecord)]) + f""" {round(weights[-1], 4)} \\\\
                    &=  {round(net, 4)}
    """)
    formula_activation(net, y)

f = open('neuralNetwork.md', 'w')
f.write(output_md)
f.close()








