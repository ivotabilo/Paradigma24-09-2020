Sal,Via,Dif = map(int,input().split())
if Sal==0:
    Sal=24
llega= Sal+Via+Dif
if llega>24:
    llega=llega-24
    print(llega)
elif llega==24:
    llega=0
    print(llega)
else:
    print(llega)

