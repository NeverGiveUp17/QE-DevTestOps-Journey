test_cases = [
    "Login",
    "Patient registration",
    "Appointment",
    "Billing",
    "Logout"
]

def display_test_cases(test_cases):
    for index, test_case in enumerate(test_cases, start=1):
        print(f"{index}. {test_case}")

def add_test_case(test_cases, new_test_case):
    test_cases.append(new_test_case)

def remove_test_case(test_cases, test_case):
    if test_case in test_cases:
        test_cases.remove()
