from utilities import Resources
from actions import Action, LureBoar, KillHerdable, GatherFood, Build
from unit_classes import Civillian


class Unit:
    cost: Resources
    s_class: str
    training_time: int
    hit_points: float
    attack: float
    attack_time: float
    last_attack_time: float = -1
    speed: float
    line_of_sight: float
    actions: list[Action]
    task = None
    is_trained: bool = False
    t_train_start: float

    def __init__(self, parent):
        self.parent = parent

    def train(self, now):
        if self.t_train_start is None:
            self.t_train_start = now
        if self.t_train_start - now >= self.training_time:
            self.is_trained = True


class Combatant(Unit):
    pass


class Villager(Unit):
    def __init__(self, parent):
        super().__init__(parent)
        self.cost = Resources(food=50)
        self.s_class = Civillian
        self.training_time = 25
        self.t_train_start = None
        self.hit_points = 25
        self.attack = 3
        self.attack_time = 2
        self.speed = .8
        self.line_of_sight = 4
        self.actions = [LureBoar, KillHerdable, GatherFood, Build]
        self.task = None

    def train(self, now):
        if self.t_train_start is None:
            self.t_train_start = now
        if now - self.t_train_start >= self.training_time:
            self.is_trained = True
