from flask import Flask
from factory import initialize_app

app = Flask(__name__, instance_relative_config=True, static_folder='static')
app = initialize_app(app)

if __name__ == '__main__':
    app.run(debug=False)
