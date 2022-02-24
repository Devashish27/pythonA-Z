import time

initial = time.time()
# print(initial)

k = 0

while(k<45):
    print("This is coder DevArun!!")
    time.sleep(2)
    k += 1
print("\nWhile loop ran in ", time.time() - initial, "Seconds\n")

initial2 = time.time()
for i in range(45):
    print("This is coder DevArun!!")
print("\nFor loop ran in ", time.time() - initial2, "Seconds")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

