import matplotlib.pyplot as plt
#улучшенная версия task1
#все решения в виде требуемых функций - в файле case_solution
def station(inp):
    lok=[55.8039100,37.7459800]
    izm=[55.7895600,37.7431300]
    sok=[55.7712800,37.7451300]
    sho=[55.7586000,37.7460100]
    delta1 = ((inp[0]-lok[0])**2+(inp[1]-lok[1])**2)**0.5
    delta2 = ((inp[0]-izm[0])**2+(inp[1]-izm[1])**2)**0.5
    delta3 = ((inp[0]-sok[0])**2+(inp[1]-sok[1])**2)**0.5
    delta4 = ((inp[0]-sho[0])**2+(inp[1]-sho[1])**2)**0.5
    delta = [delta1, delta2, delta3, delta4]
    return minimal(delta, delta1, delta2, delta3, delta4)

def minimal(delta, delta1, delta2, delta3, delta4):
    if min(delta) == delta1:
        return 'lok'
    if min(delta) == delta2:
        return 'izm'
    if min(delta) == delta3:
        return 'sok'
    if min(delta) == delta4:
        return 'sho'

def get_distance(p1, p2):
    return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5

def check_direction(fr, to):
    path = ['lok', 'izm', 'sok', 'sho']
    if path.index(fr) < path.index(to):
        return 'I'
    elif path.index(fr) > path.index(to):
        return 'II'
    else:
        return 'x'

def direction(prev, cur):
    lok=[55.8039100,37.7459800]
    izm=[55.7895600,37.7431300]
    sok=[55.7712800,37.7451300]
    sho=[55.7586000,37.7460100]
    if prev == cur:
        return 'stay'
    if 55.7586000 <= cur[0] <=  55.8039100:
        return get_dis1(cur, sho, lok, prev)
    elif cur[0] > 55.8039100:
        return get_dis2(cur, sho, lok, prev)
    elif cur[0] < 55.7586000:
        return get_dis3(cur, sho, lok, prev)
    else:
        return 'x'

def get_dis1(cur, sho, lok, prev):
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

def get_dis2(cur, sho, lok, prev):
    if get_distance(cur, lok) < get_distance(prev, lok):
        return 'I'
    elif get_distance(cur, lok) > get_distance(prev, lok):
        return 'II'
    else:
        return 'x'

def get_dis3(cur, sho, lok, prev):
    if get_distance(cur, sho) < get_distance(prev, sho):
        return 'II'
    elif get_distance(cur, sho) > get_distance(prev, sho):
        return 'I'
    else:
        return 'x'

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
    else:
        print('ready')

for i in range(len(marshrutes)):
    strt = marshrutes[i][0][0]
    for j in range(len(marshrutes[i])):
        marshrutes[i][j][0] -= strt

counter=0
errors = []
m1 = []
m2 = []
timedelta = 10
pogrs = []
index = int(input('введите номер маршрута: '))
mrsh = marshrutes[index]
prom = [int(input('начало отсчета: ')), int(input('конец отсчета: '))]
prev = [mrsh[0][1], mrsh[0][2]]
for i in mrsh:
    if (i[0]==prom[0]) or (i[0] > prom[0] and prev[0] < prom[0]):
        print('start', i)
        plt.scatter(i[2], i[1], color='RED')
        plt.text(i[2], i[1], 'Начало', fontsize=18, color='BLACK')
        start = [i[1],i[2]]
    elif (i[0]==prom[1]) or (i[0] > prom[1] and prev[0] < prom[1]):
        print('end', i)
        plt.scatter(i[2], i[1], color='RED')
        plt.text(i[2], i[1], 'Конец', fontsize=18, color='BLACK')
        end = [i[1],i[2]]
    elif i[0] in range(prom[0], prom[1]+1):
        plt.scatter(i[2], i[1], 1, color='RED')
    else:
        plt.scatter(i[2], i[1], 1, color='BLUE')
    prev = i
print(direction(start, end))
lok=[37.7459800,55.8039100]
izm=[37.7431300,55.7895600]
sok=[37.7451300,55.7712800]
sho=[37.7460100,55.7586000]
plt.title(f'Движение по маршруту {direction(start, end)}')
plt.scatter(lok[0], lok[1], color='RED')
plt.scatter(izm[0], izm[1], color='RED')
plt.scatter(sok[0], sok[1], color='RED')
plt.scatter(sho[0], sho[1], color='RED')
plt.text(lok[0], lok[1], 'Локомотив', fontsize=18, color='BLACK')
plt.text(izm[0], izm[1], 'Измайлово', fontsize=18, color='BLACK')
plt.text(sok[0], sok[1], 'Соколиная Гора', fontsize=18, color='BLACK')
plt.text(sho[0], sho[1], 'Шоссе Энтузиастов', fontsize=18, color='BLACK')
plt.show()
