while True:
  try:
    n = int(input()) - 1
    lesmas = []

    l = input().split()

    while(n>=0):

        l[n] = int(l[n])

        n -= 1

    if(min(l) < 10):
        print(1)
    elif(min(l) >= 10 and min(l) < 20):
        print(2)
    else:
        print(3)
  except EOFError:
    break