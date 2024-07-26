## Updating the Project Details JSON File

The project details are stored in a JSON file located at `data/projects.json`. To manually update this file, follow these steps:

1. Open the `data/projects.json` file in a text editor.
2. Add or update project objects as needed, making sure to adhere to the following structure:
    ```json
    {
        "project_title": "Crisis Center of Comal County",
        "client": "Client GHI",
        "location": "Comal County, TX",
        "construction_value": "2,500,000 USD",
        "services_provided": ["Multifamily"],
        "industry": "Multifamily",
        "description": "Detailed description of Crisis Center of Comal County.",
        "project_stub": "crisis-center-comal",
        "image": "crisis.jpg",
        "summary": "Multifamily"
    }
    ```
3. Save the file and ensure it is in proper JSON format.

The application will automatically read from this file to populate the service detail pages.
