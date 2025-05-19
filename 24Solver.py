import itertools

# Define the 4 basic operators
operators = ['+', '-', '*', '/']

def apply_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return None  # Avoid division by zero
        return a / b

def solve_24(numbers):
    # Try all orders of the numbers
    for num_perm in itertools.permutations(numbers):
        # Try all combinations of operators
        for ops in itertools.product(operators, repeat=3):
            # Now, try different ways to group operations
            a, b, c, d = num_perm

            expressions = [
                f"(({a} {ops[0]} {b}) {ops[1]} {c}) {ops[2]} {d}",
                f"({a} {ops[0]} ({b} {ops[1]} {c})) {ops[2]} {d}",
                f"({a} {ops[0]} {b}) {ops[1]} ({c} {ops[2]} {d})",
                f"{a} {ops[0]} (({b} {ops[1]} {c}) {ops[2]} {d})",
                f"{a} {ops[0]} ({b} {ops[1]} ({c} {ops[2]} {d}))"
            ]

            for expr in expressions:
                try:
                    if abs(eval(expr) - 24) < 1e-6:  # Allow small floating point errors
                        return expr
                except ZeroDivisionError:
                    continue
    return None

# Example usage:
numbers = list(map(int, input("Enter 4 numbers separated by space: ").split()))
result = solve_24(numbers)
if result:
    print("Solution:", result)
else:
    print("No solution found.")