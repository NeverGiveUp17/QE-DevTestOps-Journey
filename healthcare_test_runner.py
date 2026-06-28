test_cases = [
    "Patient Registration",
    "Doctor Login",
    "Schedule Appointment",
    "Cancel Appointment",
    "Prescription Upload",
    "Lab Report Download",
    "Insurance Verification",
    "Patient Search",
    "Billing",
    "Logout"
]
test_case_number = 1
for test in test_cases:
    print(f"Running Test case {test_case_number}: ")
    print("Status = PASS")
    print("-----------------------------------------")
    test_case_number += 1

regression_cycle = int(input("How many regression cycles required: "))
for count in range(1, regression_cycle+1):
    print(f"Regression cycle {count} completed")