from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    directions = parms.get('dir')
    encodedCube = parms.get('cube')
    #dirList = ['F','f','U','u','R','r','B','b','L','l']
    #cubeSet = set(encodedCube)
    
    #if (len(encodedCube) != 54):
        #result['cube'] = encodedCube
        #result['status'] = 'error: invalid cube'
        #return result
    
    #elif directions not in dirList:
        #result['cube'] = encodedCube
        #result['status'] = 'error: invalid direction'
        #return result
    
    #if cube can have 6 unique characters and have a char that is not in a set
    #use the below elif
    #elif any(x not in cubeSet for x in set(encodedCube)):
    
    #elif (len(cubeSet) > 6):
        #result['cube'] = encodedCube
        #result['status'] = 'error: extraneous key detected'
        #return result
    
    theCube = Cube(encodedCube)
    result = theCube.rotate(directions)   
         
                      
    return result

