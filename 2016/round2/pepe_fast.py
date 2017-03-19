import math
import queue

class Result:
  def __init__(self, dist, parent):
    self.dist = dist
    self.parent = parent

class Leaf:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.routes = []
    self.result = None
  
  def __str__(self):
    return 'Leaf(x=%d, y=%d)'%(self.x, self.y)
  
  def __repr__(self):
    return self.__str__()
  
  def neighbours(self):
    return [r.l2 for r in self.routes]

class Route:
  def __init__(self, l1, l2, dist):
    self.l1 = l1
    self.l2 = l2
    self.dist = dist
  
  def __str__(self):
    return '%s -> %s dist=%d' % (self.l1, self.l2, self.dist)
  def __repr__(self):
    return self.__str__()

class PepeGraph:
  def __init__(self):
    self.leaves = []
    self.routes = []

def distance(l1, l2):
  return math.sqrt((l1.x-l2.x)**2 + (l1.y - l2.y)**2)



class Kermit:
  
  def swim(self, R, X, Y):
    r = self.swim_pepe_swim(R, X, Y)
    if r == 'feels bad man':
      return 'poor kermit'
    return r
  
  def swim_pepe_swim(self, R, X, Y):
    if R <= 10:
      return '%.2f'%R
    
    graph = PepeGraph()
    
    startBank = Leaf(0,-1)
    endBank = Leaf(R,-1)
    
    graph.leaves.append(startBank)
    graph.leaves.append(endBank)
    
    leaves = []
    for i in range(0, len(X)):
      leaf = Leaf(X[i], Y[i])
      leaves.append(leaf)
      graph.leaves.append(leaf)
    
    # start leaves
    for leaf in leaves:
      if leaf.x <= 10:
        r = Route(startBank, leaf, leaf.x)
        startBank.routes.append(r)
        graph.routes.append(r)
    if not len(startBank.routes):
      return 'feels bad man'
      
    # end routes to the other river bank
    endRoutePossible = False
    for leaf in leaves:
      if (R - leaf.x) <= 10:
        r = Route(leaf, endBank, R - leaf.x)
        leaf.routes.append(r)
        graph.routes.append(r)
        endRoutePossible = True
    
    if not endRoutePossible:
      return 'feels bad man'
    
    # all other routes
    for l1 in leaves:
      for l2 in leaves:
        if l1 != l2:
          d = distance(l1,l2)
          if d <= 10:
            l1.routes.append(Route(l1, l2, d))
            graph.routes.append(l1.routes[-1])
            l2.routes.append(Route(l2, l1, d))
            graph.routes.append(l2.routes[-1])
    
    q = []
    for leaf in graph.leaves:
      leaf.result = Result(dist=2**30, parent=None)
      q.append(leaf)
    
    startBank.result = Result(dist=0, parent=None)
    
    q = sorted(q, key=lambda k: k.result.dist)
    
    while len(q):
      leaf = q[0]
      
      if leaf == endBank:
        pass
      for route in leaf.routes: #sorted(leaf.routes, key=lambda k: k.dist):
        n = route.l2
        dist = leaf.result.dist + route.dist
        if n.result is None or dist < n.result.dist:
          n.result = Result(dist=dist, parent=leaf)
      q = sorted(q[1:], key=lambda k: k.result.dist)
    
    if endBank.result is None or endBank.result.parent is None:
      return 'feels bad man'
    
    path = []
    n = endBank
    while n.result.parent:
      path.append(n)
      n = n.result.parent
    
    path = [p for p in reversed(path)]
    #print(path)
    #print(startBank.routes)
    return '%.2f'%endBank.result.dist
        
        
      
print(Kermit().swim(23, [4,5,18,10,15,17,17,1,11,8,3,6,17,22], [30,27,4,11,19,10,21,28,27,23,15,15,5,8]))
