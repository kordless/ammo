# Function Summary

# File: schumann\app.py
def file_summary():
    imports = ['flask.Flask', 'views.home']
    decorators = []
    functions = []
    function_calls = ['Flask', 'app.add_url_rule', 'app.run']
    return {
        'imports': imports,
        'decorators': decorators,
        'functions': functions,
        'function_calls': function_calls
    }

# File: schumann\views.py
def file_summary():
    imports = ['flask.render_template']
    decorators = []
    functions = ['home']
    function_calls = ['render_template']
    return {
        'imports': imports,
        'decorators': decorators,
        'functions': functions,
        'function_calls': function_calls
    }

