

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

 