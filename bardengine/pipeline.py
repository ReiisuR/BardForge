class Pipeline:

    def __init__(self):
        self.steps = []

    def add(self, step):
        self.steps.append(step)

    def run(self, song):
        for step in self.steps:
            step.process(song)