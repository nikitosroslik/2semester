class Bank:
    def __init__(self, people, schet, balanse):
        self.people = people
        self.schet = schet
        self.balanse = balanse
        
    def show_balanse(self):
        print ('на вашем балансе:  '+self.balanse)
    def popolnit(self):
        a=int(input('введите сколько хотите ввести:  '))
        b=a*0.99
        c=self.balanse + b
        print('на вашем балансе:  ',c)
    def snat(self):
        r=int(input('введите сколько хотите вывести:  '))
        t=r*1.01
        if self.balanse < t:
            print('на вашем счете недостаточно средств!!!')
        else:
            o=self.balanse - t
            print('на вашем балансе:  ',o)
            print('вы сняли:  ',r)
        
name1 = Bank("Петя",'3333',0)
name2 = Bank("Николай", "3033",3)
name3 = Bank("Гоша","3022",4500000)

name2.snat()
