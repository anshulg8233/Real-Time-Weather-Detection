from tkinter import *


# Module 1 : Collect data from live website

def weather_report():
    import requests, json
    api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=9128a6dbcba8c81d54cfb7729586a825&q='
    city = city_field.get()
    url = api_address + city
    json_data = requests.get(url).json()

    # Module 3 : Insert Data into respective field

    if json_data['cod'] == 404:

        country = json_data['sys']['country']
        latitute = json_data['coord']['lat']
        longtitute = json_data['coord']['lon']
        temperature = json_data['main']['temp']
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        description = json_data['weather'][0]['description']

        coun_field.insert(15, str(country))
        lati_field.insert(10, str(latitute))
        long_field.insert(15, str(longtitute))
        temp_field.insert(10, str(int(temperature) - 273) + " °C")
        pres_field.insert(15, str(pressure) + " hpa")
        humi_field.insert(10, str(humidity) + " %")
        wind_field.insert(15, str(wind) + " m/s")
        desc_field.insert(10, str(description))

    else:
        from tkinter import messagebox
        messagebox.showinfo("Error", "You have enter the wrong ")


# Module 4 : Clear all fields by using clear button

def clear():
    coun_field.delete(0, END)
    lati_field.delete(0, END)
    long_field.delete(0, END)
    temp_field.delete(0, END)
    pres_field.delete(0, END)
    humi_field.delete(0, END)
    wind_field.delete(0, END)
    desc_field.delete(0, END)

    city_field.delete(0, END)
    city_field.focus_set()


# Module 5 : Data Visulizationz


def graph():
    import requests
    api_address = 'https://api.openweathermap.org/data/2.5/forecast?appid=9128a6dbcba8c81d54cfb7729586a825&q='
    city = city_field.get()
    url = api_address + city
    json_data = requests.get(url).json()
    # print(json_data)

    # xx=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
    xx = [1, 2, 3, 4]
    dat = [1, 2, 3, 4]
    yy = [1, 2, 3, 4]

    a = 0
    r = range(8, 38, 8)
    for q in r:
        cel = json_data['list'][q]['main']['temp'] - 273
        yy[a] = cel
        xx[a] = json_data['list'][q]['dt_txt']
        date = xx[a]
        dat[a] = date[8:10] + " April "
        a = a + 1

    import matplotlib.pyplot as plt
    x = dat
    y = yy
    plt.plot(x, y, color='green')
    plt.ylim(0, 50)
    plt.xlabel("Date & time")
    plt.ylabel("Temperature (°C)")
    plt.title(" Next 4 days weather predication")
    plt.show()


# Module 2 : Create GUI for Data

if __name__ == "__main__":
    root = Tk()
    root.title("Weather Report ")
    root.configure(background="sky blue")
    root.geometry("525x450")

    headlabel = Label(root, text="Real time weather Detection", fg='white', bg='black', font=("Arial Bold", 10))

    label1 = Label(root, text="City Name : ", fg='black')
    label2 = Label(root, text="Country : ", fg='black')
    label3 = Label(root, text="Latitute", fg='black')
    label4 = Label(root, text="Longitute", fg='black')
    label5 = Label(root, text="Temperature : ", fg='black')
    label6 = Label(root, text="Pressure : ", fg='black')
    label7 = Label(root, text="Humidity : ", fg='black')
    label8 = Label(root, text="Wind Speed : ", fg='black')
    label9 = Label(root, text="Description : ", fg='black')

    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0, sticky="E")
    label2.grid(row=3, column=0, sticky="E")
    label3.grid(row=4, column=0, sticky="E")
    label4.grid(row=5, column=0, sticky="E")
    label5.grid(row=6, column=0, sticky="E")
    label6.grid(row=7, column=0, sticky="E")
    label7.grid(row=8, column=0, sticky="E")
    label8.grid(row=9, column=0, sticky="E")
    label9.grid(row=10, column=0, sticky="E")

    city_field = Entry(root)
    coun_field = Entry(root)
    lati_field = Entry(root)
    long_field = Entry(root)
    temp_field = Entry(root)
    pres_field = Entry(root)
    humi_field = Entry(root)
    wind_field = Entry(root)
    desc_field = Entry(root)

    city_field.grid(row=1, column=1, ipadx="100")
    coun_field.grid(row=3, column=1, ipadx="100")
    lati_field.grid(row=4, column=1, ipadx="100")
    long_field.grid(row=5, column=1, ipadx="100")
    temp_field.grid(row=6, column=1, ipadx="100")
    pres_field.grid(row=7, column=1, ipadx="100")
    humi_field.grid(row=8, column=1, ipadx="100")
    wind_field.grid(row=9, column=1, ipadx="100")
    desc_field.grid(row=10, column=1, ipadx="100")

    button1 = Button(root, text="View", bg="red", fg="black", command=weather_report)
    button1.grid(row=2, column=1)
    button2 = Button(root, text="Clear", bg="red", fg="black", command=clear)
    button2.grid(row=11, column=1)
    button3 = Button(root, text=" Next 4 days temperature", bg="red", fg="black", command=graph)
    button3.grid(row=12, column=1)

    root.mainloop()
