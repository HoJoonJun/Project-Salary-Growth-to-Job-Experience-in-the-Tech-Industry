def sum_of_numbers(n):
    """
    Returns the sum of all numbers from 1 to n.
    
    Parameters:
    n (int): A positive integer.

    Returns:
    int: The sum of all numbers from 1 to n.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    return sum(range(1, n + 1))


# Example usage
if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        print(f"The sum of numbers from 1 to {num} is {sum_of_numbers(num)}")
    except ValueError as e:
        print(f"Error: {e}")