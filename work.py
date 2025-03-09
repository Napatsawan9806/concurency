import multiprocessing


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def calculate_fibonacci_numbers(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(fibonacci, numbers)
    return results


if __name__ == "__main__":
    numbers = [int(i) for i in input("Enter number :").split()]
    print(f"Calculating Fibonacci for: {numbers}")

    ans = calculate_fibonacci_numbers(numbers)

    print(f"Results: {ans}")
