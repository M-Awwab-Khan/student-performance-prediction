
def predict(input_df):
    import pickle

    model = pickle.load(open('model.pkl', 'rb'))
    mapping = pickle.load(open('mapping.pkl', 'rb'))
    for col in input_df.select_dtypes(include=['object']):
        input_df[col] = input_df[col].map(mapping[col])

    return model.predict(input_df)


# import pandas as pd

# # Create a sample DataFrame with 3 observations
# data = {
#     'Hours_Studied': [5, 8, 3],
#     'Attendance': [90, 85, 70],
#     'Parental_Involvement': ['High', 'Medium', 'Low'],
#     'Access_to_Resources': ['High', 'Medium', 'Low'],
#     'Extracurricular_Activities': ['Yes', 'No', 'Yes'],
#     'Sleep_Hours': [7, 6, 5],
#     'Previous_Scores': [75, 88, 65],
#     'Motivation_Level': ['High', 'Medium', 'Low'],
#     'Internet_Access': ['Yes', 'No', 'Yes'],
#     'Tutoring_Sessions': [2, 4, 1],
#     'Family_Income': ['High', 'Medium', 'Low'],
#     'Teacher_Quality': ['High', 'Medium', 'Low'],
#     'School_Type': ['Public', 'Private', 'Public'],
#     'Peer_Influence': ['Positive', 'Neutral', 'Negative'],
#     'Physical_Activity': [3, 2, 4],
#     'Learning_Disabilities': ['No', 'Yes', 'No'],
#     'Parental_Education_Level': ['Postgraduate', 'College', 'High School'],
#     'Distance_from_Home': ['Near', 'Far', 'Moderate'],
#     'Gender': ['Male', 'Female', 'Male'],
# }

# # Convert the data into a DataFrame
# sample_df = pd.DataFrame(data)

# print(predict(sample_df))
