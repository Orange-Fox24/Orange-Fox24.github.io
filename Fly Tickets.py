import tkinter as tk

class Boeing737600:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Boeing 737-600")

        self.label = tk.Label(self.root, text="Уважаемые пассажиры, добро пожаловать в самолет боинг 737-600.\n"
                                             "В нашем самолете 119 мест.\n"
                                             "Все места по 5000, кроме аварийных 10A 10F по 6000",
                              font=("Arial", 12))
        self.label.pack()

        self.name_label = tk.Label(self.root, text="Введите ФИО:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.data_label = tk.Label(self.root, text="Введите ваш возраст (шаблон 01.01.24):")
        self.data_label.pack()
        self.data_entry = tk.Entry(self.root)
        self.data_entry.pack()

        self.pasport_label = tk.Label(self.root, text="Введите серию и номер паспорта:")
        self.pasport_label.pack()
        self.pasport_entry = tk.Entry(self.root)
        self.pasport_entry.pack()

        self.seat_map_label = tk.Label(self.root, text="Выбор места:")
        self.seat_map_label.pack()
        self.seat_map_text = tk.Text(self.root, width=40, height=20)
        self.seat_map_text.pack()
        self.seat_map_text.insert(tk.INSERT, """
    ---          1D  1E  1F
    2A  2B  2C   2D  2E  2F
    3A  3B  3C   3D  3E  3F    
    4A  4B  4C   4D  4E  4F
    5A  5B  5C   5D  5E  5F    
    6A  6B  6C   6D  6E  6F
    7A  7B  7C   7D  7E  7F    
    8A  8B  8C   8D  8E  8F
    9A  9B  9C   9D  9E  9F    
    10A 10B 10C  10D 10E 10F
    11A 11B 11C  11D 11E 11F    
    12A 12B 12C  12D 12E 12F
    13A 13B 13C  13D 13E 13F    
    14A 14B 14C  14D 14E 14F
    15A 15B 15C  15D 15E 15F    
    16A 16B 16C  16D 16E 16F
    17A 17B 17C  17D 17E 17F    
    18A 18B 18C  18D 18E 18F
    19A 19B 19C  19D 19E 19F    
    20A 20B 20C  20D 20E 20F
    ---          21D 21E 21F    
""")

        self.available_seats = ['1D', '1E', '1F', '2A', '2B', '2C', '2D', '2E', '2F', '3A', '3B', '3C', '3D', '3E', '3F', '4A', '4B', '4C', '4D', '4E', '4F', '5A', '5B',
                               '5C', '5D', '5E', '5F', '6A', '6B', '6C', '6D', '6E', '6F', '7A', '7B', '7C', '7D', '7E', '7F', '8A', '8B', '8C', '8D', '8E', '8F', '9A',
                               '9B', '9C', '9D', '9E', '9F', '10A', '10B', '10C', '10D', '10E', '10F', '11A', '11B', '11C', '11D', '11E', '11F', '12A', '12B',
                               '12C', '12D', '12E', '12F', '13A', '13B', '13C', '13D', '13E', '13F', '14A', '14B', '14C', '14D', '14E', '14F', '15A', '15B', '15C',
                               '15D', '15E', '15F', '16A', '16B', '16C', '16D', '16E', '16F', '17A', '17B', '17C', '17D', '17E', '17F', '18A', '18B', '18C', '18D', '18E', '18F', '19A', '19B', '19C',
                               '19D', '19E', '19F', '20A', '20B', '20C', '20D', '20E', '20F', '21D', '21E', '21F']

        self.place_label = tk.Label(self.root, text="Какое место вы хотите выбрать?")
        self.place_label.pack()
        self.place_entry = tk.Entry(self.root)
        self.place_entry.pack()

        self.price_label = tk.Label(self.root, text="")
        self.price_label.pack()

        self.payment_label = tk.Label(self.root, text="Вы хотите оплатить место?")
        self.payment_label.pack()
        self.payment_entry = tk.Entry(self.root)
        self.payment_entry.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.check_button = tk.Button(self.root, text="Проверить", command=self.check_place)
        self.check_button.pack()

        self.pay_button = tk.Button(self.root, text="Оплатить", command=self.pay_place)
        self.pay_button.pack()

    def check_place(self):
        place = self.place_entry.get().upper()
        if place in self.available_seats:
            if place in ['10A', '10F']:
                self.price_label.config(text=f'Вы выбрали место {place} по цене 6000 рублей.')
                self.price = 6000
            else:
                self.price_label.config(text=f'Вы выбрали место {place} по цене 5000 рублей.')
                self.price = 5000
        else:
            self.price_label.config(text='Такое место не существует или уже забронировано. Пожалуйста, выберите другое место.')

    def pay_place(self):
        payment = self.payment_entry.get().lower()
        if payment == 'да':
            self.available_seats.remove(self.place_entry.get().upper())
            self.result_label.config(text=f'Вы успешно оплатили место {self.place_entry.get().upper()} на сумму {self.price} рублей.')
        elif payment == 'нет':
            self.result_label.config(text='Оплата не произведена. Место не будет зарезервировано.')
        else:
            self.result_label.config(text='Некорректный ввод. Пожалуйста, введите "да" или "нет".')

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Boeing737600()
    app.run()