"""
Purpose:
Demonstrate commonly used dictionary methods in python
using a patient management example.
"""

# create a patient list
patient = {
    "patient_id": "PAT1001",
    "name": "Dathatreya",
    "city": "Hyderabad" 
}

# print patient city
print(patient["city"])
print(patient.get("city", "Not available"))

# print patient value but key is not available
#print(patient["insurance"])

# use get() method and avoid KeyError and here get returns None if key is not available.
print(patient.get("Insurance"))

# get returns Not available instead of default string None
print(patient.get("Insurance", "Not available"))

# use keys() method to get only keys instead of printing entire dictionary
print(patient.keys())

# use values() method to print only values
print(patient.values())

patient.update({
    "age": 42,
    "name": "Krishna"
})

# List of dictionaries
patient_data = [
    {"Name": "Dathatreya", "city": "Hyderabad"},
    {"Name": "Pushyami", "city": "Bangalore"}
]