def expression(n):
  if n == 0:
    result = (2, 1)
  else:
    term = continued_fraction_term(n)
    result = (1, term)
    print (n, result)
  return result

def continued_fraction_term(n):
  if n==0:
    result = 2
  elif (n+1) % 3 == 0:
    result = (n+1) * 2 // 3
  else:
    result = 1
  return result

def main():
  print([continued_fraction_term(n) for n in range(20)])
  print([expression(n) for n in range(8)])

main()