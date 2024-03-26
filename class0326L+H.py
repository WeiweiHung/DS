from dotenv import load_dotenv
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

hub_llm = HuggingFaceHub(repo_id="roborovski/superprompt-v1")

prompt = PromptTemplate(
    input_variables=["question"],
    template="Expand the following prompt to add more detail: {question}"
)

hub_chain = LLMChain(prompt = prompt, llm = hub_llm, verbose = True)
print(hub_chain("A man in a suit walking down the street"))