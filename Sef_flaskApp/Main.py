from flask import Flask, redirect, render_template, request, jsonify, session, url_for
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import json 

# Import table creation functions
from Data_Base.Create_Tables import create_table_Manager, create_table_Staff, create_table_Menue, create_table_Orders, create_table_Reservations
from generateOrders import generate_orders

app = Flask(__name__, static_url_path='/static')

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

@app.route('/LogIn')
def index5():
    return render_template('LogInAs.html')

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

@app.route('/SLogIn')
def staff_login():
    return render_template('StaffLogIn.html')

@app.route('/SLogIn', methods=['POST'])
def staff_login_process():
    data = request.json
    staff_email = data.get('StaffEmail')
    staff_password = data.get('StaffPassword')
    staff = DB_admin.Staff.find_one({"StaffEmail": staff_email, "StaffPassword": staff_password})
    if staff:
        #session['staff_id'] = staff['StaffID']
        return "Staff logged in successfully"
    return "Staff not found"

@app.route('/displayOrders', methods=['GET'])
def display_orders():
    # Fetch orders with status "placed" from the database
    orders = list(DB_admin.Orders.find({"OrderStatus": "placed"}))
    
    # Render the HTML template and pass the orders to it
    return render_template('DisplayOrders.html', orders=orders)

@app.route('/updateOrderStatus/<order_id>', methods=['POST'])
def update_order_status(order_id):
    # Retrieve the staff ID from the session
    staff_id = session.get('staff_id')
    if staff_id is None:
        return 'Unauthorized', 401
    
    # Update the order status to "In process" and assign the staff ID
    DB_admin.Orders.update_one(
        {"OrderID": order_id}, 
        {"$set": {"OrderStatus": "In process", "StaffID": staff_id}}
    )
    return 'Status changed successfully to In process', 200



if __name__ == '__main__':
    generate_orders(10)
    app.run(debug=True)