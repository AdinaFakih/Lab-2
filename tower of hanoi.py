def hanoi(n,A,B,C):
  if n==1:
    print("Move disc 1 from",A,"to",B)
  else:
    hanoi(n-1,A,C,B)
    print("Move disc",n,"from",A,"to",B)
    hanoi(n-1,C,B,A)

print("There are 3 rods A,B,C")   
num=int(input("How many discs do you want to play with? "))
hanoi(num,'A','B','C')