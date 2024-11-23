import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
window.geometry("600x400")
pricetotal=0
def shopping(cost):
    global pricetotal
    pricetotal+=cost
oilchange=tk.Button(window,text="Oil Change $30", command=lambda:shopping(30),font=('calibre',10, 'bold'))
lube=tk.Button(window,text="Lube Job $20", command=lambda:shopping(20),font=('calibre',10, 'bold'))
radiatorflush=tk.Button(window,text="Radiator Flush $40", command=lambda:shopping(40),font=('calibre',10, 'bold'))
transmissionfluid=tk.Button(window,text="Transmission Fluid $100", command=shopping(100),font=('calibre',10, 'bold'))
inspection=tk.Button(window,text="Inspection $35", command=lambda:shopping(35),font=('calibre',10, 'bold'))
muffler=tk.Button(window,text="Muffler Replacement $200", command=lambda:shopping(200),font=('calibre',10, 'bold'))
tirerotation=tk.Button(window,text="Tire Rotation $20", command=lambda:shopping(20),font=('calibre',10, 'bold'))
def submit():
    global pricetotal
#to be fully honest with you, during testing pricetotal kept reading out as 100 and i don't know why so the -100 is a patchwork solution (maybe its something with global variables or smthn else in my code but idk)
    tkinter.messagebox.showinfo(title="Order Total",message="Your total is $"+str(pricetotal-100))
submitbutton=tk.Button(window,text="Submit Order", command=submit,font=('calibre',10, 'bold'))
oilchange.pack()
lube.pack()
radiatorflush.pack()
inspection.pack()
muffler.pack()
tirerotation.pack()
submitbutton.pack()
window.mainloop()
