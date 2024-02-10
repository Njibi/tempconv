        ## TEMPERATURE CONVERTER FOR COS101 GROUP WORK

### GROUP MEMBERS
- ABDULLAHI UMAR NJIBI  BHU/23/04/05/0122
- IGBANA SOLOMON TERSOO BHU/23/04/09/0087
- JERIMIAH OLADOYIN BHU/23/05/10/0020
- ANDREW GWONG DANG  BHU/23/04/05/0119

## HOW WE DID THE TEMPERATURE CONVERTER
We used VScode as our IDE, and imported necessary modules from 'tkinter' library, python was the language used. 
The interface was designed using tkinter 

## PURPOSE
The purpose of this code is to create a simple temperature converter using Tkinter. It allows the user to input a temperature, select the conversion type (Celsius to Fahrenheit or Fahrenheit to Celsius), and then displays the converted temperature when the "Convert" button is clicked.

### FUNCTIONS
- convert_temperature(): This function retrieves the temperature entered by the user, performs the conversion based on the selected option, and updates the result label with the converted temperature. It also handles errors if the entered value is not a valid number or if an invalid option is selected.

### COMPONENTS
- root: The main window of the Tkinter application.
- entry: Entry widget for the user to input the temperature.
- option: StringVar to store the selected conversion option.
- option_menu: OptionMenu widget to display and select the conversion options.
- convert_button: Button widget to trigger the conversion process.
- result_label: Label widget to display the converted temperature.
h
