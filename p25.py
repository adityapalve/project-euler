def fibonacci_with_digit_count(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_with_digit_count(n-1, memo) + fibonacci_with_digit_count(n-2, memo)
    return memo[n]

def find_first_fib_with_x_digits(x):
    memo = {}
    i = 0
    while True:
        fib = fibonacci_with_digit_count(i, memo)
        if len(str(fib)) >= x:
            return i, fib
        i += 1

# Example usage
x = 1000  # We want to find the first Fibonacci number with 1000 digits
index, number = find_first_fib_with_x_digits(x)
print(index)