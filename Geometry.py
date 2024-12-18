def print_mirrored_triangle(height):
    for i in range(height):
        # Print spaces
        print(' ' * (height - i - 1), end='')
        # Print asterisks
        print('*' * (i + 1))

# Get the height of the triangle from the user
try:
    height = int(input("Enter the height of the mirrored right-angled triangle: "))
    if height <= 0:
        print("Please enter a positive integer.")
    else:
        print_mirrored_triangle(height)
except ValueError:
    print("Invalid input! Please enter a positive integer.")