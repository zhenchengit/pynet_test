#! python

def xyz(x, y, z):
 x=int(x)
 y=int(y)
 z=20
 return float(x+y+z)

print xyz(2,3,4)
print xyz(x=2, y=3, z=0)
print xyz(x='2', y='3', z='0')
print xyz(x=[2], y=[3], z=[0])
