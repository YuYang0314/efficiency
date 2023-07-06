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
    P_3_Y = (float(P_1_Y_entry.get())-float(P_2_Y_entry.get()))/(float(P_1_X_entry.get()) 
            - float(P_2_X_entry.get()))*(float(P_3_X_entry.get()) - float(P_1_X_entry.get())) 
    + float(P_1_Y_entry.get())
    '''
    P_3_Y = calculater(P_3)
    '''
    print(P_3_Y)
    tk.Label(win, text = P_3_Y).place(x = 0, y = 125)
def close_1():      # to quit the whole window
            #this func is for unintended activation
    res = tkinter.messagebox.askquestion('Exit the calculator',
                                                'Are you sure to exit')  
    if res ==  'yes':
        win.destroy()

    else :
        None
P_1_X_entry = tk.Entry(win,  font=('calibre',10,'normal'))
P_1_Y_entry = tk.Entry(win,  font=('calibre',10,'normal'))
P_2_X_entry = tk.Entry(win,  font=('calibre',10,'normal'))
P_2_Y_entry = tk.Entry(win,  font=('calibre',10,'normal'))
P_3_X_entry = tk.Entry(win,  font=('calibre',10,'normal'))
subtract_label_L1 = tk.Label(win, text = '-', font = ('calibre', 10, 'bold'))
subtract_label_L2 = tk.Label(win, text = '-', font = ('calibre', 10, 'bold'))
sub_btn = tk.Button(win, text = 'sumbit', command = submit)

P_1_X_entry.place(x = 50, y = 150)
P_1_Y_entry.place(x = 50, y = 100)
P_2_X_entry.place(x = 215, y = 150)
P_2_Y_entry.place(x = 215, y = 100)
P_3_X_entry.place(x = 375, y = 125)
subtract_label_L1.place(x = 199, y = 100)
subtract_label_L2.place(x = 199, y = 150)
sub_btn.place(x = 200, y = 300)




Button = tk.Button(win, text = 'Quit', width=5, height=1, command = close_1)
Button.place(x=350,y=300)
win.mainloop()

