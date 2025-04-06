

class Consumable:
    food: float
    gathering_rate: float
    parent = None

    def __init__(self, parent):
        self.parent = parent
        assert self.parent, "Warning, should have parent!"

    def remove(self):
        self.parent.consumables.remove(self)

    def consume(self, n_villagers, now, delta_t):
        food_gathered = n_villagers * delta_t * self.gathering_rate
        self.food -= food_gathered
        if self.food <= 0:
            self.remove()
        return food_gathered

class Berries(Consumable):
    def __init__(self, parent):
        super().__init__(parent)
        self.food = 125
        self.gathering_rate = .31

class HuntableAnimal(Consumable):
    hit_points: float
    attack_strenght: float
    attack_time: float
    speed: float
    decay_rate: float
    distance: float
    touch_time: float = -1
    last_attack_time: float = -1
    touch_time: float = -1
    is_alive: bool = True
    
    def __init__(self, parent):
        super().__init__(parent)

    def consume(self, now, delta_t):
        # for only decay call this with n_villagers=0
        # having only one method for consume/decay ensures we do not accidentally kill this without consuming or the other way round.
        if self.is_alive : return 0 # cannot consume if alive, dont do anything else.
        if touch_time < 0 : touch_time = now
        food_gathered = delta_t * self.gathering_rate
        self.food -= food_gathered
        return food_gathered
    
    def attack(self, who, now):
        if self.last_attack_time < 0:
            self.last_attack_time = now
            is_attacking = True
        elif self.last_attack_time + self.attack_time <= now:
            is_attacking = True
        else:
            is_attacking = False
        if is_attacking: who.hit_points -= self. attack_strenght
    
    def is_alive(self):
        if self.hit_points <= 0:
            self.is_alive = False
        return self.is_alive
    
    def remove_no_food(self):
        if self.food <= 0:
            self.remove()

    def decay(self, delta_t):
        if self.touch_time >= 0:
            self.food -= self.decay_rate * delta_t



class Sheep(HuntableAnimal):
    """This can be consumed and has a starting amount of food and rots after it starts being consumed with a fixed rate.
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.hit_points=7
        self.speed=0.7
        self.food=100
        self.gathering_rate= .33
        self.distance=0

class Boar(HuntableAnimal):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.hit_points = 75
        self.attack_strenght = 7
        self.attack_time = 2
        self.speed = 0.96
        self.food = 340
        self.gathering_rate = .41
        self.decay_rate = 0.4
        self.distance = 16 # guesstimation for typical arabia maps.
    