def insert_patient_data(name : str, age : int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError('Age cannot be negative')
        else:
            print(name)
            print(age)
            print('inserted into database')
    else:
        raise TypeError

insert_patient_data('tanu', 27) #type validation issue aaega
# abhi bhi str bhejne mein issue nahi aaega. Type hinting does not involves errors.


def updaate_patient_data(name : str, age : int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('Updated into database')
    else:
        raise TypeError

# This type checking is not scalable. Which pydantic solves.


