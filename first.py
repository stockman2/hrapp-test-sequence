import datetime
import json
import sys


def fromfile(name='test.txt'):
    file = open(name, 'r', encoding='utf-8')
    newfile = open('new.json', 'w', encoding='utf-8')
    spisok = json.load(file)
    user, data = spisok.values()
    us, dt = spisok.keys()
    newdata = []
    for x in data:
        d = datetime.date.fromisoformat(dict(x)['date'])
        if abs((datetime.date(2021, 9, 1) - d).days) <= 10:
            newdata.append(x)
    json.dump(
        {us: user, dt: newdata},
        fp=newfile,
        ensure_ascii=False,
        indent=4
    )
    file.close()
    newfile.close()


def fromprompt():
    spisok2 = json.loads(' '.join(sys.stdin.readlines()))
    user, data = spisok2.values()
    us, dt = spisok2.keys()
    newdata = []
    for x in data:
        d = datetime.date.fromisoformat(dict(x)['date'])
        if abs((datetime.date(2021, 9, 1) - d).days) <= 10:
            newdata.append(x)
    json.dump(
        {us: user, dt: newdata},
        fp=sys.stdout,
        ensure_ascii=False,
        indent=4
    )


if __name__ == "__main__":
    fromprompt()
