class Parent():
    def print_last_name(self):
        print('Morita')


class Child(Parent):
    def print_first_name(self):
        print('Anderson')

    def print_last_name(self): # in case I wanna overwrite
        print('Saito')

ander = Child()
ander.print_first_name()
ander.print_last_name()