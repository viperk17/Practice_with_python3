class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def is_dance(self):
        return f"Yes I dance {self.dance} no of times"


class Grandson(Son):
    dance = 6

    def is_dance(self):
        return f"Jacksob yeah!" \
               f"Yes I dance very awesomely {self.dance} no of times."


darry = Dad()
larry = Son()
harry = Grandson()

print(harry.is_dance())

print(harry.basketball)


"""
EXERCISE:
Classes:
1. electronic device
2. pocket gadget
3. Phone
"""