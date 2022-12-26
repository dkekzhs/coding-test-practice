input_data = "a1"
row = int(input_data[1])
col = int(ord(input_data[0]) - int(ord(input_data[0]))) +1
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
count = 0
for step in steps:
    nx = row + step[0]
    ny = col + step[1]
    if nx >= 1 and nx <=8 and ny >= 1 and ny<=8:
        count +=1
print(count)