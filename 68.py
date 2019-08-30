import pprint, itertools

def main():
  # get 5 intersection nodes out of 10 available figures - ignore 10 since it can't be an intersection based on 
  # the rules of needing a 16 digit string
  intersection_candidates = itertools.permutations(range(1,10),5)
  candidates = []
  for intersection_candidate in intersection_candidates:
    (a, b, c, d, e) = intersection_candidate
    # for a given ring of 5 numbers, the total along any branch can be between 1+2+3 to 8+9+10
    for total in range(6,28):
      (f, g, h, i, j) = (total-a-b, total-b-c, total-c-d, total-d-e, total-e-a)
      # if any number is outside the range 1-10 continue (not allowed in solution)
      if any([x not in range(1,11) for x in [f,g,h,i,j]]):
        continue
      # if all ten numbers are not in the candidate continue (no repeats - all ten numbers must be used)
      if len(set([a,b,c,d,e,f,g,h,i,j])) < 10:
        continue
      candidates.append([f,a,b,g,b,c,h,c,d,i,d,e,j,e,a])
  pprint.pprint(candidates)
  # for each candidate, there are 5 rotations, get the one with the lowest first number
  rotations = []
  for candidate in candidates:
    angle = 0
    for current_angle in range(3,15,3):
      if candidate[current_angle] < candidate[angle]:
        angle = current_angle
    rotations.append(candidate[angle:] + candidate[:angle])
  pprint.pprint(rotations)
  answer = max(["".join([str(x) for x in rotation]) for rotation in rotations])
  print(answer)

main()