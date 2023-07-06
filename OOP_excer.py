import tkinter as tk


class window(tk.Tk):
    def __init__(self):
        #this is creating window
        super(). __init__()

        self.title('bank account')
        self.height = 400
        self.width = 700
        size_geo = '%dx%d+%d+%d' % (self.width, self.height,
                     (self.winfo_screenwidth()-self.width)/2,
                     (self.winfo_screenheight()-self.height)/2)
        self.geometry(size_geo)
        #title 
        self.title_size = self.winfo_width()//20
        software_title = tk.Label(self,text = 'bank account_1',
                                  font = ('times', f"{self.title_size}", 
                                          'bold italic')) 
        software_title.pack(side = tk.TOP)
        #account
        account = tk.Label(self, text = 'account')
        account.place (relx = 0.05,y = 25)
        account_entry = tk.Entry(self, font = 'calibre')
        account_entry.place (relx = 0.25, y = 25)
        #balance
        Balance = tk.Label(self, text = 'balance')
        Balance.place(relx = 0.05, y =65)
        Balance_entry = tk.Entry(self, font='calibre')
        Balance_entry.place (relx = 0.25, y = 65)
        balance = float(Balance_entry.get())
        #amount
        Amount = tk.Label(self, text = 'amount')
        Amount.place (relx = 0.05, y =105)
        Amount_entry = tk.Entry(self, font ='calibre')
        Amount_entry.place (relx = 0.25, y=105)
        amount = Amount_entry.get() 
        #submit button
        deposite_button = tk.Button(self,text = 'deposite')
        deposite_button.place (relx = 0.5, y = 300) 

#this run the window
if __name__ == "__main__":
    app = window()
    app.mainloop()