s = "PAYPALISHIRING"
numRows = 3

Listarr = ["" for i in range(numRows)]

idx = 0
d = 1
for i in s :
    Listarr[idx] += i
    if idx == 0 :
        d = 1
    elif idx == numRows - 1 :
        d = -1
    idx += d

print(Listarr)
    
    
