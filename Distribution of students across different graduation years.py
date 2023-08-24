import pandas as pd
import matplotlib.pyplot as plt

def plot_graduation_year_distribution(data):
    student_data = data[data['Designation'].str.strip().str.lower().str.contains('student')].copy()
    graduation_years = student_data['Year of Graduation']

    plt.hist(graduation_years, bins=10, edgecolor='black', alpha=0.7)
    plt.xlabel("Year of Graduation")
    plt.ylabel("Number of Students")
    
    plt.xticks(range(int(min(graduation_years)), int(max(graduation_years)) + 1))
    
    for i in range(int(min(graduation_years)), int(max(graduation_years)) + 1):
        count = len(graduation_years[graduation_years == i])
        plt.text(i, count + 1, str(count), ha='center', va='bottom')
    
    plt.show()

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)
    plot_graduation_year_distribution(excel_sheet)
