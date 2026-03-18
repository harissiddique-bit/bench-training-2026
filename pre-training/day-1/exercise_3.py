while True:
    try:
        num = int(input("Enter a number (1–12) to generate its multiplication table: "))
        if 1 <= num <= 12:
            break
        else:
            print("Number out of range. Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def print_table(n):
    print(f"\nMultiplication Table for {n}")
    print("-" * 22)
    for i in range(1, 13):
        print(f"{n:>2} x {i:>2} = {n*i:>3}")

print_table(num)

print("\nMultiplication Tables 1 to 12 ------------------\n")
for n in range(1, 13):
    print_table(n)