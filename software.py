# numerická integrace
# numerická derivace
# řešení diferenciálních rovnic
# interpolace a aproximace
# řešení soustav nelineárních rovnic
# generátory náhodných čísel
# metoda Monte Carlo

# lineární algebra
import numpy as np
import scipy

matice = np.array([
    [1,2,3],
    [3,4,5],
    [4,5,6]
])

print(matice*3) 


matice2 = np.array([
    [1,2,3],
    [3,4,5],
    [4,5,6]
])

matice += matice2
print(matice)

nradku = 3
nsloupcu = 4
"""
I = np.ones(nradku,nsloupcu)
print(I)
"""
# np.zeros (matice obsahuje samé nuly)
# np.eye(nradku) - čtvercová matice

A = np.full((nradku, nsloupcu), fill_value=5,dtype="float") 

# hledání inverzní matice
a = np.array([
    [1,2,-1],
    [2,0,1],
    [1,-2,1]
])

x = np.linalg.inv(a)

e = np.matmul(a,x)

if a.shape[0] > np.linalg.matrix_rank(a):
    print("Nelze nalézt inverzi")

a.transpose()

# determinant matice
np.linalg.det(a)

# Cramerovo pravidlo
a = np.array([
    [3,2,1],
    [2,3,1],
    [2,1,3]
])

b = np.array =([5,1,11])
mask = np.broadcast_to(np.diag([1,1,1]),[3,3,3]).swapaxes(0,1)

ai = np.where(mask,np.repeat(b,3).reshape(3,3), a) # 3 = počet sloupců
x = np.linalg.det(ai)/np.linalg.det(a)
print(x)

# Gaussova eliminační metoda
g = np.linalg.solve(a,b)

# Jakobiho metoda
def jacobi(a,b, x0=np.ones(len(a))):
