#1.How many unique students  are included in the dataset?
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


#2.What is the average GPA of Students?
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

#3.What is the distribution of students across different graduation years?
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


#4.What is the distribution of student’s experience with Python programming
import pandas as pd
import matplotlib.pyplot as plt

def plot_python_experience_distribution(data):
    student_data = data[data['Designation'].str.strip().str.lower().str.contains('student')].copy()
    python_experience = student_data['Experience with python (Months)']
    
    plt.hist(python_experience, bins=10, edgecolor='black', alpha=0.7)
    plt.xlabel("Experience with Python (Months)")
    plt.ylabel("Number of Students")
    
    
    # Plot the histogram and get bin counts and bin edges
    bin_counts, bin_edges, _ = plt.hist(python_experience, bins=10, edgecolor='black', alpha=0.7,color="blue")
    
    # Add data labels to the bars
    for count, x in zip(bin_counts, bin_edges):
        if count > 0:  # Show data label only if count is greater than 0
            plt.text(x + (bin_edges[1] - bin_edges[0]) / 2, count, str(int(count)), ha='center', va='bottom')
    
    plt.xticks(range(int(min(python_experience)), int(max(python_experience)) + 1))
    
    plt.show()

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    plot_python_experience_distribution(excel_sheet)

#5.What is the average family income of the  student?
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

#6.How does the GPA vary among different colleges?
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


#8..What is th average GPA of the student from each city?
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

#9.Can We identify any relationship between  family income  and GPA?
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

#10..How does th expected salary vary based on factors like “GPA”,”Family Income”,”Experience with python(Months)?
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def categorize_income(value):
    if value < 300000:
        return 'Low'
    elif value < 700000:
        return 'Moderate'
    else:
        return 'High'

if __name__ == "__main__":
    # Load the Excel file into a DataFrame
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    # Clean 'Family Income' column and convert to categorized values
    excel_sheet['Family Income'] = excel_sheet['Family Income'].str.replace('[^\d.]', '', regex=True).astype(float)
    excel_sheet['Family Income Category'] = excel_sheet['Family Income'].apply(categorize_income)

    # Clean 'CGPA' column and convert to numeric
    excel_sheet['CGPA'] = pd.to_numeric(excel_sheet['CGPA'], errors='coerce')

    # Clean 'Experience with python (Months)' column and convert to numeric
    excel_sheet['Experience with python (Months)'] = pd.to_numeric(excel_sheet['Experience with python (Months)'], errors='coerce')

    # Drop rows with missing values in relevant columns
    selected_data = excel_sheet.dropna(subset=['Family Income Category', 'CGPA', 'Experience with python (Months)', 'Expected salary (Lac)'])

    # Create subplots for multi-variable visualization
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    sns.scatterplot(x='CGPA', y='Expected salary (Lac)', data=selected_data)
    plt.title('Expected Salary vs CGPA')

    plt.subplot(1, 3, 2)
    sns.scatterplot(x='Family Income', y='Expected salary (Lac)', data=selected_data)
    plt.title('Expected Salary vs Family Income')

    plt.subplot(1, 3, 3)
    sns.scatterplot(x='Experience with python (Months)', y='Expected salary (Lac)', data=selected_data)
    plt.title('Expected Salary vs Experience with Python')

    plt.tight_layout()
    plt.show()

#11.Which event tend to attract more students from the specific field of study?
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def categorize_income(value):
    if value < 300000:
        return 'Low'
    elif value < 700000:
        return 'Moderate'
    else:
        return 'High'

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    grouped_data = excel_sheet.groupby(['Events', 'Designation']).size().unstack(fill_value=0)
    grouped_data['Total Students'] = grouped_data.sum(axis=1)

    plt.figure(figsize=(15, 8))
    sns.set_palette("pastel")
    ax = grouped_data['Total Students'].plot(kind='bar', width=0.8)

    plt.title("Event Attendance by Event")
    plt.xlabel("Events")
    plt.ylabel("Number of Students")
    plt.xticks(rotation=45, ha='right')
    ax.set_xlabel('')

    for container in ax.containers:
        ax.bar_label(container, label_type='edge', fontsize=10, color='black', padding=3)

    plt.legend(loc='upper left')
    plt.tight_layout()
    image_file_path = "path_to_save_plot_image.png"
    plt.savefig(image_file_path, format='png')

    plt.clf()

    plt.show()

