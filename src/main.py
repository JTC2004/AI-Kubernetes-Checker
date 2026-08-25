#Author:            Jared Crow
#Date started:      8/23/26

#Problem statement: Kubernetes configuration issues are often discovered late in the development process, 
#                   causing unnecessary review cycles, delayed deployments, and repeated manual guidance 
#                   from platform engineers. 

#Solution:          This is an AI-assisted deployment readiness analyzer that reviews Kubernetes manifests, 
#                   identifies production-readiness issues, explains why they matter, 
#                   and then recommends concrete fixes before code reaches CI/CD or production.

#Notes for myself:
#   - Venv is a virtual environment where I can install Python independencies without effecting the rest of my PC!
#

#How to run:        uvicorn src.main:app --reload

#Imports:
from fastapi import FastAPI
from src.parser import parse_manifest

#Rules:
from src.rules import check_latest_image
from src.rules import check_resource_limits

app = FastAPI()

#The different web pages of the app:
@app.get("/")
def home():
    return {"message": "Kubernetes Readiness Advisor"}

@app.get("/analyze")
def analyze():
    manifest = parse_manifest("deployment.yaml")

    print()

    return {
        "kind": manifest["kind"],
        "name": manifest["metadata"]["name"],
        "latest?": check_latest_image(manifest),
        "resources?": check_resource_limits(manifest)
    }




#If the user wants to run just the parser instead:
if __name__ == "__main__":
    manifest = parse_manifest("sample_manifests/deployment.yaml")
    print(manifest)