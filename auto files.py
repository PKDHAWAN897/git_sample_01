for i in range(30):
    with open("%s.txt"%(i+1),'w') as f:
        f.write(str(i+1)*10)
