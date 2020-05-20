def main():
  print("Keep it logically awesome.")
  import random
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  print(quotes[rnd])

if __name__== "__main__":
  main()
