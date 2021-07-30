with open(".\Day 7\input.txt") as f:
    content = f.readlines()
RawBags = [x.strip().replace(" ", "").replace(".","").replace("bags", "").replace("bag", "") for x in content] 
Bags = []

class BagClass:
    def __init__(self, Colour, ContainedBags, empty):
        self.Colour = Colour
        self.ContainedBags = ContainedBags
        self.empty = empty

Colours = [Bag.split("contain")[0] for Bag in RawBags]


AllBags = {}
for RawBag in RawBags:
    InitialBag = RawBag.split("contain")[0]
    ContainedBags = RawBag.split("contain")[1]
    ContainedBagsList = ContainedBags.split(",")
    BagDictionary = {}
    if ContainedBagsList[0][1:] in Colours:
        for Bag in ContainedBagsList:
            BagDictionary[Bag[1:]] = Bag[0]
        AllBags[InitialBag] = BagClass(InitialBag, BagDictionary, False) 
    else:
        AllBags[InitialBag] = BagClass(InitialBag, None, True)


def GoldBagCheck(Bags, BagName, count):
    if count == 1:
        return 1
    Bag = Bags[BagName]

    if Bag.empty == True:
        return 0

    else:
        for SubBag in Bag.ContainedBags:
            # print("SUB BAG",SubBag)
            if "shinygold" in Bag.ContainedBags:
                count = 1
            count = GoldBagCheck(Bags, SubBag, count)
        return count

count = 0
for Bag in AllBags:
    # print("MAIN BAG",Bag)
    count += GoldBagCheck(AllBags, Bag, 0)

print(count)




