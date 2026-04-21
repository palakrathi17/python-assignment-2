import json as js
f=open("employees.json","w")
details=[]
def write():
    #n=input("enter name:")
    #i=eval(input("enter id:"))
    #sal=int(input("enter salary:"))
    #det=[i,sal]
    #d={n:det}
    d=[{"name":"shivanee","age":18,"address":"pune"}]
    js.dump(d,f)
write()
f.close()