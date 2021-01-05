import random

globalTotalBonds = 98952302605
bondValues = {0:0, 25:0, 50:0, 100:0, 500:0, 1000:0, 5000:0, 10000:0, 25000:0, 50000:0, 100000:0, 1000000:0}
cumulativeBondValues = [2, 6, 15, 32, 74, 160, 1808, 6752, 33547, 60342, 2868182, 98952302605]
prizeBondValues = [1000000, 100000, 50000, 25000, 10000, 5000, 1000, 500, 100, 50, 25, 0]
myBonds = 100000
trialNumber = 300
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
    bondValues[prizeBondValues[catagory]] += 1
  totalWinnings.append(sum(winnings))

averageWinnings = sum(totalWinnings)/trialNumber

text = f"""

Average monthly winnings: {averageWinnings}

Total bonds modeled: {myBonds*trialNumber}
Bonds that didn't win: {bondValues[0]}
Bonds that won 25: {bondValues[25]}
Bonds that won 50: {bondValues[50]}
Bonds that won 100: {bondValues[100]}
Bonds that won 500: {bondValues[500]}
Bonds that won 1000: {bondValues[1000]}
Bonds that won 5000: {bondValues[5000]}
Bonds that won 10000: {bondValues[10000]}

"""

f = open("output.txt", "w")
f.write(text)
f.close()