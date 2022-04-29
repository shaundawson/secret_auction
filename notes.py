#Day9: Dictionaries & Nesting

# programming_dictionary = {
#     "Bug":"An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

#Retrieve item from dictionary
# print(programming_dictionary["Bug"])

#Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

#Create an empty dictionary
# empty_dictionary ={}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])



#EXERCISE: GRADING PROGRAM EXERCISE
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

#Create an empty dictionary called student_grades.
# student_grades = {}

#Add the grades to student_grades.
# for student in student_scores:
#     test_score = (student_scores[student])
#     if test_score >= 91:
#         student_grades[student] = "Outstanding"
#     elif test_score <= 90 and test_score >= 81:
#         student_grades[student]= "Exceeds Expectations"
#     elif test_score <= 80 and test_score >= 71:
#         student_grades[student] = "Acceptable"
#     else: 
#         student_grades[student] = "Fail"    
        
# print(student_grades)


#NESTING
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting list in a dictionary, Nesting dictionary in a dictonary
travel_log = {
    "France": {
        "cities_visited":["Paris", "Lille", "Dijon"], 
        "total_visits": 12
},
    "Germany":{
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
              },
}

#Nesting a dictionary in a list
travel_log = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits":5
  },   
]



