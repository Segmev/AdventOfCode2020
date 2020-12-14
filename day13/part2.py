
def suitableTimestamp(buses):

  busDict = {}
  for index, bus in enumerate(buses):
    if bus != 0:
      busDict[bus] = index
  print(busDict)

  step = 1
  timestamp = 0
  while timestamp % step != 0:
    timestamp += 1
  iteMax = 0
  while True:
    count = 0
    keys = []
    for key, val in busDict.items():
      if ((timestamp) + val) % key != 0:
        break
      keys.append(key)
      count += 1
    if count > iteMax:
      while count > iteMax:
        step *= keys[-(count-iteMax)]
        iteMax+=1
    if len(keys) == len(busDict):
      return timestamp
    timestamp += step

def main():
  f = open("./inputs.txt")
  _ = int(f.readline())
  buses =  f.readline()[:-1].split(',')
  buses = list(map(lambda x: 0 if x == 'x' else int(x), buses))
  print(buses)
  print(suitableTimestamp(buses))


if __name__ == "__main__":
  main()
