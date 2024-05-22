from tkinter import *
import csv
from tkinter import messagebox
import os
def add_data():
    new_window_add_details = Toplevel(main_window)
  
    
    Label(new_window_add_details,text = "Enter the entry date in the format yyyy-mm-dd").grid(row = 0 , column = 0)
    entry_date = Entry( new_window_add_details)
    entry_date.grid(row = 0 , column = 1)
    Label(new_window_add_details,text = " Enter the amount you spent").grid(row = 1 , column = 0)
    entry_amount = Entry( new_window_add_details)
    entry_amount.grid(row = 1 , column  =1)

    Label(new_window_add_details,text = " enter the type of expense ").grid(row = 2 , column = 0)
    entry_expensetype = Entry(new_window_add_details)
    entry_expensetype.grid(row = 2 , column = 1)



    def submit():
     date = entry_date.get()
     amount = entry_amount.get()
     expense_type=entry_expensetype.get()

     if not date or not amount or not expense_type :
        messagebox.showwarning("input error ", "pleasei nput all the fields")
    
     entry_date.delete(0, END)
     entry_amount.delete(0, END)
     entry_expensetype.delete(0, END)

     messagebox.showinfo("lovely", "the data ahs been stored")

    

     expense = [date,amount,expense_type]
     with open('expenses.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(expense)
    submit_button = Button(new_window_add_details, text="Submit", command=submit)
    submit_button.grid(row = 4 , column = 0 , columnspan = 2 , pady=10)
     
    






def delete():
   
    new_window_delete = Toplevel(main_window)
    Label(new_window_delete, text='Enter the date of the expense you want to delete').pack()
    entry_which = Entry(new_window_delete)
    entry_which.pack()

    def confirm_delete():
        date_to_delete = entry_which.get()

        if not date_to_delete:
            messagebox.showwarning("Input Error", "You need to input the date")
            return

        expenses = []
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] != date_to_delete:
                    expenses.append(row)

        with open('expenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expenses)

        messagebox.showinfo("Success", "Expense deleted successfully")
        new_window_delete.destroy()

    delete_button = Button(new_window_delete, text="Delete", command=confirm_delete)
    delete_button.pack(pady=10)









def display():

    if not os.path.exists('expenses.csv') or os.path.getsize('expenses.csv') == 0:
        messagebox.showinfo("No Data", "No expenses to display")
        return

    expenses = []
    with open('expenses.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            expenses.append(row)

    new_window_display = Toplevel(main_window)
    new_window_display.title("All Expenses")

    text = Text(new_window_display)
    text.pack(padx=10, pady=10)

    for expense in expenses:
        text.insert(END, f"{expense}\n")
            
              



main_window = Tk()


#first label for welcoming 
entrance_welcome = Label(text = "welcome , choose from the options" , padx = 10 , pady = 10 , bd =10 , font = ('comic sans', 15) , bg = 'blue', fg ='#000000')
entrance_welcome.grid(row = 0 , column = 0 , columnspan = 2)


#buttons to choose options for the expense tracker
add_button = Button(main_window , text = "Add expense " , font =("arial", 15), command = add_data  , padx = 20 , pady = 20 , bd = 10 , relief = RAISED)
add_button.grid(row = 1 , column = 0)

delete_button = Button(main_window, text = "delete expense " , font =("arial", 15), command = delete , padx = 20 , pady = 20 ,bd = 10 , relief = RAISED)
delete_button.grid(row = 1 , column = 1)

show_button = Button(main_window , text = "show expenses " , font =("arial", 15), command = display , padx = 20 , pady = 20 ,bd = 10 , relief = RAISED)
show_button.grid(row = 2 , column = 0 , columnspan = 2)



#end the main window and display it 
main_window.mainloop()

