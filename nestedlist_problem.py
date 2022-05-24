r=[]
mark=[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        r.append([name,score])
        mark.append(score)
mark=sorted(set(mark))
m=(mark[1])
n=[]
for i in r:
        if m==i[1]:
               n.append(i[0])
n.sort()
for j in range(len(n)):
        print(n[j])