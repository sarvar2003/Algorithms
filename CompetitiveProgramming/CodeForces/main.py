def main():
   n = int(input())
   msg = "I hate"

   for i in range(2, n+1):
      if i % 2 == 1: msg += " that I hate"
      else: msg += " that I love"

   print(msg, end= " it")
main()
