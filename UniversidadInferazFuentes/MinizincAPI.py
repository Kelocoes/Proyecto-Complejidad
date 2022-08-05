import minizinc as min
import pymzn
import time

def linkZinc(n, m, ciudades):
    dznFile={}
    dznFile['n']=n
    dznFile['m']=m
    dznFile['ciudades']= ciudades
    
    print(n,m,ciudades)
    #print(result["posX"])
    #print(result["posY"])
    pymzn.dict2dzn(dznFile, fout="../Datos.dzn")
    ubicacion = min.Model("../Universidad.mzn")
    ubicacion.add_file("../Datos.dzn")
    gecode = min.Solver.lookup("gecode")
    ## creamos instancia del problema
    instance = min.Instance(gecode, ubicacion)

    time0 = time.time()
    result = instance.solve()

    
    return result['posX'], result['posY'], time.time() - time0
