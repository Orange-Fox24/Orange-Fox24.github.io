from tkinter import Tk, Label, PhotoImage, Button
from time import sleep
import tkinter as tk
import requests
import tk


def splash_screen():
    root = Tk()
    root.title("Splash Screen")
    root.geometry("1000x600")
    background_image = PhotoImage(file="Проект ПОГОДА\\MacBook-Pro-16_-1-_3_.ppm")
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.update()
    sleep(2)
    root.destroy()


def city1(city1):
    root = Tk()
    root.title("city_se")
    root.geometry("1000x600")
    root.config(bg="#BAE2EB")

    label_temp = Label(root, text='Температура: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF", bg="#BAE2EB")
    label_temp.pack(fill="both", expand=True)
    label_feels_like = Label(root, text='Ощущаемая температура: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF", bg="#BAE2EB")
    label_feels_like.pack(fill="both", expand=True)
    label_humidity = Label(root, text='Влажность: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF", bg="#BAE2EB")
    label_humidity.pack(fill="both", expand=True)
    label_wind_speed = Label(root, text='Ветер: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF", bg="#BAE2EB")
    label_wind_speed.pack(fill="both", expand=True)
    city = "Северо-Енисейский"
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=df6a5d6b1d928ad532a4d399ddd24faa')
    if response.status_code == 200:
        data = response.json()
        root.title('Погода в городе Северо-Енисейский')
        label_temp.config(text='Температура: ' + str(round(data['main']['temp'])) + '°C')
        label_feels_like.config(text='Ощущаемая температура: ' + str(round(data['main']['feels_like'])) + '°C')
        label_humidity.config(text='Влажность: ' + str(data['main']['humidity']) + '%')
        label_wind_speed.config(text='Ветер: ' + str(round(data['wind']['speed'])) + 'м/с')
    else:
        root.title('Произошла ошибка: ' + str(response.status_code))



def city2(city2):
    root = Tk()
    root.title("city_sbk")
    root.geometry("1000x600")
    root.config(bg="#BAE2EB")
    label_temp = Label(root, text='Температура: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF", bg="#BAE2EB")
    label_temp.pack(fill="both", expand=True)
    label_feels_like = Label(root, text='Ощущаемая температура: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF",
                             bg="#BAE2EB")
    label_feels_like.pack(fill="both", expand=True)
    label_humidity = Label(root, text='Влажность: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF", bg="#BAE2EB")
    label_humidity.pack(fill="both", expand=True)
    label_wind_speed = Label(root, text='Ветер: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF", bg="#BAE2EB")
    label_wind_speed.pack(fill="both", expand=True)
    city = "Северобайкальск"
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=df6a5d6b1d928ad532a4d399ddd24faa')
    if response.status_code == 200:
        data = response.json()
        root.title('Погода в городе Северобайкальск')
        label_temp.config(text='Температура: ' + str(round(data['main']['temp'])) + '°C')
        label_feels_like.config(text='Ощущаемая температура: ' + str(round(data['main']['feels_like'])) + '°C')
        label_humidity.config(text='Влажность: ' + str(data['main']['humidity']) + '%')
        label_wind_speed.config(text='Ветер: ' + str(round(data['wind']['speed'])) + 'м/с')
    else:
        root.title('Произошла ошибка: ' + str(response.status_code))

def city3(city3):
    root = Tk()
    root.title("city_kras")
    root.geometry("1000x600")
    root.config(bg="#BAE2EB")
    label_temp = Label(root, text='Температура: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF", bg="#BAE2EB")
    label_temp.pack(fill="both", expand=True)
    label_feels_like = Label(root, text='Ощущаемая температура: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF",
                             bg="#BAE2EB")
    label_feels_like.pack(fill="both", expand=True)
    label_humidity = Label(root, text='Влажность: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF", bg="#BAE2EB")
    label_humidity.pack(fill="both", expand=True)
    label_wind_speed = Label(root, text='Ветер: ', font=("Abhaya Libre SemiBold", 30), fg="#FFFFFF", bg="#BAE2EB")
    label_wind_speed.pack(fill="both", expand=True)
    city = "Красноярск"
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=df6a5d6b1d928ad532a4d399ddd24faa')
    if response.status_code == 200:
        data = response.json()
        root.title('Погода в городе Красноярск')
        label_temp.config(text='Температура: ' + str(round(data['main']['temp'])) + '°C')
        label_feels_like.config(text='Ощущаемая температура: ' + str(round(data['main']['feels_like'])) + '°C')
        label_humidity.config(text='Влажность: ' + str(data['main']['humidity']) + '%')
        label_wind_speed.config(text='Ветер: ' + str(round(data['wind']['speed'])) + 'м/с')
    else:
        root.title('Произошла ошибка: ' + str(response.status_code))


def main_window():
    root = Tk()
    root.title("Выбрать город")
    root.geometry("1000x600")
    root.config(bg="#BAE2EB")

    Label(root, text="Выбрать город")
    label = Label(root, text="Выбрать город", font=("Abhaya Libre SemiBold", 55), fg="#FFFFFF", bg="#BAE2EB")
    label.place(x=250, y=70)

    button = Button(root, text="Северо-Енисейский", font=("Abhaya Libre SemiBold", 20), fg="#FFFFFF", bg="#AED3FF")
    button.pack()
    button.config(width=18, height=8)
    button.config(command=lambda: city1("Северо-Енисейский"))

    button2 = Button(root, text="Северобайкальск", font=("Abhaya Libre SemiBold", 20), fg="#FFFFFF", bg="#AED3FF")
    button2.pack()
    button2.config(width=18, height=8)
    button2.config(command=lambda: city2("Северобайкальск"))

    button3 = Button(root, text="Красноярск", font=("Abhaya Libre SemiBold", 20), fg="#FFFFFF", bg="#AED3FF")
    button3.pack()
    button3.config(width=18, height=8)
    button3.config(command=lambda: city3("Красноярск"))

    button.place(x=30, y=220)
    button2.place(x=340, y=220)
    button3.place(x=650, y=220)
    root.mainloop()


splash_screen()
main_window()
