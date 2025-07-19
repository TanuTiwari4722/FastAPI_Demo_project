from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

#field_validator custom fileds ko validate kar sakta hai
#transformations perform karna chahte hain to

class Patient(BaseModel):

    name: str
    email: EmailStr #email str ko dekh ke validate karenge.
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')# default value after hoti hai
    @classmethod
    def age_validator(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')
    
patient_info = {
    'name' : 'tanu',
    'age' : 27,
    'weight' : 54.8,
    'email': 'tanu@hdfc.com',                    
    'linkedin_url': 'https://www.linkedin.com/in/tanu-tiwari', 
    'married': False,
    'allergies' : ['pollen', 'dust'],
    'contact_details' : {'phone' : '9629372193'}
}

patient1 = Patient(**patient_info) #yahan validation and type coersion dono hote hain.