#Author:            Jared Crow
#Date created:      8/25/26
#Description:       This file is for conducting rules on yaml objects.

#How to run:        python src/rules.py 

#Imports:
import yaml
from src.parser import parse_manifest

def check_latest_image(_manifest):

    #Open the yaml file:
    str_image = (_manifest
                ["spec"]
                ["template"]
                ["spec"]
                ["containers"]
                [0]
                ["image"]
    )

    if str_image.endswith(":latest"): return "Image is latest!"
    else: return "Image is not latest."





