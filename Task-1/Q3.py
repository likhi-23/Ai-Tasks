f = open(r'C:\Users\karri\OneDrive\Desktop\file-3.txt','r')
p = f.read()
print(p)
f.close()
with open(r'C:\Users\karri\OneDrive\Desktop\file-3.txt','r')as p:
    for i in p:
        j = i.split(".")
        for k in j:
            w = k.split(" ")
            for m in w:
                if len(m)>=6:
                    if m[-1]!=',':
                        print(m)
                    elif len(m)>6 and m[-1] == ',':
                            print(m[0:6])


#Most frequently used word
f = open(r'C:\Users\karri\OneDrive\Desktop\file-3.txt','r')
f1 = ""
d = 0
l = []

for i in f:
    j = i.lower().replace(',','').replace('.','').split(" ");
    for v in j:
        l.append(v);


for i in range(0, len(l)):
    k = 1;
    for j in range(i+1, len(l)):
        if(l[i] == l[j]):
            k = k+1;

    if(k > d):
        d = k;
        f1 = l[i];

print("most frequently used word: " + f1)
print("count: " + str(d))
f.close();
