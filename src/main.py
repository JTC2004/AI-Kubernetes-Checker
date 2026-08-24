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

#Imports:
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Kubernetes Readiness Advisor"}





