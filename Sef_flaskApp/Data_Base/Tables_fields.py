table_Manager = {
    "ManagerName": {"type": "string"},
    "ManagerEmail": {"type": "string"},
    "ManagerPassword": {"type": "string"},
}

table_Staff = {
    "StaffID": {"type": "string"},
    "StaffName": {"type": "string"},
    "StaffEmail": {"type": "string"},
    "StaffPassword": {"type": "string"},
}

table_Menue = {
    "Category": {"type": "string"},
    "ProductName": {"type": "string"},
    "Description": {"type": "string"},
    "Price": {"type": "string"},
}

table_Orders = {
    "StaffID": {"type": "string"}, # "StaffID": {"type": "string", "required": True}, # "required": True, "unique": True, "index": True, "default": "1234567890
    "OrderID": {"type": "string"},
    "OrederProducts": {"type": "string"}, # Fixed typo and removed extra '{'
    "OrderStatus": {"type" : "string"}, # Fixed syntax error and removed unnecessary dictionary
    "OrderPrice": {"type": "string"},
}

table_Reservations = {
    "ReservationName": {"type": "string"},
    "ReservationPhone": {"type": "string"},
    "ReservationDate": {"type": "string"},
    "ReservationTime": {"type": "string"},
    "ReservationStatus": {"type" : "string"}, # Fixed syntax error and removed unnecessary dictionary
}