
#pip3 install pydantic
#../venv/bin/python pydanticGuide.py


from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    @classmethod
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be postitive: {value}")
        return value

user = User(
    name="Jhonathan",
    email="jhonathan@gmail.com",
    account_id=1234
)

user_data = {
    'name': 'Jhonathan',
    'email': 'jhonathan@gmail.com',
    'account_id': 12345
}

user2 = User(**user_data)

#Note: You dont need to worry about making a __str__ or __repr__ special method
print(user)
print(user2)