def first_n_even_numbers(n):
    """Generate the first n even numbers, starting from 0.

    Args:
        n (int): The number of even numbers to generate.

    Yields:
        int: The next even number in the sequence.
    """
    for i in range(n):
        yield i * 2
