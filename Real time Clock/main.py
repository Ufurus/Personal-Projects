import tkinter as tk; import datetime

root = tk.Tk(
    baseName='Clock',
    screenName='Clock',
    className='Clock',
    useTk=1,
)

root.geometry("600x300+10+10")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.minsize(600, 300)
root.maxsize(600, 300)
root.config(bg='black')

Time = tk.Label(root, fg='limegreen', bg='black', font=('Consolas', 20))
Time.pack()

def time():
    time_now = datetime.datetime.now()
    Time.config(text=time_now.strftime("%H:%M:%S"))
    Time.after(1000, time)

time()
root.mainloop()