#Purpose:
#This program demonstrates dictionary operations used in a patient management system.

# Create patient information dictionary
patient = {
    "patient_id": "PAT1001",
    "name": "Dathatreya",
    "age": 42,
    "gender": "Male",
    "city": "Hyderabad",
    "phone_number": "9876543210",
    "status": "Active"
}

# print all the patient information
for patient_info in patient:
    print(patient[patient_info])

# update patient city information from Hyderabad to Bangalore
patient["city"] = "Bangalore"

# Add a new record to the patient information
patient["blood_group"] = "O +ve"

# Remove phone_number from the patient information
phone_num = patient.pop("phone_number", None)

# print key, value pair from the patient dictionary
for key, value in patient.items():
    print(f"{key}: {value}")

# verify whether "insurance_number" key exists in the patient dictionary. If exists print "Key exists"
if "insurance_number" in patient:
    print("key exists")