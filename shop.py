import tkinter as tk
import locale
from datetime import datetime
from datetime import timedelta
import csv
import gettext
from collections import defaultdict

def select_shoes():
    # refresh variables
    my_language = language.get()
    my_choice = choice.get()
    
    # set the locale
    locale_functions[my_language].install()
    _ = locale_functions[my_language].gettext
    locale.setlocale(locale.LC_ALL, my_language)
    
    # get the price
    exchange_rate = my_prices["USD"][my_locales[language.get()]]
    USD_price = choice_to_prices[choice.get()]
    final_price = USD_price * exchange_rate
    formatted_price = locale.currency(final_price, grouping=True, international=True)

    # get delivery days
    delivery_days = choice_to_delivery_days[my_choice]

    # set up the messages
    price_message = _("The price of your selection is %(price)s.") % {'price' : formatted_price}
    arriving = _("Your order will arrive in %(days)s days.") % {'days' : delivery_days}
    total_message = " ".join([price_message, arriving])
    message.config(text = total_message)

    # refresh all prices on buttons
    price_1_USD = choice_to_prices[1]
    price_1_final = price_1_USD * exchange_rate
    price_1_formatted = locale.currency(price_1_final, grouping=True, international=True)
    price_1 = tk.Label(photo_1_frame, text=price_1_formatted, compound="top", bd=5)
    price_1.pack(side=tk.BOTTOM)

    price_2_USD = choice_to_prices[2]
    price_2_final = price_2_USD * exchange_rate
    price_2_formatted = locale.currency(price_2_final, grouping=True, international=True)
    price_2 = tk.Label(photo_2_frame, text=price_2_formatted, compound="top", bd=5)
    price_2.pack(side=tk.BOTTOM)

    price_3_USD = choice_to_prices[3]
    price_3_final = price_3_USD * exchange_rate
    price_3_formatted = locale.currency(price_3_final, grouping=True, international=True)
    price_3 = tk.Label(photo_3_frame, text=price_3_formatted, compound="top", bd=5)
    price_3.pack(side=tk.BOTTOM)


def read_forex(path):
    my_prices = defaultdict(dict)
    with open(path, "r", encoding="utf-8") as my_file:
        my_reader = csv.reader(my_file)
        data = [row for row in my_reader]
        for row in data[1:]:
            for col in range(1, len(row)):
                my_prices[row[0]].update({data[0][col] : float(row[col])})
    return my_prices

en = gettext.translation('es_MX',
                         localedir='locale',
                         languages=['es'],
                         fallback=True)
zh = gettext.translation('zh_CN',
                         localedir='locale',
                         languages=['zh'],
                         fallback=True)
ru = gettext.translation('ru_RU',
                         localedir='locale',
                         languages=['ru'],
                         fallback=True)
es = gettext.translation('es_MX',
                         localedir='locale',
                         languages=['es'],
                         fallback=True)
fr = gettext.translation('fr_FR',
                         localedir='locale',
                         languages=['fr'],
                         fallback=True)
ko = gettext.translation('ko_KR',
                         localedir='locale',
                         languages=['ko'],
                         fallback=True)
ja = gettext.translation('ja_JP',
                         localedir='locale',
                         languages=['ja'],
                         fallback=True)

locale_functions = {
    "en_US" : en,
    "zh_CN" : zh,
    "ru_RU" : ru,
    "es_MX" : es,
    "fr_FR" : fr,
    "ko_KR" : ko,
    "ja_JP" : ja}

my_locales = {
    "en_US" : "USD",
    "zh_CN" : "RMB",
    "ru_RU" : "RUB",
    "es_MX" : "MXN",
    "fr_FR" : "EUR",
    "ko_KR" : "KRW",
    "ja_JP" : "JPY",}

choice_to_prices = {
    1 : 19.99,
    2 : 29.99,
    3 : 14.99,}

choice_to_delivery_days = {
    1 : 2,
    2 : 4,
    3 : 6,}

root = tk.Tk()
root.withdraw()

root.title('Shoe Shop')
root.deiconify()

top_bar = tk.Frame(root, bd=5)
top_bar.pack(side=tk.TOP)

top = tk.Frame(root, bd=5)
top.pack(side=tk.TOP)

choice = tk.IntVar()

my_prices = read_forex('forex.csv')

photo_1_frame = tk.Frame(top)
photo_1_frame.pack(side=tk.LEFT)
photo_1 = tk.PhotoImage(file="shoes/shoes_1.png")
photo_1_label = tk.Label(photo_1_frame, image=photo_1, text="Rainbow Stars", compound="top", bd=5)
photo_1_label.pack(side=tk.TOP)
R1 = tk.Radiobutton(photo_1_frame, text="Option 1", variable=choice, value=1, command=select_shoes)
R1.pack(side=tk.BOTTOM)
price_1 = tk.Label(photo_1_frame, text="$19.99", compound="top", bd=5)
price_1.pack(side=tk.BOTTOM)
# Delivery Days: 1

photo_2_frame = tk.Frame(top)
photo_2_frame.pack(side=tk.LEFT)
photo_2 = tk.PhotoImage(file="shoes/shoes_2.png")
photo_2_label = tk.Label(photo_2_frame, image=photo_2, text="Converse", compound="top", bd=5)
photo_2_label.pack(side=tk.TOP)
R2 = tk.Radiobutton(photo_2_frame, text="Option 2", variable=choice, value=2, command=select_shoes)
R2.pack(side=tk.BOTTOM)
price_2 = tk.Label(photo_2_frame, text="$29.99", compound="top", bd=5)
price_2.pack(side=tk.BOTTOM)
# Delivery Days: 2

photo_3_frame = tk.Frame(top)
photo_3_frame.pack(side=tk.LEFT)
photo_3 = tk.PhotoImage(file="shoes/shoes_3.png")
photo_3_label = tk.Label(photo_3_frame, image=photo_3, text="Slip Ons", compound="top", bd=5)
photo_3_label.pack(side=tk.TOP)
R3 = tk.Radiobutton(photo_3_frame, text="Option 3", variable=choice, value=3, command=select_shoes)
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


bottom = tk.Frame(root, borderwidth=5)
bottom.pack(side=tk.BOTTOM)

language = tk.StringVar()
language.set("en_US")
language_menu = tk.OptionMenu(top_bar, language, *locale_functions.keys())
language_menu.pack(side=tk.LEFT)

message = tk.Label(bottom)
message.pack()



tk.mainloop()