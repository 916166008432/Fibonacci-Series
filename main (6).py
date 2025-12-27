def fibonacciseries(n):
    a=0
    b=1
    for i in range(1,n):
        print(a,end=" ")
        a,b=b,a+b
n=int(input())
fibonacciseries(n)    