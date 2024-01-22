import pandas as pd

weeks = list(range(1, 53))     #Weeks list
df = pd.DataFrame({"Uge nr": weeks})   #Dataframe

#Roles
hosts = ["Nick", "Jens", "Emil", "Marc"]
pcs = ["Henrik", "Marco", "Patrick", "Ledig", "Martin", "Louis", "Marcus", "Silas"]
mikser = ["Martin", "Louis", "Marcus", "Silas", "Henrik", "Marco,", "Patrick", "Ledig"]
podium = ["August", "Viggo"]


df["PC"] = [pcs[i % len(pcs)] for i in range(len(weeks))]
df["Mikser"] = [mikser[i % len(mikser)] for i in range(len(weeks))]
df["Host"] = [hosts[i % len(hosts)] for i in range(len(weeks))]
df["Podiet"] = [podium[i % len(podium)] for i in range(len(weeks))]


print(df.head()) #Første 5

#Excel
excel_file_path = "CSV_AND_EXCEL/Teknik2024xlsx.xlsx"
df.to_excel(excel_file_path, index=False)

#CSV
csv_file_path = "CSV_AND_EXCEL/TEKNIK2024csv.csv"
df.to_csv(csv_file_path, index=False)


print(f"Excel file saved to {excel_file_path}")

print(f"CSV file saved to {csv_file_path}")