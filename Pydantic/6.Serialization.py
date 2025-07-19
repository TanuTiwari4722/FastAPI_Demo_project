from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'katni', 'state': 'MP', 'pin': '483501'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Tanu', 'age': 25, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(include=['name'])
#model_dump_json .json mein export karega 
print(temp)
print(type(temp))

#iclude/exclude
#exclude unset
