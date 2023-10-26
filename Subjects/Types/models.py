from pydantic import BaseModel, ValidationError


class User(BaseModel):
    name: str
    age: int
    email: str


user = User(name="John Doe", age=30, email="john.doe@example.com")
user_dict = user.model_dump()


json_data = '{"name": "John Doe", "age": 30, "email": "john.doe@example.com"}'
try:
    person = User.model_validate_json(json_data)
    print(person)
except ValidationError as e:
    print(e)
