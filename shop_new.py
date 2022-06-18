import tkinter as tk
import locale
import gettext
from datetime import datetime
from datetime import timedelta


def format_price(price):
    currency = LOCALE_CURRENCY[selected_locale.get()]
    exchange_rate = EXCHANGE_RATE[currency]
    final_price = price * exchange_rate
    formatted_price = locale.currency(final_price, grouping=True, international=True)
    return formatted_price

def refresh_messages():
    shoes_1_price_var.set(format_price(shoes_1_price))
    shoes_2_price_var.set(format_price(shoes_2_price))
    shoes_3_price_var.set(format_price(shoes_2_price))

def set_locale(*args):
    my_locale = selected_locale.get()
    LOCALE_FUNCTIONS[my_locale].install()
    _ = LOCALE_FUNCTIONS[my_locale].gettext
    locale.setlocale(locale.LC_ALL, my_locale)
    refresh_messages()

en = gettext.translation('en_US',
                         localedir='locale',
                         languages=['en'],
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
LOCALE_FUNCTIONS = {
    "en_US" : en,
    "zh_CN" : zh,
    "ru_RU" : ru,
    "es_MX" : es,
    "fr_FR" : fr,
    "ko_KR" : ko,
    "ja_JP" : ja}
EXCHANGE_RATE = {
    "USD" : 1,
    "RMB" : 6.38,
    "JPY" : 109.18,
    "RUB" : 73.46,
    "MXN" : 19.85,
    "EUR" : 0.82,
    "KRW" : 1116.86,}
LOCALE_CURRENCY = {
    "en_US" : "USD",
    "zh_CN" : "RMB",
    "ru_RU" : "RUB",
    "es_MX" : "MXN",
    "fr_FR" : "EUR",
    "ko_KR" : "KRW",
    "ja_JP" : "JPY",}

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

selected_choice = tk.IntVar()
selected_choice.set(1)

selected_locale = tk.StringVar()
selected_locale.set("en_US")
LOCALE_FUNCTIONS["en_US"].install()
_ = LOCALE_FUNCTIONS["en_US"].gettext
locale.setlocale(locale.LC_ALL, "en_US")


shoes_1_price = 19.99
shoes_1_price_var = tk.StringVar()
shoes_1_price_var.set(format_price(shoes_1_price))
shoes_1_name = "Neon Star"
shoes_1_name_var = tk.StringVar()
shoes_1_name_var.set(shoes_1_name)

shoes_2_price = 29.99
shoes_2_price_var = tk.StringVar()
shoes_2_price_var.set(format_price(shoes_2_price))
shoes_2_name = "Converse Casual"
shoes_2_name_var = tk.StringVar()
shoes_2_name_var.set(shoes_2_name)

shoes_3_price = 15.99
shoes_3_price_var = tk.StringVar()
shoes_3_price_var.set(format_price(shoes_3_price))
shoes_3_name = "Slip-on Black"
shoes_3_name_var = tk.StringVar()
shoes_3_name_var.set(shoes_3_name)

photo_1_frame = tk.Frame(middle)
photo_1_frame.pack(side=tk.LEFT)
photo_1 = tk.PhotoImage(file="shoes/shoes_1.png")
photo_1_label = tk.Label(photo_1_frame, image=photo_1, textvariable=shoes_1_price_var, compound="top", bd=5)
photo_1_label.pack(side=tk.TOP)
R1 = tk.Radiobutton(photo_1_frame, text=shoes_1_name, variable=selected_choice, value=1, command=refresh_messages)
R1.pack(side=tk.BOTTOM)

photo_2_frame = tk.Frame(middle)
photo_2_frame.pack(side=tk.LEFT)
photo_2 = tk.PhotoImage(file="shoes/shoes_2.png")
photo_2_label = tk.Label(photo_2_frame, image=photo_2, textvariable=shoes_2_price_var, compound="top", bd=5)
photo_2_label.pack(side=tk.TOP)
R2 = tk.Radiobutton(photo_2_frame, text=shoes_2_name, variable=selected_choice, value=2, command=refresh_messages)
R2.pack(side=tk.BOTTOM)

photo_3_frame = tk.Frame(middle)
photo_3_frame.pack(side=tk.LEFT)
photo_3 = tk.PhotoImage(file="shoes/shoes_3.png")
photo_3_label = tk.Label(photo_3_frame, image=photo_3, textvariable=shoes_3_price_var, compound="top", bd=5)
photo_3_label.pack(side=tk.TOP)
R3 = tk.Radiobutton(photo_3_frame, text=shoes_3_name, variable=selected_choice, value=3, command=refresh_messages)
R3.pack(side=tk.BOTTOM)

selected_locale.trace("w", set_locale)

language_menu = tk.OptionMenu(top_bar, selected_locale, *LOCALE_FUNCTIONS.keys())
language_menu.pack(side=tk.LEFT)

message = "Your %s will arrive in %d days on %s."
message_var = tk.StringVar()
message_var.set(message)

message = tk.Label(bottom)
message.pack()

tk.mainloop()