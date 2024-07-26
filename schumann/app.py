import json
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    # Home page logic
    return render_template('index.html')

@app.route('/projects')
def projects():
    with open('data/projects.json', 'r') as file:
        projects_data = json.load(file)
    return render_template('projects.html', projects=projects_data)

@app.route('/project/<project_stub>')
def project_detail(project_stub):
    with open('data/projects.json', 'r') as file:
        projects_data = json.load(file)
    project = next((proj for proj in projects_data if proj['project_stub'] == project_stub), None)
    return render_template('service-detail.html', project=project)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
