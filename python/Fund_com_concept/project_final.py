from os import name
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import ttk
from datetime import datetime
from datetime import date
from tkinter.constants import FALSE
import json

#funtion_main_windows
def delete_one():
    de = lb_tasks.get("active")
    if de in score_list:
        score_list.remove(de)
    update_tasks()

def update_tasks():
    clear_listbox()
    for task in score_list:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def exit_app():
    confex = messagebox.askquestion(
        'Quit Confirmation', 'are you sue you want to quit?')
    if confex.upper() == "YES":
        root.destroy()
    else:
        pass

def save_act():
    savecon = messagebox.askquestion(
        'Save Confirmation', 'save your progress?')
    if savecon.upper() == "YES":
        with open("SaveHomework.json", "w",encoding='utf-8') as filehandle:
            for listitem in score_list :
                filehandle.write('%s %s %s %s %s %s %s %s\n' % listitem)
    else:
        pass

def load_act():
    loadcon = messagebox.askquestion(
        'Save Confirmation', 'save your progress?')
    if loadcon.upper() == "YES":
        score_list.clear()

        with open('SaveHomework.json', 'r',encoding='utf-8') as filereader:
            for line in filereader:
                currentask = line
                score_list.append(currentask)
            update_tasks()
    else:
        pass

#add_task_wimdows
def Add_task():
    M_window = Tk()
    M_window.title('Add_Homework')
    M_window.geometry('350x250')

    #funtion
    def clear_listbox():
        lb_tasks.delete(0, "end")
        combo.delete(0,"end")
        subject.clear()
        tasks.clear()
        timeremaining.clear()

    def update_tasks():
        clear_listbox()
        for task in score_list:
            lb_tasks.insert("end", task)
  
    def add_task():
        label_dsply["text"] = ""
        Ntask = text_input.get()
        v = combo.get()
        d = text_input_time_day.get()
        m = text_input_time_m.get()
        y = text_input_time_y.get()
        if Ntask != "":
            Ntask
        if v != '':
            v
        if d != "":
            d
        if m != "":
            m
        if y != "":
            date = str(d+'/'+m+'/'+y)
            today = datetime.today()
            d1 = today.strftime("%d/%m/%Y")
            d2 = date
            start = datetime.strptime(d1, "%d/%m/%Y")
            end = datetime.strptime(d2, "%d/%m/%Y")
            diff = end.date() - start.date()
            timeremaining.append(diff.days)
            subject.append(v)
            tasks.append(Ntask)
            lc = []
            sp = []
            for i in subject:
                i
            for x in tasks:
                x
            for t in timeremaining:
                p = (str(t))
            mix =  i + "___" + x 
            lc.append(mix)
            sp.append(p)
            list = sp+lc
            day = []
            mix = []
            c=0
            for i in list:
                if c%2==0:
                    i = int(i)
                    day.append(i)
                else:
                    mix.append(i)
                c+=1
            dic = dict()
            for i in range(len(mix)):
                dic[mix[i]] = int(day[i])
            a = []
            b = []
            for i in dic:
                a.append(i)
                b.append(dic[i])
            combined_dict = dict(zip(mix,day))
            for key in combined_dict:
                a = combined_dict[key]
                tp = ("Due",a," day from ",d1,'(due',date,')',key)
                score_list.append(tp)
            score_list.sort(reverse=FALSE)
            update_tasks()
            M_window.destroy()
        else:
            label_dsply["text"] = "please enter the text"
        text_input.delete(0, 'end')
        combo.delete(0,"end")

#GUI
    #add_the_button
    label_dsply = tkinter.Label(M_window, text="",pady=20)
    label_dsply.place(x=120,y=10)

    #select Sub.

    Label(M_window,text='select subject').place(x=15,y=5)
    choice = StringVar(value='select subject')
    combo = ttk.Combobox(M_window,textvariable=choice,width=35)
    combo['values'] = ('CALCULUS 1','COMPUTER PROGRAMMING','ENGINEERING DRAWING',
    'FOUNDATION. ENGLISH','GENERAL CHEMISTRY','GENERAL CHEMISTRY LABORATORY',
    'GENERAL PHYSICS 1','GENERAL PHYSICS LABORATORY 1','SPORTS AND RECREATIONAL ACTIVITIES')
    combo.place(x=95,y=5)


    label_ll = tkinter.Label(M_window, text="Task Name",pady=5)
    label_ll.place(x=140,y=55)
    text_input = tkinter.Entry(M_window, width=40)
    text_input.place(x=50,y=90)

    label_time_day = tkinter.Label(M_window, text="day",pady=5)
    label_time_day.place(x=45,y=120)
    text_input_time_day = tkinter.Entry(M_window, width=5)
    text_input_time_day.place(x=75,y=125)

    label_time_m = tkinter.Label(M_window, text="month",pady=5)
    label_time_m.place(x=120,y=120)
    text_input_time_m = tkinter.Entry(M_window, width=5)
    text_input_time_m.place(x=170,y=125)

    label_time_y = tkinter.Label(M_window, text="year",pady=5)
    label_time_y.place(x=205,y=120)
    text_input_time_y = tkinter.Entry(M_window, width=8)
    text_input_time_y.place(x=240,y=125)

    text_add_bttn = tkinter.Button(
        M_window, text="add homework", bg="white", fg="green", width=15, command=add_task)
    text_add_bttn.place(x=117,y=180)

#mainwindow
root = Tk()
root.title("Homework reminder")
root.geometry('800x300')
tasks = []
timeremaining = []
subject = []
score_list = []

label_title = tkinter.Label(root, text="Wellcome to Home work reminder",pady=10)
label_title.grid(row=0,column=1)

#add_button_main
Add_task = tkinter.Button(
    root, text="Add task", bg="white", fg="green", width=25,height=2, command=Add_task ,pady=5)
Add_task.grid(row=2,column=0)

delete = tkinter.Button(
    root, text="Delete", bg="white", fg="green", width=25,height=2, command=delete_one,pady=5)
delete.grid(row=3,column=0)

save = tkinter.Button(
    root, text="Save", bg="white", fg="green", width=25,height=2, command=save_act,pady=5)
save.grid(row=4,column=0)

load = tkinter.Button(
    root, text="Load savefile", bg="white", fg="green", width=25,height=2, command=load_act,pady=5)
load.grid(row=5,column=0)

exit = tkinter.Button(
    root, text="Exit", bg="white", fg="green", width=25,height=2, command=exit_app,pady=5)
exit.grid(row=6,column=0)

#lb_tasks = tkinter.Listbox(root,width=62,height=15)
lb_tasks = tkinter.Listbox(root,width=96,height=15)
lb_tasks.place(x=200,y=40)

#main loop
root.mainloop()
#//////////////////////////////////
#//////// f i n a l l y ///////////
#//////////////////////////////////