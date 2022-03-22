import random

students = ["efds","sdfsdf","sadfsdf","sdfsdf"]

myDict = {student:random.randint(0,100) for student in students}

print(myDict)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

dictSentence = {word:sentence.split(" ").count(word) for word in sentence.split(" ")}

print(dictSentence)

import pandas

student_dict = {
    "students": students,
    "score": [1,2,3,5]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)

for (index, row) in student_df.iterrows():
    print(row)
    print(index," = ",row.score)
    print("###################")