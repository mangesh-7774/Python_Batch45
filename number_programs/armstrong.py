def armstrong(num):
    num_digit=len(str(num))
    total=0
    temp=num
    while temp>0:
        digit=temp%10
        total+=digit**num_digit
        temp//=10
    return total==num
num=int(input("Enter number:"))
if armstrong(num):
    print(f"{num} is an armstrong number")
else:
    print(f"{num}is not an armstrong num")