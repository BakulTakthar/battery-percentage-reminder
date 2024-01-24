import customtkinter as ctk 
import tkinter as tk
option1 = "remind after crossing given battery percentage"
option2 = "remind after using certain percentage of battery"

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

root = ctk.CTk()
root.geometry('500x350')


def login():
    print('Battery Notifier')
    
    
frame = ctk.CTkFrame(master=root)
frame.pack(pady = 20, padx = 60, fill = 'both', expand = True)

label = ctk.CTkLabel(master = frame, text = "Battery Notifier Client", font = ("Roboto", 24))
label.pack(pady = 12, padx = 10)

tabview = ctk.CTkTabview(root)
tabview.pack()

tab1 = tabview.add("utils")
tab2 = tabview.add(" remind after \n crossing given battery percentage ")
tab2 = tabview.add(" remind after \n using certain percentage of battery ")

tabview.set("utils")


START_BUTTON1 = ctk.CTkButton(tabview.tab(" remind after \n crossing given battery percentage "), text="start")
START_BUTTON1.pack()


START_BUTTON2 = ctk.CTkButton(tabview.tab(" remind after \n using certain percentage of battery "), text="start")
START_BUTTON2.pack()
# def option(choice):
#     button_op2 = ctk.CTkButton(master = frame, command = None, text = "option2 ")
#     button_op1 = ctk.CTkButton(master = frame, command = None, text = "option1 ")
#     if choice == option1:
#         def option1_cmd():
#             button_op2.widget.pack_forget()
#             button_op1.pack(pady=12, padx=10)
#         option1_cmd()
        
#     if choice == option2:
#         def option2_cmd():
#             button_op1.widget.pack_forget()
#             button_op2.pack(pady=12, padx=10)
#         option2_cmd()
    
# optionmenu = ctk.CTkOptionMenu(frame, values=[option1, option2], command = option)
# optionmenu.pack(pady= 12, padx = 10)
# optionmenu.set("select mode")

# button = ctk.CTkButton(master = frame, command = None, text = 'start')
# button.pack(pady= 12, padx = 10)

root.mainloop()