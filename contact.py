
# example program for dictionary
# // this block of code is an example of JSON format 
contacts = {
    "number":4,
    "students":
    [
        {"name":"Harry Potter","email":"harrypotter@example.com"},
        {"name":"Lilly Potter","email":"lillypotter@example.com"},
        {"name":"James Potter","email":"jamespotter@example.com"},
        {"name":"Genny Potter","email":"gennypotter@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])


