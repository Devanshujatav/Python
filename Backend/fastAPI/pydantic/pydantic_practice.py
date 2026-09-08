from pydantic import(
    BaseModel,
    Field,
    field_validator,
    model_validator,
    ConfigDict,
    ValidationError,
)

from typing import List , Dict , Optional , Union

from datetime import datetime

from enum import Enum


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# ==========================================================
# 1. BASIC MODEL
# ==========================================================
section("1. BASIC MODEL")

class User(BaseModel):
    id : int 
    name : str
    is_active : bool = True

user = User(id = 1 , name = "Dev")
print(user)
print("name : " , user.name)
print("as_Dict : " , user.model_dump())
print("as JSON : " , user.model_dump_json())

# ==========================================================
# 2. TYPE COERCION
# ==========================================================
section("2. TYPE COERCION")

class Product(BaseModel):
    price : float
    quantity : int

p = Product(price = "99.99" , quantity="99")

print(p , " --> type : " , type(p.price) , type(p.quantity))

# ==========================================================
# 3. VALIDATION ERRORS
# ==========================================================
section("3. VALIDATION ERRORS")

try: 
    User(id = "abc" , name = "Dev")
except ValidationError as e:
    print("Caught error as expected:")
    print(e)
    print(e.errors())


# ==========================================================
# 4. COMMON FIELD TYPES (list, dict, optional, union, datetime)
# ==========================================================
section("4. COMMON FIELD TYPES")

class Example(BaseModel):
    name : str
    age: int
    height : float
    is_student : bool
    tags : List[str]
    scores : Dict[str , int]
    nickname : Optional[str] = None
    id_or_code : Union[int , str]
    created_at : datetime

ex = Example(
    name = "Aditi",
    age = 22,
    height = 5.4,
    is_student=True,
    tags=["Python" , "ml"],
    scores={"math" : 90 , "science" : 85},
    id_or_code="A123",
    created_at="2024-05-10T10:00:00",
)

print(ex)
print("created_at type " ,type(ex.created_at))

# ==========================================================
# 5. Field() CONSTRAINTS
# ==========================================================
section("5. Field() CONSTRAINTS")

class ProductConstrained(BaseModel):
    name : str = Field(... , min_length=2 , max_length=50)
    price : float = Field(... , gt=0 , description="Price must be greater than 0")
    quantity : int = Field(default=1 , gt=0 , le=1000)
    discount : float = Field(default=0.0 , ge=0 , le=1)

pc = ProductConstrained(name="DEV" , price=50000)
print(pc)

try:
    ProductConstrained(name="A" , price=-1999)
except ValidationError as e:
    print("Constrained Error : ")
    print(e)


# ==========================================================
# 6. CUSTOM FIELD VALIDATORS
# ==========================================================
section("6. CUSTOM FIELD VALIDATORS")

class Account(BaseModel):
    username : str
    password : str

    @field_validator("username")
    @classmethod
    def username_no_spaces(cls , value):
        if " " in value:
            raise ValueError("Username must not contain spaces")

        return value.lower()

    @field_validator("password")
    @classmethod
    def password_strength(cls , value):
        if (len(value) < 8):
            raise ValueError("Password must be at least 8 characters")

        return value


acc = Account(username = "DJ" , password = "Devanshu@12345")
print(acc)

try:
    Account(username = "D J" , password = "pass")
except ValidationError as e:
    print("Validation Error")
    print(e)


# ==========================================================
# 7. MODEL VALIDATOR (cross-field validation)
# ==========================================================
section("7. MODEL VALIDATOR (cross-field)")

class SignupForm(BaseModel):
    password : str
    confirm_password : str

    @model_validator(mode = "after")
    def password_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")

        return self

try:
    SignupForm(password = "abc133" , confirm_password = "zrh133")
except ValidationError as e:
    print(e)

good_form = SignupForm(password = "abc233" , confirm_password = "abc233")
print("valid_form : " , good_form)

