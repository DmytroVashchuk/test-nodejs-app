from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

# Шлях до файлу з даними
CSV_FILE = 'students.csv'

# Функція для зчитування даних з CSV
def read_students():
    students = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            students = [row for row in reader]
    return students

# Функція для запису даних у CSV
def write_students(students):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ['id', 'first_name', 'last_name', 'age']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

# Генерація нового ID
def generate_id(students):
    if not students:
        return 1
    else:
        return max(int(student['id']) for student in students) + 1

# Повернення всіх студентів
@app.route('/students', methods=['GET'])
def get_all_students():
    students = read_students()
    return jsonify(students)

# Повернення студента за ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    students = read_students()
    student = next((s for s in students if int(s['id']) == student_id), None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404

# Повернення студентів за прізвищем
@app.route('/students/lastname/<last_name>', methods=['GET'])
def get_students_by_last_name(last_name):
    students = read_students()
    matching_students = [s for s in students if s['last_name'].lower() == last_name.lower()]
    if matching_students:
        return jsonify(matching_students)
    else:
        return jsonify({"error": "Student not found"}), 404

# Створення нового студента
@app.route('/students', methods=['POST'])
def create_student():
    if not request.json or not all(k in request.json for k in ('first_name', 'last_name', 'age')):
        return jsonify({"error": "Invalid input"}), 400

    students = read_students()
    new_student = {
        'id': generate_id(students),
        'first_name': request.json['first_name'],
        'last_name': request.json['last_name'],
        'age': request.json['age']
    }
    students.append(new_student)
    write_students(students)
    return jsonify(new_student), 201

# Оновлення студента за ID (PUT)
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    if not request.json or not all(k in request.json for k in ('first_name', 'last_name', 'age')):
        return jsonify({"error": "Invalid input"}), 400

    students = read_students()
    student = next((s for s in students if int(s['id']) == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    student['first_name'] = request.json['first_name']
    student['last_name'] = request.json['last_name']
    student['age'] = request.json['age']
    write_students(students)
    return jsonify(student)

# Оновлення віку студента за ID (PATCH)
@app.route('/students/<int:student_id>', methods=['PATCH'])
def patch_student_age(student_id):
    if not request.json or 'age' not in request.json:
        return jsonify({"error": "Invalid input"}), 400

    students = read_students()
    student = next((s for s in students if int(s['id']) == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    student['age'] = request.json['age']
    write_students(students)
    return jsonify(student)

# Видалення студента за ID
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    students = read_students()
    student = next((s for s in students if int(s['id']) == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    students = [s for s in students if int(s['id']) != student_id]
    write_students(students)
    return jsonify({"message": "Student deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

