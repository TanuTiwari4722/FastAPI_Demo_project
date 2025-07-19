from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):
    name : str
    age : int
    gender : str
    address : Address

address_dict = {'city' : 'katni', 'state' : 'MP', 'pin': '483501'}

address1 = Address(**address_dict)

patient_dict = {'name':'tanu', 'gender': 'female', 'age' : 26, 'address': address1}

patient1 = Patient(**patient_dict)
print(patient1)
print(patient1.address.city)
print(patient1.address.pin)

# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed