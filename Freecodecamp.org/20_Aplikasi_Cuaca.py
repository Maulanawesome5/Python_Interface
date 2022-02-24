from tkinter import *
from PIL import ImageTk, Image
import requests
import json

# Top widget
root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')
root.geometry("400x50")
root.configure(background="green")

# API cuaca
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=11627D2D-1B94-49C8-B4EF-53ED7237AE84

# api_request = requests.get("") # copy API cuaca URL kedalam sini

global city, quality, category

try:
    # copy API cuaca URL kedalam sini
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=11627D2D-1B94-49C8-B4EF-53ED7237AE84")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

except Exception as e:
    api = "Error bro..! Mungkin kamu offline atau terdapat typo pada API_KEY"


myLabel = Label(
    master=root,
    # text=api,
    text=city + " Air Quality " + str(quality) + " " + category,
    font=("Helvetica", 20),
    background="green"
)
myLabel.pack()



root.mainloop()