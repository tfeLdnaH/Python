def health_calc(age, apples_ate, cigs_smoked):
    answ = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answ)

amorita_list = [27, 20, 0]

health_calc(amorita_list[0], amorita_list[1], amorita_list[2])
health_calc(*amorita_list)