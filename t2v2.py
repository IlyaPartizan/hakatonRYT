from datetime import datetime
import matplotlib.pyplot as plt

def stan(inp):
    lok=[55.8039100,37.7459800]
    izm=[55.7895600,37.7431300]
    sok=[55.7712800,37.7451300]
    sho=[55.7586000,37.7460100]
    delta1 = ((inp[0]-lok[0])**2+(inp[1]-lok[1])**2)**0.5
    delta2 = ((inp[0]-izm[0])**2+(inp[1]-izm[1])**2)**0.5
    delta3 = ((inp[0]-sok[0])**2+(inp[1]-sok[1])**2)**0.5
    delta4 = ((inp[0]-sho[0])**2+(inp[1]-sho[1])**2)**0.5
    delta = [delta1, delta2, delta3, delta4]
    if min(delta) == delta1:
        return 'lok'
    if min(delta) == delta2:
        return 'x'
    if min(delta) == delta3:
        return 'x'
    if min(delta) == delta4:
        return 'sho'

def direction(fr, to):
    path = ['lok', 'izm', 'sok', 'sho']
    if fr == 'x' or to == 'x':
        return 'x'
    if path.index(fr) < path.index(to):
        return 'I'
    elif path.index(fr) > path.index(to):
        return 'II'
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
    if direction(stan([a[1], a[2]]), stan([b[1], b[2]])) == 'x':
        counter+=1
    if direction(stan([a[1], a[2]]), stan([b[1], b[2]])) == 'I':
        m1.append(marshrutes[i])
    if direction(stan([a[1], a[2]]), stan([b[1], b[2]])) == 'II':
        m2.append(marshrutes[i])

ys = {}

for i in m1:
    for j in i:
        a = round(j[1], 4)
        if a in ys.keys():
            ys[a].append((j[2], j[1], j[3]))
        else:
            ys[a] = [(j[2], j[1], j[3])]
r1 = []
for i in ys.keys():
    print(i)
    s1 = 0
    s2 = 0
    c = 0
    for j in ys[i]:
        s1 += j[0]*j[2]
        s2 += j[1]*j[2]
        c += j[2]
    r1.append((s1/c, s2/c))

for i in r1:
    plt.scatter(i[0], i[1], 1, color='BLUE')

lok=[37.7459800,55.8039100]
izm=[37.7431300,55.7895600]
sok=[37.7451300,55.7712800]
sho=[37.7460100,55.7586000]
plt.title('Маршрут I(Локомотив-Шоссе Энтузиастов)')
plt.scatter(lok[0], lok[1], color='RED')
plt.scatter(izm[0], izm[1], color='RED')
plt.scatter(sok[0], sok[1], color='RED')
plt.scatter(sho[0], sho[1], color='RED')
plt.text(lok[0], lok[1], 'Локомотив', fontsize=12, color='BLACK')
plt.text(izm[0], izm[1], 'Измайлово', fontsize=12, color='BLACK')
plt.text(sok[0], sok[1], 'Соколиная Гора', fontsize=12, color='BLACK')
plt.text(sho[0], sho[1], 'Шоссе Энтузиастов', fontsize=12, color='BLACK')
plt.show()

ys = {}

for i in m2:
    for j in i:
        a = round(j[1], 4)
        if a in ys.keys():
            ys[a].append((j[2], j[1], j[3]))
        else:
            ys[a] = [(j[2], j[1], j[3])]
r1 = []
for i in ys.keys():
    print(i)
    s1 = 0
    s2 = 0
    c = 0
    for j in ys[i]:
        s1 += j[0]*j[2]
        s2 += j[1]*j[2]
        c += j[2]
    r1.append((s1/c, s2/c))

for i in r1:
    plt.scatter(i[0], i[1], 1, color='BLUE')

lok=[37.7459800,55.8039100]
izm=[37.7431300,55.7895600]
sok=[37.7451300,55.7712800]
sho=[37.7460100,55.7586000]
plt.title('Маршрут II(Шоссе Энтузиастов-Локомотив)')
plt.scatter(lok[0], lok[1], color='RED')
plt.scatter(izm[0], izm[1], color='RED')
plt.scatter(sok[0], sok[1], color='RED')
plt.scatter(sho[0], sho[1], color='RED')
plt.text(lok[0], lok[1], 'Локомотив', fontsize=12, color='BLACK')
plt.text(izm[0], izm[1], 'Измайлово', fontsize=12, color='BLACK')
plt.text(sok[0], sok[1], 'Соколиная Гора', fontsize=12, color='BLACK')
plt.text(sho[0], sho[1], 'Шоссе Энтузиастов', fontsize=12, color='BLACK')
plt.show()
