import customtkinter as ctk 

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.geometry('500x350')


def login():
    print('Battery Notifier')
    
    
frame = ctk.CTkFrame(master=root)
frame.pack(pady = 20, padx = 60, fill = 'both', expand = True)

label = ctk.CTkLabel(master = frame, text = "Battery Notifier Client", font = ("Roboto", 24))
label.pack(pady = 12, padx = 10)


def option1(choice):
    button_op1 = ctk.CTkButton(master = frame, command = None, text = "option1 ")
    button_op1.pack(pady=12, padx=10)
    
optionmenu = ctk.CTkOptionMenu(frame, values=["remind after crossing given battery percentage", "remind after using certain percentage of battery"], command = option1)
optionmenu.pack(pady= 12, padx = 10)
optionmenu.set("select mode")

button = ctk.CTkButton(master = frame, command = None, text = 'start')
button.pack(pady= 12, padx = 10)

root.mainloop()