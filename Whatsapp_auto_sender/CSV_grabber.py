import csv
def reader(ugenr):
    ugenr = ugenr -1
    with open("Teknik 2023 Amager Strand Menighed.csv", "r") as datafil:
        csv_laeser = csv.reader(datafil, delimiter=",")
        next(csv_laeser)
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







