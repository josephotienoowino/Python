import random
def random_walk_2(n):
    x,y=0,0 #initializing x,y as first value assign x and second value assign y.
    for i in range(n):# we uses for loop to simulate 'n' block
      (dx,dy)=random.choice([(0,1), (0,-1), (1,0),(-1,0)])#dx, dy is just an abbreviation for values in difference in x and y"
      x+=dx
      y+=dy
      return(x,y)
    number_of_walk=1000
    for walk_length in range(1,31):
      no_transport = 0
      # number of walks 4 or fewer blocks from home
    for i in range(number_of_walk):
      (x,y)=random_walk_2(walk_length)
      distance=abs(x)+abs(y)
      if distance<=4:
        no_transport+=1
        no_transport_percentage=float(no_transport)/number_of_walk
        print("walk size=", walk_length, "/% no transport=", 100*no_transport_percentage)