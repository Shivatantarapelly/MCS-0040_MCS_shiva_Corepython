dave = [180]
owen = [50]
amr = [150]
laura = [360]
vic = [0]

dave.append(dave[-1] - 180)
laura.append(laura[-1] + 180 / 3)
owen.append(owen[-1] + 180 / 3)
vic.append(vic[-1] + 180 / 3)

owen.append(owen[-1] - 50)
dave.append(dave[-1] + 50)

amr.append(amr[-1] - 150)
vic.append(vic[-1] + 150 / 2)
owen.append(owen[-1] + 150 / 2)

laura.append(laura[-1] - 360)
amr.append(amr[-1] + 360 / 2)
vic.append(vic[-1] + 360 / 2)

print(f"Dave {dave[-1]}, Laura {int(laura[-1])}, Owen {int(owen[-1])}, Vic {int(vic[-1])}, Amr {int(amr[-1])}")

# -------------------------------

data = {'dave': 180, 'owen': 50, 'amr': 150, 'laura': 360, 'vic': 0}
dave, owen, amr, laura, vic = data['dave'], data['owen'], data['amr'], data['laura'], data['vic']
num = 0

for i, j in data.items():
    if i == 'dave':
        num1 = j
        for k, l in data.items():
            if k == 'laura' or k == 'owen' or k == 'vic':
                num = dave / 3
                data[k] = l + num
                data[i] = num1 - num
                num1 -= num

    elif i == 'owen':
        num1 = j
        for k, l in data.items():
            if k == 'dave':
                num = owen
                data[k] = l + num
                data[i] = num1 - num
                num1 -= num
    elif i == 'amr':
        num1 = j
        for k, l in data.items():
            if k == 'vic' or k == 'owen':
                num = amr / 2
                data[k] = l + num
                data[i] = num1 - num
                num1 -= num
    elif i == 'laura':
        num1 = j
        for k, l in data.items():
            if k == 'vic' or k == 'amr':
                num = laura / 2
                data[k] = l + num
                data[i] = num1 - num
                num1 -= num
    else:
        pass
print(data)
