# Code Course: Introduction to Python
# Week 1: Introduction and first data file
# ID: 066432238
# Name: Tamadur Sawaed
import pandas as pd
participant_id = [1, 2, 3, 4, 5, 6]
gender = ["male", "female", "female", "male", "female", "male"]
age = [15, 26, 33, 24, 37, 40]
depression = [0, 1, 1, 0, 0, 1]
df = pd.DataFrame ({
   "Participant_id": participant_id,
   "Gender": gender,
   "Age": age,
   "Depression": depression
})
df.to_csv("participants.csv", index=False, encoding="utf-8")

