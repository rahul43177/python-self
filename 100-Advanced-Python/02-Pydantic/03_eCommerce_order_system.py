"""
The Scenario: You are building the backend for an online store. You need to validate an incoming order and then prepare it to be saved into the database. Databases don't understand Pydantic classes; they only understand plain Dictionaries (JSON).

Your Task:
1. Create a model OrderItem with:
    name: string (must be at least 2 chars).
    price: float (must be greater than 0).
    quantity: int (must be at least 1).

2. Create a model Order with:
    order_id: int.
    customer_email: string (use a simple email regex or just string if you prefer).
    items: A list of OrderItem.

3. The Action:
    Create an Order instance with at least 2 items.
    Convert it to a dictionary using .model_dump().
    Print the dictionary.

Bonus Check: Try to access a value using dictionary syntax (e.g., data["order_id"]) to prove it's really a dict and not a model anymore.
"""

from pydantic import BaseModel , Field
from random import randint
class OrderItem(BaseModel):
    """
    name: string (must be at least 2 chars).
    price: float (must be greater than 0).
    quantity: int (must be at least 1).
    """

    name : str = Field(min_length = 2)
    price : float = Field(gt=0)
    quantity : int = Field(ge=1)

class Order(BaseModel):
    """
    order_id: int.
    customer_email: string(use a simple email regex or just string if you prefer).
    items: A list of OrderItem.
    """

    order_id : int
    customer_email : str = Field(pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    items : list[OrderItem]

item1 = OrderItem(
    name = "One Plus 15" ,
    price = 80000 ,
    quantity=1
)

item2 = OrderItem(
    name = "Classmate Pulse Notebook" ,
    price=45.90 ,
    quantity=2
)

place_order = Order(
    order_id = randint(1000 , 2000) ,
    customer_email= "rahulmishra4317@gmail.com" ,
    items = [item1 , item2]
)
## Printing the data in python format -- dict
data = place_order.model_dump()
print(data)

## TRYING TO access data using dictionary in python

"""
Data looks something like this right now : 
data = {
  "order_id": 1508,
  "customer_email": "rahulmishra4317@gmail.com",
  "items": [
    {
      "name": "One Plus 15",
      "price": 80000,
      "quantity": 1
    },
    {
      "name": "Classmate Pulse Notebook",
      "price": 45.9,
      "quantity": 2
    }
  ]
}
"""
print("="*50)
print(data["order_id"])
print(data["items"][0]["name"])
