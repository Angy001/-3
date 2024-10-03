a = float(input('Длина 1 стороны: ')) 
b = float(input('Длина 2 стороны: ')) 
c = float(input('Длина 3 стороны: ')) 
def areaTriangle(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

print('Area = {:.2f}'.format(areaTriangle(a, b, c)))