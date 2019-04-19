X = [69, 63, 66, 64, 67, 64, 70, 66, 68, 67, 65, 71]
Y = [70, 65, 68, 65, 69, 66, 68, 65, 71, 67, 64, 72]
sumX = sum(X)
sumXX = sum(map(lambda x: x**2, X))
sumY = sum(Y)
sumXY = sum(map(lambda x: x[0]*x[1], zip(X, Y)))
print('sum(X)  =', sumX)
print('sum(X^2)=', sumXX)
print('sum(Y)  =', sumY)
print('sum(XY) =', sumXY)

meanX = sum(X)/len(X)
meanY = sum(Y)/len(Y)

# sum Y  = c * n    + m * sum X
# sum XY = c * sumX + m * sum XX
# n = len(X)
# c = (sumY * sumXX - sumXY * sumX ) / (n * sumXX - sumX**2)
# print('m=', c)

numer = sum(map(lambda xy: (xy[0]-meanX)*(xy[1]-meanY), zip(X, Y)))
denom = sum(map(lambda  x: (x-meanX)**2, X))
b1 = numer / denom

b0 = meanY - b1 * meanX
print('B1=', b1)
print('B0=', b0)

print('Line is:' f'Y = {b1}X + {b0}')

'''
OUTPUT:
sum(X)  = 800
sum(X^2)= 53402
sum(Y)  = 810
sum(XY) = 54059
B1= 0.859223300970874
B0= 10.218446601941729
Line is:Y = 0.859223300970874X + 10.218446601941729
'''