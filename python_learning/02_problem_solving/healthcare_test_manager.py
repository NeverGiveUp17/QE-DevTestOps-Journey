# Defining Function without parameters and return value
def welcome():
    print("Introduction to Functions topic")

# call the function
welcome()

# Defining function with parameters
def welcome_with_parameter(test_case):
    print(test_case)

# call the function
welcome_with_parameter("Login")
welcome_with_parameter("Logout")

# Defining a function with return values and parameters
def calculate_ctc(ctc):
    return ctc*0.20

new_ctc = calculate_ctc(20)
print(new_ctc)