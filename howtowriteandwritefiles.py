'''fw = open('sample.txt', 'w')
fw.write('Write somenthing bla bla bla\n')
fw.write('I like egg\n')
fw.close()'''

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()