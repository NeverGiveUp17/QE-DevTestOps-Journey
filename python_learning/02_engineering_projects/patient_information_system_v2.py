"""
Project : Patient Information System
File    : patient_information_system_v2.py
Author  : Dathatreya Rao

Purpose:
Demonstrate professional use of Python dictionaries, functions,
and clean coding practices for managing patient information.

Concepts Covered:
- Dictionary
- Functions
- Single Responsibility Principle
- Dictionary Methods
- PEP 8 Naming

Quality Engineering Perspective:
Models patient data similar to healthcare applications and API responses.
"""

# define create_patient method and return patient dictionary
def create_patient():
    # define patient dictionary
    patient = {
    "name": "Dathatreya",
    "age": 42,
    "city": "Hyderabad"
    }
    return patient


# Display patient information
def display_patient(patient):
    for key, value in patient.items():
        print(f"{key}: {value}")

# update patient information
def update_patient(patient):
    patient.update(
        {
        "city": "Bangalore",
        "blood_group": "A positive"
    }
    )

def main():

    # create patient
    patient = create_patient()

    # print patient information before update
    print("\npatient information (before update)")
    print("-" * 40)
    display_patient(patient)

    # update patient
    update_patient(patient)

    # print patient information after update
    print("\npatient information (after update)")
    print("-" * 40)
    display_patient(patient)

if __name__ == "__main__":
    main()



    