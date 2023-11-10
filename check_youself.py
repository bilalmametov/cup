# 1) Создайте класс Auto в нем реализуйте метод ride который выводит сообщение 'Riding on a ground'.
# Создайте класс Boat реализуйте метод swim, который выводит 'Floating on water'.
# Создайте класс Amphibian который наследуется от класса Auto и Boat.
# Создайте от него объект obj и вызовите все методы.
# Ввод:
# obj = Amphibian()
# obj.ride()
# obj.swim()
# Вывод:
# Riding on a ground
# Floating on water

# 2)Создайте класс ContactList, который должен наследоваться от встроенного класса list.
# В вашем классе должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений.
# Создайте экземпляр класса в переменной all_contacts и передайте список ваших контактов.
# Примерный ввод:

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
# print(all_contacts.search_by_name('Olya'))
# Метод search_by_name возвращает все строки содержащие подстроку "Olya":

# ['Ivan Olya', 'Olya Ivan'] 

class Auto:
    def ride(self):
        print('Riding on a ground')
class Boat:
    def boat(self):
        print('Floating on water') 

class Amphibian(Auto, Boat):
    pass

obj = Amphibian()
obj.boat()
obj.ride() 


class ContactList(list):
    def search_by_name(self, name):
        return [contact for contact in self if name.lower() in contact.lower()]

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])

results = all_contacts.search_by_name('Olya')
print(results)