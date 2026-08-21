import json

patient_json = '{"patient_id": "PAT001", "patient_name": "Rahul", "is_active": "true"}'

patient_data = json.loads(patient_json)

print(patient_data)
print(patient_data["patient_id"])
print(patient_data["patient_name"])
print(patient_data.get("is_active"))