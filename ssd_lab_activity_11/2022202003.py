import csv


l = []
with open('lab_11_data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        l.append(row[0:7])

temp = l[0]
del l[0]

new_l = filter(lambda x: False if float(x[-1]) < -3 else True, l)

newww = []
for i in new_l:
    newww.append(i)

with open('avg_output.txt', 'w') as avgfile:
    openval = [i[1].replace(",", "") for i in newww]
    highval = [i[2].replace(",", "") for i in newww]
    lowval = [i[3].replace(",", "") for i in newww]

    openval = list(map(float, openval))
    highval = list(map(float, highval))
    lowval = list(map(float, lowval))

    avgopen = lambda x: sum(x)/len(x)   

    avgfile.write(str(avgopen(openval)) + "\n")
    avgfile.write(str(avgopen(highval)) + "\n")
    avgfile.write(str(avgopen(lowval)))

with open('stock_output.txt', 'w') as csvfile:
    cha = input("Enter Character: ")
    for i in newww:
        if (i[0][0] == cha.upper()):
            csvfile.write(" ".join(i) + "\n")
