import csv
def write():
    f=open("data.csv","w",newline="")
    wo=csv.writer(f)
    wo.writerow(["roll no.","name","marks"])
    while True:
        rn=int(input("enter rollno:"))
        n=input("enter name:")
        m=int(input("enter marks:"))
        details=[rn,n,m]
        wo.writerow(details)
        ch=input("more?(y/n):")
        if ch=="n":
            break
    f.close()
def count():
    f=open("data.csv","r")
    count=0
    ro=csv.reader(f)
    next(ro)
    for i in ro:
        count+=1
    print(count)
    f.close()
write()
count()


