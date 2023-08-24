import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    high_cgpa_experience = excel_sheet[(excel_sheet['CGPA'] > 7) & (excel_sheet['Experience with python (Months)'] > 6)]
    low_cgpa_experience = excel_sheet[(excel_sheet['CGPA'] <= 7) & (excel_sheet['Experience with python (Months)'] <= 6)]

    avg_salary_high_cgpa = high_cgpa_experience['Expected salary (Lac)'].mean()
    avg_salary_low_cgpa = low_cgpa_experience['Expected salary (Lac)'].mean()

    plt.figure(figsize=(8, 6))
    plt.bar(['High CGPA & Experience', 'Low CGPA & Experience'], [avg_salary_high_cgpa, avg_salary_low_cgpa],
            color=['blue', 'orange'])
    plt.ylabel('Average Expected Salary (Lac)')
    plt.title('Average Expected Salary Comparison')

    for i, value in enumerate([avg_salary_high_cgpa, avg_salary_low_cgpa]):
        plt.text(i, value, f'{value:.2f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()
