from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

#annotated se metadata add karte hain

class Patient(BaseModel):
    #    name : str = Field(max_length=50)
       name : Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in 50 characters', examples=['tanu', 'ruchi'])]

       email : EmailStr
       age : int = Field(gt=0, lt=100)
       linkedin_url : AnyUrl
       # weight : float = Field(gt=0)
       weight : Annotated[float, Field(gt=0, strict=True)]
    
    #    married : Optional[bool] = Field(max_length=5) #Optional banane par ek default value deni padti hai
       married : Annotated[bool, Field(default=None, description='Is the patient married or not')] 

       allergies : List[str] #list likhte to only list validate kar paate, but list ke andar string nahi dekh paate.
       contact_details : Dict[str, str]

# ye saare fields required honge. Required and optional set karna padta hai.


def insert_patient_data(patient : Patient):
       print(patient.name)
       print(patient.age)
       print(patient.allergies)
       print('inserted into database')

def update_patient_data(patient : Patient):
       print(patient.name)
       print(patient.age)
       print('updated into database')
       

# patient_info = {'name' : 'tanu', 'age' : 27, 'weight' : 54.5, 'married': False, 'allergies' : ['pollen', 'dust'], 'contact_details' : {'email' : 'abc@gmail.com', 'phone' : '9629372193'}}

patient_info = {
    'name' : 'tanu',
    'age' : 27,
    'weight' : 54.8,
    'email': 'tanu@example.com',                    
    'linkedin_url': 'https://www.linkedin.com/in/tanu-tiwari', 
    'married': False,
    'allergies' : ['pollen', 'dust'],
    'contact_details' : {'phone' : '9629372193'}
}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)
