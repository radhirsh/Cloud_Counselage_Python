import pandas as pd
import matplotlib.pyplot as plt

def map_designation_to_color(designation):
    color_map = {
        'Students': 'blue',
        'Principal': 'orange',
        'Asst. Professor': 'green',
        'HoD': 'red',
        'Professor': 'purple',
        'Computer Engineer': 'brown',
        'Interior designer': 'pink',
        'CVO': 'gray',
        'Web Development': 'cyan',
        'Data Science and Analyst': 'magenta',
        # Add more color mappings as needed
    }
    return color_map.get(designation, 'gray')

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    excel_sheet['Family Income'] = excel_sheet['Family Income'].str.replace('[^\d.]', '', regex=True)
    excel_sheet['Family Income'] = pd.to_numeric(excel_sheet['Family Income'], errors='coerce')

    excel_sheet['CGPA'] = pd.to_numeric(excel_sheet['CGPA'], errors='coerce')

    selected_data = excel_sheet.dropna(subset=['Family Income', 'CGPA'])

    cgpa_counts = selected_data['CGPA'].value_counts()
    avg_income_by_cgpa = selected_data.groupby('CGPA')['Family Income'].mean()

    plt.figure(figsize=(10, 6))

    for x, y, label in zip(cgpa_counts.index, avg_income_by_cgpa[cgpa_counts.index], cgpa_counts.index):
        color = map_designation_to_color(label)
        plt.scatter(x, y, color=color)

    for x, y, label in zip(cgpa_counts.index, avg_income_by_cgpa[cgpa_counts.index], cgpa_counts.index):
        color = map_designation_to_color(label)
        plt.annotate(f'CGPA {label}', (x, y), textcoords="offset points", xytext=(5,-5), ha='left')

    colors = ['blue' if label in [6, 7, 8, 9] else 'gray' for label in cgpa_counts.index]
    plt.scatter(cgpa_counts.index, avg_income_by_cgpa[cgpa_counts.index], color=colors)

    plt.xlabel('Distinct CGPA')
    plt.ylabel('Average Family Income')
    plt.title('Relationship between Distinct CGPA and Average Family Income')

    plt.tight_layout()
    plt.show()
