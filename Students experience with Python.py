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
