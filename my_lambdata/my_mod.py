# my_lambdata/my_mod.py
# my_lambdata.my_mod

def enlarge(num):
   return num * 100

if __name__ == "__main__":
   x = 11
   print(enlarge(x))

   y = int(input("Please choose a number (e.g. 5)"))
   print(enlarge(y))