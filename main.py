import random

globalTotalBonds = 98952302605
bondValues = {0:98949434423, 25:2807840, 50:26795, 100:26795, 500:4944, 1000:1648, 5000:86, 10000:42, 25000:17, 50000:9, 100000:4, 1000000:2}
cumulativeBondValues = [2, 6, 15, 32, 74, 160, 1808, 6752, 33547, 60342, 2868182, 98952302605]
prizeBondValues = [1000000, 100000, 50000, 25000, 10000, 5000, 1000, 500, 100, 50, 25, 0]
myBonds = 100000
trialNumber = 1000
totalWinnings = []

for i in range(trialNumber):
  winnings = []
  for j in range(myBonds):
    ticket = random.randint(0, globalTotalBonds)
    for k in range(len(cumulativeBondValues)):
      if cumulativeBondValues[k] > ticket:
        catagory = k
        break
    winnings.append(prizeBondValues[catagory])
  totalWinnings.append(sum(winnings))
print(sum(totalWinnings)/trialNumber)