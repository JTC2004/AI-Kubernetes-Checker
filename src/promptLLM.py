#Author:            Jared Crow
#Date created:      8/26/26
#Description:       This program:
#                       1) summarize_analysis()
#                       2) Send prompt
#                       3) Receive response
#                       4) Return summary

#ChatGPT recommended this prompt: 
# You are a senior DevOps engineer reviewing a Kubernetes Deployment.
# You are given structured findings from an automated analyzer.
# Write a concise report that:
# - Summarizes the overall deployment health
# - Explains the most important issues
# - Explains why they matter
# - Suggests the highest-priority next steps.
# Do not invent issues that are not present in the findings.
# Limit your response to about 150 words.


#Notes for self:
#                   Then shorter/more concise the prompts, the better.


#How to run:        python src/promptLLM.py 



#Imports:
import yaml
from src.parser import parse_manifest

