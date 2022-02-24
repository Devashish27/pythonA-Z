class Dad:
    basketball = 1


class Daughter(Dad):
    cars = 1
    basketball = 12

    def iscars(self):
        return f"Yes, I Drive {self.cars} Number Of Times"


class Grandson(Daughter):

    cars = 7

    def iscars(self):
        return f"Yo Man!!" \
            f"Yes, I Drive Very Good {self.cars} Types Of Cars Including Suv's and Muv's"


Grandpa = Dad()
sonny = Daughter()
tyro = Grandson()

# print(tyro.iscars())
print(tyro.basketball)

