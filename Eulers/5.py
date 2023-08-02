def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

if __name__ == "__main__":
    N = 20  # Replace this with the desired value of N
    answer = smallest_multiple(N)
    print("The smallest positive number divisible by all numbers from 1 to", N, "is:", answer)

