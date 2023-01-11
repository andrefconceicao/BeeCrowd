while True:
  try:
    n = int(input())

    i = 0
    while(i<n):
        
        j = 0

        while(j<n):
            if(i+j == n-1):
                print(2, end='')
            elif(i == j):
                print(1, end='')
            else:
                print(3, end='')
            
            j+=1

        print("\n", end='')

        i += 1
  except EOFError:
    break