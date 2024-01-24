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

entry1 = None