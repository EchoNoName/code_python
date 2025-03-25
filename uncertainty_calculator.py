import math

def addUncertainty(num1, num2):
    value = num1[0] + num2[0]
    uncert = num1[1] + num2[1]
    return value, uncert

def subUncertainty(num1, num2):
    value = num1[0] + num2[0]
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

operation = input('Enter the operation: ')
if operation == '^2':
    firstNum = input('Enter the first number and its uncertainty')
    firstNum = firstNum.split(' ')
    firstNum[0] = float(firstNum[0])
    firstNum[1] = float(firstNum[1])
    print(multUncertainty(firstNum, firstNum))
else:
    firstNum = input('Enter the first number and its uncertainty: ')
    secondNum = input('Enter the second number and its uncertainty: ')
    firstNum = firstNum.split(' ')
    firstNum[0] = float(firstNum[0])
    firstNum[1] = float(firstNum[1])
    secondNum = secondNum.split(' ')
    secondNum[0] = float(secondNum[0])
    secondNum[1] = float(secondNum[1])
    funcs = {
        '+': addUncertainty,
        '-': subUncertainty,
        '*': multUncertainty,
        '/': diviUncertainty
    }
    print(funcs[operation](firstNum, secondNum))
