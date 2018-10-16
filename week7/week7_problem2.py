def calcTriangle(b, h):
    area = float(b*h*0.5)

    return area

bottom = int(input('Bottom in cm: '))
height = int(input('Height in cm: '))

S = calcTriangle(bottom, height)

print('Area in cm^2: ', S)
