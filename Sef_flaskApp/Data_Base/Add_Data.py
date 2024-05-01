def add_Manager(db, ManagerName, ManagerEmail, ManagerPassword):
    db.Manager.insert_one({
        "ManagerName": ManagerName,
        "ManagerEmail": ManagerEmail,
        "ManagerPassword": ManagerPassword,
    })
    return True

def add_Staff(db, StaffID, StaffName, StaffEmail, StaffPassword):
    db.Staff.insert_one({
        "StaffID": StaffID,
        "StaffName": StaffName,
        "StaffEmail": StaffEmail,
        "StaffPassword": StaffPassword,
    })
    return True

def add_Menue(db, Category, ProductName, Description, Price):
    db.Menue.insert_one({
        "Category": Category,
        "ProductName": ProductName,
        "Description": Description,
        "Price": Price,
    })
    return True

def add_Orders(db, StaffID, OrderID, OrederProducts, OrderStatus, OrderPrice):
    db.Orders.insert_one({
        "StaffID": StaffID,
        "OrderID": OrderID,
        "OrederProducts": OrederProducts,
        "OrderStatus": OrderStatus,
        "OrderPrice": OrderPrice,
    })
    return True

def add_Reservations(db, ReservationName, ReservationPhone, ReservationDate, ReservationTime, ReservationStatus):
    db.Reservations.insert_one({
        "ReservationName": ReservationName,
        "ReservationPhone": ReservationPhone,
        "ReservationDate": ReservationDate,
        "ReservationTime": ReservationTime,
        "ReservationStatus": ReservationStatus,
    })
    return True 
