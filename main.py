from random import randint

globalTotalBonds = 98952302605
bondValues = {0:98949434423, 25:2807840, 50:26795, 100:26795, 500:4944, 1000:1648, 5000:86, 10000:42, 25000:17, 50000:9, 100000:4, 1000000:2}
cumulativeBondValues = [2, 6, 15, 32, 74, 160, 1808, 6752, 33547, 60342, 2868182, 98952302605]
prizeBondValues = [1000000, 100000, 50000, 25000, 10000, 5000, 1000, 500, 100, 50, 25, 0]
myBonds = 50000
winnings = []

for i in range(myBonds):
  ticket = randint(0, globalTotalBonds)
  for j in range(len(cumulativeBondValues)):
    if cumulativeBondValues[j] > ticket:
      catagory = j
      break
  winnings.append(prizeBondValues[catagory])

print(sum(winnings))