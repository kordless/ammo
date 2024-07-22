## Updating the Project Details JSON File

The project details are stored in a JSON file located at `data/projects.json`. To manually update this file, follow these steps:

1. Open the `data/projects.json` file in a text editor.
2. Add or update project objects as needed, making sure to adhere to the following structure:
    ```json
    {
        "project_title": "Project Title",
        "client": "Client Name",
        "location": "Location",
        "construction_value": "Value",
        "services_provided": ["List of Services"],
        "industry": "Industry",
        "description": "Detailed description."
    }
    ```
3. Save the file and ensure it is in proper JSON format.

The application will automatically read from this file to populate the service detail pages.
