###########################################################################
# 
# Flight time tracker it is created in customtkinter and python 
# Created by Ismael Galarza
# Date: 1 Jan 2025 
#
###########################################################################

import customtkinter as ctk
import tkinter as tk
from datetime import datetime

# Function to validate input fields and set their colors
def validate_field(entry, expected_format):
    try:
        datetime.strptime(entry.get(), expected_format)
        entry.configure(fg_color="green")  # Set background to green if valid
        return True
    except ValueError:
        entry.configure(fg_color="red")  # Set background to red if invalid
        return False

# Function that calculates the flight time from the entered time
def calTime(launch_date_entry, launch_time_entry, landing_date_entry, landing_time_entry, result_entry, use_date_var):

    use_date = use_date_var.get() == "yes"
    
    if use_date:
        # Validate all fields including dates
        valid_launch_date = validate_field(launch_date_entry, "%d%b%Y")
        valid_launch_time = validate_field(launch_time_entry, "%H%M")
        valid_landing_date = validate_field(landing_date_entry, "%d%b%Y")
        valid_landing_time = validate_field(landing_time_entry, "%H%M")
        
        if not (valid_launch_date and valid_launch_time and valid_landing_date and valid_landing_time):
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Invalid Input")
            return
        
        try:
            # Combine date and time for calculation
            launch_datetime = datetime.strptime(f"{launch_date_entry.get()} {launch_time_entry.get()}", "%d%b%Y %H%M")
            landing_datetime = datetime.strptime(f"{landing_date_entry.get()} {landing_time_entry.get()}", "%d%b%Y %H%M")
        except ValueError:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Calculation Error")
            return
    else:
        # Validate only the time fields
        valid_launch_time = validate_field(launch_time_entry, "%H%M")
        valid_landing_time = validate_field(landing_time_entry, "%H%M")
        
        if not (valid_launch_time and valid_landing_time):
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Invalid Input")
            return
        
        try:
            # Use only the time for calculation (assume the same day)
            launch_datetime = datetime.strptime(launch_time_entry.get(), "%H%M")
            landing_datetime = datetime.strptime(landing_time_entry.get(), "%H%M")
        except ValueError:
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Calculation Error")
            return
    
    # Calculate flight duration
    if landing_datetime < launch_datetime:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Error: Landing < Launch")
    else:
        flight_duration = landing_datetime - launch_datetime
        total_seconds = flight_duration.total_seconds()
        total_hours = total_seconds / 3600  # Convert seconds to hours
        # Display the result
        result_entry.delete(0, tk.END)
        result_entry.insert(0, f"{total_hours:.1f} hours")

def main():
    # Styling of the application here
    app = ctk.CTk()
    app.title('FlightTime Converter')
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app.minsize(400, 400)
    app.maxsize(400, 400)
    
    # Labels for Launch
    ctk.CTkLabel(app, text="Launch Date:").place(relx=0.2, rely=0.1, anchor=tk.CENTER)
    ctk.CTkLabel(app, text="Launch Time:").place(relx=0.2, rely=0.2, anchor=tk.CENTER)
    
    # Labels for Landing
    ctk.CTkLabel(app, text="Landing Date:").place(relx=0.2, rely=0.3, anchor=tk.CENTER)
    ctk.CTkLabel(app, text="Landing Time:").place(relx=0.2, rely=0.4, anchor=tk.CENTER)
    
    # Label for Result
    ctk.CTkLabel(app, text="Flight Time:").place(relx=0.2, rely=0.5, anchor=tk.CENTER)
    
    # Input fields for Launch
    launch_date_entry = ctk.CTkEntry(app, placeholder_text="DDMMMYYYY")
    launch_date_entry.place(relx=0.6, rely=0.1, anchor=tk.CENTER)
    
    launch_time_entry = ctk.CTkEntry(app, placeholder_text="HHMM")
    launch_time_entry.place(relx=0.6, rely=0.2, anchor=tk.CENTER)
    
    # Input fields for Landing
    landing_date_entry = ctk.CTkEntry(app, placeholder_text="DDMMMYYYY")
    landing_date_entry.place(relx=0.6, rely=0.3, anchor=tk.CENTER)
    
    landing_time_entry = ctk.CTkEntry(app, placeholder_text="HHMM")
    landing_time_entry.place(relx=0.6, rely=0.4, anchor=tk.CENTER)
    
    # Input field for Result
    result_entry = ctk.CTkEntry(app, placeholder_text="Result")
    result_entry.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
    
    # Radio buttons for date usage
    use_date_var = tk.StringVar(value="yes")
    ctk.CTkLabel(app, text="Use Date in Calculation:").place(relx=0.2, rely=0.6, anchor=tk.CENTER)
    ctk.CTkRadioButton(app, text="Yes", variable=use_date_var, value="yes").place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    ctk.CTkRadioButton(app, text="No", variable=use_date_var, value="no").place(relx=0.7, rely=0.6, anchor=tk.CENTER)
    
    # Buttons
    submitButton = ctk.CTkButton(
        app, 
        text="Submit", 
        width=90, 
        command=lambda: calTime(launch_date_entry, launch_time_entry, landing_date_entry, landing_time_entry, result_entry, use_date_var)
    ).place(relx=0.4, rely=0.7, anchor=tk.CENTER)
    
    clearButton = ctk.CTkButton(
        app, 
        text="Clear", 
        width=90, 
        command=lambda: clearFields([launch_date_entry, launch_time_entry, landing_date_entry, landing_time_entry, result_entry])
    ).place(relx=0.7, rely=0.7, anchor=tk.CENTER)
    
    app.mainloop()

def clearFields(entries):
    for entry in entries:
        entry.delete(0, tk.END)  # Clear the entry
        entry.configure(fg_color="black")  # Reset

if __name__ == "__main__":
    main()
