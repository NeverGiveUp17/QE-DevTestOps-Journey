# create a list of test cases...
test_cases = [
    "Login",
    "Patient Registration",
    "Appointment",
    "Billing",
    "Logout"
]

# print all test cases before modification to the list
for test in test_cases:
    print(test) 

# Append "Insurance verification" test step
test_cases.append("Insurance verification")
print()
for test in test_cases:
    print(test)

# Insert "Doctor Login" at Index 1
test_cases.insert(1, "Doctor Login")
print()
for test in test_cases:
    print(test)

# Remove billing test case
test_cases.remove("Billing")
print()
for test in test_cases:
    print(test)

# Print total number of test cases
print(f"\nTotal test cases: {len(test_cases)}")

