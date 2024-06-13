# Импортируем библиотеку tkinter для создания графического интерфейса
import tkinter as tk
# Импортируем библиотеку json для работы с файлом glossary.json
import json
# Импортируем библиотеку PIL для работы с изображениями
from PIL import Image, ImageTk

# Определяем пути к файлам
IMAGE_PATH = "Превью.png"
GLOSSARY_FILE = "glossary.json"
ICON_PATH = "Иконка.ico"


# Создаем класс CodeTalker
class CodeTalker:
    def __init__(self):
        # Создаем окно приложения
        self.window = tk.Tk()
        self.window.iconbitmap(ICON_PATH)
        # Устанавливаем заголовок окна
        self.window.title("Code Talker")
        # Устанавливаем цвет фона окна
        self.window.configure(bg="white")

        # Загружаем словарь из файла glossary.json
        self.glossary = self.load_glossary()
        # Создаем переменную для хранения запроса поиска
        self.search_query = tk.StringVar()

        # Инициализируем интерфейс приложения
        self.init_ui()

        self.is_black = False
        self.buttonTems = tk.Button(self.window, text="Темная Тема", command=self.change_color)
        self.buttonTems.pack(pady=20)

    # Метод для загрузки словаря из файла glossary.json
    def load_glossary(self):
        try:
            # Открываем файл glossary.json для чтения
            with open(GLOSSARY_FILE, "r", encoding="utf-8") as f:
                # Загружаем словарь из файла
                return json.load(f)
        except FileNotFoundError:
            # Если файл не найден, выводим сообщение об ошибке
            print("Файл glossary.json не найден")
            return []
        except json.JSONDecodeError:
            # Если файл имеет неправильный формат, выводим сообщение об ошибке
            print("Файл glossary.json имеет неправильный формат")
            return []

    # Метод для поиска термина в словаре
    def search_glossary(self, keyword):
        # Проходим по всем терминам в словаре
        for term in self.glossary:
            # Если запрос поиска содержится в имени термина, возвращаем термин
            if keyword.lower() in term["name"].lower():
                return term
        # Если термин не найден, возвращаем None
        return None

    # Метод для отображения термина
    def display_term(self, term):
        if term:
            # Очищаем текстовое поле
            self.result_text.delete("1.0", tk.END)
            # Вставляем информацию о термине в текстовое поле
            self.result_text.insert(tk.END, f"{term['name']}\n")
            self.result_text.insert(tk.END, f"{term['forms']}\n")
            self.result_text.insert(tk.END, f"{term['description']}\n")
        else:
            # Очищаем текстовое поле
            self.result_text.delete("1.0", tk.END)
            # Вставляем сообщение об ошибке в текстовое поле
            self.result_text.insert(tk.END, "Термин не найден.\n")

    # Метод для поиска термина по запросу
    def search_term(self):
        # Получаем запрос поиска из поля ввода
        keyword = self.search_query.get()
        # Ищем термин в словаре
        term = self.search_glossary(keyword)
        # Отображаем термин
        self.display_term(term)

    # Метод для отображения превью изображения
    def preview(self):
        # Открываем изображение из файла
        image = Image.open(IMAGE_PATH)
        # Создаем объект ImageTk для отображения изображения в tkinter
        preview_image = ImageTk.PhotoImage(image)
        # Устанавливаем изображение в метке
        self.preview_label.config(image=preview_image)
        # Сохраняем ссылку на изображение, чтобы оно не было удалено сборщиком мусора
        self.preview_label.image = preview_image
        # Устанавливаем таймер для скрытия изображения через 5 секунд
        self.window.after(5000, lambda: self.preview_label.config(image=""))

    def init_ui_components(self):
        # Создаем метку для отображения превью изображения
        self.preview_label = tk.Label(self.main_frame, bg="white")
        # Устанавливаем метку в главном фрейме с отступом по вертикали в 10 пикселей
        self.preview_label.pack(pady=10)

        # Создаем фрейм для поиска
        self.search_frame = tk.Frame(self.main_frame, bg="white")
        # Устанавливаем фрейм в главном фрейме с отступом по вертикали в 10 пикселей
        self.search_frame.pack(pady=10)

        # Создаем метку для отображения текста "Что найти?"
        self.label = tk.Label(self.search_frame, text="Что найти?", font=("Inconsolata", 14, "bold"), fg="#04269E",
                              bg="white")
        # Устанавливаем метку в фрейме поиска с отступом по горизонтали в 10 пикселей
        self.label.pack(side=tk.LEFT, padx=10)

        # Создаем поле ввода для поиска
        self.entry = tk.Entry(self.search_frame, width=20, font=("Inconsolata", 14), fg="#04269E", bg="white",
                              textvariable=self.search_query)
        # Устанавливаем поле ввода в фрейме поиска с отступом по горизонтали в 10 пикселей
        self.entry.pack(side=tk.LEFT, padx=10)

        # Создаем кнопку поиска
        self.search_button = tk.Button(self.search_frame, text="Поиск", command=self.search_term,
                                       font=("Inconsolata", 14, "bold"), fg="#04269E", bg="white")
        # Устанавливаем кнопку в фрейме поиска с отступом по горизонтали в 10 пикселей
        self.search_button.pack(side=tk.LEFT, padx=10)

        # Создаем текстовое поле для отображения результата поиска
        self.result_text = tk.Text(self.main_frame, wrap=tk.WORD, height=10, font=("Inconsolata", 14), fg="#04269E",
                                   bg="white")
        # Устанавливаем текстовое поле в главном фрейме с отступом по вертикали в 10 пикселей
        self.result_text.pack(pady=10)

        # Создаем список для отображения терминов
        self.term_list = tk.Listbox(self.main_frame, width=40, height=20, font=("Inconsolata", 14), fg="#04269E",
                                    bg="white")
        # Устанавливаем список в главном фрейме с отступом по вертикали в 10 пикселей
        self.term_list.pack(pady=10)

        # Добавляем термины в список
        for term in self.glossary:
            self.term_list.insert(tk.END, term["name"])

        # Привязываем событие выбора термина в списке к методу on_term_select
        self.term_list.bind("<<ListboxSelect>>", self.on_term_select)

    def on_term_select(self, event):
        # Получаем выбранный термин из списка
        selected_term = self.term_list.get(self.term_list.curselection())
        # Ищем термин в словаре
        for term in self.glossary:
            if term["name"] == selected_term:
                # Отображаем термин
                self.display_term(term)
                break

    def init_ui(self):
        # Создаем главный фрейм
        self.main_frame = tk.Frame(self.window, bg="white")
        # Устанавливаем главный фрейм в окне с возможностью растягивания
        self.main_frame.pack(fill="both", expand=True)
        # Инициализируем компоненты интерфейса
        self.init_ui_components()

        # Отображаем превью изображения
        self.preview()

        # Устанавливаем окно в верхний слой
        self.window.wm_attributes("-topmost", True)
        # Устанавливаем размер окна в полный экран
        self.window.state("zoomed")

    def run(self):
        # Запускаем главный цикл приложения
        self.window.mainloop()


    def change_color(self):  # режим стар варс на темную ли светлую сторону
        if self.is_black:
            self.window.configure(bg="white")
            self.main_frame.configure(bg="white")
            self.term_list.configure(bg="white")
            self.search_button.configure(bg="white")
            self.result_text.configure(bg="white")
            self.preview_label.configure(bg="white")
            self.search_frame.configure(bg="white")
            self.label.configure(bg="white")
            self.buttonTems.configure(text="Темная тема")
        else:
            self.window.configure(bg="black")
            self.main_frame.configure(bg="black")
            self.term_list.configure(bg="black")
            self.search_button.configure(bg="black")
            self.result_text.configure(bg="black")
            self.preview_label.configure(bg="black")
            self.search_frame.configure(bg="black")
            self.label.configure(bg="black")
            self.buttonTems.configure(text="Светлая тема")
        self.is_black = not self.is_black



if __name__ == "__main__":
        # Создаем экземпляр класса CodeTalker
    app = CodeTalker()
    app.run()
