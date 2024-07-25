from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

def generate_project_name(project_description, project_type):
    llm = openai(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['project_description', 'project_type'],
        template="I am making {project_type} project that {project_description} and I want a cool name for it. Suggest me five cool names for my project."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="project_name")

    response = name_chain({'project_description': project_description, 'project_type': project_type})
    return response

def langchain_agent():
    llm = openai(temperature=0.5)
    
    tools = load_tools(["wikipedia", "llm-math"], llm = llm)

    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    result = agent.run(
        "What is the average time it takes to build a web application? Divide by 2."
    )

    print(result)

if __name__ == "__main__":
    langchain_agent()
    # print (generate_project_name("generates personalized mock interviews", "website"))