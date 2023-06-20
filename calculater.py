###Author Yang Date 2023/6/20
###Goal: deal linear calculation
import tkinter as tk 
import tkinter.messagebox

win = tk.Tk()
win.title ('linear calculation')
win.geometry('600x400')

'''
def calculater(P_3):
    Y = ((P_1_Y_entry)-(P_2_Y_entry))/((P_1_X_entry) - (P_2_X_entry))*((P_3_X_entry) - (P_1_X_entry)) + (P_1_Y_entry)
    return calculater(P_3)
'''
def submit():
    P_3 = [float(P_1_Y_entry.get()),float(P_2_Y_entry.get()),float(P_3_X_entry.get()),float(P_1_X_entry.get()),float(P_2_X_entry.get())]
    P_3_Y = (int(P_1_Y_entry.get())-int(P_2_Y_entry.get()))/(int(P_1_X_entry.get()) - int(P_2_X_entry.get()))*(int(P_3_X_entry.get()) - int(P_1_X_entry.get())) + int(P_1_Y_entry.get())
    '''
    P_3_Y = calculater(P_3)
    '''
    print(P_3_Y)
    tk.Label(win, text = P_3_Y).grid(row = 2, column = 0)

P_1_X_entry = tk.Entry(win,  font=('calibre',10,'normal'))
P_1_Y_entry = tk.Entry(win,  font=('calibre',10,'normal'))
P_2_X_entry = tk.Entry(win,  font=('calibre',10,'normal'))
P_2_Y_entry = tk.Entry(win,  font=('calibre',10,'normal'))
P_3_X_entry = tk.Entry(win,  font=('calibre',10,'normal'))
sub_btn = tk.Button(win, text = 'sumbit', command = submit)

P_1_X_entry.grid(row = 3, column = 1)
P_1_Y_entry.grid(row = 0, column = 1)
P_2_X_entry.grid(row = 3, column = 2)
P_2_Y_entry.grid(row = 0, column = 2)
P_3_X_entry.grid(row = 3, column = 3)
sub_btn.grid(row = 5, column = 4)



def close_1():      # to quit the whole window
            #this func is for unintended activation
    res = tkinter.messagebox.askquestion('Exit the calculator',
                                                'Are you sure to exit')  
    if res ==  'yes':
        win.destroy()

    else :
        None
    Button = tk.Button(win, text = 'Quit', width=10, height=5, command = close_1)
    Button.place(x=400,y=20)
win.mainloop()

