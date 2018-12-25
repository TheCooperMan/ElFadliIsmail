from flask_frozen import Freezer
from application import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    freezer.run(debug=True)