import pandas as pd

weeks = list(range(1, 53))     #Weeks list
df = pd.DataFrame({"Uge nr": weeks})   #Dataframe

#Roles
hosts = ["Jens", "Emil", "Marc"]
pcs = ["Henrik", "Viggo", "Patrick", "Benjamin", "Martin", "Marco", "Louis", "Silas", "Viggo"]
mikser = ["Martin", "Louis", "Silas", "Henrik", "Marco", "Viggo", "Patrick", "Benjamin", ]
podium = ["August", "Vilfred", "Villads"]


df["PC"] = [pcs[i % len(pcs)] for i in range(len(weeks))]
df["Mikser"] = [mikser[i % len(mikser)] for i in range(len(weeks))]
df["Host"] = [hosts[i % len(hosts)] for i in range(len(weeks))]
df["Podiet"] = [podium[i % len(podium)] for i in range(len(weeks))]


stævne = {"PC": "Stævne", "Mikser": "Stævne", "Host": "Stævne", "Podiet": "Stævne"}
df.loc[df['Uge nr'] == 13, stævne.keys()] = stævne.values()
df.loc[df['Uge nr'] == 28, stævne.keys()] = stævne.values()


print(df.head()) #Første 5

#Excel
excel_file_path = "CSV_AND_EXCEL/Teknik2024xlsx.xlsx"
df.to_excel(excel_file_path, index=False)

#CSV
csv_file_path = "CSV_AND_EXCEL/TEKNIK2024csv.csv"
df.to_csv(csv_file_path, index=False)


print(f"Excel file saved to {excel_file_path}")

print(f"CSV file saved to {csv_file_path}")