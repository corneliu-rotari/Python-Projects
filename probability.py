import random
import copy

class Hat:
    def __init__(self, **k):
        self.contents = list()
        for color, nr in k.items():
            for i in range(nr):
                self.contents.append(color)

    def draw(self, number):
        removed = list()
        if number > len(self.contents):
            return self.contents
        for i in range(number):
            rand = random.randrange(len(self.contents))
            removed.append(self.contents[rand])
            self.contents.remove(self.contents[rand])
        return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    nr_of_succesc = 0
    for i in range(num_experiments):
        existence = True
        result = dict()
        hat_copy = copy.deepcopy(hat)
        lista = hat_copy.draw(num_balls_drawn)
        for j in lista:
            result[j]= result.get(j,0) + 1
        
        for k,v in expected_balls.items():
            if k in result:
                if result[k] < v:
                    existence = False
                    break
            else:
                existence = False
                break
        if existence : nr_of_succesc+=1
    return nr_of_succesc/num_experiments

        

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)