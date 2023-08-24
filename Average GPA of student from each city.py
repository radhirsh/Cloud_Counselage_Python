import pandas as pd
import matplotlib.pyplot as plt

excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
excel_sheet = pd.read_excel(excel_file)

excel_sheet['CGPA'] = pd.to_numeric(excel_sheet['CGPA'], errors='coerce')

average_gpa_by_city = excel_sheet.groupby('City')['CGPA'].mean().reset_index()

average_gpa_by_city_sorted = average_gpa_by_city.sort_values(by='CGPA', ascending=False)

top_10_cities = average_gpa_by_city_sorted.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_10_cities['City'], top_10_cities['CGPA'], color='blue')
plt.xlabel('City', fontsize=12)
plt.ylabel('Average GPA', fontsize=12)
plt.title('Average GPA of Students in Top 10 Cities', fontsize=14)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()

for i, value in enumerate(top_10_cities['CGPA']):
    plt.text(i, value + 0.1, f'{value:.2f}', ha='center', va='bottom')

plt.show()
