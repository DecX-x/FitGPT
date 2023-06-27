import gradio as gr 
import openai   
from dotenv import load_dotenv
import os

def fitness_evaluation(Age, Height, Weight, Gender, Activity_level, Free_time_daily, additional_info):
    messages = []
    messages.append({"role": "system", "content": "FitGPT is a chatbot that will give you a personalized fitness advice based on your input"})
        
    message = f"Give a person with age of {Age}, height of {Height} meters, The Gender Is {Gender}, weight of {Weight} kg, activity levels of {Activity_level} with 1 being the highest activity level, free time daily of {Free_time_daily} in hours, and has additional info of {additional_info}"
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    fitness_advice = reply
    return fitness_advice

demo = gr.Interface(
    fn=fitness_evaluation,
    inputs=["text", gr.Slider(0, 5), gr.Slider(0, 300), gr.Radio(["Male", "Female"]), gr.Radio(["1", "2", "3", "4", "5"]), gr.Slider(0, 24),"text"],
    outputs=["text"],
    title="FitGPT",
    article="Checkout My Github Account for more Projects and more information about me https://github.com/DecX-x"
)
    
if __name__ == "__main__":
    demo.launch()