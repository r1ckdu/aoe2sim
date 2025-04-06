from units import Villager


class Queue:
    items: list = []

    def __init__(self, maxsize):
        self.maxsize = maxsize

    def append(self, item):
        if self.items.__len__() <= self.maxsize:
            self.items.append(item)


class Building:
    name: str
    actions: list
    population: int

    def __init__(self, parent):
        self.parent = parent


class TownCenter(Building):
    queue_size: int = 15
    queue = Queue(queue_size)

    def __init__(self, parent):
        super().__init__(parent)

        self.population = 5

        self.actions = ["TrainVillager", "ResearchLoom"]

    def action(self, what):
        match what:
            case "TrainVillager":
                to_train = Villager(self.parent)
                if self.parent.resources.food >= to_train.cost.food:
                    self.queue.append(to_train)
                    self.parent.resources.food -= to_train.cost.food
            case "ResearchLoom":
                raise NotImplementedError()

    def progress(self, now, delta_t):
        if len(self.queue.items) == 0: return
        item = self.queue.items[0]
        match item:
            case Villager():
                if self.parent.add_training_unit(item):
                    item.train(now)
                    if item.is_trained:
                        self.parent.villagers.append(item)
                        self.queue.items.remove(item)
                        self.parent.training_units.remove(item)