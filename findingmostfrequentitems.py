from collections import Counter

text = "A number of other sites were affected, including those of Ohio's First Lady Karen Kasich, " \
       "the Ohio Department of Rehabilitation and Corrections, the Ohio Office of Health Transformation, " \
       "the Ohio Inspector General and the Ohio Department of Medicaid."

words = text.split()
#print(words)

counter = Counter(words)
top_two = counter.most_common(2)
print(top_two)