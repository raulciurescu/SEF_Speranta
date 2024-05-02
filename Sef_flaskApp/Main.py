from flask import Flask, redirect, render_template, request, jsonify, url_for
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import json 

# Import table creation functions
from Data_Base.Create_Tables import create_table_Manager, create_table_Staff, create_table_Menue, create_table_Orders, create_table_Reservations

app = Flask(__name__)

client = MongoClient()  # Connect to the default host and port 27017
DB_admin = client["Restaurants_Management"] # Create a database called 'DB_admin'





create_table_Manager(DB_admin)
create_table_Staff(DB_admin)
create_table_Menue(DB_admin)
create_table_Orders(DB_admin)
create_table_Reservations(DB_admin)



@app.route('/addManager')
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

@app.route('/MLogIn')
def index2():
    return render_template('ManagerLogIn.html')


@app.route('/MLogIn', methods=['POST'])
def manager_login():
    data = request.json
    manager_email = data.get('ManagerEmail')
    manager_password = data.get('ManagerPassword')
    manager = DB_admin.Manager.find_one({"ManagerEmail": manager_email, "ManagerPassword": manager_password})
    if manager:
        return "Manager logged in successfully"
    return "Manager not found"

@app.route('/dashboard')
def dashboard():
    return render_template('AddStaff_Menue.html')

@app.route('/AddStaff') 
def index3():
    return render_template('AddStaff.html')

@app.route('/AddStaff', methods=['POST'])
def add_staff():
    data = request.json
    staff_id = data.get('StaffID')
    staff_name = data.get('StaffName')
    staff_email = data.get('StaffEmail')
    staff_password = data.get('StaffPassword')
    staff = {
        "StaffID": staff_id,
        "StaffName": staff_name,
        "StaffEmail": staff_email,
        "StaffPassword": staff_password
    }
    DB_admin.Staff.insert_one(staff)
    return "Staff added successfully"





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
