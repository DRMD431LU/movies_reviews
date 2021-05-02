from pydantic import validator
from pydantic import BaseModel

class UserRequestModel(BaseModel):
    username : str
    password : str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('La longitud debe ser entre 3 y 50 :v')
        return username

class UserResponseModel(BaseModel):
    id: int
    username: str
