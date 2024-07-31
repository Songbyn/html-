num1 = [1,2, 7]
num2 = [9,4,5]
num1.extend(num2)
num1.sort()
midNum = 0
print(int((len(num1)+1)/2))
if len(num1) % 2 != 0 :
    midNum = num1[int(((len(num1)+1)/2 - 1))]
elif len(num1) % 2 == 0 :
    midNum = (num1[int(len(num1)/2 - 1)] + num1[int(len(num1)/2)]) / 2
print(midNum)