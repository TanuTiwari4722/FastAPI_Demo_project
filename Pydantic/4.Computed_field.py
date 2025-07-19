from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float 
    height: float 
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    #dynamically calculate karna hai baaki ki fields se 
    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi = round(self.weight/self.height**2, 2)
        return bmi


patient_info = {'name':'tanu', 'email':'abc@icici.com', 'age': '25', 'weight': 55.2, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

patient1 = Patient(**patient_info)