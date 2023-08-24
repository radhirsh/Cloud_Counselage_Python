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
