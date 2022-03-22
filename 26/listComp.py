listOld = [1,2,3,4,5,6]
listNew = [i + 1 for i in listOld]

print(listNew)

listnew2 = [num*2 for num in range(1,5)]
print(listnew2)

names = ["alperen", "aslfjaef","sdsda","alskjnlka","sdf","sadşklfjklsdf"]

namesUpper = [name.upper() for name in names if len(name) > 5]
print(namesUpper)

numbers = [1,1,2,3,5,8,12,21,33,55]
numberNew = [num*num for num in numbers]
result = [num**2 for num in numbers if num% 2 == 0]
print(numberNew, result)

with open("file1.txt") as file1:
    file1List = [int(num) for num in file1.readlines()]

with open("file2.txt") as file2:
    file2List = [int(num) for num in file2.readlines()]

print(file2List, file1List)
sames = [num for num in file1List if num in file2List]

print(sames)
