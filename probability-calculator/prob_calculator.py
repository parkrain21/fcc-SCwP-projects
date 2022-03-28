import random
import copy
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    
    for ball_color, qty in kwargs.items():
      for i in range(qty):
        self.contents.append(ball_color)

  def draw(self, num_balls=1):
    drawn_contents = []  

    if num_balls >= len(self.contents):
      return self.contents
    for n in range(num_balls):  
      ball = self.contents.pop(random.randrange(len(self.contents)))
      drawn_contents.append(ball)
       
    return drawn_contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  '''
  hat = class instance object
  expected_balls = dictionary of expected result
  num_balls_drawn = access the draw function in the Hat class
  num_experiments = number of loops
  '''
  
  m = 0
  for i in range(num_experiments):

    #create a copy of the hat instance itself
    hat_copy = copy.deepcopy(hat)

    # get a list of n number of draws and put the count in a dictionary format
    balls_drawn = hat_copy.draw(num_balls_drawn)
    actual_balls = dict()

    for balls in balls_drawn:
      actual_balls[balls] = actual_balls.get(balls, 0) + 1

    # check if actual items are greater or equal to expected
    true_count = 0
    for b,q in expected_balls.items():
      if b not in actual_balls:
        break
      elif actual_balls[b] >= q:
        true_count += 1

    if len(expected_balls) == true_count:
      m += 1

  return round(m/num_experiments,3)