X = int(input())
Z = int(input())
N = int(input())


pcord = [[i,j,k] for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i+j+k != N]
print(pcord)