#item = ['December 23, 2017', 'Bread Gloves', 8.51]
#print(item[0])
#date, name, price = ['December 23, 2017', 'Bread Gloves', 8.51]
#print(name)

def drop_first_last(grades):
    first, *middle, last = grades #dynamic "*"
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([65, 76, 98, 54, 21])