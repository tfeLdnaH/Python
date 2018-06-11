def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age

amorita = allowed_dating_age(27)
maluco = allowed_dating_age(49)
print("Anderson can date girls:", amorita, "or older")
print("Maluco can date girls:", maluco, "or older")