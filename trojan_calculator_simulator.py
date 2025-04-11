import os
import tkinter as tk


def perform_calculation():
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        operation = selected_oper.get()

        if operation == "+":
            result= num1+num2
        elif operation == "-":
            result= num1-num2
        elif operation == "*":
            result= num1*num2
        elif operation == "/":
            if num2!=0:
                result= num1/num2
            else:
                result_lbl.config(text="Error! Division by zero.")
                return
        result_lbl.config(text="Result: "+ str(result))

        Payload()
    except ValueError:
        result_lbl.config(text="Invalid Input. Please enter Valid numbers.")


def Payload():
    with open("fake_file.txt","w") as fake_file:
        fake_file.write("this is a fake file created by the trojan simulator .")
    print("Done")




#Main Window
window = tk.Tk()
window.title("Simple Calculator")

#input fields for num
entry1 = tk.Entry(window)
entry1.grid(row=0,column=0,padx=10,pady=10)

entry2 = tk.Entry(window)
entry2.grid(row=0,column=1,padx=10,pady=10)

#dropdown for operations

selected_oper=tk.StringVar(window)
selected_oper.set("+")

oper_menu=tk.OptionMenu(window,selected_oper,"+","-","/","*")
oper_menu.grid(row=1,column=0,columnspan=2,pady=10)

#button
calcul_btn=tk.Button(window,text="Calculate",command=perform_calculation)
calcul_btn.grid(row=2,column=0,columnspan=2,pady=10)

#label
result_lbl=tk.Label(window,text="Result: ")
result_lbl.grid(row=3,column=0,columnspan=2,pady=10)

#run the GUI
window.mainloop()