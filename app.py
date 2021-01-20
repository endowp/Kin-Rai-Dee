import tkinter as tk
import random

#TKinter color chart website: http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
bgcolor = "sandy brown"
fcolor = "saddle brown"
buttcolor = "light salmon" 
buttfcolor = "maroon"
buttprescolor = "salmon" #Salmon is the best food ever

window = tk.Tk()
window.title("Kin Rai Dee - What2Eat")
window.geometry("450x250")
window.configure(bg = bgcolor)
window.resizable(0, 0) #disable resizing

menu_list = ["Noodles", "Hamburger", "Salad", "Steak", "Fried Chicken", "Fried Rice", "Pizza", "Sushi", "Soup", \
    "Pasta", "Ramen", "Bento", "Curry", "Shabu", "Suki"] 
th_menu_list = ["ข้าวต้ม", "ก๋วยเตี๋ยว", "ข้าวมันไก่", "ข้าวขาหมู", "ผัดกะเพรา", "บะหมี่เกี๊ยว", "ข้าวผัด", "แกงจืด", "ต้มยำ", \
    "แกงเขียวหวาน", "ไข่เจียว", "ผัดไทย", "หอยทอด", "ข้าวหน้าเป็ด", "ส้มตำ", "ยำ", "ผัดพริกแกง", "ข้าวซอย", "น้ำพริก", \
    "ขนมจีน", "ไก่ย่าง", "ผัดขี้เมา", "คะน้าหมูกรอบ", "ผัดผงกะหรี่", "ไก่ผัดขิง", "พะแนง", "ฉู่ฉี่", "ผัดซีอิ้ว", "ก๋วยเตี๋ยวคั่วไก่"] 

icon = 'image/qmark.ico'
window.iconbitmap(icon)
menu_mode = 1 #1 is eng, -1 is th

def randMenu(): #random a menu
    if(menu_mode == 1):
        rand_int = random.randint(0, len(menu_list)-1)
        rand_label = tk.Label(window, text = menu_list[rand_int], width = 50, bg = bgcolor, fg = fcolor)
        rand_label.configure(font = ("CityBlueprint", 28, "bold"))
    else:
        rand_int = random.randint(0, len(th_menu_list)-1)
        rand_label = tk.Label(window, text = th_menu_list[rand_int], width = 50, bg = bgcolor, fg = fcolor)
        rand_label.configure(font = ("CityBlueprint", 28))
    rand_label.place(x = 220, y = 115, anchor = "center")

def swapMenu(): #swap btw international and Thai menu
    global menu_mode
    menu_mode = -1 * menu_mode
    randMenu()

def addMenu(): #to add new menu to th_menu_list or menu_list
    
    def addNewMenu():
        menu_list.append(menu_entry.get())
        added("international")

    def addNewThMenu():
        th_menu_list.append(menu_entry.get())
        added("Thai")

    def added(type): #added successfully popup window
        added_popup = tk.Tk()
        added_popup.wm_title("Added")
        added_popup.geometry("280x75")
        added_popup.configure(bg = bgcolor)
        added_popup.iconbitmap(icon)

        added_label = tk.Label(added_popup, text = menu_entry.get() + " was added to " + type + " menu", bg = bgcolor, fg = fcolor, activebackground = buttprescolor)
        added_label.configure(font = ("Helvetica", 11))
        added_label.pack(side = "top", fill = "x", pady = 10)
        ok_butt = tk.Button(added_popup, text = "OK", command = added_popup.destroy, bg = buttcolor, fg = buttfcolor, activebackground = buttprescolor)
        ok_butt.pack()

        added_popup.mainloop()

    popup = tk.Tk()
    popup.wm_title("Add Menu")
    popup.geometry("225x165")
    popup.configure(bg = bgcolor)
    popup.resizable(0, 0)
    popup.iconbitmap(icon)

    label = tk.Label(popup, text = "Insert New Menu", bg = bgcolor, fg = fcolor)
    label.configure(font = ("Helvetica", 11, "bold"))
    close_butt = tk.Button(popup, text = "close", command = popup.destroy, bg = buttcolor, fg = buttfcolor, activebackground = buttprescolor)
    menu_entry = tk.Entry(popup, bg = "navajo white")
    toadd_butt = tk.Button(popup, text = "add to international menu", command = addNewMenu, bg = buttcolor, fg = buttfcolor, activebackground = buttprescolor)
    toaddth_butt = tk.Button(popup, text = "add to Thai menu", command = addNewThMenu, bg = buttcolor, fg = buttfcolor, activebackground = buttprescolor)
    
    label.place(x = 52, y = 16)
    menu_entry.place(x = 53, y = 42)
    toadd_butt.place(x = 40, y = 70)
    toaddth_butt.place(x = 60, y = 100)
    close_butt.place(x = 94, y = 130)
   
    popup.mainloop()

init_label = tk.Label(window, text = "Click \"Random!\" to random menu", width = 50, bg = bgcolor, fg = "white")
init_label.configure(font = ("CityBlueprint", 16, "bold"))
rand_butt = tk.Button(window, text = "Random!", command = randMenu, width = 10, bg = buttcolor, fg = buttfcolor, activebackground = buttprescolor)
rand_butt.configure(font = ("Helvetica", 12, "bold"))
add_butt = tk.Button(window, text ="Add Menu", command = addMenu, width = 10, bg = buttcolor, fg = buttfcolor, activebackground = buttprescolor)
swap_butt = tk.Button(window, text ="Swap international/Thai menu", command = swapMenu, width = 24, bg = buttcolor, fg = buttfcolor, activebackground = buttprescolor)
swap_butt.configure(font = ("Helvetica", 8))

init_label.place(x = -22, y = 105)
rand_butt.place(x = 166, y = 180)
add_butt.place(x = 180, y = 218)
swap_butt.place(x = 290, y = 220)

window.mainloop()