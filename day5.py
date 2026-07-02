#      statement/block of code to be executed

# age = 10
# if age > 18:
#      print("you can vote")
# else:
#      print("You cannot vote")

# password = "nepal12366"

# if password=="nepal123":
#      print("login success, password matched")
# else:
#      print("Login failed, password didnt matched")


marks = 80

# if marks >= 90:
#     print("A+ aayo")
# elif marks >= 80:
#     print("A aayo")
# elif marks >= 70:
#     print("B+ aayo")
# else:
#     print("fail vaiyo")


for i in range(1,5):
    print(i, end=" ")


countries = ["japan", "usa", "nepal"] #list
# Loop through the list and print each country
for country in countries:
    print(country)

prediction_scores = [77, 99, 23, 67]

# Loop prediction_scores
for score in prediction_scores:
    if score > 80:
        print(f"{score}: good")
    else:
        print(f"{score}: not good score")
   

emails_lists = [
    "Bhatbhateeni ma discount",
    "Yeti airlines free ticket congrats jityo",
    "What is the project update guys?",
    "Congratutionss, you won rolex watch"
]
for email in emails_lists:

    lower_email = email.lower()
    

    if "congrats" in lower_email or "congrat" in lower_email:
        print(f"'{email}' -> spam")
    else:
        print(f"'{email}' -> non spam")   