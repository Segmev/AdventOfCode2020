
def earliestBus(timestamp, buses):
  waitTime = 0
  while True:
    for bus in buses:
      if (timestamp + waitTime) % bus == 0:
        return { 'id' : bus, 'wait_time': waitTime }
    waitTime += 1

def main():
  f = open("./inputs.txt")
  timestamp = int(f.readline())
  buses =  f.readline()[:-1].split(',')
  while 'x' in buses:
    buses.remove('x')
  buses = list(map(lambda x: int(x), buses))
  res = earliestBus(timestamp, buses)
  print(res['wait_time'] * res['id'])

if __name__ == "__main__":
  main()
