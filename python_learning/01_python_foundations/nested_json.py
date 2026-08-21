import json
patient_json = '''
{
    "patients": [
        {
            "patient_id": "PAT001",
            "name": "Rahul",
            "status": "Active"
        },
        {
            "patient_id": "PAT002",
            "name": "Priya",
            "status": "Inactive"
        },
        {
            "patient_id": "PAT003",
            "name": "Anil",
            "status": "Active"
        }
    ]
}
'''

patient_data = json.loads(patient_json)
active_patients_count = 0
for patient in patient_data["patients"]:
    print(f"Patient ID: {patient['patient_id']}")
    if patient["status"] == "Active":
        active_patients_count += 1
print(f"Total number of active patients: {active_patients_count}")
