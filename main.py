import cnlunar
import datetime


a = cnlunar.Lunar(datetime.datetime(1989, 1, 5, 18, 0), godType='8char')

tian = ''.join([x[0] for x in reversed([a.year8Char, a.month8Char, a.day8Char, a.twohour8Char])])
di = ''.join([x[1] for x in reversed([a.year8Char, a.month8Char, a.day8Char, a.twohour8Char])])
print(tian)
print(di)
