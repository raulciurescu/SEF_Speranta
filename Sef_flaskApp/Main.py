from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import json 

# Import table creation functions
from Data_Base.Create_Tables import create_table_Manager, create_table_Staff, create_table_Menue, create_table_Orders, create_table_Reservations

app = Flask(__name__)

client = MongoClient()  # Connect to the default host and port 27017
DB_admin = client["Restaurants_Management"] # Create a database called 'DB_admin'




print("Function is executed. And Manager is added.")
create_table_Manager(DB_admin)
create_table_Staff(DB_admin)
create_table_Menue(DB_admin)
create_table_Orders(DB_admin)
create_table_Reservations(DB_admin)
url = "http://127.0.0.1:5000/addManager"
data = {
        "ManagerName": "Raul" ,
        "ManagerEmail" : "raul.ciurescu@studentupt.ro" ,
        "ManagerPassword" : "1234567890"
        }
        

@app.route('/')
def index():
    return render_template('ptManager.html')


@app.route('/addManager', methods=['POST'])        
def add_manager():
    data = request.json
    manager_name = data.get('ManagerName')
    manager_email = data.get('ManagerEmail')
    manager_password = data.get('ManagerPassword')
    manager = {
        "ManagerName": manager_name,
        "ManagerEmail": manager_email,
        "ManagerPassword": manager_password
    }
    DB_admin.Manager.insert_one(manager)
    return "Manager added successfully"


@app.route('/addStaff', methods=['GET','POST'])
def add_staff():
    staff = request.get_json()
    DB_admin.Staff.insert_one(staff)
    return jsonify({"message": "Staff added successfully"}), 200

@app.route('/addMenue', methods=['GET','POST'])
def add_menue():
    menue = request.get_json()
    DB_admin.Menue.insert_one(menue)    
    return jsonify({"message": "Menue added successfully"}), 200

@app.route('/addOrders', methods=['GET','POST'])
def add_orders():
    orders = request.get_json()
    DB_admin.Orders.insert_one(orders)
    return jsonify({"message": "Orders added successfully"}), 200

@app.route('/addReservations', methods=['GET','POST'])
def add_reservations():
    reservations = request.get_json()
    DB_admin.Reservations.insert_one(reservations)
    return jsonify({"message": "Reservations added successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
