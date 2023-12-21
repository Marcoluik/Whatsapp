import pandas as pd


weeks = list(range(1, 53))
df = pd.DataFrame({"Uge nr": weeks})


hosts = ["Nick", "Jens", "Emil", "Marc"]
pcs = ["Martin", "Henrik", "Louis", "Marco", "Marcus", "Patrick", "Silas", "Benjamin"]
podium = ["August", "Viggo"]


df["PC"] = [pcs[i % len(pcs)] for i in range(len(weeks))]
df["Mikser"] = [name for i in range(len(weeks)) for name in pcs if name != df.loc[i, "PC"]][0:len(weeks)] #Sørger for at Pc og Mikser ikke kan være samme person
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