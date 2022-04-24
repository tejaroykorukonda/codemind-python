Number = int(input())
Sum = 0
rem = 0

Temp = Number
while Temp > 0:
    rem = Temp % 10
    Sum = Sum + rem
    Temp = Temp // 10


if Number % Sum == 0:
    print("True")
else:
    print("False")