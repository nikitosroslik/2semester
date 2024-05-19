import csv

def age( data):
    allNumbers=0
    number = 0
    w=0
    m = 0
    for row in data:
        if row[0]!= 'п»їname;age ;place':
            row1 = row[0]
            start = row1.find(';')
            end =row1.find(';',start+1)
            a=row1[start+1:end]
            a1 = int(a)
            allNumbers+=a1
            number+=1
            end =row1.find(';')
            a=row1[0:end]
            print(a)
            if a == 'm':
                m+=1
            if a == 'w':
                w+=1

    print('men:', m)
    print('women:', w)
    middleNumber = allNumbers//number
    print('age:', middleNumber)


           

file1 = open("file1.csv", "r")

data = csv.reader(file1)

# poll(data)
age(data)

file1.close()

