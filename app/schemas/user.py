from pydantic import BaseModel, ConfigDict
from datetime import datetime

#this class is used to define the UserBase schema for user information
class UserBase(BaseModel):
    name: str
    email: str
    phone: str | None = None


class UserCreate(UserBase):
    pass

#this class is used to define the UserUpdate schema for updating user information
class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None

#this class is used to define the UserResponse schema for returning user information
class UserResponse(UserBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)