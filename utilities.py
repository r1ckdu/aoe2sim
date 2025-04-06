class Resources:
    food: int
    wood: int
    gold: int
    stone: int

    def __init__(self, food=0, wood=0, gold=0, stone=0):
        self.food  = food
        self.wood  = wood
        self.gold  = gold
        self.stone = stone

    def possible(self, food, wood, gold, stone):
        if (food  >= self.food ) and \
           (wood  >= self.wood ) and \
           (gold  >= self.gold ) and \
           (stone >= self.stone):

           return True
        else:
            return False
