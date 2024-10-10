import requests
import json

BASE_URL = 'http://127.0.0.1:5000/students'

def log_response(response):
    print(response.status_code)
    try:
        print(response.json())
    except json.JSONDecodeError:
        print(response.text)

def test_api():
    # Отримання всіх студентів
    response = requests.get(BASE_URL)
    log_response(response)

    # Створення студентів
    students = [
        {"first_name": "John", "last_name": "Doe", "age": 20},
        {"first_name": "Jane", "last_name": "Doe", "age": 22},
        {"first_name": "Emily", "last_name": "Smith", "age": 21}
    ]
    for student in students:
        response = requests.post(BASE_URL, json=student)
        log_response(response)

    # Отримання всіх студентів
    response = requests.get(BASE_URL)
    log_response(response)

    # Оновлення віку другого студента (PATCH)
    student_id = 2
    response = requests.patch(f"{BASE_URL}/{student_id}", json={"age": 23})
    log_response(response)

    # Отримання інформації про другого студента
    response = requests.get(f"{BASE_URL}/{student_id}")
    log_response(response)

    # Оновлення даних третього студента (PUT)
    student_id = 3
    updated_data = {"first_name": "Emily", "last_name": "Brown", "age": 24}
    response = requests.put(f"{BASE_URL}/{student_id}", json=updated_data)
    log_response(response)

    # Отримання інформації про третього студента
    response = requests.get(f"{BASE_URL}/{student_id}")
    log_response(response)

    # Видалення першого студента
    student_id = 1
    response = requests.delete(f"{BASE_URL}/{student_id}")
    log_response(response)

    # Отримання всіх студентів
    response = requests.get(BASE_URL)
    log_response(response)

if __name__ == "__main__":
    test_api()

