from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/adventure'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Employee model
class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)

    def __init__(self, name, department, role):
        self.name = name
        self.department = department
        self.role = role

# Function to initialize the database
def init_db():
    with app.app_context():
        db.create_all()

# Route to insert new employee details
@app.route('/employees', methods=['POST'])
def insert_employee():
    data = request.get_json()

    # Check if the data contains the required fields
    if not all(key in data for key in ['name', 'department', 'role']):
        return jsonify({"error": "Missing data"}), 400

    # Create a new employee object
    new_employee = Employee(
        name=data['name'],
        department=data['department'],
        role=data['role']
    )

    try:
        # Insert the new employee into the database
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({"message": "Employee added successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Initialize the database with app.app_context()
    init_db()
    app.run(debug=True)
