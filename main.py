# Import libraries

import pandas as pd
import numpy as np

# Get CSV data and check the first 5 lines

df = pd.read_csv('StudentPerformanceFactors.csv')
df.head()

# Create a filter for students who have extracurricular activies and who have hours studied above 10

df_condition = df[(df['Extracurricular_Activities']=='Yes') & (df['Hours_Studied'] > 10)]

# Calculate the average exam score by hours studied in descending order

df_condition.groupby('Hours_Studied')['Exam_Score'].mean().sort_values(ascending=False)

# Create a new column separating hours studied in ranges

df['hours_studied_range'] = np.where(
        df['Hours_Studied'].between(1, 5, inclusive=True), '1-5 hours',
    np.where(
        df['Hours_Studied'].between(6, 10, inclusive=True), '6-10 hours',
    np.where(
        df['Hours_Studied'].between(11, 15, inclusive=True), '11-15 hours',
        '16+ hours')
    )
)

# Calculate the average exam score by the range of studied hours in descending order

df.groupby('hours_studied_range')['Exam_Score'].mean().sort_values(ascending=False)

# Create a new column ranking the exam score using the dense method and sorting the results

df['exam_rank'] = df['Exam_Score'].rank(method='dense', ascending=False).astype(int).sort_values()

# Display the 30 first lines of the requested columns sorted by exam rank

df[['Attendance', 'Hours_Studied', 'Sleep_Hours', 'Tutoring_Sessions', 'exam_rank']].sort_values(by='exam_rank')[:30]
