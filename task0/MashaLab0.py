import random
random.seed()

my_list = []
my_list2 = []
index = 0
n_index = 0
biggest = -101

for i in range(30):
    my_list.append(random.randint(-100, 100))
print("First list: \n", my_list)

for number in my_list:
    index+=1
    if number>biggest:
        biggest=number
        n_index=index
print("The biggest number =", biggest, ". Serial number =" , n_index)

for i in range(len(my_list)):
    if my_list[i]%2!=0:
        my_list2.append(my_list[i])
my_list2.sort(reverse=True)
print("List of unpaired numbers sorted from highest to lowest: \n", my_list2)
