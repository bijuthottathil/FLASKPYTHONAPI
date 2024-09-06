from flask import Flask, jsonify, request

# Create a Flask app
app = Flask(__name__)

# Sample data (to simulate a database)
employees = [
    {"id": 1, "name": "John Doe", "job": "Software Engineer"},
    {"id": 2, "name": "Jane Smith", "job": "HR Manager"},
    {"id": 3, "name": "Sam Wilson", "job": "Marketing Specialist"}
]

# Define a route to get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify({"employees": employees})

# Define a route to get an employee by ID
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((e for e in employees if e["id"] == employee_id), None)
    if employee:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404

# Define a route to create a new employee
@app.route('/employees', methods=['POST'])
def create_employee():
    new_employee = request.get_json()
    new_employee["id"] = len(employees) + 1
    employees.append(new_employee)
    return jsonify(new_employee), 201

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