#12.Do students in leadership positions during their college years tend to have high GPAs or better expected salary?
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    excel_sheet['Expected salary (Lac)'] = pd.to_numeric(excel_sheet['Expected salary (Lac)'], errors='coerce')
    excel_sheet['Leadership- skills'] = excel_sheet['Leadership- skills'].str.strip()

    plt.figure(figsize=(10, 6))
    plot = sns.scatterplot(x='Leadership- skills', y='CGPA', hue='Expected salary (Lac)', data=excel_sheet, palette='coolwarm', s=50, alpha=0.7)

    plt.xlabel('Leadership Skills', fontsize=12)
    plt.ylabel('CGPA (GPA)', fontsize=12)

    legend = plot.legend(title='Expected Salary (Lac)')
    legend_labels = ['5 Lakhs', '7 Lakhs', '10 Lakhs', '14 Lakhs', '15 Lakhs','30 Lakhs','35 Lakhs']
    for text, label in zip(legend.texts, legend_labels):
        text.set_text(label)

    plt.tight_layout()
    plt.show()

#13.Is there a correlation between leadership skills and expected salary of the students?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    excel_sheet['Leadership- skills'] = excel_sheet['Leadership- skills'].map({'yes': 1, 'no': 0})

    plt.figure(figsize=(10, 6))
    sns.regplot(x='Leadership- skills', y='Expected salary (Lac)', data=excel_sheet, scatter_kws={'s': 50}, line_kws={'color': 'red'}, label='Regression Line')

    plt.xlabel('Leadership Skills', fontsize=12)
    plt.ylabel('Expected Salary (Lac)', fontsize=12)

    plt.legend()

    plt.tight_layout()
    plt.show()

#14.How many students are graduating by the end of 2024?

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

#15.Which Promotion Channel brings in more students participation for the event?
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    student_records = excel_sheet[excel_sheet['Designation'] == 'Students']

    promotion_channel_counts = student_records['How did you come to know about this event?'].value_counts()

    top_10_promotion_channels = promotion_channel_counts.head(10)

    plt.figure(figsize=(20,10))
    patches, texts, autotexts = plt.pie(top_10_promotion_channels, labels=top_10_promotion_channels.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    
    plt.legend(patches, top_10_promotion_channels.index, title='Promotion Channels', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.axis('equal')
    
    plt.show()

#16.Find the total number of students who attended the events related to Data science?(From all Data Science related courses)
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

#17.Those who have high CGPA & More experience in language those who had high expectations for salary? (Avg)
        
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
  

#18.Those who have high CGPA & More experience in language those who had high expectations for salary? (Avg)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    excel_file = "C:\\Users\\giris\\Downloads\\Data analyst Data.xlsx"
    excel_sheet = pd.read_excel(excel_file)

    college_event_counts = excel_sheet[excel_sheet['How did you come to know about this event?'] == 'SPOC/ College Professor']

    college_event_counts = college_event_counts['College Name'].value_counts().reset_index()
    college_event_counts.columns = ['College Name', 'Number of Students']

    top_5_colleges = college_event_counts.nlargest(5, 'Number of Students')

    plt.figure(figsize=(10, 6))
    sns.set_palette("pastel")
    ax = sns.barplot(y='Number of Students', x='College Name', data=top_5_colleges)

    plt.title("Students Who Know About the Event from Top 5 Colleges")
    plt.ylabel("Number of Students")
    plt.xlabel("College Name")

    plt.xticks(range(len(top_5_colleges)), top_5_colleges['College Name'], rotation=45, ha='right')

    plt.yticks(range(0, top_5_colleges['Number of Students'].max() + 1, 10))

    for index, row in top_5_colleges.iterrows():
        plt.annotate(str(row['Number of Students']), xy=(index, row['Number of Students']),
                     ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()

        

