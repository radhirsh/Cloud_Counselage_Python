import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    data_science_course_event = 'IS DATA SCIENCE FOR YOU?'
    data_science_course_attendees = excel_sheet[excel_sheet['Events'] == data_science_course_event]

    total_data_science_course_attendees = len(data_science_course_attendees)
    total_non_attendees = len(excel_sheet) - total_data_science_course_attendees

    plt.figure(figsize=(8, 6))
    bars = plt.bar(['Attended', 'Did Not Attend'], [total_data_science_course_attendees, total_non_attendees], color=['green', 'red'])

    plt.title('Attendance for "IS DATA SCIENCE FOR YOU?" Event')
    plt.xlabel('Attendance Status')
    plt.ylabel('Number of Students')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval), ha='center', va='bottom')

    plt.legend()

    plt.show()
