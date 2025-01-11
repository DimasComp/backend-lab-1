from backend import app
import os

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT', 5000))