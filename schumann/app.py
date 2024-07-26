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
    
    # Find the index of the current project
    current_index = next((index for (index, proj) in enumerate(projects_data) if proj['project_stub'] == project_stub), None)
    
    if current_index is not None:
        project = projects_data[current_index]
        
        # Replace newline characters with paragraph breaks in description
        project['description'] = project['description'].replace('\n', '</p><p>')
        
        # Determine the previous project stub
        prev_index = (current_index - 1) % len(projects_data)
        prev_project_stub = projects_data[prev_index]['project_stub']
        
        # Determine the next project stub
        next_index = (current_index + 1) % len(projects_data)
        next_project_stub = projects_data[next_index]['project_stub']
        
        return render_template('project-detail.html', 
                               project=project, 
                               prev_project_stub=prev_project_stub, 
                               next_project_stub=next_project_stub)
    else:
        # Handle the case where the project is not found
        return "Project not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
