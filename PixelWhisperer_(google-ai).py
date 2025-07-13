# pip install -q -U google-generativeai

import google.generativeai as genai

genai.configure(api_key="AIzaSyCjnMkwXykKi9zztTsWDCZ-4Z76NlOAknY")

'''
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

try:
    response = model.generate_content("Difference between rugby vs soccer")
    print(response.text)  # Instead of print(response)
except Exception as e:
    print("Error:", e)
'''

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('.', '*')
    return Markdown(textwrap.indent(text, '>', predicate=lambda _: True))


''''for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)'''

model = genai.GenerativeModel('models/gemini-2.5-flash-lite-preview-06-17')

import PIL.Image

img1 = PIL.Image.open(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\PROJECTS_NARESH_IT\Pixel_Whisperer_-GenAI\random_Img1.jpg")
#print(img1)
img2 = PIL.Image.open(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\PROJECTS_NARESH_IT\Pixel_Whisperer_-GenAI\random_Img2.jpg")
#print(img2)

response1 = model.generate_content(img1)
print(response1.text)  # Works in any terminal

response2 = model.generate_content(img2)
print(response2.text)  # Works in any terminal

