n = str(input())
p = 'программист'
if (n[len(n)-2]+n[len(n)-1]) == '11' and n != '1' or n == '0' or n == '1000': print(n,p+'ов')
elif n[len(n)-1] == '1': print(n,p)
elif 1<int(n[len(n)-1])<5 and not 11<int((n[len(n)-2]+n[len(n)-1]))<15: print(n,p+'а')
elif 1<int(n[len(n)-1])<10 or n[len(n)-1] == '0': print(n,p+'ов')
