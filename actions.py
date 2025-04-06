class Action:
    name: str

class LureBoar(Action):
    def __init__(self):
        self.name = "Lure Boar"

class KillHerdable(Action):
    def __init__(self):
        self.name = "KillHerdable"

class Build(Action):
    def __init__(self):
        self.name = "Build"

class GatherFood(Action):
    def __init__(self):
        self.name = "Gather Food"