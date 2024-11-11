import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from main import predict
import sv_ttk

root = tk.Tk()
root.title("Student Performance Predictor")
root.geometry("400x600") 

canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

columns_order = [
    'Hours_Studied', 'Attendance', 'Parental_Involvement', 'Access_to_Resources',
    'Extracurricular_Activities', 'Sleep_Hours', 'Previous_Scores', 'Motivation_Level',
    'Internet_Access', 'Tutoring_Sessions', 'Family_Income', 'Teacher_Quality',
    'School_Type', 'Peer_Influence', 'Physical_Activity', 'Learning_Disabilities',
    'Parental_Education_Level', 'Distance_from_Home', 'Gender'
]

numeric_fields = [
    'Hours_Studied', 'Attendance', 'Sleep_Hours', 'Previous_Scores', 'Tutoring_Sessions', 'Physical_Activity'
]

entry_widgets = {}
for idx, field in enumerate(numeric_fields):
    label = ttk.Label(scrollable_frame, text=field)
    label.grid(row=idx, column=0, padx=10, pady=5, sticky='w')
    entry = ttk.Entry(scrollable_frame)
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entry_widgets[field] = entry

categorical_fields = {
    'Parental_Involvement': ['High', 'Medium', 'Low'],
    'Access_to_Resources': ['High', 'Medium', 'Low'],
    'Extracurricular_Activities': ['Yes', 'No'],
    'Motivation_Level': ['High', 'Medium', 'Low'],
    'Internet_Access': ['Yes', 'No'],
    'Family_Income': ['High', 'Medium', 'Low'],
    'Teacher_Quality': ['High', 'Medium', 'Low'],
    'School_Type': ['Public', 'Private'],
    'Peer_Influence': ['Positive', 'Neutral', 'Negative'],
    'Learning_Disabilities': ['Yes', 'No'],
    'Parental_Education_Level': ['Postgraduate', 'College', 'High School'],
    'Distance_from_Home': ['Near', 'Moderate', 'Far'],
    'Gender': ['Male', 'Female']
}

for idx, (field, options) in enumerate(categorical_fields.items(), start=len(numeric_fields)):
    label = ttk.Label(scrollable_frame, text=field)
    label.grid(row=idx, column=0, padx=10, pady=5, sticky='w')
    combobox = ttk.Combobox(scrollable_frame, values=options)
    combobox.grid(row=idx, column=1, padx=10, pady=5)
    entry_widgets[field] = combobox

def predict_performance():
    try:
        input_data = []
        for column in columns_order:
            value = entry_widgets[column].get()
            if column in numeric_fields:
                input_data.append(int(value))
            else:
                input_data.append(value)

        input_df = pd.DataFrame([input_data], columns=columns_order)

        print('making prediction')
        prediction = predict(input_df)
        print('prediction', prediction)
        messagebox.showinfo("Prediction", f"Predicted Exam Score: {prediction[0]}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

predict_button = ttk.Button(scrollable_frame, text="Predict", command=predict_performance)
predict_button.grid(row=len(numeric_fields) + len(categorical_fields), columnspan=2, pady=20)

sv_ttk.set_theme("light")

root.mainloop()
