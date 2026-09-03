# Kubernetes-health-dashboard
An AI-assisted deployment readiness analyzer that reviews Kubernetes manifests, identifies production-readiness issues, explains why they matter, and recommends concrete fixes before code reaches CI/CD or production.

Notes: 
    - This project currently only supports the "Deployment" Kubernetes format. Support for multiple kinds of Kubernetes format will be added in future development.

    - This project is designed for use with a 16 to 17 GIGABYTE local LLM: qwen3.8:27b. Don't download this projet if you don't have enough free space on your machine.
        - I may add an option for the use to use a remote LLM in the future.

What to know/do before running:
    This project uses a virtual environment called venv, 
    which requires you to install dependencies inside of in order to run.

    1) How to create the virtual environment (Windows):     py -m venv .venv
    How to create the virtual environment (Mac):            python3 -m venv .venv

    2) How to run virtual environment(Windows):     .venv\Scripts\activate
    How to run virtual environment(Mac/Unix):       source .venv/bin/activate

    3) Install these dependencies WHILE the virtual environment is running:
        pip install fastapi              For building REST APIs quickly.
        pip install uvicorn              Actually hosts the API.
        pip install pyyaml               Reads & writers YAML files.

        pip install ollama
        pip install python-dotenv

    4) Next, install ollama outside of the virtual machine to your OS:
        winget install Ollama.Ollama                        (use this on Windows)
        curl -fsSL https://ollama.com/install.sh | sh       (use this on Mac)
    
    5) Then, use the following command in your OS to install the correct LLM ( be sure to have at least 17 GB free):
        ollama run qwen3.8:27b


7) Once the setup is done, use the following command to run the program inside the virtual environment:
    uvicorn src.main:app --reload

8) Finally, while the program is running, go to the directory [your localhost directory here]/analyze to run the LLM.
    - For example: http://127.0.0.1:8000/analyze
    - Doing so will output the LLM's response to your terminal, which may take 1 to 5 minutes while the LLM is 'thinking'.

Type deactivate to exit the virtual environment.


Extra:
    If the program isn't working after following the above steps, try installing these optional dependencies:
        pip install pydantic             Helps w/ maintainability. Validates, parses, and serializes Python data 
                                            using type hints.
        pip install jinja2               A templating engine for generating HTML or text files by inserting data 
                                            into templates.
        pip install rich                 Makes terminal output nicer with colors, tables, progress bars, syntax 
                                            highlighting, tree views, and formatted logging.
        pip install pytest               Used for writing/running automated unit & integration tests for my Python code.