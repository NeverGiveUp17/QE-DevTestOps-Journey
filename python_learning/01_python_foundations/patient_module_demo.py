import patient_utils

patient = {
    "name": "Rahul",
    "status": "Active"
}

print(patient_utils.get_patient_name(patient))
print(patient_utils.is_active_patient(patient))