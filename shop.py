import tkinter as tk
import locale
from datetime import datetime
from datetime import timedelta
import csv
import gettext
from collections import defaultdict

def sel():
    my_language = language.get()
    locale_functions[my_language].install()
    _ = locale_functions[my_language].gettext
    locale.setlocale(locale.LC_ALL, my_language)
    choice = var.get()

    exchange_rate = my_prices["USD"][my_locales[language.get()]]
    USD_price = choice_to_prices[var.get()]
    print(exchange_rate)
    print(USD_price)
    final_price = USD_price * exchange_rate
    formatted_price = locale.currency(final_price, grouping=True)
    price_message = _(f"The price of your selection is {formatted_price}.")
    delivery_days = choice_to_delivery_days[choice]
    arriving = _(f"Your order will arrive in {delivery_days} days.")
    total_message = " ".join([price_message, arriving])
    message.config(text = total_message)

def read_forex(path):
    my_prices = defaultdict(dict)
    with open(path, "r", encoding="utf-8") as my_file:
        my_reader = csv.reader(my_file)
        data = [row for row in my_reader]
        for row in data[1:]:
            for col in range(1, len(row)):
                my_prices[row[0]].update({data[0][col] : float(row[col])})
    return my_prices

es = gettext.translation('es_MX',
                         localedir='locale',
                         languages=['es'],
                         fallback=True)
locale_functions = {
    "es_MX" : es
}

options = [
    "en_US",
    "zh_CN",
    "ru_RU",
    "es_MX",
    "fr_FR",
    "ko_KR",
    "ja_JP",
]

my_locales = {
    "en_US" : "USD",
    "zh_CN" : "RMB",
    "ru_RU" : "RUB",
    "es_MX" : "MXN",
    "fr_FR" : "EUR",
    "ko_KR" : "KRW",
    "ja_JP" : "JPY",
}

choice_to_prices = {
    1 : 19.99,
    2 : 29.99,
    3 : 14.99,
}

choice_to_delivery_days = {
    1 : 2,
    2 : 4,
    3 : 6,
}

root = tk.Tk()
root.withdraw()

root.title('Shoe Shop')
root.deiconify()

top_bar = tk.Frame(root, bd=5)
top_bar.pack(side=tk.TOP)

top = tk.Frame(root, bd=5)
top.pack(side=tk.TOP)

var = tk.IntVar()

photo_1_frame = tk.Frame(top)
photo_1_frame.pack(side=tk.LEFT)
photo_1 = tk.PhotoImage(file="shoes/shoes_1.png")
photo_1_label = tk.Label(photo_1_frame, image=photo_1, text="Rainbow Stars", compound="top", bd=5)
photo_1_label.pack(side=tk.TOP)
R1 = tk.Radiobutton(photo_1_frame, text="Option 1", variable=var, value=1, command=sel)
R1.pack(side=tk.BOTTOM)
price_1 = tk.Label(photo_1_frame, text="$19.99", compound="top", bd=5)
price_1.pack(side=tk.BOTTOM)
# Delivery Days: 1

photo_2_frame = tk.Frame(top)
photo_2_frame.pack(side=tk.LEFT)
photo_2 = tk.PhotoImage(file="shoes/shoes_2.png")
photo_2_label = tk.Label(photo_2_frame, image=photo_2, text="Converse", compound="top", bd=5)
photo_2_label.pack(side=tk.TOP)
R2 = tk.Radiobutton(photo_2_frame, text="Option 2", variable=var, value=2, command=sel)
R2.pack(side=tk.BOTTOM)
price_2 = tk.Label(photo_2_frame, text="$29.99", compound="top", bd=5)
price_2.pack(side=tk.BOTTOM)
# Delivery Days: 2

photo_3_frame = tk.Frame(top)
photo_3_frame.pack(side=tk.LEFT)
photo_3 = tk.PhotoImage(file="shoes/shoes_3.png")
photo_3_label = tk.Label(photo_3_frame, image=photo_3, text="Slip Ons", compound="top", bd=5)
photo_3_label.pack(side=tk.TOP)
R3 = tk.Radiobutton(photo_3_frame, text="Option 3", variable=var, value=3, command=sel)
R3.pack(side=tk.BOTTOM)
price_3 = tk.Label(photo_3_frame, text="$14.99", compound="top", bd=5)
price_3.pack(side=tk.BOTTOM)
# Delivery Days: 3

my_loc = "es"
locale.setlocale(locale.LC_ALL, my_loc)
# create a timestamp
delivery_days = 3
delivery_date = datetime.now() + timedelta(days=delivery_days)
format = "%A, %d %b %Y %H:%M:%S %Z"
delivery_date = delivery_date.strftime(format)
# print the locale and the timestamp in that locale
print(my_loc, delivery_date)

bottom = tk.Frame(root, borderwidth=5)
bottom.pack(side=tk.BOTTOM)

language = tk.StringVar()
language.set("en_US")
language_menu = tk.OptionMenu(top_bar, language, *options)
language_menu.pack(side=tk.LEFT)

message = tk.Label(bottom)
message.pack()

my_prices = read_forex('forex.csv')
for start, conversions in my_prices.items():
    print(start, conversions)

tk.mainloop()