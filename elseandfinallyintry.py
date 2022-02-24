f1 = open("tyro.txt")

try:
    f = open("does.txt")

except EOFError as e:
    print("Print EOF Error is here", e)

except IOError as e:
    print("Print IO Error is here", e)

# except Exception as e:
#     print(e)

else:
    print("This will run only if except is not running....!!")

finally:
    print("Run This Anyway...!")
    # f.close()
    f1.close()


print("Important Stuff")
