# Returns the patient name
def get_patient_name(patient):
    return patient.get("name")

# Returns if the patient is active or not
def is_active_patient(patient):
    return patient.get("status") == "Active"