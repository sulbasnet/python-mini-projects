choice= int(input("Enter your choice: Coding or Decoding?(1 or 2)\n"))
if choice==1:
    a=(input("Enter the word you want to code:"))
    if len(a)<3:
       print(a[::-1])
    elif len(a)>=3:
       ran=str(input("Enter 3 random words to be added in the front:\n"))
       dom=str(input("Enter 3 random words to be added at the back:\n"))
       b=a[1:]+a[0]
       print(f"Your coded word is {ran+b+dom}")
      
elif choice==2:
   a=(input("Enter the word you want to decode:"))
   if len(a)<3:
      print(a[::-1])
   elif len(a)>=3:
      b=a[3:-3]
      c=b[-1]+b[:-1]
      print(f"Your decoded word is:{c}")
