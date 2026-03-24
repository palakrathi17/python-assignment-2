set1={25,59,77,94,32}
set2={46,90,56,32,48,88}
for i in set1:
    print(i)
union=set1.union(set2)
print("the union of the two set is",union)
intersection=set1.intersection(set2)
print("the intersection of the two set are",intersection)
diff=set1-set2
print("The difference of the two set is",diff)