import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
topic="school"
prompt = ChatPromptTemplate.from_template("Tell a joke about {topic}")

# Gemini Pro model via LangChain official integration
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    google_api_key=api_key
)

# Output parser
output_parser = StrOutputParser()

chain= prompt | model | output_parser

result=chain.invoke({"topic":"python"})
print(result)