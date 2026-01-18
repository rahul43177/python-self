from pydantic import BaseModel , Field

class SignUpRequest(BaseModel) :
    age : int = Field(ge=18)
    username : str = Field(pattern="^[a-zA-Z0-9]+$")


new_user = SignUpRequest(
    age = 15 ,
    username = "asdadsa@99"
)

print(new_user)
print(new_user.username)

"""
OUTPUT : 
Traceback (most recent call last):
  File "/Users/rahulmishra/Desktop/learning/python-self/100-Advanced-Python/02-Pydantic/01_baseModel.py", line 8, in <module>
    new_user = SignUpRequest(
               ^^^^^^^^^^^^^^
  File "/Users/rahulmishra/Library/Caches/pypoetry/virtualenvs/backend-D0Rf8yfp-py3.12/lib/python3.12/site-packages/pydantic/main.py", line 214, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 2 validation errors for SignUpRequest
age
  Input should be greater than or equal to 18 [type=greater_than_equal, input_value=15, input_type=int]
    For further information visit https://errors.pydantic.dev/2.10/v/greater_than_equal
username
  String should match pattern '^[a-zA-Z0-9]+$' [type=string_pattern_mismatch, input_value='asdadsa@99', input_type=str]
    For further information visit https://errors.pydantic.dev/2.10/v/string_pattern_mismatch

Process finished with exit code 1
"""