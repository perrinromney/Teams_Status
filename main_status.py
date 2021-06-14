import test_client
import tkinter as tk
import time
baseColor = 'green'

gui = tk.Tk(className='Window Color Example')
gui.geometry("400x200")
gui.wm_attributes("-topmost",1)
def Refresher():
    presence = test_client.fetch_presence()
    activity = presence['activity']
    if activity == 'InACall':
        color = 'red'
    else:
        color = baseColor
    gui.configure(bg=color)
    gui.after(5000,Refresher)
Refresher()
gui.mainloop()