from tkinter import *
window=Tk()
window.title("First Application of Tkinter")
def click():
    entered_text=textentry.get()
    output.delete(0.0,END)
    
    try:
        defination=my_compdictionery[entered_text]
        Label(window,text="Yes in dictionery Check Console",fg="yellow",bg="red").grid(row=10,column=0)
        print(defination)
    except:
        defination="sorry there is no word in it please try again"
        output.insert(END,defination)


def close_window():
    window.destroy()
    exit()    
photo1=PhotoImage(file="C:\\Users\\hp\\Desktop\\panda copy.png")
Label(window,image=photo1,bg="black").grid(row=0,column=0)
Label(window,text="rishabh",fg="white",bg="black",font="none 12 bold").grid(row=1,column=0)
textentry=Entry(window,width=20,bg="white")
textentry.grid(row=2,column=0)
Button(window,text="SELECT",width=6,command=click).grid(row=3,column=0)

output=Text(window,width=75,height=6,wrap=WORD,background="white")
output.grid(row=5,column=0,columnspan=2,sticky=W)


my_compdictionery = {
    'algorithm' : 'A piece of code is called algorithm',  'bug' : 'Any Problem in a program'
    }

Label(window,text="Click To Exit:",bg="black",fg="white",font="none 12 bold").grid(row=6,column=0)

Button(window,text="CLOSE",width=6,command=close_window).grid(row=7,column=0)



    
window.mainloop()
