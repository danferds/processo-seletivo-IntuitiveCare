from flask import Flask
from controller.operator_controller import OperadoraController


app = Flask(__name__)

operadora_controller = OperadoraController(app)

if __name__ == '__main__':
    app.run(debug=True)
