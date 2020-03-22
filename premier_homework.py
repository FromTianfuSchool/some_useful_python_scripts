import random

# fmt = '{:>2} {sign} {:^2} =  {:<8}'
fmt = '{:>2} {sign} {:^2} =     '
def plus_equation(plus):
    if not isinstance(plus, int):
        raise ValueError('suppose int type')
    equal = []
    while (len(equal) < plus):
        x, y = 0, 0
        while (x + y <= 10):
            x = random.randint(0, WITHIN/2)
            y = random.randint(0, WITHIN/2)
        tostr = fmt.format(x, y, x + y, sign='+')
        if tostr in equal:
            continue
        equal.append(tostr)
    return equal


def subs_equation(sub):
    if not isinstance(sub, int):
        raise ValueError('suppose int type')
    equal = []
    while (len(equal) < sub):
        x, y = 0, 0
        while ( max(x, y) - min(x, y) >= 10) or x == 0 or y==0:
            x = random.randint(11, 19)
            y = random.randint(6, 9)
        tostr = fmt.format(max(x, y), min(x, y), max(x, y) - min(x, y), sign='-')
        if tostr in equal:
            continue
        equal.append(tostr)
    return equal


def save(filename, file):
    i = 0
    with open(filename, 'w') as fp:
        for pair in file:
            fp.write(pair)
            i += 1
            if i % 3 == 0:
                fp.write('\n')

def generate_equation(total, plus_equa_num):
    equal = []
    sub = total - plus_equa_num
    equal.extend(plus_equation(plus_equa_num))
    equal.extend(subs_equation(sub))
    return equal


if __name__ == '__main__':
    # 总算数等式
    TOTAL = 30
    # 加法算式数目
    PLUS = 15
    # 页码数
    PAGE = 11
    # 多少以内加减法
    WITHIN = 20
    import os
    if not os.path.exists('homework'):
        os.mkdir('homework')
    os.chdir('homework')

    for i in range(PAGE):
        filename = ''.join(['homework', str(i), '.txt'])
        equation = generate_equation(total=TOTAL, plus_equa_num=PLUS)
        random.shuffle(equation)
        save(filename, equation)
        print('保存成功{}'.format(filename))