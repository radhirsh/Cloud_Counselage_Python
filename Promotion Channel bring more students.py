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
