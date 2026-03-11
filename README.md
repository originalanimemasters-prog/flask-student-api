# Flask Student API

This is a simple backend project built using **Python and Flask**.
The API provides authentication and basic management of student records.

The project includes **JWT authentication, password hashing, and CRUD operations** for students.

## Features

* User registration
* User login with JWT authentication
* Password hashing for security
* Create student records
* View all students
* View a student by ID
* Update student details
* Delete student records

## Tech Used

* Python
* Flask
* Flask SQLAlchemy
* SQLite / SQL Database
* JWT Authentication
* Password hashing (Werkzeug)
* REST API

## Database Structure

### Student Table

| Field | Type    |
| ----- | ------- |
| id    | Integer |
| name  | String  |
| age   | Integer |

### User Table

| Field    | Type            |
| -------- | --------------- |
| id       | Integer         |
| username | String          |
| password | String (hashed) |
| role     | String          |

## Example Response

Example student object returned by the API:

{
"id": 1,
"name": "Rahul",
"age": 20
}

Example user object:

{
"id": 1,
"username": "admin",
"role": "admin"
}

## API Routes

Authentication

POST /register – create a new user
POST /login – login and receive JWT token

Student APIs

GET /students – get all students
GET /students/<id> – get student by id
POST /students – create new student
PUT /students/<id> – update student
DELETE /students/<id> – delete student

## How to Run the Project

Clone the repository

git clone https://github.com/originalanimemasters-prog/flask-student-api.git

Go to the project folder

cd flask-student-api

Install dependencies

pip install -r requirements.txt

Run the application

python app.py

The server will start at:

http://127.0.0.1:5000/

## API Testing

The API can be tested using tools like **Postman** or **cURL**.
Protected routes require a **JWT token** received after login.

## Author

Parshant
GitHub: https://github.com/originalanimemasters-prog
