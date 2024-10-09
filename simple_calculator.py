import tkinter as tk
#ساخت پنجره و دادن تایتل و ابعاد
win=tk.Tk()
win.title("Calculator")
win.config(background="#F2E8C6")
win.geometry("300x450+500+100")
win.resizable(False,False)

#ساخت توابع برای عملیات هامون

def sum():
    try:
        number1=int(entry1.get())
        number2=int(entry2.get())
        end=number1+number2
        label.config(text=f"{end}")
    except Exception:
        label.config(text=f"Error value")
    
def sub():
    try:
        number1=int(entry1.get())
        number2=int(entry2.get())
        end=number1-number2
        label.config(text=f"{end}")
    except Exception:
        label.config(text=f"Error value")

def mul():
    try:
        number1=int(entry1.get())
        number2=int(entry2.get())
        end=number1*number2
        label.config(text=f"{end}")
    except Exception:
        label.config(text=f"Error value")
    
def div():
    try:
        number1=int(entry1.get())
        number2=int(entry2.get())
        end=number1/number2
        label.config(text=f"{end}")  
    except Exception:
        label.config(text=f"Error value") 



#گرفتن ورودی ها
entry1=tk.Entry(win,background="#BCF2F6",width=10,font=("Arial",25))
entry1.grid(row=0,column=0,padx=5,pady=5)
entry2=tk.Entry(win,background="#B7B7B7",width=10,font=("Arial",25))
entry2.grid(row=1,column=0,padx=5,pady=5)

#ساخت کلید هامون
btn1=tk.Button(win,
               background="#697565",
               foreground="white",
               padx=20,
               pady=20,
               anchor='ne',
               text="+",
               font=(50),
               command=sum)
btn1.grid(row=2,column=0,padx=5,pady=5)

btn2=tk.Button(win,
               background="#697565",
               foreground="white",
               padx=20,
               pady=20,
               anchor='ne',
               text="-",
               font=(50),
               command=sub)
btn2.grid(row=2,column=1,padx=5,pady=5)


btn3=tk.Button(win,
               background="#697565",
               foreground="white",
               padx=20,
               pady=20,
               anchor='ne',
               text="x",
               font=(50),
               command=mul)
btn3.grid(row=3,column=0,padx=5,pady=5)

btn4=tk.Button(win,
               background="#697565",
               foreground="white",
               padx=20,
               pady=20,
               anchor='ne',
               text="/",
               font=(50),
               command=div)
btn4.grid(row=3,column=1,padx=5,pady=5)

#ساخت دکمه خروج
exit_btn=tk.Button(win,background="#FF6969",padx=5,pady=5,text="Exit",command=win.destroy)
exit_btn.grid(row=1,column=5,padx=5,pady=5)

#نمایش نتیجه
label= tk.Label(win,text="result",font=("Arial",25),background="#B99470",foreground="#000000",padx=5,pady=20)
label.grid(row=6,columnspan=2,padx=40,pady=40)
tk.mainloop()