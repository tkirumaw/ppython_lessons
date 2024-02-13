# num=5
# while num <= 15:
#     print(num)
#     num+=1
import time

# num_2=100
# while num_2>=0:
#     print(num_2)
#     num_2-=10

#for loops

# students=["Joy","Keisha","Kevin","Joseph","Aubrey"]
# students.sort()
# for name in students:
#     time.sleep(0.5)
#     print(name)

my_numbers =[1,2,3,4,5,6,7,8,9]
total=0
while my_numbers !=3 and my_numbers !=4 and total<=90:
    for i in my_numbers :
        total = total + i
        print(total)
