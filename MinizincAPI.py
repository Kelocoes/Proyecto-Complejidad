import minizinc as min
import pymzn

def linkZinc(n, m, ciudades):
    dznFile={}
    dznFile['n']=n
    dznFile['m']=m
    dznFile['ciudades']= ciudades
    
    print(n,m,ciudades)
    #print(result["posX"])
    #print(result["posY"])
    pymzn.dict2dzn(dznFile, fout='./Datos.dzn')
    ubicacion = min.Model('./Problema universidad Gen Kevin.mzn')
    ubicacion.add_file('./Datos.dzn')
    gecode = min.Solver.lookup("gecode")
    ## creamos instancia del problema
    instance = min.Instance(gecode, ubicacion)

    result = instance.solve()
    return result['posX'], result['posY']
