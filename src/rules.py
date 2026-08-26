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
    rules = None                    #Will equal a dictionary of rules and their results.

    if(manifest["kind"] == "Deployment"):
        rules = {
            "kind": manifest["kind"],
            "name": manifest["metadata"]["name"],
            "image": check_latest_image(manifest),
            "resources": check_resource_limits(manifest),
            "readinessProbe": check_readiness_probe(manifest),
            "livenessProbe": check_liveness_probe(manifest),
        }
    else:
        rules = {
            "kind": "Warning: Not a valid kind of yaml file.",
        }


    return rules


#The rules:
def check_latest_image(_manifest):

    #Open the yaml file:
    container = getContainer(_manifest)

    if container["image"].endswith(":latest"): return "Image is latest."
    else: return "Image is not latest."


def check_resource_limits(_manifest):

    container = getContainer(_manifest)

    if (container.get("resources") is None): return "Warning: No resource limit."
    else: return f"Resource limit(s) is {container["resources"]["requests"]}"


#A readiness probe tells Kubernetes: "Is my application ready to receive user traffic?"
def check_readiness_probe(_manifest):

    container = getContainer(_manifest)

    if (container.get("readinessProbe") is None): return "Warning: No readiness probe."
    else: return f"Readiness Probe limit(s) is {container["readinessProbe"]["httpGet"]}"


#A liveness probe tells Kubernetes: "Is my application still alive?"
def check_liveness_probe(_manifest):

    container = getContainer(_manifest)

    if (container.get("livenessProbe") is None): return "Warning: No liveness probe."
    else: return f"Liveness Probe limit(s) is {container["livenessProbe"]["httpGet"]}"



#Repeated code actions:
def getContainer(_manifest):
    return (_manifest
                ["spec"]
                ["template"]
                ["spec"]
                ["containers"]
                [0]
    )