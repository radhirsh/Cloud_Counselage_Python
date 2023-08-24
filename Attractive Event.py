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
