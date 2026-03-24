dict={1:"name",2:"class",3:"course",4:"subject"}
print("the original dictionary is",dict)
print("accesing the elements of dictionary",dict[2])
print("accesing the elements of dictionary",dict[1])
dict[4]="topic"
print("updated dictionary is",dict)
dict.pop(4)
print("dictionary after removing last element",dict)
dict2={5:"chapter",6:"writer"}
merge=dict|dict2
print("merged dictionaries =",merge)

