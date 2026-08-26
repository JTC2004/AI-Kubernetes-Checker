#Author:            Jared Crow
#Date started:      8/23/26
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
#   Step 3: Use a Local LLM to The LLM should instead answer: "How do I explain these findings to a developer?"
#   Step 4: 

#Notes for myself:
#   - Venv is a virtual environment where I can install Python independencies without effecting the rest of my PC!


#Imports:
from fastapi import FastAPI
from src.parser import parse_manifest

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

    #[Print AI response here]

    #Check compliance with rules:
    return checkRules(manifest)




#If the user wants to run just the parser instead:
if __name__ == "__main__":
    manifest = parse_manifest("sample_manifests/deployment.yaml")
    print(manifest)