def factorial(num):
    if num in {0, 1}:
        return 1
    else:
        return num * factorial(num - 1)
    

def factorial_tail(num, tail = 1):
    if num in {0, 1}:
        return tail
    else: 
        return factorial_tail(num - 1, tail * num)

print(factorial(10))
print(factorial_tail(10))

# 1000 hits the max recursion depth