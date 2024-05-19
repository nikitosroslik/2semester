import csv
m=[]
with open('tttt.csv') as a:
    reader=csv.reader(a, delimiter=';')
    for row in reader:
       m.append(row[1])
ans=[]
for i in range(len(m)):
    if m[i].isdigit():
        ans.append(int(m[i]))
print(sum(ans))
