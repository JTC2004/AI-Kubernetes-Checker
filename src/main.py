#Author:            Jared Crow
#Date started:      8/23/26
#Start venv:        .venv\Scripts\activate
#How to run:        uvicorn src.main:app --reload

#Problem statement: Kubernetes configuration issues are often discovered late in the development process, 
#                   causing unnecessary review cycles, delayed deployments, and repeated manual guidance 
#                   from platform engineers. 

#Solution:          This is an AI-assisted deployment readiness analyzer that reviews Kubernetes manifests, 
#                   identifies production-readiness issues, explains why they matter, 
#                   and then recommends concrete fixes before code reaches CI/CD or production.

#How it works:
#   Step 1: Read & parse JSON into a manifest (Python object) in parser.py.
#   Step 2: Test the data against rules to answer factual questions about the data in rules.py.
#       - That way, when the AI reads the data, it doesn't have to read the raw YAML data.
#   Step 3: Use a Local LLM to answer: "How do I explain these findings to a developer?"

#Features to add:
#   - Let user know progress of LLM prompting in the terminal.
#   - Use AWAIT so localhost loads before LLM message is ready.
#   - Print result to localhost.

#Notes for myself:
#   - Venv is a virtual environment where I can install Python independencies without effecting the rest of my PC!


#Imports:
from fastapi import FastAPI
from src.parser import parse_manifest
from src.promptLLM import *

#Rules:
from src.rules import *         #Import all functions from rules.py

app = FastAPI()

#Variables:
#a_rules = []

#The different web pages of the app:
@app.get("/")
def home():
    return {"message": "Kubernetes Readiness Advisor"}

@app.get("/analyze")
def analyze():
    manifest = parse_manifest("deployment.yaml")

    findings = checkRules(manifest)

    #[Print AI response here]
    promptWithManifest(findings)

    #Check compliance with rules:
    return findings



#Prints the parsed manifest to the terminal when localhost is accessed:
if __name__ == "__main__":
    manifest = parse_manifest("deployment.yaml")
    print(manifest)