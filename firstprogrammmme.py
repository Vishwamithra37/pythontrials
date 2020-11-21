print("Enter a value greater than zero and press enter")
count=0
total=0
while True:
    line=input("integer")
    if line:
        number=int(line)
        total+=number
        count+=1
    else:
        break
if count:
    print("count=", count)
    print("total=", total)
    print("mean=", total/count)
    
            
