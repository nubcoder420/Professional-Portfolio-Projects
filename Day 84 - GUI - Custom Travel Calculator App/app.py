import customtkinter

BASE_FUEL_CONSUMPTION_VALUE = 7 # 7 km/L default vehicle fuel consumption
BASE_FUEL_PRICE = 65 # 65 pesos per liter current average price
BASE_VEHICLE_RENT_COST = 4500 # 4500 pesos per day


def calculate_cost():
    
    total_distance = float(distance.get()) if distance.get() else 0
    fuel_consumption_value = float(fuel_consumption.get()) if fuel_consumption.get() else BASE_FUEL_CONSUMPTION_VALUE
    fuel_price_value = float(fuel_price.get()) if fuel_price.get() else BASE_FUEL_PRICE
    toll_fee_value = float(toll_fee.get()) if toll_fee.get() else 0
    vehicle_rental_value = float(vehicle_rental_cost.get()) if vehicle_rental_cost.get() else BASE_VEHICLE_RENT_COST

    estimated_total_cost = (((total_distance * 2) / fuel_consumption_value) * fuel_price_value) + toll_fee_value + vehicle_rental_value

    print(estimated_total_cost)

app = customtkinter.CTk()
app.title('LakbayPinas Travel Cost Estimator')
app.geometry('600x500')

# ----- LEFT COLUMN ----- #
distance_label = customtkinter.CTkLabel(app, text="Enter Total Distance from Point A to B in Kilometers:")
distance = (customtkinter.CTkEntry(app, width=300, placeholder_text='e.g. 100'))

fuel_consumption_label = customtkinter.CTkLabel(app, text='Enter Vehicle Fuel Consumption (km/L)')
fuel_consumption = customtkinter.CTkEntry(app, width=300, placeholder_text='e.g. 8')

fuel_price_label = customtkinter.CTkLabel(app, text='Enter Current Fuel Price (pesos/L):')
fuel_price = customtkinter.CTkEntry(app, width=300, placeholder_text='e.g. 65')

toll_fee_label = customtkinter.CTkLabel(app, text='Enter Toll Fee Estimate in Pesos:')
toll_fee = customtkinter.CTkEntry(app, width=300, placeholder_text='e.g. 1000')

vehicle_rental_label = customtkinter.CTkLabel(app, text='Cost of Vehicle Rental: ')
vehicle_rental_cost = customtkinter.CTkEntry(app, width=300, placeholder_text='e.g. 4000 if one day, 8000 if two days, etc.')

calculate_button = customtkinter.CTkButton(app, width=300, text='Estimate Cost', command=calculate_cost)


# ----- LEFT GRID LAYOUT ----- #
distance_label.grid(row=0, column=0, padx=20, pady=5, sticky='w')
distance.grid(row=1, column=0, padx=20, pady=5)

fuel_consumption_label.grid(row=2, column=0, padx=20, pady=5, sticky='w')
fuel_consumption.grid(row=3, column=0, padx=20, pady=5)

fuel_price_label.grid(row=4, column=0, padx=20, pady=5, sticky='w')
fuel_price.grid(row=5, column=0, padx=20, pady=5)

toll_fee_label.grid(row=6, column=0, padx=20, pady=5, sticky='w')
toll_fee.grid(row=7, column=0, padx=20, pady=5)

vehicle_rental_label.grid(row=8, column=0, padx=20, pady=5, sticky='w')
vehicle_rental_cost.grid(row=9, column=0, padx=20, pady=5, sticky='w')

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