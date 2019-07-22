import itertools

def main():
  hashes = {}
  index = 1
  most_permutations = 0
  most_hash = 0
  while True:
    if index % 10 == 0:
      print("testing index", index)
    if index >= 1000000:
      break
    cube = index * index * index
    cube_hash = "".join(sorted(list(str(cube))))
    hashes[cube_hash] = (cube_hash in hashes) and (hashes[cube_hash] + [cube]) or [cube]
    if len(hashes[cube_hash]) > most_permutations:
      most_permutations = len(hashes[cube_hash])
      most_hash = cube_hash
      if most_permutations >= 5:
        print("THE ANSWER IS:")
        print(most_hash)
        print(hashes[most_hash])
        print(min(hashes[most_hash]))
        break

    index = index+1

main()