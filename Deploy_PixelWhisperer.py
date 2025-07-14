
#------------------------------------------------PIXEL WHISPERER-------------------------------------------------#

# Import Libraries
import gradio as gr
import PIL.Image
import google.generativeai as genai

# Setup Gemini
genai.configure(api_key="AIzaSyCjnMkwXykKi9zztTsWDCZ-4Z76NlOAknY")
model = genai.GenerativeModel('models/gemini-2.5-flash-lite-preview-06-17')

# Define the captioning function
def describe_image(img: PIL.Image.Image):
    try:
        response = model.generate_content(img)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio UI
iface = gr.Interface(
    fn=describe_image,
    inputs=gr.Image(type="pil", label="Upload a JPG Image"),
    outputs=gr.Textbox(label="Image Description"),
    title="Pixel Whisperer",
    description="Upload an image (.jpg) and Gemini will whisper what it sees.",
    allow_flagging="never",
    examples=[]  # You can optionally add example images here
)

iface.launch()