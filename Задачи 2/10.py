class Class:
    def __init__(self,name,age,spisok,marks):
        self.spisok = spisok
        self.name = name
        self.age = age
        self.marks = marks
        
    def append(self,urok):
        self.spisok.append(urok)
        print(self.spisok)
        s=int(input('введите оценку по добавленному предмету: '))
        if s>5 or s<0:
            print('оценка может быть только от 0 до 5')
        else:
            self.marks.append(s)
            print('оценки по данным предметам: ',self.marks)
        
    def remove(self,urok):
        for i in range(len(self.spisok)):
            if self.spisok[i] == urok:
                self.marks.remove(self.marks[i]) 
        self.spisok.remove(urok) 
        print(self.spisok)
        print(self.marks)
        
    def markses(self):
        print('все предметы ученика:', self.spisok)
        s= sum(self.marks)
        w=s/len(self.marks)
        print('средний балл студента:',w)        

b = Class('Петя',23,['математика','русский'],[2,5])

b.append('литература')
