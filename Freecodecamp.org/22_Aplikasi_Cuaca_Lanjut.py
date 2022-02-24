from tkinter import *
from PIL import ImageTk, Image
import requests
import json

# Top widget
root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')
# root.geometry("400x50")

# API cuaca
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=11627D2D-1B94-49C8-B4EF-53ED7237AE84

# api_request = requests.get("") # copy API cuaca URL kedalam sini

global city, quality, category

# mengetahui kondisi AQI berdasarkan zipcode yang dimasukkan melalui entry
def zipLookup():
    # zip.get()
    # zipLabel = Label(master=root, text=zip.get())
    # zipLabel.grid(row=1, column=0, columnspan=2)

    try:
        # copy API cuaca URL kedalam sini
        api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip.get()}&distance=5&API_KEY=11627D2D-1B94-49C8-B4EF-53ED7237AE84")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "green"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Gropus":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)

        myLabel = Label(
            master=root,
            # text=api,
            text=city + " Air Quality " + str(quality) + " " + category,
            font=("Helvetica", 20),
            background=weather_color
        )
        myLabel.grid(row=1, column=0, columnspan=2)
        
        root.geometry(len(myLabel)) # mengatur size window agar otomatis menyesuaikan panjang tulisan

    except Exception as e:
        api = "Error bro..! Mungkin kamu offline atau terdapat typo pada API_KEY"

zip = Entry(master=root)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton = Button(master=root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, sticky=W+E+N+S)


root.mainloop()
