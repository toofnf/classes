class Node(object): #объявили класс "Узел"
    def __init__(self, contained_object, next): #Конструктор
        self.contained_object = contained_object
        self.next = next

class MyQueue(object): #объявили класс "Очередь"
    def __init__(self): #конструктор изначально пустой очереди
        self.head = None #начало очереди (голова)
        self.end = None #конец очереди (так удобнее работать)

    def add(self,i,x): #добавление элемента x на позицию номер i
        if self.head == None: #если очередь пока пустая, то добавим элемент - он будет и первым, и последним (он же один будет)
            self.head = self.end = Node(x, None)
            return
        if i == 0: #добавление в начало списка
          self.head = Node(x,self.head)
          return
        #далее добавление в произвольную часть списка (но не в начало), мы итерируемся по списку до нужной нам позиции и ставим элемент на нужное место
        current = self.head #отслеживаемый элемент
        count = 0 #номер отслеживаемого элемента
        while current != None: #отслеживаемый элемент существует
            count += 1 #счетчик увеличиваем
            if count == i: #если позиция счетчика совпадает с необходимой то ок
              current.next = Node(x,current.next)
              if current.next.next == None: #проверка на то чтобы очередь не закончилась внезапно
                self.end = current.next
              break #что хотели - сделали
            current = current.next

    def remove(self, i): #удаление элемента, стоящего на позиции номер i
        if self.head == None: #если очередь пустая, то и удалять нечего
            return
        current = self.head #удаление элемента, стоящего в произвольной части списка, мы итерируемся по списку до нужной нам позиции и удаляем нужный элемент
        count = 0
        if i == 0: #удаление первого узла в очереди
            self.head = self.head.next
            return
        while current != None:
            if count == i:
                if current.next == None: #убеждаемся что очередь заканчивается коректно
                    self.end = current
                previous.next = current.next #сдвиг очереди вперед
                break
            previous = current
            current = current.next
            count += 1

    def clear(self):
        self.__init__() #очередь пустая теперь (конструктор породил НИЧТО)

    def convert_into_array(self):
        current = self.head
        arr = []
        while current != None:
            arr.append(current.contained_object)
            current = current.next
        return arr

    def print_queue(self):
        current = self.head
        if current == None:
            print('Очереди нет.')
        else:
            print('Вот ваша очередь: ',end="")
            while current != None:
                if current == self.end:
                    print(' ->', current.contained_object)
                else:
                    print(' ->', current.contained_object, end="")
                current = current.next

class Country(object):
    def __init__(self,population,capital):
        self.population = population
        self.capital = capital

    def __str__(self):

        return(f"Население данной страны составляет {self.population} человек, а её столица - {self.capital}.")

#разберемся с первой очередью (из чисел)
queue1 = MyQueue() #создали очередь, далее обозначаем числа
q101 = 1
q102 = -2
q103 = 3
q104 = 5
#создаем узлы
q11 = Node(q101,q102)
q12 = Node(q102,q103)
q13 = Node(q103,q104)
q14 = Node(q104,None)
#формируем из узлов очередь
queue1.add(0,q11.contained_object)
queue1.add(1,q12.contained_object)
queue1.add(2,q13.contained_object)
queue1.add(3,q14.contained_object)
#печатаем
queue1.print_queue()

#делаем АБСОЛЮТНО то же самое но со странами
queue2 = MyQueue() #создали очередь, далее обозначаем числа
the_most_populated_country = Country("9000000000 - как же много человек!","cap1")
the_middle_populated_country = Country("5000000000 - среднее число человек!","cap2")
the_least_populated_country = Country("1000000000 - как же мало человек!","cap3")
#создаем узлы
q21 = Node(the_most_populated_country.population,the_middle_populated_country.population)
q22 = Node(the_middle_populated_country.population,the_least_populated_country.population)
q23 = Node(the_least_populated_country.population,None)
#формируем из узлов очередь
queue1.add(0,q21.contained_object)
queue1.add(1,q22.contained_object)
queue1.add(2,q23.contained_object)
#печатаем
queue1.print_queue()