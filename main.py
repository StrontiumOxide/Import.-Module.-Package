import datetime as dt
from application import people as p, salary as s
from dirty_main import *

if __name__ == '__main__':
    time = dt.datetime.now().date()
    print(time)
    print(p.get_employess())
    print(s.calculate_salary())