# Kubernetes-health-dashboard
An AI-assisted deployment readiness analyzer that reviews Kubernetes manifests, identifies production-readiness issues, explains why they matter, and recommends concrete fixes before code reaches CI/CD or production.

What to know before running:
    - This project uses a virtual environment called venv, 
    which requires you to install dependencies inside of in order to run.


    How to create the virtual environment:      py -m venv .venv

    How to run virtual environment(Windows):    .venv\Scripts\activate
    How to run virtual environment(Mac/Unix):   source .venv/bin/activate

    Install these dependencies WHILE the virtual environment is running:
        pip install fastapi              For building REST APIs quickly.
        pip install uvicorn              Actually hosts the API.
        pip install pyyaml               Reads & writers YAML files.
        pip install pydantic             Helps w/ maintainability. Validates, parses, and serializes Python data 
                                            using type hints.
        pip install jinja2               A templating engine for generating HTML or text files by inserting data 
                                            into templates.
        pip install rich                 Makes terminal output nicer with colors, tables, progress bars, syntax 
                                            highlighting, tree views, and formatted logging.
        pip install pytest               Used for writing/running automated unit & integration tests for my Python code.

        pip install ollama
        pip install python-dotenv


Once the setup is done, use the following command to run the program inside the virtual environment:
    uvicorn src.main:app --reload

Type deactivate to exit the virtual environment.