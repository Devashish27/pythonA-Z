import pickle

# Pickling A Python Object..!!
# cars = ["Ferrari", "Porshe", "Mitsubishi", "Honda", "Tata", "BMW", "Merc-Benz", "Fiat", "VW", "Ford"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))

