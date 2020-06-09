def factorial(n):
    try:
        start = 1
        fact = 1
        while start <= n:
            yield fact
            start = start + 1
            fact = fact * start
    except ValueError:
        return f"Wrong input"


for el in factorial(5):
    print(el)