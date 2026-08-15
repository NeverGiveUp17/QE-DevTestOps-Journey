# Convert a value to an integer and return None if conversion fails.
def convert_to_integer(value):
    try:
        return int(value)
    except ValueError:
        return None


def main():
    result = convert_to_integer(input("Enter a number:"))
    if result is not None:
        print(f"Entered valid number is {result}.")
    else:
        print("please enter a valid number.")

if __name__ == "__main__":
    main()
