import tkinter
import customtkinter as ctk


app = tkinter.Tk()

app.geometry('400x240')
app.title('LakbayPinas Van Rental Estimate Calculator')


def estimate_price_button():
    print('button pressed')


ctk.set_appearance_mode('Dark')

button = ctk.CTkButton(
    fg_color='gray',
    master=app,
    corner_radius=10,
    command=estimate_price_button,  
)

button.place(
    relx=0.5,
    rely=0.5,
    anchor=tkinter.CENTER,
)





app.mainloop()