import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


loader = PyPDFLoader("Mastering RAG.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
chunks = splitter.split_documents(docs)
# prompt = ChatPromptTemplate.from_template("Tell 5 joke about {topic}")


# 2. Now, define the template as a multi-line string using triple quotes (""")


summary_prompt = ChatPromptTemplate.from_template(
    """**Role:** You are a senior financial analyst at an investment firm.

**Objective:** Your task is to analyze the provided corporate document and prepare a concise briefing for an executive meeting. The output must be clear, accurate, and easy to scan.

**Instructions:**
From the document provided below the "---" separator, execute the following actions:

**1. Executive Summary:**
   - Generate a summary of no more than 5 key takeaways in a bulleted list.
   - Each bullet point should represent a significant finding related to financial performance, strategic shifts, or market position.

**2. Financial Data Analysis:**
   - **Part A: Key Performance Indicators (KPIs):**
     - List the primary financial KPIs mentioned in the text.
   - **Part B: Financial Performance Table:**
     - Create a markdown table with columns: `Financial Metric`, `Value Reported`, `Comparison Period (e.g., YoY, QoQ)`, `Noteworthy Change`.
     - Extract figures exactly as stated. If a value is not available, use "Not Mentioned".

**3. Visual Chart Generation (Mermaid JS):**
   - Based on the data in the Financial Performance Table, generate the code for two visual charts using Mermaid JS syntax.
   - **Chart A (Bar Chart):** Create a bar chart comparing key metrics like 'Revenue', 'Gross Profit', and 'Net Income'. If comparison data is available, show both the current and prior periods.
   - **Chart B (Pie Chart):** Create a pie chart showing the composition of a key category, such as 'Revenue by Segment' or 'Operating Expense Breakdown', if the data is available in the document. If not, create another relevant bar chart.
   - Enclose each Mermaid code block in triple backticks with the `mermaid` tag (```mermaid ... ```).

---
{docs}
---
Instructions:
        1. Focus on information directly relevant to the query
        2. Synthesize the key points from multiple sources
        3. Provide a coherent and well-structured summary
        4. If there are conflicting information, mention it
        5. Keep the summary concise but informative
"""
)

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)


output_parser = StrOutputParser()

chain= summary_prompt | model | output_parser

result=chain.invoke({"docs":chunks})
print(result)