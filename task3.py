import matplotlib.pyplot as plt

def get_distance(p1, p2):
    return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5

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

dirc = int(input('dir: '))
cords = [float(input('lat: ')), float(input('lon: '))]

if dirc == 1:
    lok=[37.7459800,55.8039100]
    izm=[37.7431300,55.7895600]
    sok=[37.7451300,55.7712800]
    sho=[37.7460100,55.7586000]
    md = 1000
    mp = 0
    for i in r1:
        if get_distance(cords, i) < md:
            md = get_distance(cords, i)
            mp = i
        plt.scatter(i[0], i[1], 1, color='BLUE')
    plt.scatter(cords[0], cords[1], color='RED')
    plt.text(cords[0], cords[1], 'Xпол', fontsize=12, color='BLACK')
    plt.scatter(mp[0], mp[1], color='RED')
    plt.text(mp[0], mp[1], 'Xпр', fontsize=12, color='BLACK')
    plt.scatter(lok[0], lok[1], color='RED')
    plt.scatter(izm[0], izm[1], color='RED')
    plt.scatter(sok[0], sok[1], color='RED')
    plt.scatter(sho[0], sho[1], color='RED')
    plt.text(lok[0], lok[1], 'Локомотив', fontsize=12, color='BLACK')
    plt.text(izm[0], izm[1], 'Измайлово', fontsize=12, color='BLACK')
    plt.text(sok[0], sok[1], 'Соколиная Гора', fontsize=12, color='BLACK')
    plt.text(sho[0], sho[1], 'Шоссе Энтузиастов', fontsize=12, color='BLACK')
    plt.xlim([37.735, 37.76])
    plt.ylim([55.75, 55.81])
    plt.show()
elif dirc == 2:
    lok=[37.7459800,55.8039100]
    izm=[37.7431300,55.7895600]
    sok=[37.7451300,55.7712800]
    sho=[37.7460100,55.7586000]
    md = 1000
    mp = 0
    for i in r2:
        if get_distance(cords, i) < md:
            md = get_distance(cords, i)
            mp = i
        plt.scatter(i[0], i[1], 1, color='BLUE')
    plt.scatter(cords[0], cords[1], color='RED')
    plt.text(cords[0], cords[1], 'Xпол', fontsize=12, color='BLACK')
    plt.scatter(mp[0], mp[1], color='RED')
    plt.text(mp[0], mp[1], 'Xпр', fontsize=12, color='BLACK')
    plt.scatter(lok[0], lok[1], color='RED')
    plt.scatter(izm[0], izm[1], color='RED')
    plt.scatter(sok[0], sok[1], color='RED')
    plt.scatter(sho[0], sho[1], color='RED')
    plt.text(lok[0], lok[1], 'Локомотив', fontsize=12, color='BLACK')
    plt.text(izm[0], izm[1], 'Измайлово', fontsize=12, color='BLACK')
    plt.text(sok[0], sok[1], 'Соколиная Гора', fontsize=12, color='BLACK')
    plt.text(sho[0], sho[1], 'Шоссе Энтузиастов', fontsize=12, color='BLACK')
    plt.xlim([37.74, 37.75])
    plt.ylim([55.75, 55.81])
    plt.show()
else:
    print('wrong direction')


