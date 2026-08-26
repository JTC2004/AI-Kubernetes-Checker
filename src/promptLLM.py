#Author:            Jared Crow
#Date created:      8/26/26
#Description:       This program:
#                       1) summarize_analysis()
#                       2) Send prompt
#                       3) Receive response
#                       4) Return summary

#Notes for self:
#                   Then shorter/more concise the prompts, the better.
#                   Model being used:  ollama run qwen3.8:27b
#                   ChatGPT recommended this prompt: 
                        # You are a senior DevOps engineer reviewing a Kubernetes Deployment.
                        # You are given structured findings from an automated analyzer.
                        # Write a concise report that:
                        # - Summarizes the overall deployment health
                        # - Explains the most important issues
                        # - Explains why they matter
                        # - Suggests the highest-priority next steps.
                        # Do not invent issues that are not present in the findings.
                        # Limit your response to about 150 words.

#How to run:        python src/promptLLM.py 

#Imports:
import yaml
from ollama import chat

str_model = "qwen3.8:27b"
str_manifestMessage = """
        You are a senior DevOps engineer reviewing a Kubernetes Deployment.
        You are given structured findings from an automated analyzer.

        Write a concise report that:
        - Summarizes the overall deployment health.
        - Explains the most important issues.
        - Explains why they matter.
        - Suggests the highest-priority next steps.

        Do not invent issues that are not present in the findings.
        Limit your response to about 150 words.
    """

#Prompt the LLM to summarize and write a report for YAML data:
def promptWithManifest(_findings):
    print("-----------------------------------")
    
    str_prompt = f"{str_manifestMessage}\nHere are the findings to report: {_findings}"

    print(f"Prompt: \n{str_prompt}\n")
    print(f"Promting LLM {str_model}...\n")             #Update user on prompting progress.

    response = chat(
            model = str_model,
            messages = [
                {
                    "role": "user",
                    "content": str_prompt
                }
            ]
        )

    
    print(response.message.content)
    print("-----------------------------------")


    return response.message.content


def sendPrompt(_message):

    response = chat(
        model = str_model,
        messages = [
            {
                "role": "user",
                "content": "Say hello!"
            }
        ]
    )

    print(response.message.content)

def printManifestMessage():
    print(str_manifestMessage)

