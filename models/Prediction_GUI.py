import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import numpy as np

# Load all models
with open("all_models.pkl", "rb") as f:
    models = pickle.load(f)

weather_map = {'drizzle': 0, 'rain': 1, 'fog': 2, 'sun': 3}

root = tk.Tk()
root.title("Weather Temp Max Predictor")
root.geometry("400x450")

tk.Label(root, text="Precipitation").pack()
entry_precip = tk.Entry(root)
entry_precip.pack()

tk.Label(root, text="Temp Min").pack()
entry_temp_min = tk.Entry(root)
entry_temp_min.pack()

tk.Label(root, text="Wind").pack()
entry_wind = tk.Entry(root)
entry_wind.pack()

tk.Label(root, text="Weather (drizzle, rain, fog, sun)").pack()
entry_weather = tk.Entry(root)
entry_weather.pack()

model_var = tk.StringVar()
model_dropdown = ttk.Combobox(root, textvariable=model_var)
model_dropdown['values'] = list(models.keys())
model_dropdown.set("Random Forest")
model_dropdown.pack(pady=10)

def predict():
    try:
        precip = float(entry_precip.get())
        temp_min = float(entry_temp_min.get())
        wind = float(entry_wind.get())
        weather_str = entry_weather.get().strip().lower()

        if weather_str not in weather_map:
            messagebox.showerror("Invalid Input", "Weather must be: drizzle, rain, fog, sun")
            return

        weather = weather_map[weather_str]
        input_data = np.array([[precip, temp_min, wind, weather]])

        selected_model = model_var.get()
        model = models[selected_model]
        prediction = model.predict(input_data)[0]

        messagebox.showinfo("Prediction", f"{selected_model} Prediction:\n\nTemp Max: {prediction:.2f} °C")

    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Button(root, text="Predict", command=predict, bg="green", fg="white").pack(pady=20)

root.mainloop()
