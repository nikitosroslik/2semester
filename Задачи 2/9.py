class Produkt:
    def __init__(self, name, zena, N):
        self.name = name
        self.zena = zena
        self.N = N
        
    def dobavka(self):
        print('Товара "',self.name,'" -', self.N)
        a=int(input('введите на сколько хотите увеличить товар:  '))
        b=self.N + a
        print('на складе теперь ',b," товар(а)")
    
    def ybrat(self):
        print('Товара "',self.name,'" -', self.N)
        a=int(input('введите на сколько хотите уменьшить товар:  '))
        b=self.N - a
        if a>self.N:
            print('на складе недостаточно товара для уменьшения')
        else:
            print('на складе теперь ',b," товар(а)")
    def cost(self):
        print('Товара "',self.name,'" -', self.N)
        g=self.N*self.zena
        print('общая стоимость товара: ',g)
        
p1 = Produkt("фломастеры",100,0)
p2 = Produkt("апельсины", 30,3)
p3 = Produkt("бутылки",20,4500000)

p3.cost()
