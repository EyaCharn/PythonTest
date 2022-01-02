#the number of stalls
NumStalls = int(input())
#the prefered temperature of the stalls
PreferedTemp = list(map(int,input().split()))

#the current temperature of the stalls
CurrentTemp = list(map(int,input().split()))

#the difference between the prefered temp and the current temp
Difs = [x-y for x,y in zip(PreferedTemp,CurrentTemp)]

print(sum(abs(x-y) for x,y in zip(Difs+[0],[0]+Difs))//2)