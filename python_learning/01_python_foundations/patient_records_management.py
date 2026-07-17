

# Method to create patients
def create_patients():
    # Create sample patient records
    patients = [
    {
        "patient_id": "PAT1001",
        "name": "Rahul",
        "city": "Hyderabad",
        "status": "Active"
    },
    {
        "patient_id": "PAT1002",
        "name": "Priya",
        "city": "Bangalore",
        "status": "Inactive"
    },
    {
        "patient_id": "PAT1003",
        "name": "Anil",
        "city": "Chennai",
        "status": "Active"
    }
    ]
    return patients

# Method to display all the patients information
def display_all_patients(patients):
    for index, patient in enumerate(patients, start=1):
        print(f"\npatient - {index} data")
        for key, value in patient.items():
            print (f"{key}: {value}")


# Method to Identify the active patients
def count_active_patients(patients):
    active_count = 0    
    for patient in patients:
        if patient.get("status") == "Active":
            active_count += 1            

    return active_count    
    
# Method to search a patient using patient id
def search_patient(patients, patient_id):
    for patient in patients:
        if patient.get("patient_id") == patient_id:
            return patient
        
    return None

def main():
    # get patients list
    patients = create_patients()

    # Display individual patient
    display_all_patients(patients)

    # search a patient
    patient = search_patient(patients, "PAT1002")

    if patient:
        for key, value in patient.items():            
            print(f"\n{key}: {value}")
    else:
        print("patient not found")

    # Active patients
    active_patients = count_active_patients(patients)

    print(f"\nTotal patients: {len(patients)}")
    print(f"\nActive patient: {active_patients}")

if __name__ == "__main__":
    main()

        
    
