def function_1(prev, cur):
    lok=[55.8039100,37.7459800]
    izm=[55.7895600,37.7431300]
    sok=[55.7712800,37.7451300]
    sho=[55.7586000,37.7460100]
    if prev == cur:
        return 'stay'
    if 55.7586000 <= cur[0] <=  55.8039100:
        if get_distance(cur, sho) < get_distance(prev, sho):
            return 'I'
        elif get_distance(cur, lok) < get_distance(prev, lok):
            return 'II'
        elif get_distance(cur, sho) > get_distance(prev, sho):
            return 'II'
        elif get_distance(cur, lok) > get_distance(prev, lok):
            return 'I'
        else:
            return 'x'
    elif cur[0] > 55.8039100:
        if get_distance(cur, lok) < get_distance(prev, lok):
            return 'I'
        elif get_distance(cur, lok) > get_distance(prev, lok):
            return 'II'
        else:
            return 'x'
    elif cur[0] < 55.7586000:
        if get_distance(cur, sho) < get_distance(prev, sho):
            return 'II'
        elif get_distance(cur, sho) > get_distance(prev, sho):
            return 'I'
        else:
            return 'x'
    else:
        return 'x'

def get_distance(p1, p2):
    return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5

def function_2():
    file = open('bd.csv')
    info = file.read().split('\n')
    file.close()
    for i in range(len(info)):
        info[i] = info[i].split(',')
    prev = int(info[0][0])
    marshrutes = [[]]
    ind = 0
    for i in range(len(info)):
        if info[i][0]:
            A = int(info[i][0])
            B = float(info[i][1])
            C = float(info[i][2])
            D = int(info[i][3])
            if abs(A-prev) > 400:
                ind+=1
                marshrutes.append([])
            marshrutes[ind].append([A,B,C,D])
            prev = A
    counter=0
    errors = []
    m1 = []
    m2 = []
    for i in range(len(marshrutes)):
        start = marshrutes[i][0][0]
        for j in range(len(marshrutes[i])):
            marshrutes[i][j][0]-=start
    for i in range(len(marshrutes)):
        a = marshrutes[i][0]
        b = marshrutes[i][-1]
        if function_1([a[1], a[2]], [b[1], b[2]]) == 'x':
            counter+=1
        if function_1([a[1], a[2]], [b[1], b[2]]) == 'I':
            m1.append(marshrutes[i])
        if function_1([a[1], a[2]], [b[1], b[2]]) == 'II':
            m2.append(marshrutes[i])
    ys = {}
    for i in m1:
        for j in i:
            a = round(j[1], 4)
            if a in ys.keys():
                ys[a].append((j[2], j[1], j[3]))
            else:
                ys[a] = [(j[2], j[1], j[3])]
    r = []
    for i in ys.keys():
        s1 = 0
        s2 = 0
        c = 0
        for j in ys[i]:
            s1 += j[0]*j[2]
            s2 += j[1]*j[2]
            c += j[2]
        r.append((s1/c, s2/c))
    res = ''
    for i in range(len(r)):
        res += f'{r[i][1]},{r[i][0]}\n'
    file = open('res1.csv', 'w')
    file.write(res)
    file.close()
    ys = {}
    for i in m2:
        for j in i:
            a = round(j[1], 4)
            if a in ys.keys():
                ys[a].append((j[2], j[1], j[3]))
            else:
                ys[a] = [(j[2], j[1], j[3])]
    r = []
    for i in ys.keys():
        s1 = 0
        s2 = 0
        c = 0
        for j in ys[i]:
            s1 += j[0]*j[2]
            s2 += j[1]*j[2]
            c += j[2]
        r.append((s1/c, s2/c))
    res = ''
    for i in range(len(r)):
        res += f'{r[i][1]},{r[i][0]}\n'
    file = open('res2.csv', 'w')
    file.write(res)
    file.close()

def function_3(dirc, cords):
    f = open('res1.csv')
    r1 = f.read().split('\n')[:-1]
    for i in range(len(r1)):
        r1[i] = list(map(float, r1[i].split(',')))
    f.close()
    f = open('res2.csv')
    r2 = f.read().split('\n')[:-1]
    for i in range(len(r2)):
        r2[i] = list(map(float, r2[i].split(',')))
    f.close()
    if dirc == "I":
        md = 1000
        mp = 0
        for i in r1:
            if get_distance(cords, i) < md:
                md = get_distance(cords, i)
                mp = i
        return mp
    elif dirc == "II":
        md = 1000
        mp = 0
        for i in r2:
            if get_distance(cords, i) < md:
                md = get_distance(cords, i)
                mp = i
        return mp
    else:
        return 'wrong direction'

class Corrector:
    def __init__(self):
        self.timedelta = 5
        self.dir = 0
        self.trace = []

    def fix(self, record):
        if self.dir:
            return function_3(self.dir, [record[1],record[2]])
        else:
            self.trace.append(record)
            a = self.trace[0]
            b = self.trace[-1]
            if abs(b[0]-a[0]) >= self.timedelta:
                dirc = function_1([a[1],a[2]],[b[1],b[2]])
                if dirc == 'I' or dirc == 'II':
                    self.dir = dirc
                    return self.fix(record)
                else:
                    return None
            else:
                return None

cor = Corrector()
print(cor.fix((1652249232,55.808840,37.745871,22)))
print(cor.fix((1652249233,55.808616,37.745861,22)))
print(cor.fix((1652249234,55.808406,37.745873,22)))
print(cor.fix((1652249235,55.808186,37.745884,22)))
print(cor.fix((1652249236,55.807990,37.745889,22)))
print(cor.fix((1652249237,55.807783,37.745891,22)))
print(cor.fix((1652249238,55.807585,37.745904,22)))
print(cor.fix((1652249239,55.807385,37.745918,22)))
print(cor.fix((1652249240,55.807210,37.745918,22)))
print(cor.fix((1652249241,55.807031,37.745919,22)))
print(cor.fix((1652249242,55.806850,37.745931,18)))
print(cor.fix((1652249243,55.806671,37.745924,18)))
print(cor.fix((1652249244,55.806501,37.745846,17)))
print(cor.fix((1652249245,55.806331,37.745874,17)))
print(cor.fix((1652249246,55.806186,37.745891,19)))

