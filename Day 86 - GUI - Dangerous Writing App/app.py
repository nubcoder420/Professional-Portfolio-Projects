import customtkinter


app = customtkinter.CTk()
app.title('Dangerous Writing')
app.geometry('600x600')


textbox = customtkinter.CTkTextbox(master=app, width=560, height=560)
textbox.grid(padx=20, pady=20)


def on_textbox_change(event):
    print('Text changed: ', textbox.get('1.0', 'end-1c'))
    app.after_cancel(app.after_id)
    app.after_id = app.after(5000, check_typing_timeout)


def check_typing_timeout():
    print('User stopped typing for 5 seconds. Deleting text.')
    textbox.delete('1.0', 'end')

textbox.bind('<Key>', on_textbox_change)

app.after_id = None
app.after_id = app.after(5000, check_typing_timeout)



app.mainloop()