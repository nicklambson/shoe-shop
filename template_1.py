import tkinter as tk
import locale
import gettext
from datetime import datetime
from datetime import timedelta

def format_price(price):
    currency = LOCALE_CURRENCY[selected_locale.get()]
    exchange_rate = 0 # how to get the exchange rate? use the EXCHANGE_RATE dictionary
    final_price = 0 # how to get the final price? multiply price by exchange rate
    formatted_price = locale.currency(final_price, grouping=True, international=True)
    return formatted_price

def refresh_messages():
    # this is the function that runs every time you click on a new option
    # it refreshes all the prices and strings to be localized.
    # you have some variables for shoes_1_price_var, etc.
    # set each one to a new price and remember to format it
    # with format_price

    # later, we will also refresh the shoe names and message.
    pass

EXCHANGE_RATE = {
    "USD" : 1,
    "RMB" : 6.38,
    "JPY" : 109.18,
    "RUB" : 73.46,
    "MXN" : 19.85,
    "EUR" : 0.82,
    "KRW" : 1116.86,
    }

LOCALE_CURRENCY = {
    "en_US" : "USD",
    "zh_CN" : "RMB",
    "ru_RU" : "RUB",
    "es_MX" : "MXN",
    "fr_FR" : "EUR",
    "ko_KR" : "KRW",
    "ja_JP" : "JPY",
    }

root = tk.Tk()
root.withdraw()
root.deiconify()

shop_title = "Shoe Shop"
shop_title_var = tk.StringVar()
shop_title_var.set(shop_title)
root.title(shop_title_var.get())

top_bar = tk.Frame(root, bd=5)
top_bar.pack(side=tk.TOP)

middle = tk.Frame(root, bd=5)
middle.pack(side=tk.TOP)

bottom = tk.Frame(root, borderwidth=5)
bottom.pack(side=tk.BOTTOM)

# This is a string that stores the users's choice
# when they click on a locale
# default is en_US
selected_locale = tk.StringVar()
selected_locale.set("en_US")
locale.setlocale(locale.LC_ALL, "en_US")
# when we make the program multilingual,
# we will need to add some code here to
# set the locale

# This is an integer that stores the user's choice
# when the click on a radio button
# default is 1
selected_choice = tk.IntVar()
selected_choice.set(1)

shoes_1_price = 19.99
shoes_1_price_var = tk.StringVar()
shoes_1_price_var.set(format_price(shoes_1_price))
shoes_1_name = "Neon Star"
shoes_1_name_var = tk.StringVar()
shoes_1_name_var.set(shoes_1_name)

# create your own price and name variables
# for shoes_2 and shoes_3. Use the same setup as above.

photo_1_frame = tk.Frame(middle)
photo_1_frame.pack(side=tk.LEFT)
# put your images in a folder called shoes.
# make sure your images are png format.
photo_1 = tk.PhotoImage(file="shoes/shoes_1.png")
photo_1_label = tk.Label(photo_1_frame, image=photo_1, textvariable=shoes_1_price_var, compound="top", bd=5)
photo_1_label.pack(side=tk.TOP)
R1 = tk.Radiobutton(photo_1_frame, text=shoes_1_name, variable=selected_choice, value=1, command=refresh_messages)
R1.pack(side=tk.BOTTOM)

# create your own photo frame for photos 2 and 3
# use the code above as a template.

# the language menu sits in the top_bar.
# when the user selects an option (from LOCALE_CURRENCY.keys())
# tkinter updates the selected_locale StringVar.
language_menu = tk.OptionMenu(top_bar, selected_locale, *LOCALE_CURRENCY.keys())
language_menu.pack(side=tk.LEFT)

tk.mainloop()