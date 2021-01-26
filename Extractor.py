import tkinter

window=tkinter.Tk()
window.title("new")
tkinter.Label(window,text="File Extractor App",bg="black",fg="white",pady=10,width=500,font=10).pack()
tkinter.Label(window).pack()
tkinter.Label(window).pack()
entry=tkinter.Entry(window,width=70,font=10)
entry.pack()
tkinter.Label(window).pack()
tkinter.Label(window).pack()
entry1=tkinter.Entry(window,width=70,font=10)
entry1.pack()
tkinter.Label(window).pack()
def create():
      if entry.get():
           f=open(entry.get(), "r")
           k=open(entry1.get(),"w")
           h=f.read()
           k.write(h)
           f.close()
           k.close()
       



b=tkinter.Button(window, text="Extract",command=create,bg="black",fg="white",padx=20,font=5)
b.pack()
tkinter.Label(window).pack()
tkinter.Label(window).pack()



