import pandas as pd
import matplotlib.pyplot as plt

excel_sheet = pd.read_excel(r"C:\Users\giris\Downloads\Data analyst Data.xlsx")

unique_students = excel_sheet['Email ID'].nunique()
total_students = len(excel_sheet)
non_unique_students = total_students - unique_students

fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie([unique_students, non_unique_students], labels=None, autopct='%1.1f%%', startangle=90, pctdistance=0.85, wedgeprops=dict(width=0.4))

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')

count_text = f"Unique Count: {unique_students}\nNon-Unique Count: {non_unique_students}"
plt.text(0, 0, count_text, ha='center', va='center', fontsize=12, color='black')

plt.title('Distribution of Unique Students')
plt.show()
