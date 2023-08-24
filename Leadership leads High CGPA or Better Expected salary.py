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
