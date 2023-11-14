import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if unit_var.get() == "kg/m":
            bmi = weight / (height ** 2)
        else:
            weight_kg = weight * 0.453592
            height_m = height * 0.0254
            bmi = weight_kg / (height_m ** 2)
        result_label.config(text=f"Your BMI is: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")
    
    if bmi > 30:
        message = "You are obese"
    elif 30 > bmi > 24.9:
        message = "You are overweight"
    elif 18.5 > bmi > 24.9:
        message = "You are normal weight"
    else:
        message = "You are underweight"
    
    message_label.config(text=message)
        

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x400")

weight_label = tk.Label(window, text="Weight: ")
weight_label.grid(row=0, column=0, pady=10)

weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1, pady=10)

height_label = tk.Label(window, text="Height: ")
height_label.grid(row=1, column=0, pady=10)

height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1, pady=10)

unit_var = tk.StringVar()
unit_var.set("kg/m")

unit_kg_m = tk.Radiobutton(window, text="kg/m", variable=unit_var, value="kg/m")
unit_kg_m.grid(row=2, column=0, pady=5, padx=10)

unit_lb_inch = tk.Radiobutton(window, text="lb/inch", variable=unit_var, value="lb/inch")
unit_lb_inch.grid(row=2, column=1, columnspan= 2, pady=5, padx=10)

calculate_button = tk.Button(window, text="Calculate Your BMI", command=calculate_bmi)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="Your BMI is: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

message_label = tk.Label(window, text="")
message_label.grid(row=5, column=0, columnspan=2, pady=10)


window.mainloop()