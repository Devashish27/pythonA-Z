# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)


def funargs(normal, *argsdev, **kwargsziva):
    print(normal)
    # print(type(args))
    # print(args[0])

    for item in argsdev:
        print(item)

    print("\nNow I am Introducing Some Of Our Models")

    for key, value in kwargsziva.items():
        print(f"{key} is a {value}")

# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

tyro = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "Joker"]
# tyro = ("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

normal = "I am a normal argument and the students are: "
# funargs(*tyro)

kw = {"Rohit": "Monitor", "Anjali": "Yoga Instructor",
      "Aniket": "Fitness Instructor", "Megha": "Zoomba Instructor"}

funargs(normal, *tyro, **kw)
