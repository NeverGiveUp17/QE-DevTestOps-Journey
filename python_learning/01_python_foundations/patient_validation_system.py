# Sample patient data
patients = [
    {
        "patient_id": "PAT1001",
        "status": "Active",
        "city": "Hyderabad"
    },
    {
        "patient_id": "PAT1002",
        "status": "Active",
        "city": "Bangalore"
    },
    {
        "patient_id": "PAT1003",
        "status": "Inactive",
        "city": "Hyderabad"
    }
]

#Scenario 1: In this case python first creates a list and compares
result = []
for patient in patients:
    result.append(patient.get("status") == "Active")
    
print(any(result))


#scenario 2: As soon as it identifies an Inactive it will come out of the loop. So, it saves memory
# check if ANY of the patient is Inactive
result = any(
    patient.get("status") == "Inactive"
    for patient in patients
)

# Define a function to identify the Inactive patient
def has_inactive_patient(patients):
    for patient in patients:
        if patient.get("status") == "Inactive":
            return True

    return False

if has_inactive_patient(patients):
    print("Inactive patient found")

