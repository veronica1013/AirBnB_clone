![AirBnB_clone](https://github.com/bdbaraban/AirBnB_clone/raw/master/assets/hbnb_logo.png)
Description :AirBnB_clone Project:
ALXBnB is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

# AirBnB Clone - Command Interpreter

## Description of the Project
Welcome to the **AirBnB Clone** project! This is the first step towards building a full web application: the AirBnB clone. The command interpreter developed in this project is a fundamental component that will be used in subsequent tasks, including HTML/CSS templating, database storage, API development, and front-end integration.

The command interpreter provides functionality to manage AirBnB objects such as `User`, `State`, `City`, `Place`, and more. These features include creating, updating, retrieving, and destroying objects. Additionally, the interpreter handles serialization and deserialization of objects to and from JSON format, ensuring persistent storage using a file-based system.

## Description of the Command Interpreter
The command interpreter is a custom-built shell, similar to the UNIX shell but specialized for managing AirBnB objects. It enables users to:
- Create new objects (e.g., a `User` or `Place`).
- Retrieve stored objects from files.
- Perform operations on objects (e.g., counting or computing statistics).
- Update attributes of existing objects.
- Delete objects.

The interpreter uses Python's `cmd` module to provide an interactive interface for these tasks.

## How to Start the Command Interpreter
To start the command interpreter:
1. Clone the repository to your local machine.
2. Navigate to the root directory of the project.
3. Run the command:
   ```bash
   ./console.py

## Examples
Here are some examples of how to use the command interpreter:

1. Create a New Object
```
$ ./console.py
(hbnb) create User
f25db1a7-6b9c-4f3d-b836-2e82f5b7c7e6
(hbnb)
```

The above command creates a new User object and returns its unique ID.

2. Show an Object
```
(hbnb) show User f25db1a7-6b9c-4f3d-b836-2e82f5b7c7e6
[User] (f25db1a7-6b9c-4f3d-b836-2e82f5b7c7e6) {'id': 'f25db1a7-6b9c-4f3d-b836-2e82f5b7c7e6', 'created_at': '2024-11-17T00:00:00', 'updated_at': '2024-11-17T00:00:00'}
(hbnb)
```

3. Update an Object
```
(hbnb) update User f25db1a7-6b9c-4f3d-b836-2e82f5b7c7e6 name "John Doe"
(hbnb) show User f25db1a7-6b9c-4f3d-b836-2e82f5b7c7e6
[User] (f25db1a7-6b9c-4f3d-b836-2e82f5b7c7e6) {'id': 'f25db1a7-6b9c-4f3d-b836-2e82f5b7c7e6', 'created_at': '2024-11-17T00:00:00', 'updated_at': '2024-11-17T00:01:00', 'name': 'John Doe'}
(hbnb)
```

4. Delete an Object
```
(hbnb) destroy User f25db1a7-6b9c-4f3d-b836-2e82f5b7c7e6
(hbnb) all User
[]
(hbnb)
```

5. Display All Objects
```
(hbnb) all
[User] (d93c39b3-9e5f-4536-bf89-98434f989127) {'id': 'd93c39b3-9e5f-4536-bf89-98434f989127', 'created_at': '2024-11-16T23:59:59', 'updated_at': '2024-11-16T23:59:59'}
(hbnb)
```

## Additional Notes
Ensure Python 3.8.5 or later is installed.
All code adheres to the PEP 8 coding standard.
Unit tests are located in the tests directory and can be run using:
```
python3 -m unittest discover tests
```

6. Running Unit Tests
Unit tests are essential for ensuring the stability of the project. To run the tests:

1. Navigate to the root directory of the project.
2. Execute the following command:
```
python3 -m unittest discover tests
```
This will run all test cases located in the tests directory.

**Explore, test, and enjoy the AirBnB Clone project! 🚀**
