#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Letters/starting_letter.txt") as file:
    data = file.read()

with open("Input/Names/invited_names.txt") as file2:
    data2 = file2.readlines()
    for i in data2:
        i = i.strip()
        pathAndName = "Output/ReadyToSend/letterTo_" + i +".txt"
        
        with open(pathAndName,"a") as file3:
            file3.write(data.replace("[name]",i))