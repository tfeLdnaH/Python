import random
import sys
import os

# comentario
'''cometario multiline
#Numbers String Lists Tuples Dictionaries
#+ - * / % ** //

print("Hello world")
#myName = input('what is your name?')
#print(myName)

print("5+2=", 5+2)
print("5-2=", 5-2)
print("5*2=", 5*2)
print("5/2=", 5/2)
print("5%2=", 5%2)
print("5**2=", 5**2)
print("5//2=", 5//2)

quotes = "\"Always remenbmer"
'''


'''
grocery_list = ['juice', 'tomatos', 'potatoes','banada']

print('First item', grocery_list[0])

grocery_list[0] = 'green juice'
print('fisrt item', grocery_list[0])
print(grocery_list[1:3])

other_events = ['wash car', 'pick up kids', 'cook']

to_do_list = [other_events, grocery_list]

print(to_do_list[1][1])

grocery_list.append('Onios')
print(to_do_list)

grocery_list.insert(1, 'Picket')

grocery_list.remove('Picket')

grocery_list.sort()

grocery_list.reverse()

del grocery_list[4]

print(to_do_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))
'''


'''
pi_tuple = (3,1,4,1,5,9)

new_tuple = list(pi_tuple)

new_list= tuple(new_tuple)
len(tuple) min(tuple) max(tuple)
'''

'''
super_v = {'Fiddler': 'Isaac Bowin',
            'Captain Cold' : 'Leonard Snart',
           'Weather Wizard' : 'Mark Mardon',
           'Mirror Master': 'Sam Scudder',
           'Pied Piper': 'Thomas Peterson'
           }

print(super_v['Captain Cold'])

del super_v['Fiddler']

super_v['Pied Piper'] = 'Harley Rathaway'

print(len(super_v))

print(super_v.get('Pied Piper'))

print(super_v.keys())

print(super_v.values())
'''

#if else elif == != > >= <=
'''
age = 21

if age > 16:
    print("you are old enough to drive")
else:
    print("you are not old enough to drive")

'''

'''
for x  in range(0, 10):
    print(x, ' ', end='')
print('\n')


grocery_list = ['banana', 'tomatoes', 'potatos']

for y in grocery_list:
    print(y)

for x in [1,2,3,4,6,8]:
    print(x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])
'''

'''
random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)
'''

'''
i = 0;
while (i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i += 1
        continue

    i+=1
'''

'''
def addNumb(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

#print(addNumb(1,4))

string = addNumb(1,4)
print(string)
'''

'''
print('Whats ur name')
name = sys.stdin.readline()

print('Hello',name)
'''

'''
long_string = 'I´ll catch you if you fall - the floor'

print (long_string[0:4])

print (long_string[-5])

print (long_string[:-5])

print (long_string[:4] + "be there")

print("%c is my %s letter and my number %d number is %.5f" %
      ('X', 'favorite', 1, .14))
'''

'''
long_string = 'I´ll catch you if you fall - the floor'
print(long_string.capitalize())

print(long_string.find('floor'))

print(long_string.isalpha())

print(long_string.isalnum())

print(len(long_string))

print(long_string.replace('floor', 'ground'))

print(long_string.strip())

quote_list = long_string.split(" ")
print(quote_list)
'''

'''
#"ab+" to read & append to file
test_file = open("test.txt", "wb")

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("Wrte me to the file \n", 'UTF-8'))

test_file.close()


test_file = open('teste.txt', "r+")

text_in_file = text_file.read()

print(text_in_file)

os.remove("text.txt")
'''

#encapsulation
class Animal:
    __name = ""  # or ""   / __ indicate private
    __heigh = 0
    __weight = 0
    __sound = 0

#constructor
    def __init__(self, name, heigh, weight, sound):
        self.__name = name
        self.__heigh = heigh
        self.__weight = weight
        self.__sound = sound        

    def set_name(self, name):
        self.__name = name
    
    def set_heigh(self, heigh):
        self.__heigh = heigh
    
    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_heigh(self):
        return self.__heigh

    def get_weight(self):
        return self.__weight

    def get_sound(self):
        return self.__sound

    def get_type(self): #polimorfism
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
                                                                     self.__heigh,
                                                                     self.__weight,
                                                                     self.__sound
                                                                         )

    
cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())


#inheritance
class dog(Animal):
    __owner = ""

    def __init__(self, name, heigh, weight, sound, owner): #overwrite de contructor from animal
        self.__owner = owner
        super(dog, self).__init__(name, heigh, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner
    
    def get_type(self):
        print("dog")

    def toString(self):
        return "{} is {} cm, tall and {} kilograms, and say {}, owner {}".format(self.get_name(),
                                                                                 self.get_heigh(),
                                                                                 self.get_weight(),
                                                                                 self.get_sound(),
                                                                                 self.__owner)
    

#overload
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


spot = dog("spot", 53, 27, "Ruff", "teste")
print(spot.toString())

#polimorfism
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
spot.multiple_sounds()

'''
Whiskers is 33 cm tall and 10 kilograms and say Meow
spot is 53 cm, tall and 27 kilograms, and say Ruff, owner teste
Animal
dog
RuffRuffRuffRuff
Ruff
'''























































