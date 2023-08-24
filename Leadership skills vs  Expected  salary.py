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
