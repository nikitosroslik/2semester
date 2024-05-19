a = [int(x) for x in input().split()]
pred = a[0]
mass_nevoz = []
mass_prom = [pred]
for i in range(1, len(a)):
    znach=a[i]
    if znach <= pred:
        if len(mass_prom)==0:
            mass_prom.append(pred)
        mass_prom.append(znach)
    else:
        if len(mass_prom)>0:
            mass_nevoz.append(mass_prom)
        mass_prom=[]
    pred = znach
mass_nevoz.append(mass_prom)
mass=[len(i) for i in mass_nevoz]
print(" ".join(list(map(str,mass_nevoz[mass.index(max(mass))]))))
