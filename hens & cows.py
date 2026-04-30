legs=int(input("enter number of legs:"))
head=int(input("enter number of heads:"))
flag=False
for cow in range(0,head):
    cal_hens=head-cow
    cows=cow*4
    hens=cal_hens*2
    total=cows+hens
    if(total==legs):
        flag=True
        break 
if(flag==True):
    print("COWS:",cow)
    print("HENS:",cal_hens)
else:
    print("No solution"
