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
menu_list = ["Noodles", "Hamburger", "Salad", "Steak", "Fried Chicken", "Fried Rice", "Pizza", "Sushi", "Soup"] 
#NEED MORE MENU
window.iconbitmap('image/qmark.ico')

def randMenu():
    rand_int = random.randint(0,len(menu_list)-1)
    rand_label = tk.Label(window, text = menu_list[rand_int] ,width = 50, bg = bgcolor, fg = fcolor)
    rand_label.configure(font = ("Helvetica", 16, "bold"))
    rand_label.place(x = 220, y = 115, anchor = "center")

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

label = tk.Label(window, text = "Click the button to random menu", width = 50, bg = bgcolor, fg = "grey15")
rand_butt = tk.Button(window, text = "Random!", command = randMenu, width = 10)
rand_butt.configure(font = ("Helvetica", 10, "bold"))
add_butt = tk.Button(window, text ="Add Menu", command = addMenu, width = 10)

add_butt.place(x = 180, y = 210)
rand_butt.place(x = 175, y = 180)
label.place(x = 45, y = 105)

window.mainloop()
