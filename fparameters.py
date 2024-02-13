def safarimidmorning(name,age,gender):
    print(f"My name is {name} and I am {age} years.({gender})".format(name=name,age=age,gender=gender))
# safarimidmorning(name="John",age="18",gender="male")
# safarimidmorning(name="Ray",age="12",gender="gay")
# safarimidmorning(name="Aubrey",age="18",gender="female")
# safarimidmorning(name="Odic",age="59",gender="rather not say")
# safarimidmorning(name="John",age="18",gender="male")

def palindrome(s):
    test_string=''.join(s.split()).lower()
    return test_string==test_string[::-1]


inp_string=input("Enter the word: ")
if palindrome(inp_string):
    print("Palindrome")
else:
    print("Not Palindrome")
