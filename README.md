# SQLAlchemy Management System

SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. Its fundamental working principle revolves around representing and managing relational databases with Python classes. Through the ORM layer, database tables are defined as Python classes, and relationships between tables are managed through Python objects. This allows for database operations to be performed without writing SQL queries. SQLAlchemy also offers a layer known as the Core, which provides the ability to work directly with SQL expressions. This dual-layer architecture supports both high-level ORM abstraction and low-level SQL operations, offering flexible and powerful database management.

## Table of Contents

- [Importance of SQLAlchemy](#importance-of-sqlalchemy)
- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Importance of SQLAlchemy

SQLAlchemy is a powerful and flexible SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access. Key features include:

- **Flexibility**: SQLAlchemy can be used with many different types of databases and provides a comprehensive system for managing SQL constructs. This allows developers to work seamlessly across various database systems without needing to rewrite applications.

- **Expressive ORM**: SQLAlchemy offers a full suite of features for object-relational mapping, allowing developers to define database models as Python classes and manipulate data using Pythonic methods. This abstraction simplifies database interactions and makes the codebase more maintainable.

- **Advanced Querying**: SQLAlchemy supports complex and advanced querying capabilities, including filters, joins, subqueries, and eager loading. It enables developers to write sophisticated queries efficiently, optimizing database performance and reducing query complexity.

By leveraging SQLAlchemy, developers can build scalable and robust database applications in Python, focusing on business logic rather than database intricacies. SQLAlchemy's ORM capabilities streamline the development process and facilitate the creation of maintainable and database-independent applications.


## Project Description

This project consists of several Python classes mapped to database tables, representing students, cities, lessons, teachers, and their associated notes. The main goal is to demonstrate SQLAlchemy's capabilities through various operations such as adding, updating, deleting records, and querying complex relationships.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/serkanyasr/Python-SQLAlchemy-FrameWork.git
    cd Python-SQLAlchemy-FrameWork
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    Ensure you have a SQL Server instance running and update the connection string in the `create_engine` call in the `create_session` function.

## Usage

To use the system, you can run the script directly:
```sh
python main.py

```
## Contributing

We welcome contributions! Please open an issue first to discuss what you would like to change before submitting a pull request.

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature-name`)
3. **Commit** your changes (`git commit -m 'Add some feature'`)
4. **Push** to the branch (`git push origin feature-name`)
5. **Open** a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

