import random
import time
import json

def runSimulation():
  t1s,t2s = 0,0
  for _ in range(0, 10):
    t1dr = random.randint(1,6) + random.randint(1,6)
    t2dr = random.randint(1,6) + random.randint(1,6)
    if t1dr == 7:
      t1s = 0
    else:
      t1s += t1dr
    if t2dr == 7:
      t2s = 0
    else:
      t2s += t2dr
  return t1s, t2s

def runFunc(it):
  t1w,t2w = 0,0
  for _ in range(0, it):
    a1, a2 = runSimulation()
    if a1 > a2:
      t1w += 1
    elif a2 > a1:
      t2w += 1 
  return t1w, t2w

def runTournament(gpr, r):
  t1w, t2w, ties = 0,0,0
  for _ in range(0, r):
    r1w, r2w = runFunc(gpr)
    if r1w > r2w:
      t1w += 1
    elif r2w > r1w:
      t2w += 1
    else:
      ties += 1
  return t1w, t2w, ties

def doAll(i, xit):
  start_time = time.time()
  t1w, t2w, ties = runTournament(i, i)
  L = json.dumps({
      "iterations": i*i,
      "team_1_wins": t1w,
      "team_2_wins": t2w,
      "ties": ties,
      "time_taken": time.time()-start_time,
      "xIt": xit,
      "t1wp": t1w/i*i,
      "t2wp": t2w/i*i,
      "tiep": ties/i*i
  })+'\n'
  return L

for i in range(1, 10000000000):
  if i % 100 == 0:
    print(f'Iterating on {i}')
    for x in range(0, 5):
      L = doAll(i, x)
      file1 = open("data.txt", "a")
      file1.write(L)
      file1.close()
