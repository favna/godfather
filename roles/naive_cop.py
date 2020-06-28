from .cop import Cop


class NaiveCop(Cop):
    def __init__(self):
        super().__init__()
        self.name = 'Naive Cop'

    def result_modifier(self, innocence):
        return True
