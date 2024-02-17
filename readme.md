# Flask Project Structure

This repository contains a Flask project with a well-organized directory structure for building web applications using Flask.

## Project Structure

The project follows a recommended Flask project structure for easy maintenance and scalability. Here's a brief overview of the directory structure:

```plaintext
/flask-PY-API
    ├── api/
    │   ├── flask_app/
    |   |   ├── business_collection/
    |   |   ├── endpoints/
    |   |   ├── helpers/
    |   |   ├── serializers/
    |   │   └── endpoints/
    │   └── restplus.py
    ├── factory.py
    ├── logger/
    |   ├── __init__.py/
    │   └── log_handler.py/
    ├── settings/
    │   └── __init__.py/
    ├── requirements.txt
    ├── venv/
    ├── .gitignore
    ├── logging.conf
    └── README.md
    └── app.py
    └── .env

```

- api/: This directory contains the main Flask application.
- api/flask_app/: main application folder for the application
- api/flask_app/business_collection/: contains all the business logic 
- api/flask_app/endpoints/: contains all the endpoints
- api/flask_app/helpers/: contains the helper functions
- api/flask_app/serializers/: includes support for data serialization and deserialization
- api/flask_app/endpoints/: contains endpoints/routes
- api/restplus.py/:  Initializes the Flask application and extensions.
- logger/: contains logging setup
- settings/: configuration settings for the application.
- factory.py: creating and configure the Flask app instance
- venv/: Virtual environment (create using virtualenv or venv).
- requirements.txt: List of all the required packages
- logging.conf: logging config
- .gitignore: List of files and directories to ignore in version control.
- app.py: Entry point for running the Flask application.
- README.md: This documentation file.
- .env: contains env variables


## Getting Started

Follow these instructions to get the Flask project up and running on your local machine.

Prerequisites
Python (3.6 or higher)
pip (Python package manager)
virtualenv (recommended for creating a virtual environment)
Installation
Clone this repository to your local machine:

bash
```git clone https://github.com/yourusername/flask-project.git```
Navigate to the project directory:

bash
```cd flask-project```
Create a virtual environment (optional but recommended):

bash
```python -m venv venv```
Activate the virtual environment:

On Windows:

bash
```venv\Scripts\activate```
On macOS and Linux:

bash
``` source venv/bin/activate```
Install project dependencies:

bash
``` pip install -r requirements.txt``` 
Usage
Run the Flask application:

bash
``` flask run --port=5000 ```
``` uwsgi --socket 0.0.0.0:5000 --protocol http -w app:app ```


Open your web browser and navigate to http://localhost:5000 to access the application.

For Health Check: navigate to http://localhost:5000/v1/system/health


Start building your Flask web application by modifying the code in the app/ directory and defining routes in app/routes.py.