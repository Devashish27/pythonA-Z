def searcher():
    import time
    # Some 4 Seconds Time Consuming Tasks..!
    book = "This is a book on jimmy and his fellows and its very good"
    time.sleep(4)

    while True:
        text = (yield)

        if text in book:
            print("Your book is good in story...")
        else:
            print("Your book is not good in book story...")


search = searcher()
print("Search Started!!")
next(search)
print("Next Method Running...")
search.send("Tyro")

search.close()
search.send("jimmy..!!")

# input("Press Any Key!")
# search.send("jimmy and his fellows")
# input("Press Any Key!")
# search.send("Awsome man")
# input("Press Any Key!")
# search.send("Oh My God!! ")
# input("Press Any Key!")
# search.send("Have You Got Any ")



# Example:
# def name_definer():
#     names = open('text.txt', 'r')
#     reader = names.read()
#
#     while True:
#         text = (yield)
#         if text in reader:
#             print('Your name is in the list')
#         else:
#             print("You are not in the list")
#
# inp = input("Enter your name here: ")
# search = name_definer()
# next(search)
# search.send(inp)
