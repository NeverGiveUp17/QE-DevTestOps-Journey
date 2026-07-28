# Sample patient data
patients = [
    {
        "patient_id": "PAT1001",
        "name": "Rahul",
        "city": "Hyderabad",
        "status": "Active"
    },
    {
        "patient_id": "PAT1002",
        "name": "Sneha",
        "city": "Chennai",
        "status": "Inactive"
    },
    {
        "patient_id": "PAT1003",
        "name": "Amit",
        "city": "Hyderabad",
        "status": "Active"
    }
]


# function to Identify active patients
def active_patients(patients):    
    active_patients = []
    for each_patent in patients:
        if each_patent.get("status") == "Active":
            active_patients.append(each_patent)
    return active_patients


# function to display patients information
def display_patients(patients):
    for each_patient in patients:
        for key, value in each_patient.items():
            print(f"{key}: {value}")
        print(f"-"*30)


def main():
    # Get list of active patients
    active_patients_list = active_patients(patients)

    # display active patients
    display_patients(active_patients_list)
        
if __name__ == "__main__":
    main() 