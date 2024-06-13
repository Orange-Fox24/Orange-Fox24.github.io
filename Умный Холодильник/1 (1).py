import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from PIL import Image, ImageTk
import requests
from deep_translator import GoogleTranslator
from io import BytesIO

class Recipe:
    def __init__(self, name, category, ingredients, instructions, image_url):
        self.name = name
        self.category = category
        self.ingredients = ingredients
        self.instructions = instructions
        self.image_url = image_url


catalog = []

def get_recipe(texter): #получение ням ням
    url = 'https://www.themealdb.com/api/json/v1/1/'+texter
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        recipe_data = data['meals'][0]

        name = recipe_data['strMeal']
        category = recipe_data['strCategory']
        ingredients = [recipe_data[f'strIngredient{i}'] for i in range(1, 21) if recipe_data[f'strIngredient{i}']]
        instructions = recipe_data['strInstructions']
        image_url = recipe_data['strMealThumb']

        return Recipe(name, category, ingredients, instructions, image_url)
    else:
        return None


def translate_recipe(text): #переводчик
    translated_text = GoogleTranslator(sourse="auto", target ="ru").translate(text)
    return translated_text

def add_recipe(category_recipe_id): # Добавлялка по коду рецепта через категории
    print(category_recipe_id)
    for i in range(len(category_recipe_id)):
        texter = "lookup.php?i="+(str(category_recipe_id[i]))
        recipe = get_recipe(texter)
        if recipe:
            catalog.append(recipe)
            translated_name = translate_recipe(recipe.name)
            lb_recipes.insert(tk.END, translated_name)
            lbl_status.config(text=f"Рецепт '{translated_name}' добавлен в каталог.")
        else:
            messagebox.showerror("Ошибка", "Не удалось получить рецепт с сайта")


def add_random_recipe_to_catalog(): # Случайный рецепт
    texter = "random.php"
    recipe = get_recipe(texter)
    if recipe:
        catalog.append(recipe)
        translated_name = translate_recipe(recipe.name)
        lb_recipes.insert(tk.END, translated_name)
        lbl_status.config(text=f"Рецепт '{translated_name}' добавлен в каталог.")
    else:
        messagebox.showerror("Ошибка", "Не удалось получить рецепт с сайта")

def select_recipe_category(): # Выбор категории
    def on_select():
        category = v.get()
        index_categories_recipe = categories_recipe_translated.index(category)

        messagebox.showinfo("Ваш выбор", f"Вы выбрали: {category}")
        category_window.destroy()
        categories_recipe = ["Beef", "Breakfast", "Chicken", "Dessert", "Goat", "Lamb", "Miscellaneous",
                             "Pasta", "Pork", "Seafood", "Side", "Starter", "Vegan", "Vegetarian"]
        index_recipe = categories_recipe[int(index_categories_recipe)]
        url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + index_recipe
        response = requests.get(url)
        category_recipe_id = []
        data = response.json()
        for i in range(len(data["meals"])):
            recipe_data = data['meals'][i]
            category_recipe_id.append(recipe_data["idMeal"])
        add_recipe(category_recipe_id)


    category_window = tk.Toplevel(root)
    category_window.title("Выберите категорию")

    categories_recipe_translated = ["Говядина", "Завтрак", "Курица", "Десерт", "Козлятина", "Баранина", "Разное",
"Паста", "Свинина", "Морепродукты", "Гарнир", "Закуска", "Веганский", "Вегетарианский"]
    v = tk.StringVar()


    for category in categories_recipe_translated:
        tk.Radiobutton(category_window, text=category, variable=v, value=category).pack(anchor="w")

    ok_button = tk.Button(category_window, text="OK", command=on_select)
    ok_button.pack()


def view_selected_recipe(event): # Выводит рецепты
    index = lb_recipes.curselection()[0]
    recipe = catalog[index]
    translated_instructions = translate_recipe(recipe.instructions)
    translated_ingredients = translate_recipe('\n'.join(recipe.ingredients))
    translated_category = translate_recipe(recipe.category)

    lbl_recipe.insert("1.0", f"Категория: {translated_category}\n\nИнгредиенты:\n{translated_ingredients}\n\nИнструкция: {translated_instructions}")

    image_response = requests.get(recipe.image_url)
    image = Image.open(BytesIO(image_response.content))
    image.thumbnail((200, 200))
    photo = ImageTk.PhotoImage(image)
    lbl_image.config(image=photo)
    lbl_image.image = photo


# Создать графический интерфейс
root = tk.Tk()
root.title("Recipe Catalog")

btn_add_recipe = tk.Button(root, text="Добавить случайный рецепт", command=add_random_recipe_to_catalog)
btn_add_category = tk.Button(root, text="Добавить рецепты по категории", command=select_recipe_category)
btn_add_food = tk.Button(root, text="Добавить рецепты по основному продукту")
btn_add_recipe.pack(pady=10)
btn_add_category.pack(pady=10)
btn_add_food.pack(pady=10)

lb_recipes = tk.Listbox(root)
lb_recipes.pack(pady=10)
lb_recipes.bind('<<ListboxSelect>>', view_selected_recipe)

lbl_status = tk.Label(root, text="")
lbl_status.pack(pady=10)

lbl_recipe = scrolledtext.ScrolledText(root, width=40, height=10)
lbl_recipe.pack(pady=10)

lbl_image = tk.Label(root)
lbl_image.pack(pady=10)

root.mainloop()
