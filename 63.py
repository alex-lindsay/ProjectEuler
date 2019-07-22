def main():
  result = 0
  power = 0
  while True:
    power = power + 1
    print("Working on", power, "digit numbers.")
    root = 1
    power_values = 0
    while True:
      value = pow(root, power)
      if value >= pow(10, power):
        break
      elif value >= pow(10, power-1):
        power_values = power_values + 1
        result = result + 1
        print(root, power, value, result)
      root = root+1

    if power == 100:
      break

  print("The result is", result)

main()