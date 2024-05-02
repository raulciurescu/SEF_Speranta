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

@app.route('/AddStaff', methods=['GET', 'POST'])
def manage_staff():
    if request.method == 'POST':
        # Check if the request contains data to add staff
        if request.json:
            staff_data = request.json
            DB_admin.Staff.insert_many(staff_data)
            return "Staff added successfully"
        # Check if the request is to delete all staff
        elif request.form.get('action') == 'deleteAll':
            # You can add code here to delete all staff from the database
            # For example:
            # DB_admin.Staff.delete_many({})  # Delete all staff records from the collection
            return "All staff deleted successfully"
    # Render the template for adding staff
    return render_template('AddStaff.html')


@app.route('/AddMenue')
def index4():
    return render_template('Menue.html')

@app.route('/AddMenue', methods=['POST'])
def add_menue():
    data = request.json
    menu_items = data
    DB_admin.Menue.insert_many(menu_items)  # Use insert_many to insert multiple documents
    return "Menue added successfully"

if __name__ == '__main__':
    app.run(debug=True)