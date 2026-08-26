#Author:            Jared Crow
#Date created:      8/25/26
#Description:       This file is for conducting rules on yaml objects,
#                   assuming the yaml file follows proper Kubernetes formatting.
#                   Each rule should only check ONE thing!
#Notes for self:
#                   It's ok to hard-code the searches because a general search loses the context of what those fields mean.
#                   (For example, 'image' can mean a disk image in one set, or a png in another set)


#How to run:        python src/rules.py 



#Imports:
import yaml
from src.parser import parse_manifest

manifest = None


#Run different kinds of rule checks based on what kind of yaml file is being read:
def checkRules(_manifest):
    manifest = _manifest            #The yaml data object read from the yaml file.
    analysis = None                 #Will hold the final analysis results when returned.
    rules = None                    #Will equal a dictionary of rules and their results.

    #Gathering the results of checking data against the rules:
    if(manifest["kind"] == "Deployment"):
        rules = {
            "image": check_latest_image(manifest),
            "resources": check_resource_limits(manifest),
            "readinessProbe": check_readiness_probe(manifest),
            "livenessProbe": check_liveness_probe(manifest),
        }
    else:
        rules = {
            "kind": "Warning: Not a valid kind of yaml file.",
        }

    #Creating the final analysis:
    analysis = {
        "kind": manifest["kind"],
        "name": manifest["metadata"]["name"],
        "findings": [rules]
    }


    return analysis


#The rules:
def check_latest_image(_manifest):

    container = getContainer(_manifest)

    if (not container["image"].endswith(":latest")):
        return {
            "severity": "Warning",
            "rule": "Latest Image Tag",
            "container": container.get("name"),
            "description": "The container uses the 'latest' image tag.",
            "recommendation": "Use a specific version tag (for example, nginx:1.27)."
        }

    return {
        "severity": "None",
        "rule": "Pinned Image Version",
        "container": container.get("name"),
        "description": "The container uses a specific image version.",
        "recommendation": "N/A"
    }


def check_resource_limits(_manifest):

    container = getContainer(_manifest)

    if container.get("resources") is None:
        return {
            "severity": "Warning",
            "rule": "Missing Resource Limits",
            "container": container.get("name"),
            "description": "The container does not define CPU or memory resources.",
            "recommendation": "Add resource requests and limits."
        }

    return {
        "severity": "None",
        "rule": "Resource Limits Configured",
        "container": container.get("name"),
        "description": "The container defines resource requests and limits.",
        "recommendation": "N/A"
    }


#A readiness probe tells Kubernetes: "Is my application ready to receive user traffic?"
def check_readiness_probe(_manifest):

    container = getContainer(_manifest)

    if (container.get("readinessProbe") is None): return {
        "severity": "Warning",
        "rule": "Missing Readiness Probe",
        "container": container.get("name"),
        "description": "The container has no readiness probe.",
        "recommendation": "Add a readinessProbe."
    }

    return {
        "severity": "None",
        "rule": "Has A Readiness Probe",
        "container": container.get("name"),
        "description": "The container has a readiness probe.",
        "recommendation": "N/A"
    }


#A liveness probe tells Kubernetes: "Is my application still alive?"
def check_liveness_probe(_manifest):

    container = getContainer(_manifest)

    if container.get("livenessProbe") is None:
        return {
            "severity": "Warning",
            "rule": "Missing Liveness Probe",
            "container": container.get("name"),
            "description": "The container has no liveness probe.",
            "recommendation": "Add a livenessProbe."
        }

    return {
        "severity": "None",
        "rule": "Has A Liveness Probe",
        "container": container.get("name"),
        "description": "The container has a liveness probe.",
        "recommendation": "N/A"
    }


#Repeated code actions:
def getContainer(_manifest):
    return (_manifest
                ["spec"]
                ["template"]
                ["spec"]
                ["containers"]
                [0]
    )