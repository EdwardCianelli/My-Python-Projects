** start of main.py **

import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(num_balls)]    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        drawn = temp_hat.draw(num_balls_drawn)

        drawn_count = {}
        for color in drawn:
            drawn_count[color] = drawn_count.get(color, 0) + 1

        success = True
        for color, count in expected_balls.items():
            if drawn_count.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments

** end of main.py **

