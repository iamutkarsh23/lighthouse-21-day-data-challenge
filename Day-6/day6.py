import random 
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

# avg sized hole
avg_sized_hole = sum(hole_sizes)/100
print(avg_sized_hole)
sum_of_holes = 0
cost_map = [1.3,1.6,2.1]
for i in range(0,100):
    if(hole_sizes[i] < 20):
        sum_of_holes += cost_map[0]
    elif(hole_sizes[i] >= 20 and hole_sizes[i] < 70):
        sum_of_holes += cost_map[1]
    elif(hole_sizes[i] >= 70):
        sum_of_holes += cost_map[2]
print(sum_of_holes, sum_of_holes/100)

# ANSWERS

# 28.39
# 148.79999999999987 1.4879999999999987