#arithmetic operators
import time

nambari_1=int(input("Enter the first number: "))
time.sleep(0.5)
nambari_2=int(input("Enter the second number: "))
time.sleep(0.5)
print(nambari_1+nambari_2)
time.sleep(0.5)
print(nambari_1-nambari_2)
time.sleep(0.5)
print(nambari_1*nambari_2)
time.sleep(0.5)
print(nambari_1/nambari_2)
time.sleep(0.5)
print(nambari_1%nambari_2)

# comparison operators
nambari_3=int(input("Enter the third: "))
time.sleep(0.5)
nambari_4=int(input("Enter the fourth: "))
time.sleep(0.5)
print(f"{nambari_3} is equal to {nambari_4} : {nambari_3==nambari_4}")
print(f"{nambari_3} is  not equal to {nambari_4} : {nambari_3!=nambari_4}")
print(f"{nambari_3} is greater than {nambari_4} : {nambari_3>=nambari_4}")
print(f"{nambari_3} is less than {nambari_4} : {nambari_3<=nambari_4}")

nambari_5=(input("Pick a number: "))
time.sleep(0.5)
nambari_6=(input("Pick another number: "))

print(f"both statements should be true{nambari_5==9 and nambari_5==15}")
print(f"one statement should be true{nambari_5==9 or nambari_5==15}")





