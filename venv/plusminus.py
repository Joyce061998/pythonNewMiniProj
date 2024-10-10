def plusMinus(arr):
    # Initialize counters for positive, negative, and zero
    positive_count = 0
    negative_count = 0
    zero_count = 0
    n = len(arr)  # Number of elements in the array

    # Count positives, negatives, and zeros
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    # Calculate the ratios
    positive_ratio = positive_count / n
    negative_ratio = negative_count / n
    zero_ratio = zero_count / n

    # Print results with 6 decimal places
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


def main():
    # Get the size of the array from user
    n = int(input("Enter the number of elements in the array: "))

    # Get the array elements from user
    arr = list(map(int, input("Enter the elements of the array (space-separated): ").strip().split()))

    # Ensure the length of the input array matches 'n'
    if len(arr) != n:
        print(f"Error: You should enter exactly {n} elements.")
        return

    # Call the plusMinus function with the user input
    plusMinus(arr)


# Run the main function
if __name__ == "__main__":
    main()
