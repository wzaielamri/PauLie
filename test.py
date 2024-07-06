from bitarray import bitarray
from time import perf_counter
import psutil
from common.generator import *
from common.algebras import *





# Getting % usage of virtual_memory ( 3rd field)
#    print('RAM memory % used:', psutil.virtual_memory()[2])
# Getting usage of virtual_memory in GB ( 4th field)
#    print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)

start_time = perf_counter()
subgroups = getSubGroupsOfAlgebraByName(getAlgebras(), 'a4')
print(f"number nodes {subgroups.getCountNodes()}")
print(f"get subgroups {subgroups.getSubgroups()}")
print(f"get quadratic intersec I, Z {subgroups.getQuadraticForm({'I', 'Z'})}")
print(f"get EZ {subgroups.getEZ()}")

print(f"Test get EZ second moment to all algebra n = 2")

def calcAllAlgebra():
    algebras = getAlgebras()
    for algebra in algebras.keys():
        sym = getSubGroupsOfAlgebraByName(algebras, algebra)
        print(f"{algebra} EZ = {sym.getEZ() :0.3f}")
        print(f"subset {sym.getSubgroups()}")
        print(f"quadratic I, Z {sym.getQuadraticForm({'I', 'Z'})}")
        
calcAllAlgebra()
end_time = perf_counter()
print(f'time excexution {end_time - start_time: 0.2f} sec.')
