from collections import namedtuple
from math import sqrt
from queue import Queue

Leaf = namedtuple('Leaf', ['x','y'])
Step = namedtuple('Step', ['leaf', 'path', 'dist'])

def distance(l1, l2):
  return sqrt((l1.x-l2.x)**2 + (l1.y-l2.y)**2)

def reachable_leaves(step, leaves, max_dist=10):
  reachable = []
  for leaf in leaves:
    if distance(step.leaf, leaf) <= max_dist:
      if leaf not in step.path:
        reachable.append(leaf)
  return reachable

def swim(R, X, Y):
  if R <= 10:
    return '%.2f'%R # trivial
  # convert to points
  leaves = []
  for i in range(0, len(X)):
    leaves.append(Leaf(x=X[i],y=Y[i]))
  
  q = Queue()
  
  s_path = None
  s_dist = None
  
  for leaf in leaves:
    if leaf.x <= 10:
      q.put(Step(leaf=leaf, path=[leaf], dist=leaf.x))
  
  while not q.empty():
    step = q.get()
    
    if (R - step.leaf.x) <= 10:
      # possible solution
      if s_path is None:
        s_dist = step.dist + (R-step.leaf.x)
        s_path = step.path
        continue
      else:
        if s_dist > (step.dist + (R - step.leaf.x)):
          s_dist = step.dist + (R-step.leaf.x)
          s_path = step.path
          continue
     
    for r_leaf in reachable_leaves(step, leaves):
      if s_dist is not None and s_dist < step.dist + distance(step.leaf, r_leaf):
        continue
      q.put(Step(leaf=r_leaf, path=step.path+[r_leaf], dist=step.dist + distance(step.leaf, r_leaf)))
  
  
  if s_dist is None:
    return 'feels bad man'
  return '%.2f'%s_dist