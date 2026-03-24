import multiprocessing


def calculate_square(n):
    """Function to square a number."""
    return n * n


if __name__ == "__main__":
    numbers = range(101)
    # Create a process pool using a context manager
    with multiprocessing.Pool(processes=3) as pool:
        # Distribute the square function across the numbers
        results = pool.map(calculate_square, numbers)

    print(results)
    # Output: [1, 4, 9, 16, 25]
