import time
import tkinter as tk
from PIL import Image, ImageTk # display img icons in tk


def show_pop(title,message):
    root=tk.Tk()
    root.title(title)

    screen_width= root.winfo_screenwidth()
    screen_height= root.winfo_screenheight()

    window_w=350
    window_h=120

    x=(screen_width//2)-(window_w//2)
    y=(screen_height//2)-(window_h//2)

    root.geometry(f"{window_w}x{window_h}+{x}+{y}")
    root.attributes("-topmost",True) # to stay on top of all tabs
    root.overrideredirect(True)
    img=Image.open("D:/Documents/Downloads/sad-cat.ico").resize((150, 150))
    photo = ImageTk.PhotoImage(img)

    icon_label=tk.Label(root,image=photo)
    icon_label.image=photo
    icon_label.pack(side="left", padx=10,pady=10)


    label=tk.Label(root,text=message,font=("Arial",12), justify="left", padx=10,pady=10)
    label.pack(side="left")

    root.after(5000,root.destroy)
    root.mainloop()
    icon_path = "D:/Documents/Downloads/sad-cat.ico"
while True:
    show_pop("~ ~ Break Time ~ ~", "System Shutting Down \nFor Break!\nCtrl+Alt+Cry Initiated")
    time.sleep(10)
