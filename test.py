import Tkinter as tk
import time
import threading
import Queue
import requests
import tkMessageBox


main_window = tk.Tk()
def on_closing():
    if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
        main_window.destroy()
def timer_function(seconds):
    test_queues(seconds)
def test_queues(seconds):
    button.config(state = tk.DISABLED)
    time.sleep(seconds)
    tkMessageBox.showinfo('message', "passed {}".format(seconds))
    req = requests.get('https://www.google.com')
    tkMessageBox.showinfo('message',"status request {}".format(req.status_code))
    req2 = requests.get('https://mail.google.com')
    tkMessageBox.showinfo('message',"status second request {}".format(req2.status_code))
    for i in range(100):
            r = requests.get('https://www.google.com.mx')
            print("Result request {}".format(r.status_code))
    tkMessageBox.showinfo('message','all requests were done')
    button.config( state = tk.NORMAL)
tk.Label(main_window, text = 'Test').grid(row = 0)
button = tk.Button(main_window, text = 'click me', command=lambda : threading.Thread(target=timer_function, args = (2,) ).start() )
button.grid(row = 1)    
main_window.protocol("WM_DELETE_WINDOW", on_closing)

main_window.mainloop()

