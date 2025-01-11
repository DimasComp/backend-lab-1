from server import app
import os

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', 5000), host=os.getenv('HOST', '0.0.0.0'))