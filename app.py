from init import app
from routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)