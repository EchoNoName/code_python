import math

def addUncertainty(num1, num2):
    value = num1[0] + num2[0]
    uncert = num1[1] + num2[1]
    return value, uncert

def subUncertainty(num1, num2):
    value = num1[0] - num2[0]
    uncert = num1[1] + num2[1]
    return value, uncert

def multUncertainty(num1, num2):
    value = num1[0] * num2[0]
    uncert = value
    hold1 = num1[1] / num1[0]
    hold2 = num2[1] / num2[0]
    percent = hold1 + hold2
    uncert *= percent
    return value, uncert

def diviUncertainty(num1, num2):
    value = num1[0] / num2[0]
    uncert = value
    hold1 = num1[1] / num1[0]
    hold2 = num2[1] / num2[0]
    percent = hold1 + hold2
    uncert *= percent
    return value, uncert

def constantGetter(constantName):
    constants = {
        'pi': math.pi
    }
    return constants[constantName]

funcs = {
    '+': addUncertainty,
    '-': subUncertainty,
    '*': multUncertainty,
    '/': diviUncertainty
}
numOfVar = input('Enter the number of variables: ')
varDict = {}
for i in range(int(numOfVar)):
    var = input('Enter the varible name, # and uncertainty: ')
    var = var.split(' ')
    if var[0] == 'pi':
        vari = constantGetter(var[0])
        varDict[var[0]] = vari, 0
    elif var[0] == 'g':
        varDict['g'] = 9.81, 0
    elif var[0].isdigit():
        varDict[var[0]] = float(var[0]), 0
    else:
        varDict[var[0]] = float(var[1]), float(var[2])

varDict['ans'] = 0, 0
while True:
    oper = input('Enter the operation to perform: ')
    oper = oper.split('*')
    operation = '*'
    if len(oper) == 1:
        oper = ''.join(oper)
        oper = oper.split('/')
        operation = '/'
        if len(oper) == 1:
            oper = ''.join(oper)
            oper = oper.split('+')
            operation = '+'
            if len(oper) == 1:
                oper = ''.join(oper)
                oper = oper.split('-')
                operation = '-'
    if oper[0] == 'end':
        break
    else:
        varDict['ans'] = funcs[operation](varDict[oper[0]], varDict[oper[1]])
        print('Ans: ' + str(varDict['ans']))
print(varDict['ans'])