#Author:            Jared Crow
#Date created:      8/24/26
#Description:       This file is for parsing yaml files into Python objects.

#How to run:        python src/parser.py 

#Imports:
import yaml

def parse_manifest(str_filename):

    #Open the yaml file ("r" means read mode):
    with open("sample_manifests/" + str_filename, "r") as file:
        obj_manifest = yaml.safe_load(file)                         #This creates a dictionary object containing the yaml data.
                                                                    #Similar to a JSON object.

        print(obj_manifest)                                         #Prints the yaml data.

        #print(obj_manifest["metadata"]["name"])                     #Print just the name of the manifest.
        #print(obj_manifest["kind"])                                 #Print just the kind of the manifest.

        return obj_manifest


