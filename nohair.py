from tkinter import*
from pynput.keyboard import Key, Listener
from threading import Thread

print("Nohair has launched succesfully. V1.0")
print("Use the Up and Down arrow to disable and enable the crosshair.")

def show():
    global label, root
    print("Crosshair On")
    root = Tk()
    scrnwidth = root.winfo_screenwidth()
    scrnheight = root.winfo_screenheight()
    sw = scrnwidth - 22
    sh = scrnheight - 60
    dsw = str(int(sw / 2))
    dsh = str(int(sh / 2))
    label = Label(root, text="+", font=('Arial','20'), fg='red', bg='black')
    label.master.overrideredirect(True)
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "black")
    label.master.geometry("+"+dsw+"+"+dsh)
    label.pack()
    root.mainloop()


def remove():
    print("Crosshair Off")
    label.destroy()
    root.withdraw()
    
    

def released(key):
    if key == Key.up:
         thread = Thread(target=show)
         thread.start()
    elif key == Key.down:
        remove()
              

with Listener(on_release=released) as listener:
    listener.join()
