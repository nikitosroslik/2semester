import csv
def gog():
    with open("gog.csv") as f:
        a=csv.reader(f)
        mass_temp=[]
        for row in a:
            for i in row:
                if i[i.rfind(';')+1:].count('%')>0:
                    m=i[i.rfind(';')+1:].split()
                    if m[0].count("%")>0:
                        clima=m[0][:len(m[0])-2]
                        if clima.count("–")>0:
                            clima=clima[:-3]
                    else:
                        clima=m[0]
                    mass_temp.append(int(clima))
    print(sum(mass_temp)/len(mass_temp))                     
                    
gog()
