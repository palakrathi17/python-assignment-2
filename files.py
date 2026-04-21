#create file
f=open("Palak.txt","w")
f.write("hello Palak\n")
print("file created successfully!!")
f.close()

#read file
f=open("Palak.txt")
print(f.read())
f.close()

#append
f=open("Palak.txt","a")
f.write("how are you?")
print("content appended successfully!!")
f=open("Palak.txt")
print(f.read())
f.close()

f=open("Palak.txt","r")
print(f.read())


f=open("Palak.txt","w")
f.write("mit adt university")
f=open("Palak.txt","r")
print(f.read())
f.close()
