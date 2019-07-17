import itertools as it
import time
def done():
  return False

def main():
  # load the encrypted file
  with open('p059_cipher.txt') as f:
    source_data = [int(x) for x in f.read().split(',')]
    print('source data has ' + str(len(source_data)) + ' elements.')
  keys = it.product(range(ord('a'),ord('z')+1), repeat=3)
  for key in keys:
    # decrypt the file with the current key (cycled)
    decrypted = ''.join([chr(a^b) for (a,b) in zip(source_data, it.cycle(key))])
    index = decrypted.find(" ")
    index2 = decrypted.find(" ", index+1)
    
    print('key: ' + ''.join([chr(x) for x in key]) + " produces " + decrypted[0:50] + "...")
    if (index < 10) and (index > -1) and (index2 < 20) and (index2 > -1):
      # output the key and decryption
      print('key: ' + ''.join([chr(x) for x in key]) + " produces " + decrypted[0:50] + "..." + str(sum([ord(x) for x in list(decrypted)])))
      time.sleep(5)

main()