import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    excel_sheet['Year of Graduation'] = pd.to_numeric(excel_sheet['Year of Graduation'], errors='coerce')

    students_with_valid_graduation_year = excel_sheet.dropna(subset=['Year of Graduation'])

    graduation_year_counts = students_with_valid_graduation_year['Year of Graduation'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    bars = plt.bar(graduation_year_counts.index, graduation_year_counts.values, color='blue', alpha=0.7)

    for bar in bars:
        if bar.get_height() == graduation_year_counts[2024]:
            bar.set_color('red')

    plt.xlabel('Year of Graduation')
    plt.ylabel('Number of Students')
    plt.title('Number of Students by Graduation Year')
    plt.xticks(graduation_year_counts.index, rotation=45)

    for i, value in enumerate(graduation_year_counts):
        plt.text(graduation_year_counts.index[i], value, f'{value}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()
