class Girl:
    gender = 'female' #equal to all object
    def __init__(self, name):
        self.name = name  #inique each object

r = Girl('Raquel')
s = Girl('Stefy')

print(r.gender)
print(s.gender)
print(r.name)
print(s.name)
