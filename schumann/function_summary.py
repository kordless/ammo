# Function Summary

# File: schumann\app.py
def file_summary():
    imports = ['json', 'flask.Flask', 'flask.render_template']
    decorators = []
    functions = ['home', 'projects', 'project_detail']
    function_calls = ['Flask', 'render_template', 'app.route', 'open', 'json.load', 'render_template', 'app.route', 'open', 'json.load', 'next', 'render_template', 'app.route', 'app.run']
    return {
        'imports': imports,
        'decorators': decorators,
        'functions': functions,
        'function_calls': function_calls
    }

# File: schumann\function_summary.py
def file_summary():
    imports = []
    decorators = []
    functions = ['file_summary']
    function_calls = []
    return {
        'imports': imports,
        'decorators': decorators,
        'functions': functions,
        'function_calls': function_calls
    }

