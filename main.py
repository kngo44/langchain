from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_project_name(project_description):
    llm = openai(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['project_description'],
        template="I am developing a website that {project_description} and I want a cool name for it. Suggest me five cool names for my project."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    response = name_chain({'project_description': project_description})
    return response

if __name__ == "__main__":
    print (generate_project_name("generates personalized mock interviews"))