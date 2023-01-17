import tkinter as tk

# create a class which inherits frok Tkinker Buttons object with super() method
# for buttons which will insert a number or sign to entry box
# buttons have some repeatable properties build-in and allow to pass self to command
# which is button_clicked function which then will read their text and insert it 
class CalculatorButton(tk.Button):
    def __init__(self, master, text, row, column, command=None):
        super().__init__(master, text=text, command=lambda:command(self),
                         width=3, height=1, font=("Arial", 20))
        self.grid(row=row, column=column)

# inserting text of the calculator buttons to entry box
# condition needed to allow validate_entry_operators function to work properly 
def button_clicked(button):
    if validate_entry_operators(button["text"]):
        entry_box["state"] = tk.NORMAL
        entry_box.insert(tk.END, button["text"])
        entry_box["state"] = "readonly"
    
# allow multiple validate functions for entry box
def validate_entry(P):
    return validate_entry_len(P) and validate_entry_operators(P) \
        and validate_entry_restricted
    
# function restricting the length of entrybox
def validate_entry_len(P):
    if len(P) > 20:
        return False
    return True

# function which not allows consecutive special signs
def validate_entry_operators(P):
    operators = ["+","-","*","/","."]
    if len(P) > 0:
        last_char = entry_box.get()
        if last_char:
            last_char = last_char[-1]
        else:
            last_char = ""
        proposed_char = P[-1]
        if last_char in operators and proposed_char in operators:
            entry_box["state"] = tk.NORMAL
            entry_box.delete(len(entry_box.get())-1, tk.END)
            entry_box.insert(tk.END, proposed_char)
            entry_box["state"] = "readonly"
        else:
            return True

# function to allow keyboard input but restrict to key chars
def validate_entry_restricted(P):
    restricted = [str(range(10), "+","-","*","/",".")]
    proposed_char = P[-1]
    if proposed_char in restricted:
        entry_box["state"] = tk.NORMAL
        entry_box.insert(tk.END, proposed_char)
        entry_box["state"] = "readonly"
    else:
        return False

# backspace button function
def backspace_entrybox():
    entry_box["state"] = tk.NORMAL
    entry_box.delete(len(entry_box.get())-1, tk.END)
    entry_box["state"] = "readonly"

# clear button function
def clear_entrybox():
    entry_box["state"] = tk.NORMAL
    entry_box.delete(0, tk.END)
    entry_box["state"] = "readonly"
    
# equal button function which evaluates mathematical expression in entry box
def evaluate_entrybox():
    if entry_box.get():
        entry_box["state"] = tk.NORMAL
        try:
            result = eval(entry_box.get())
            entry_box["state"] = tk.NORMAL
            entry_box.delete(0, tk.END)
            entry_box.insert(tk.END, result)
            entry_box["state"] = "readonly"
        except (ZeroDivisionError, ValueError, SyntaxError, NameError) as e:
            entry_box["state"] = tk.NORMAL
            entry_box.delete(0, tk.END)
            entry_box.insert(tk.END, "Error")
            entry_box["state"] = "readonly"


# main app layout
root = tk.Tk()
root.geometry("500x400+50+50")
root.title("Calculator by ZP")
root.resizable(False, False)

frame_entry = tk.Frame(root, padx=5, pady=5)
frame_entry.pack()

frame_buttons = tk.Frame(root, padx=5, pady=5)
frame_buttons.pack()

entry_box = tk.Entry(frame_entry)
vcmd = (root.register(validate_entry), "%P")
entry_box.config(width=20, border=5, font=("Arial", 20), 
                 validate="key", validatecommand=vcmd, state="readonly")
#entry_box.bind()
entry_box.pack()

# avoid first click issue on the equal button by brute-force
entry_box.insert(0, "0")
evaluate_entrybox()
evaluate_entrybox()

# generation buttons with number or sign insertion
button0 = CalculatorButton(frame_buttons, "0", 4, 1, command=button_clicked)
button1 = CalculatorButton(frame_buttons, "1", 3, 0, command=button_clicked)
button2 = CalculatorButton(frame_buttons, "2", 3, 1, command=button_clicked)
button3 = CalculatorButton(frame_buttons, "3", 3, 2, command=button_clicked)
button4 = CalculatorButton(frame_buttons, "4", 2, 0, command=button_clicked)
button5 = CalculatorButton(frame_buttons, "5", 2, 1, command=button_clicked)
button6 = CalculatorButton(frame_buttons, "6", 2, 2, command=button_clicked)
button7 = CalculatorButton(frame_buttons, "7", 1, 0, command=button_clicked)
button8 = CalculatorButton(frame_buttons, "8", 1, 1, command=button_clicked)
button9 = CalculatorButton(frame_buttons, "9", 1, 2, command=button_clicked)
multiplication_button = CalculatorButton(frame_buttons, "/", 0, 1, command=button_clicked)
multiplication_button = CalculatorButton(frame_buttons, "*", 0, 2, command=button_clicked)
minus_button = CalculatorButton(frame_buttons, "-", 2, 3, command=button_clicked)
addition_button = CalculatorButton(frame_buttons, "+", 1, 3, command=button_clicked)
coma_button = CalculatorButton(frame_buttons, ".", 4, 2, command=button_clicked)

# generating buttons with other command functions
back_button = tk.Button(frame_buttons, text="<-", command=backspace_entrybox,
                    width=3, height=1, font=("Arial", 20))
back_button.grid(row=0, column=3)

clear_button = tk.Button(frame_buttons, text="C", command=clear_entrybox,
                    width=3, height=1, font=("Arial", 20))
clear_button.grid(row=0, column=0)

equal_frame = tk.Frame(frame_buttons)
equal_frame.grid(row=3, column=3, rowspan=2, columnspan=1)

equal_button = tk.Button(equal_frame, text="=", command=evaluate_entrybox,
                            width=3, height=3, font=("Arial", 20))
equal_button.pack()

#run main window
root.mainloop()