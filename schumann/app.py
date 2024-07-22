from flask import Flask
from flask import render_template

app = Flask(__name__)

def home():
 return render_template('index.html')

app.add_url_rule('/', 'home', home)

@app.route('/projects')
def projects():
 return render_template('projects.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# comment