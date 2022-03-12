def arithmetic_arranger(problems, exectuion=False):
    # Limit check
    arranged_problems = str()
    nr_oper = len(problems)
    if nr_oper > 5:
        return "Error: Too many problems."
    num1 = list()
    op = list()
    num2 = list()

    for opp in problems:
        all = opp.split()
        # Error check
        if all[1] not in "+-":
            return "Error: Operator must be '+' or '-'."
        if not all[0].isdigit() or not all[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(all[0]) > 4 or len(all[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        num1.append(all[0])
        op.append(all[1])
        num2.append(all[2])
    # First number
    arranged_problems += " "
    for i in range(nr_oper):
        arranged_problems += " "
        if len(num1[i]) < len(num2[i]):
            for j in range(len(num2[i]) - len(num1[i])):
                arranged_problems += " "

        arranged_problems += num1[i]
        if i != nr_oper-1:
            arranged_problems += "     "
    arranged_problems +="\n"
   
    # Seconde an op
    for i in range(nr_oper):
        arranged_problems += op[i] +' '
        if len(num2[i]) < len(num1[i]):
            for j in range(len(num1[i]) - len(num2[i])):
                arranged_problems += " "

        arranged_problems += num2[i]
        if i != nr_oper-1:
            arranged_problems += "    "
    arranged_problems +="\n"

    # Line
    for i in range(nr_oper):
        length = 2 
        if len(num2[i]) > len(num1[i]):
            length += len(num2[i])
        else:
            length += len(num1[i])
        for j in range(length):
            arranged_problems+= "-"
        if i != nr_oper-1:
            arranged_problems += "    "
    
    # Calculations
    if exectuion == True:
        arranged_problems += "\n"
        for i in range(nr_oper):
            length = 2 
            if len(num2[i]) > len(num1[i]):
                length += len(num2[i])
            else:
                length += len(num1[i])
            if op[i] == '+':
                result = str(int(num1[i]) + int(num2[i]))
            else:
                result = str(int(num1[i]) - int(num2[i]))
            for j in range(length-len(result)):
                arranged_problems += " "
            arranged_problems += result
            if i != nr_oper-1:
                arranged_problems += "    "
            
    return arranged_problems

print(arithmetic_arranger(['55 + 64','23 - 5', '234 - 10']))