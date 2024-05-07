import random
import string
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client["Restaurants_Management"]
Orders = db['Orders']

def generate_orders(num_orders):
    for _ in range(num_orders):
        order = {
            "StaffID": "your_staff_id",  # Replace with the actual staff ID
            "OrderID": ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
            "OrederProducts": "Product 1, Product 2",  # Example product list
            "OrderStatus": "placed",
            "OrderPrice": str(random.randint(50, 200)),  # Example price range
        }
        Orders.insert_one(order)

