import csv
import pandas as pd
import datetime
dt = datetime.datetime.now()
year = datetime.date.today().year
def reader(ugenr,year):
    ugenr = ugenr -1
    file_path = f"CSV_AND_EXCEL/TEKNIK{year}csv.csv"
    data = pd.read_csv(file_path)
    with open(f"CSV_AND_EXCEL/TEKNIK{year}csv.csv", "r") as datafil:
        csv_laeser = csv.reader(datafil, delimiter=",")
        next(csv_laeser)
        uge = []
        PC = []
        Mikser = []
        Host = []
        Podiet = []

        for linje in csv_laeser:
            try:
                if int(linje[0]) < 53:
                    uge.append(linje[0])
                    PC.append(linje[1])
                    Mikser.append(linje[2])
                    Host.append(linje[3])
                    Podiet.append(linje[4])
            except:
                pass
        return PC[ugenr] , Mikser[ugenr] , Host[ugenr] , Podiet[ugenr]


def find_name(name):
    current_week = dt.isocalendar()[1]
    for i in range(1, 53):
        next_week = (current_week + i) % 53
        if next_week == 0:
            next_week = 1  # Adjust for wrap-around to week 1 after week 52

        PC, Mikser, Host, Podiet = reader(next_week, year)

        job = None
        if name in PC:
            job = 'PC'
        elif name in Mikser:
            job = 'Mikser'
        elif name in Host:
            job = 'Host'
        elif name in Podiet:
            job = 'Podiet'

        if job:
            return {
                'current_week': current_week,
                'next_week': next_week,
                'name': name,
                'job': job
            }

    return {
        'current_week': current_week,
        'next_week': None,
        'name': name,
        'job': 'No job assigned'
    }




