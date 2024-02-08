import tkinter as tk

#function to convert temperature
def convert_temperature():
    try:
        temperature = float(entry.get())
        
        # Convert the temperature based on the selected option
        if option.get() == "Celsius to Fahrenheit":
            converted_temperature = (temperature * 9/5) + 32
        elif option.get() == "Fahrenheit to Celsius":
            converted_temperature = (temperature - 32) * 5/9
        else:
            raise ValueError("Invalid option selected.")
        
        # Update the label with the converted temperature
        result_label.config(text=f"Result: {converted_temperature:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

 # Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create a label for the entry widget
entry_label = tk.Label(root, text="Enter temperature:")
entry_label.pack()

# Create an entry widget to input temperature
entry = tk.Entry(root)
entry.pack()

# Create a label for the option menu
option_label = tk.Label(root, text="Select conversion:")
option_label.pack()

# Create an option menu for selecting conversion type
option = tk.StringVar(root)
option.set("Celsius to Fahrenheit")  # Default option
option_menu = tk.OptionMenu(root, option, "Celsius to Fahrenheit", "Fahrenheit to Celsius")
option_menu.pack()

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the main event loop
root.mainloop()