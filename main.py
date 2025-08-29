from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class InputData(BaseModel):
    data: list

@app.post("/bfhl")
def bfhl_endpoint(payload: InputData):
    full_name = 'john_doe'
    dob = '17091999'
    user_id = f"{full_name.lower()}_{dob}"
    email = "john@xyz.com"
    roll_number = "ABCD123"

    arr = payload.data

    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    total_sum = 0

    for item in arr:
        if isinstance(item, str) and item.isdigit():
            if int(item) % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
            total_sum += int(item)
        elif isinstance(item, str) and re.match("^[a-zA-Z]+$", item):
            alphabets.append(item.upper())
        else:
            special_characters.append(item)

    flat_alpha = ''.join([x for x in arr if isinstance(x, str) and re.match("^[a-zA-Z]+$", x)])
    reversed_string = flat_alpha[::-1]
    concat_string = ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(reversed_string))

    return {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string
    }
