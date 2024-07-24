from langchain.llms import openai
from dotenv import load_dotenv\

load_dotenv()

def generate_project_name():
    llm = openai(temperature=0.7)

    name = llm("I am developing a website that creates personalized mock interviews and I want a cool name for it. Suggest me five cool names for my project.")

    return name

