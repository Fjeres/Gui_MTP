from tkinter import *
from textwrap import wrap
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
def add_text(event, temp):
    temp += lbl['text']
    temp_list = list(temp)
    if event.keysym == "BackSpace" or event.keysym == 'Delete':
        index = temp_list.index('|')
        if index != 0:
            temp_list.remove("|")
            temp_list[index - 1] = '|'
        temp = ''.join(temp_list)
        lbl.configure(text=temp)
        return lbl.configure(text=temp)
    elif event.keysym == 'Left':
        index = temp_list.index("|")
        if index != 0: temp_list[index], temp_list[index - 1] = temp_list[index - 1], temp_list[index]
        temp = ''.join(temp_list)
        lbl.configure(text=temp)
    elif event.keysym == 'Right':
        index = temp_list.index("|")
        if index != len(temp) - 1: temp_list[index], temp_list[index + 1] = temp_list[index + 1], temp_list[index]
        temp = ''.join(temp_list)
        lbl.configure(text=temp)
    elif event.keysym == 'Up':
       #47
        if len(temp_list) > 47:
            index = temp_list.index("|")
            temp_list.remove("|")
            temp_list.insert(index-46,'|')
            temp = ''.join(temp_list)
            lbl.configure(text=temp)

        lbl.configure(text=temp)
    elif event.keysym == 'Down':
        if len(temp_list) > 47:
            index = temp_list.index("|")
            temp_list.remove("|")
            temp_list.insert(index+46,'|')
            temp = ''.join(temp_list)
            lbl.configure(text=temp)
    elif event.keysym == 'Home':
            temp_list.remove("|")
            temp_list.insert(0,'|')
            temp = ''.join(temp_list)
            lbl.configure(text=temp)
    elif event.keysym == 'End':
        temp_list.remove("|")
        temp_list.insert(len(temp_list), '|')
        temp = ''.join(temp_list)
        lbl.configure(text=temp)
    else:
        if len(temp) != 0:
            index = temp_list.index("|")
            temp_list.insert(index, str(event.char))
            temp = ''.join(temp_list)
            return lbl.configure(text=temp)
        else:
            temp += str(event.char) + '|'
            return lbl.configure(text=temp)

def openfile():
    filename = askopenfilename(parent=root)
    f = open(filename, encoding='UTF-8')
    temp = f.read()
    temp +="|"
    return lbl.configure(text=temp)

def savefile():
    f = asksaveasfile(mode='w', defaultextension=".txt")
    temp = lbl['text']
    temp_list = list(temp)
    temp_list.remove("|")
    temp = ''.join(temp_list)
    f.write(temp)





root = Tk()
temp = ''
root.minsize(width=800, height=400)
root.bind('<Key>', lambda e, temp=temp: add_text(e, temp))
lbl = Label(root, text=temp, font="Arial 20", justify=LEFT, wraplength=700)
lbl.grid(column=0, row=0)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
root.update()
root.mainloop()
