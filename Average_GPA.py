import pandas as pd
import matplotlib.pyplot as plt

def calculate_average_student_cgpa(data):
    student_data = data[data['Designation'].str.strip().str.lower().str.contains('student')].copy()
    student_data.dropna(subset=['CGPA'], inplace=True)
    average_cgpa = student_data['CGPA'].mean()
    return average_cgpa

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    avg_student_cgpa = calculate_average_student_cgpa(excel_sheet)
    print("Average Student CGPA:", avg_student_cgpa)

    plt.plot([], [])
    plt.scatter(["Average Student CGPA"], [avg_student_cgpa], color='blue', marker='o', label=f'Average: {avg_student_cgpa:.2f}')
    plt.legend()
    plt.ylabel("CGPA")
    plt.show()
