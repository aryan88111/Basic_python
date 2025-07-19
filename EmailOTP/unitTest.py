# import unittest

# def add(x, y):
#     return x + y

# class TestMathFunctions(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2, 3), 5)

# if __name__ == "__main__":
#     unittest.main()


# import unittest

# def divide(a, b):
#     return a / b

# class TestCalc(unittest.TestCase):
#     def test_divide(self):
#         self.assertEqual(divide(10, 2), 5)

#     def test_divide_by_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             divide(10, 0)

# if __name__ == "__main__":
#     unittest.main()
# from openai import OpenAI
# import os
# from dotenv import load_dotenv, find_dotenv

# # Load environment variables
# _ = load_dotenv(find_dotenv())
# key = os.getenv("OPENAI_API_KEY")

# # Initialize OpenAI client
# client = OpenAI(api_key=key)

# # Call GPT model with new API
# response = client.chat.completions.create(
#    model="gpt-3.5-turbo",

#     messages=[
#         {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
#     ]
# )

# # Print the output
# print(response.choices[0].message.content)


import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini client
genai.configure(api_key=api_key)

# Create the model
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
# model2 = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

message= input("Enter your question anything :")
# message2= input("Enter your question anything :")

# Make a prompt request
response = model.generate_content(message)
# response2 = model2.generate_content(message2) 


# Print the response
print(response.text)
# print("response 2 \n")
# print(response2.text)

with open("result.md","a+")as file:
    file.write(response.text)
    # file.write(response2.text)
    
from fpdf import FPDF

# Create PDF instance
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# Wrap the response text (multiline)
text = response.text
for line in text.split('\n'):
    pdf.multi_cell(0, 10, line)

# Save PDF file
pdf.output("output.pdf")

    
