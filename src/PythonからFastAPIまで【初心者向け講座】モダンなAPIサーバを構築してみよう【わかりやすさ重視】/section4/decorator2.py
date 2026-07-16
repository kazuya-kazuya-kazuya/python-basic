from datetime import datetime

def print_datetime(f):
  def wrapper(base, height):
    print(f'開始: {datetime.now()}')
    f(base, height)
    print(f'終了: {datetime.now()}')
  return wrapper

@print_datetime
def calc(base, height):
  print(base*height/2)

# print_datetime(calc)(3, 10)

calc(3, 10)


