

file = open("my_file.txt",encoding="utf-8")

contents = file.read()
print(contents)
file.close()
print("#"*50)


# "r" - Read - Default. Opens for reading,   error if the file does not exist
# "a" - Append - Opens for appending,        creates the file if it does not exist
# "w" - Write - Opens for writing,           creates the file if it does not exist
# "x" - Create - Creates the file,           returns an error if the file exists

"""
with open("my_file.txt", mode="w", encoding="utf-8") as file2:
    file2.write("yeni yazıığ")
"""
with open("my_file.txt", mode="a", encoding="utf-8") as file2:
    file2.write("lan asjkldhnasdjkfhnsjk\n")