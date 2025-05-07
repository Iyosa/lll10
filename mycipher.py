import sys

def readInput():
  return sys.stdin.read()

def caesarEncrypt(text, shiftAmt):
  cleanText = ''.join(ch.upper() for ch in text if ch.isalpha())
  encoded = ""
 
  for ch in cleanText:
    base = ord('A')
    shifted = chr((ord(ch) - base + shiftAmt) % 26 + base)
    encoded += shifted

    letterBlocks = [encoded[i:i+5] for i in range(0, len(encoded), 5)]
    finalLines = [' '.join(letterBlocks[i:i+10]) for i in range(0, len(letterBlocks), 10)]

    return '\n'.join(finalLines)

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 mycipher.py <shift>")
      return

  try:
    shiftVal = int(sys.argv[1])
    rawInput = readInput()
    result = caesarEncrypt(rawInput, shiftVal)
    print(result)
  except ValueError:
    print("Error: The argument must be an integer.")

if __name__ == "__main__":
  main()

