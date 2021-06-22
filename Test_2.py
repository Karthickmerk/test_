x = input("Enter your word: ")
a= x[int(len(x)/2)]
t=""
for i in range(int(len(x)/2),len(x)):
    t=t+x[i]
    print(t)
for i in range(0,int(len(x)/2)):
    t=t+x[i]
    print(t)