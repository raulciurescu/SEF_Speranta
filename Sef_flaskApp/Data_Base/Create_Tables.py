from Data_Base.Tables_fields import table_Manager, table_Staff, table_Menue, table_Orders, table_Reservations
# Create collection with schema
def create_collection_with_fields(db, collection_name, schema):
    validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": list(schema.keys()),
            "properties": {
                field: {"bsonType": details["type"]} for field, details in schema.items()
            }
        }
    }
    db.create_collection(
        collection_name,
        validator=validator
    )

def create_table_Manager(db):
    if "Manager" in db.list_collection_names():
        db.drop_collection("Manager")
    create_collection_with_fields(db, "Manager", table_Manager)

def create_table_Staff(db):
    if "Staff" in db.list_collection_names():
        db.drop_collection("Staff")
    create_collection_with_fields(db, "Staff", table_Staff)

def create_table_Menue(db):
    if "Menue" in db.list_collection_names():
        db.drop_collection("Menue")
    create_collection_with_fields(db, "Menue", table_Menue)

def create_table_Orders(db):    
    if "Orders" in db.list_collection_names():
        db.drop_collection("Orders")
    create_collection_with_fields(db, "Orders", table_Orders)

def create_table_Reservations(db):
    if "Reservations" in db.list_collection_names():
        db.drop_collection("Reservations")
    create_collection_with_fields(db, "Reservations", table_Reservations)