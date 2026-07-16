# 1. Square of a Number
def square(n):
    return n * n

print("Square of 5:", square(5))


# 2. Even or Odd
def is_even(n):
    return "Even" if n % 2 == 0 else "Odd"

print("10 is:", is_even(10))
print("7 is:", is_even(7))


# 3. Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))


# 4. Sum of Digits
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print("Sum of digits of 123:", sum_digits(123))


# 5. Reverse String
def reverse_string(s):
    return s[::-1]

print("Reverse of 'hello':", reverse_string("hello"))


# 6. Check Prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))
print("Is 10 prime?", is_prime(10))


# 7. Fibonacci Series
def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

print("First 10 Fibonacci numbers:", fibonacci(10))


# 8. Greatest of Three Numbers
def greatest(a, b, c):
    return max(a, b, c)

print("Greatest among 10, 25, 7:", greatest(10, 25, 7))


# 9. Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

print("Is 'madam' palindrome?", is_palindrome("madam"))
print("Is 'hello' palindrome?", is_palindrome("hello"))


# 10. Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print("Number of vowels in 'education':", count_vowels("education"))
