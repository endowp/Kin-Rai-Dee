import tkinter as tk
import random

#TKinter color chart website: http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
bgcolor = "sandy brown"
fcolor = "saddle brown"

window = tk.Tk()
window.title("Kin Rai Dee")
window.geometry("450x250")
window.configure(bg = bgcolor)
window.resizable(0, 0)
menu_list = ["Noodles", "Hamburger", "Salad", "Steak", "Fried Chicken", "Fried Rice", "Pizza", "Sushi", "Soup", \
    "Pasta", "Ramen", "Bento", "Curry", "Shabu", "Suki"] 
th_menu_list = ["ข้าวต้ม", "ก๋วยเตี๋ยว", "ข้าวมันไก่", "ข้าวขาหมู", "ผัดกะเพรา", "บะหมี่เกี๊ยว", "ข้าวผัด", "แกงจืด", "ต้มยำ", \
    "แกงเขียวหวาน", "ไข่เจียว", "ผัดไทย", "หอยทอด", "ข้าวหน้าเป็ด", "ส้มตำ", "ยำ", "ผัดพริกแกง", "ข้าวซอย", "น้ำพริก", \
    "ขนมจีน", "ไก่ย่าง", "ผัดขี้เมา", "คะน้าหมูกรอบ", "ผัดผงกะหรี่", "ไก่ผัดขิง", "พะแนง", "ฉู่ฉี่", "ผัดซีอิ้ว", "ก๋วยเตี๋ยวคั่วไก่"]
#NEED MORE MENU
window.iconbitmap('image/qmark.ico')
menu_mode = 1 #1 is eng, -1 is th

def randMenu():
    rand_int = random.randint(0,len(menu_list)-1)
    if(menu_mode == 1):
        rand_label = tk.Label(window, text = menu_list[rand_int] ,width = 50, bg = bgcolor, fg = fcolor)
        rand_label.configure(font = ("CityBlueprint", 24, "bold"))
    else:
        rand_label = tk.Label(window, text = th_menu_list[rand_int] ,width = 50, bg = bgcolor, fg = fcolor)
        rand_label.configure(font = ("CityBlueprint", 22))
    rand_label.place(x = 220, y = 115, anchor = "center")

def swapMenu():
    global menu_mode
    menu_mode = -1 * menu_mode

def addMenu(): #NOT FINISHED YET, CAN'T ADD NEW MENU
    popup = tk.Tk()
    popup.wm_title("Add Menu")
    popup.geometry("225x125")
    popup.configure(bg = bgcolor)
    popup.resizable(0, 0)
    popup.iconbitmap('image/qmark.ico')

    label = tk.Label(popup, text = "Insert Menu", bg = bgcolor, fg = fcolor)
    label.configure(font = ("Helvetica", 10, "bold"))
    toadd_butt = tk.Button(popup, text = "add", command = popup.destroy)
    close_butt = tk.Button(popup, text = "close", command = popup.destroy)
    new_menu = tk.Entry(popup)

    label.pack(side = "top", fill="x", pady = 10)
    new_menu.pack(side = "top")
    toadd_butt.pack()
    close_butt.pack()
    new_menu.pack()

    popup.mainloop()

init_label = tk.Label(window, text = "Click \"Random!\" to random menu", width = 50, bg = bgcolor, fg = "white")
init_label.configure(font = ("CityBlueprint", 16, "bold"))
rand_butt = tk.Button(window, text = "Random!", command = randMenu, width = 10)
rand_butt.configure(font = ("Helvetica", 10, "bold"))
add_butt = tk.Button(window, text ="Add Menu", command = addMenu, width = 10)
swap_butt = tk.Button(window, text ="Swap International/Thai menu", command = swapMenu, width = 24)
swap_butt.configure(font = ("Helvetica", 8))

init_label.place(x = -22, y = 105)
rand_butt.place(x = 175, y = 180)
add_butt.place(x = 180, y = 210)
swap_butt.place(x = 290, y = 220)

window.mainloop()
