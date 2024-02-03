'''
# TODO: Make UTILS tab
# TODO: fix paddding
# TODO: add event callback
# TODO: mkae it prettier :)
'''

'''#? master frame'''
# import target_percent
import customtkinter as ctk
import psutil

battery = psutil.sensors_battery()  # Update the battery information inside the loop
current_percent = battery.percent
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()

root.geometry('720x480')


def login():
    print('Battery Notifier')


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60)

label = ctk.CTkLabel(master=frame, text="Battery Notifier Client", font=("Roboto", 24))
label.pack()

lable2 = ctk.CTkLabel(master=frame, text="created by Bakul Takthar 2024", font=("Roboto", 12), )
lable2.pack()
# progressbar.set(target_percent.current_percent/100)
if current_percent >= 50:
    progressbar = ctk.CTkProgressBar(master = frame, orientation="horizontal", progress_color='green', border_color='black', fg_color='grey', width = 200, height = 15)
    progressbar.set(current_percent/100)
    
if current_percent <= 35:
    progressbar = ctk.CTkProgressBar(master = frame, orientation="horizontal", progress_color='orange', border_color='black', fg_color='grey', width = 200, height = 15)
    progressbar.set(current_percent/100)
    
progressbar.pack()
'''#? Tabview Starts'''
tabview = ctk.CTkTabview(root)
tabview.pack(expand=True, fill='both', padx=20, pady=20)

tab1 = tabview.add("utils")
tab2 = tabview.add("🔢 remind after \n crossing given battery percentage ")
tab3 = tabview.add("⏱️ remind after \n using certain percentage of battery ")

tabview.set("utils")

'''#? Tab 1'''
textbox0 = ctk.CTkTextbox(tab1, width=450, height=120)

textbox0.insert("0.0", "this mode helps you by reminding you to plug your device in when you cross a given battery level.\n EG- \n \
    What battery percent do you want to be notified at?\n>> 25\
        \nyou will be notified at '25 percent battery'")  # insert at line 0 character 0
text = textbox0.get("0.0", "end")  # get text from line 0 character 0 till the end

textbox0.configure(state="disabled")  # configure textbox to be read-only
textbox0.pack(pady = 20)
'''tab2'''
textbox1 = ctk.CTkTextbox(tab2, width=450, height=120)

textbox1.insert("0.0", "this mode helps you by reminding you to plug your device in when you cross a given battery level.\n EG- \n \
    What battery percent do you want to be notified at?\n>> 25\
        \nyou will be notified at '25 percent battery'")  # insert at line 0 character 0
text = textbox1.get("0.0", "end")  # get text from line 0 character 0 till the end

'''#? Tab 2'''

textbox1.configure(state="disabled")  # configure textbox to be read-only
textbox1.pack(pady = 20)

value_enter1 = ctk.CTkEntry(tab2, placeholder_text='enter the battery percentage to be reminded at')
value_enter1.pack(pady=20)

START_BUTTON1 = ctk.CTkButton(tab2, text="start")
START_BUTTON1.pack(pady=10)

'''#? Tab3'''

textbox2 = ctk.CTkTextbox(tab3, width=450, height=120)

textbox2.insert("0.0", "this mode helps you by reminding you to plug your device in when you cross a given battery percentage range.\n EG- \n \
    how often should the notifications be sent?\n>> 5\
        \nyou will be notified at evrey time the device cosumes '5 percent battery'")  # insert at line 0 character 0
text = textbox2.get("0.0", "end")  # get text from line 0 character 0 till the end
textbox2.configure(state="disabled")  # configure textbox to be read-only
textbox2.pack(pady = 20)
value_enter2 = ctk.CTkEntry(tab3, placeholder_text='enter the battery percentage to be reminded at')
value_enter2.pack(pady=20)
START_BUTTON2 = ctk.CTkButton(tab3, text="start",)
START_BUTTON2.pack(pady=10)


root.mainloop()
