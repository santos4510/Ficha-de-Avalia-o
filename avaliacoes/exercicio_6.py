precos = ["121",112,420,"",96,"viniccius13",14.99]

sum = 0
for index, i in enumerate(precos):
    if isinstance(i, str) and  index != 0:
        precos.pop(index)
        

for i in precos:
    if isinstance(i, (int, float)):
        sum += i

print(sum)