import customtkinter


def calculate_cost():
    print('button pressed')


app = customtkinter.CTk()
app.title('LakbayPinas Travel Cost Estimator')
app.geometry('600x400')

# ----- LEFT COLUMN ----- #
distance_label = customtkinter.CTkLabel(app, text="Enter Total Distance from Point A to B in Kilometers:")
distance = customtkinter.CTkEntry(app, width=300, placeholder_text='Distance in Kilometers')

fuel_consumption_label = customtkinter.CTkLabel(app, text='Enter Vehicle Fuel Consumption (km/L)')
fuel_consumption = customtkinter.CTkEntry(app, width=300, placeholder_text='e.g. 8')

fuel_price_label = customtkinter.CTkLabel(app, text='Enter Current Fuel Price:')
fuel_price = customtkinter.CTkEntry(app, width=300, placeholder_text='e.g. 65 pesos/L')

toll_fee_label = customtkinter.CTkLabel(app, text='Enter Toll Fee Estimate in Pesos:')
toll_fee = customtkinter.CTkEntry(app, width=300, placeholder_text='e.g. 1000')

calculate_button = customtkinter.CTkButton(app, width=300, text='Estimate Cost', command=calculate_cost)


# ----- LEFT GRID LAYOUT ----- #
distance_label.grid(row=0, column=0, padx=20, pady=5, sticky='w')
distance.grid(row=1, column=0, padx=20, pady=5)

fuel_consumption_label.grid(row=3, column=0, padx=20, pady=5, sticky='w')
fuel_consumption.grid(row=4, column=0, padx=20, pady=5)

fuel_price_label.grid(row=6, column=0, padx=20, pady=5, sticky='w')
fuel_price.grid(row=7, column=0, padx=20, pady=5)

toll_fee_label.grid(row=9, column=0, padx=20, pady=5, sticky='w')
toll_fee.grid(row=10, column=0, padx=20, pady=5)

calculate_button.grid(row=15, column=0, padx=20, pady=40, sticky='w')


# ----- RIGHT COLUMN ----- #
description = customtkinter.CTkLabel(
    app,
    wraplength=200,
    justify='left',
    text=f'DESCRIPTION PLACEHOLDER',
)

# ----- RIGHT GRID LAYOUT ----- #
description.grid(row=0, column=1, padx=20, pady=5, sticky='w', rowspan=1)

app.mainloop()