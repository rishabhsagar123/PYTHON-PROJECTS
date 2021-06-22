import tkinter.tix as tix
import tkinter.messagebox as mb
top=tix.Tk()
hello=tix.NoteBook(top,width=100,height=100)
hello.pack(expand=True,fill='both')

hello.add('page1',label="Text")
f1=tix.Frame(hello.subwidget('page1'))
st=tix.ScrolledText(f1)
st.subwidget('text').insert("1.0","Here is the text")
st.pack(expand=True)
f1.pack()

hello.add('page2',label="Message Boxes")
f2=tix.Frame(hello.subwidget('page2'))
tix.Button(f2,text="error",bg="lightblue",command=lambda t="hello",m="this is not good" : mb.showinfo(t,m)).pack(fill='x',expand=True) 
f2.pack(side='top',fill='x')
hello.mainloop()
