from flask import Flask
from views import home

app = Flask(__name__)

app.add_url_rule('/', 'home', home)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# comment
