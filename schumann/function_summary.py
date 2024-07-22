# Function Summary

# File: schumann\app.py
def file_summary():
    imports = ['flask.Flask', 'flask.render_template']
    decorators = []
    functions = ['home', 'projects']
    function_calls = ['Flask', 'render_template', 'app.add_url_rule', 'render_template', 'app.route', 'app.run']
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
    functions = ['file_summary', 'file_summary']
    function_calls = []
    return {
        'imports': imports,
        'decorators': decorators,
        'functions': functions,
        'function_calls': function_calls
    }

