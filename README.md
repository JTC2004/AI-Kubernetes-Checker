# Kubernetes-health-dashboard
An AI-assisted deployment readiness analyzer that reviews Kubernetes manifests, identifies production-readiness issues, explains why they matter, and recommends concrete fixes before code reaches CI/CD or production.

How to run virtual environment(Windows):       .venv\Scripts\activate
How to run virtual environment(Mac/Unix):      source .venv/bin/activate

Installed Dependencies:
   py -m pip install fastapi                For building REST APIs quickly.
   py -m pip install uvicorn                Actually hosts the API.
   py -m pip install pyyaml                 Reads & writers YAML files.
   py -m pip install pydantic               Validates, parses, and serializes Python data using type hints.
   py -m pip install jinja2                 A templating engine for generating HTML or text files by inserting data 
                                            into templates.
   py -m pip install rich                   Makes terminal output nicer with colors, tables, progress bars, syntax 
                                            highlighting, tree views, and formatted logging.
   py -m pip install pytest                 Used for writing/running automated unit & integration tests for my Python code.