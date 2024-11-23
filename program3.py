import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
hours_var=tk.StringVar()
def callcalc(time):
    hours=int(hours_var.get())
    if time == 0:
        cost=hours*0.02
        tkinter.messagebox.showinfo(title="Cost of Call",message="Your total is "+str(cost))
    elif time == 1:
        cost=hours*0.12
        tkinter.messagebox.showinfo(title="Cost of Call",message="Your total is "+str(cost))
    elif time == 2:
        cost=hours*0.05
        tkinter.messagebox.showinfo(title="Cost of Call",message="Your total is "+str(cost))
hours_label=tkinter.Label(window,text="Input hours in field below:")
hours = tk.Entry(window,textvariable = hours_var, font=('calibre',10,'normal'))
daytime=tk.Button(window,text="Daytime (6:00-17:59)", command=lambda:callcalc(0),font=('calibre',10, 'bold'))
evening=tk.Button(window,text="Evening (18:00-23:59)", command=lambda:callcalc(1),font=('calibre',10, 'bold'))
off_peak=tk.Button(window,text="Off-Peak(0:00-5:59)", command=lambda:callcalc(2),font=('calibre',10, 'bold'))
hours_label.pack(),hours.pack(),daytime.pack(),evening.pack(),off_peak.pack()
window.mainloop()
