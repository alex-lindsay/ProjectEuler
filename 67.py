from pprint import pprint
from copy import deepcopy

rows = 100

def import_source_data(source_file_name):
  result = []
  with open(source_file_name, "r") as source_file:
    source_lines = source_file.readlines()
  result = [line.split() for line in source_lines]
  result = [[int(x) for x in line] for line in result]
  return result

def process_tree(source_data, result_data):
  print("row", rows-1, "before", source_data[rows-1])
  for row in range(rows-2, -1, -1):
    print("row", row, "before", source_data[row])
    for col in range(len(source_data[row])):
      if (result_data[row+1][col] > result_data[row+1][col+1]):
        result_data[row][col] = source_data[row][col] + result_data[row+1][col]
      else:
        result_data[row][col] = source_data[row][col] + result_data[row+1][col+1]
    print("row", row, "after", result_data[row])


def main():
  source_file_name = "p067_triangle.txt"
  source_data = import_source_data(source_file_name)
  # print(source_data[:rows])
  result_data = deepcopy(source_data)
  process_tree(source_data, result_data)
  # print(result_data[:rows])
  print(result_data[0])

main()