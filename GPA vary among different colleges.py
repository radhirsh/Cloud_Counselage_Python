import pandas as pd
import matplotlib.pyplot as plt

excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
excel_sheet = pd.read_excel(excel_file)

excel_sheet['CGPA'] = pd.to_numeric(excel_sheet['CGPA'], errors='coerce')

unique_cgpa_count = excel_sheet.groupby('CGPA')['College Name'].nunique()

plt.figure(figsize=(10, 6))
ax = unique_cgpa_count.plot(kind='bar')
plt.xlabel('Unique CGPA')
plt.ylabel('Number of Colleges')
plt.title('Number of Colleges with Unique CGPA')
plt.xticks(rotation=45)

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.tight_layout()
plt.show()
