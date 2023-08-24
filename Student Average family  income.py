import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def categorize_income(value):
    if value <= 200000:
        return '0-2 Lakh'
    elif value <= 500000:
        return '2-5 Lakh'
    elif value <= 700000:
        return '5-7 Lakh'
    else:
        return '7 Lakh+'

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    excel_sheet['Family Income'] = excel_sheet['Family Income'].str.replace('[^\d.]', '', regex=True)
    excel_sheet['Family Income'] = pd.to_numeric(excel_sheet['Family Income'], errors='coerce')

    selected_designations = ['Students', 'Data Science and Analyst', 'Software developer', 'Intern']
    selected_data = excel_sheet[excel_sheet['Designation'].isin(selected_designations)]

    selected_data = selected_data.dropna(subset=['Family Income'])

    avg_family_income_by_designation = selected_data.groupby('Designation')['Family Income'].mean()

    plt.figure(figsize=(10, 6))
    colors = ['purple', 'blue', 'green', 'cyan']  # Adjusted colors, "Students" bar is set to cyan
    ax = avg_family_income_by_designation.plot(kind='bar', color=colors, alpha=0.7)
    plt.xlabel('Designation')
    plt.ylabel('Average Family Income')
    plt.xticks(rotation=45)
    
    for i, value in enumerate(avg_family_income_by_designation):
        plt.text(i, value, f'{value:.2f}', ha='center', va='bottom')

    plt.tight_layout()

    # Add custom legend for "Students" bar color
    legend_labels = ["Data Science and Analyst", "Intern", "Software developer"]
    legend_elements = [Patch(facecolor='cyan', edgecolor='black', alpha=0.7, label='Students')] + \
                       [Patch(facecolor=colors[i], edgecolor='black', alpha=0.7, label=legend_labels[i]) for i in range(3)]

    ax.legend(handles=legend_elements, loc='upper right')

    plt.show()
