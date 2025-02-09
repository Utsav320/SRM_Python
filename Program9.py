# Program for breaking the set into list of sets.

def listofitems(Inputsets):
    OutputList = []
    for i in Inputsets:
        emptyset = set()
        emptyset.add(i)
        OutputList.append(emptyset)
        return (OutputList)
Inputsets = {"Hello", "SRM", "family"}
print("The given set is :", Inputsets)
print("Breaking the inputed sets into list of sets:\n", listofitems(Inputsets))