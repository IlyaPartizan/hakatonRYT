import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import math as mt



mpl.rcParams['font.family'] = 'fantasy'
def mnkGP(x,y): # функция которую можно использзовать в програме
              n=len(x) # количество элементов в списках
              s=sum(y) # сумма значений y
              s1=sum([1/x[i] for i in  range(0,n)]) #  сумма 1/x
              s2=sum([(1/x[i])**2 for i in  range(0,n)]) #  сумма (1/x)**2
              s3=sum([y[i]/x[i]  for i in range(0,n)])  # сумма y/x                   
              a= round((s*s2-s1*s3)/(n*s2-s1**2),3) # коэфициент а с тремя дробными цифрами
              b=round((n*s3-s1*s)/(n*s2-s1**2),3)# коэфициент b с тремя дробными цифрами
              s4=[a+b/x[i] for i in range(0,n)] # список значений гиперболической функции              
              so=round(sum([abs(y[i] -s4[i]) for i in range(0,n)])/(n*sum(y))*100,3)   # средняя ошибка аппроксимации
              plt.title('Аппроксимация гиперболой Y='+str(a)+'+'+str(b)+'/x\n Средняя ошибка--'+str(so)+'%',size=14)
              plt.xlabel('Координата X', size=14)
              plt.ylabel('Координата Y', size=14)
              plt.plot(x, y, color='r', linestyle=' ', marker='o', label='Data(x,y)')
              plt.plot(x, s4, color='g', linewidth=2, label='Data(x,f(x)=a+b/x')
              plt.legend(loc='best')
              plt.grid(True)
              plt.show()



file = open('2022_12_01_mcc.csv')
info = file.read().split('\n')
file.close()

for i in range(len(info)):
    info[i] = info[i].split(',')

for i in range(250834, len(info)):
    info.pop(i)

info.sort(key = lambda x: x[1])

for i in range(len(info)):
    info[i][1] = float(info[i][1])
    info[i][2] = float(info[i][2])

x = []
y = []
number = len(info)

for i in range(number):
    
    x.append(info[i][2])
    y.append(info[i][1])

mnkGP(x,y)