# Input comma seperated elements and give it as string ang tuples
string = input("Enter comma seperated integers:")
print(string)
list = string.split(',')
print(list)
def convert(list):
    return (*list, )
print(convert(list))