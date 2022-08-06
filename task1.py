'''
Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.
Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.

например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55

то в итоге будет, 3*x^3 + 12*x^2+10*x+66
'''

def sum(a, b):
    res = list(map(lambda m, n: m+n, a, b))
    y = ''
    for i in range(len(res)):
        y = str(res[i])+'*x^'+str(i) + ' + ' + y
    y = y.replace('x^1 ', 'x ')
    y = y.replace('*x^0', '')
    y = y.replace(' 1*x', ' x')
    y = y.replace(' + -', ' - ')
    y = y[:-3]
    return y

def row(input):
    with open(input, 'r') as p:
        res = p.read().replace(' - ', ' + -').split(' + ')
    return res

def sort(data):
    N = []
    for i in range(len(data)):
        try:
            if int(data[i]):
                data[i] += '*x^0'
        except:
            pass
        N.append(list(data[i].split('x')))
        if N[i][0] == '' and N[i][1] != '':
            N[i][0] = '1*'
        if N[i][0] != '' and N[i][1] == '':
            N[i][1] = '^1'
        N[i][1] = int(N[i][1].replace('^', ''))
    return N

def item(data):
    for i in range(len(data)):
        max = data[0][1]
        if data[i][1] > max:
            max = data[i][1]
    item = [0]*max
    for i in range(max):
        try:
            item.insert(data[i][1], int(data[i][0].replace('*', '')))
            item.pop(data[i][1]+1)
        except:
            pass
    return item


a = 'test1.txt'
b = 'test2.txt'

print(sum(item(sort(row(a))), item(sort(row(b)))))