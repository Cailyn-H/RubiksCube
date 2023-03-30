from rubik.model.constants import *

class Cube:
    def __init__(self, encodedCube):
        self.cube = encodedCube
        
    def rotate(self, directions):
        result = {}
        #print("rotating")
        #########################################################
        #                                                       #
        #          Checking for Missing direction/Cube          #
        #                                                       #
        #########################################################
        #if direction is missing
        if directions is None:
            result['cube'] = self.cube
            result['status'] = 'error: invalid direction'
            return result
        
        #if cube is missing
        elif self.cube is None:
            result['cube'] = self.cube
            result['status'] = 'error: invalid cube'
            return result
        
        #########################################################
        #                                                       #
        #            Checking for Direction                     #
        #                                                       #
        #########################################################
        #this separates one string of multiple directions into multiple strings
        
        
        #validation for multiple direction is in direction list
        for i in list(directions):
            if i not in Legaldirection:
                result['cube'] = self.cube
                result['status'] = 'error: invalid direction'
                return result
        
        #validation for empty directions
        if len(directions) < 1:
            result['cube'] = self.cube
            result['status'] = 'error: invalid direction'
            return result
        
        #########################################################
        #                                                       #
        #            Checking for Cube                          #
        #                                                       #
        #########################################################
        #validation for cube length
        if (len(self.cube) != numofElements):
            result['cube'] = self.cube
            result['status'] = 'error: invalid cube'
            return result
        
        #if cube can have 6 unique characters and have a char that is not in a set
        #use the below elif
        #elif any(x not in cubeSet for x in set(encodedCube))
        elif (len(set(self.cube)) > numofFaces):
            result['cube'] = self.cube
            result['status'] = 'error: extraneous key detected'
            return result
        
        
        #########################################################
        #                                                       #
        #                    Cube Rotations                     #
        #                                                       #
        #########################################################
        #validation successed
        cubeList = list(self.cube)
        rotated = cubeList[:]
        
        
        for i in list(directions):
            
            if (i == 'F'):
                cubeList = list(rotated[:])
                '''rotating the front face'''
                rotated[FTR] = cubeList[FTL]
                rotated[FMR] = cubeList[FTM]
                rotated[FBR] = cubeList[FTR]
                rotated[FTM] = cubeList[FML]
                rotated[FMM] = cubeList[FMM]
                rotated[FBM] = cubeList[FMR]
                rotated[FTL] = cubeList[FBL]
                rotated[FML] = cubeList[FBM]
                rotated[FBL] = cubeList[FBR]
                '''sides connected to the front face'''
                rotated[DTR] = cubeList[RTL]
                rotated[DTM] = cubeList[RML]
                rotated[DTL] = cubeList[RBL]
                rotated[UBL] = cubeList[LBR]
                rotated[UBM] = cubeList[LMR]
                rotated[UBR] = cubeList[LTR]
                rotated[RTL] = cubeList[UBL]
                rotated[RML] = cubeList[UBM]
                rotated[RBL] = cubeList[UBR]
                rotated[LTR] = cubeList[DTL]
                rotated[LMR] = cubeList[DTM]
                rotated[LBR] = cubeList[DTR]
                self.cube = "".join(rotated)
                
            elif (i == 'f'):
                cubeList = list(rotated[:])
                '''rotating the front face'''
                rotated[FBL] = cubeList[FTL]
                rotated[FML] = cubeList[FTM]
                rotated[FTL] = cubeList[FTR]
                rotated[FBM] = cubeList[FML]
                rotated[FMM] = cubeList[FMM]
                rotated[FTM] = cubeList[FMR]
                rotated[FBR] = cubeList[FBL]
                rotated[FMR] = cubeList[FBM]
                rotated[FTR] = cubeList[FBR]
                '''sides connected to the front face'''
                rotated[UBL] = cubeList[RTL]
                rotated[UBM] = cubeList[RML]
                rotated[UBR] = cubeList[RBL]
                rotated[DTR] = cubeList[LBR]
                rotated[DTM] = cubeList[LMR]
                rotated[DTL] = cubeList[LTR]
                rotated[LBR] = cubeList[UBL]
                rotated[LMR] = cubeList[UBM]
                rotated[LTR] = cubeList[UBR]
                rotated[RBL] = cubeList[DTL]
                rotated[RML] = cubeList[DTM]
                rotated[RTL] = cubeList[DTR]              
                self.cube = "".join(rotated)
                
            elif (i == 'R'):
                cubeList = list(rotated[:])
                '''rotate right clockwise'''
                rotated[RTL] = cubeList[RBL]
                rotated[RTM] = cubeList[RML]
                rotated[RTR] = cubeList[RTL]
                rotated[RML] = cubeList[RBM]
                rotated[RMM] = cubeList[RMM]
                rotated[RMR] = cubeList[RTM]
                rotated[RBL] = cubeList[RBR]
                rotated[RBM] = cubeList[RMR]
                rotated[RBR] = cubeList[RTR]
                '''sides connected to the right face'''
                rotated[BTL] = cubeList[UBR]
                rotated[BML] = cubeList[UMR]
                rotated[BBL] = cubeList[UTR]
                rotated[UTR] = cubeList[FTR]
                rotated[UMR] = cubeList[FMR]
                rotated[UBR] = cubeList[FBR]
                rotated[DTR] = cubeList[BBL]
                rotated[DMR] = cubeList[BML]
                rotated[DBR] = cubeList[BTL]
                rotated[FTR] = cubeList[DTR]
                rotated[FMR] = cubeList[DMR]
                rotated[FBR] = cubeList[DBR]         
                self.cube = "".join(rotated)
                
            elif (i == 'r'):
                cubeList = list(rotated[:])
                '''rotate right counterclockwise'''
                rotated[RTL] = cubeList[RTR]
                rotated[RTM] = cubeList[RMR]
                rotated[RTR] = cubeList[RBR]
                rotated[RML] = cubeList[RTM]
                rotated[RMM] = cubeList[RMM]
                rotated[RMR] = cubeList[RBM]
                rotated[RBL] = cubeList[RTL]
                rotated[RBM] = cubeList[RML]
                rotated[RBR] = cubeList[RBL]
                '''sides connected to the right face'''
                rotated[FTR] = cubeList[UTR]
                rotated[FMR] = cubeList[UMR]
                rotated[FBR] = cubeList[UBR]
                rotated[BTL] = cubeList[DBR]
                rotated[BML] = cubeList[DMR]
                rotated[BBL] = cubeList[DTR]
                rotated[UTR] = cubeList[BBL]
                rotated[UMR] = cubeList[BML]
                rotated[UBR] = cubeList[BTL]
                rotated[DTR] = cubeList[FTR]
                rotated[DMR] = cubeList[FMR]
                rotated[DBR] = cubeList[FBR]          
                self.cube = "".join(rotated)
                
            elif (i == "B"):
                cubeList = list(rotated[:])
                '''rotate back clockwise'''
                rotated[BTL] = cubeList[BBL]
                rotated[BTM] = cubeList[BML]
                rotated[BTR] = cubeList[BTL]
                rotated[BML] = cubeList[BBM]
                rotated[BMM] = cubeList[BMM]
                rotated[BMR] = cubeList[BTM]
                rotated[BBL] = cubeList[BBR]
                rotated[BBM] = cubeList[BMR]
                rotated[BBR] = cubeList[BTR]
                '''sides connected to the back face'''
                rotated[DBL] = cubeList[LTL]
                rotated[DBM] = cubeList[LML]
                rotated[DBR] = cubeList[LBL]
                rotated[UTL] = cubeList[RTR]
                rotated[UTM] = cubeList[RMR]
                rotated[UTR] = cubeList[RBR]
                rotated[LTL] = cubeList[UTR]
                rotated[LML] = cubeList[UTM]
                rotated[LBL] = cubeList[UTL]
                rotated[RTR] = cubeList[DBR]
                rotated[RMR] = cubeList[DBM]
                rotated[RBR] = cubeList[DBL]          
                self.cube = "".join(rotated)
                
            elif (i == "b"):
                cubeList = list(rotated[:])
                '''rotate back counterclockwise'''
                rotated[BTL] = cubeList[BTR]
                rotated[BTM] = cubeList[BMR]
                rotated[BTR] = cubeList[BBR]
                rotated[BML] = cubeList[BTM]
                rotated[BMM] = cubeList[BMM]
                rotated[BMR] = cubeList[BBM]
                rotated[BBL] = cubeList[BTL]
                rotated[BBM] = cubeList[BML]
                rotated[BBR] = cubeList[BBL]
                '''sides connected to the back face'''
                rotated[DBL] = cubeList[RBR]
                rotated[DBM] = cubeList[RMR]
                rotated[DBR] = cubeList[RTR]
                rotated[UTL] = cubeList[LBL]
                rotated[UTM] = cubeList[LML]
                rotated[UTR] = cubeList[LTL]
                rotated[LTL] = cubeList[DBL]
                rotated[LML] = cubeList[DBM]
                rotated[LBL] = cubeList[DBR]
                rotated[RTR] = cubeList[UTL]
                rotated[RMR] = cubeList[UTM]
                rotated[RBR] = cubeList[UTR]          
                self.cube = "".join(rotated)
                
            elif (i == "L"):
                cubeList = list(rotated[:])
                '''rotate Left clockwise'''
                rotated[LTL] = cubeList[LBL]
                rotated[LTM] = cubeList[LML]
                rotated[LTR] = cubeList[LTL]
                rotated[LML] = cubeList[LBM]
                rotated[LMM] = cubeList[LMM]
                rotated[LMR] = cubeList[LTM]
                rotated[LBL] = cubeList[LBR]
                rotated[LBM] = cubeList[LMR]
                rotated[LBR] = cubeList[LTR]
                '''sides connected to the left face'''
                rotated[FTL] = cubeList[UTL]
                rotated[FML] = cubeList[UML]
                rotated[FBL] = cubeList[UBL]
                rotated[UTL] = cubeList[BBR]
                rotated[UML] = cubeList[BMR]
                rotated[UBL] = cubeList[BTR]
                rotated[BTR] = cubeList[DBL]
                rotated[BMR] = cubeList[DML]
                rotated[BBR] = cubeList[DTL]
                rotated[DBL] = cubeList[FBL]
                rotated[DML] = cubeList[FML]
                rotated[DTL] = cubeList[FTL]        
                self.cube = "".join(rotated)
                
            elif (i == "l"):
                cubeList = list(rotated[:])
                '''rotate Left counterclockwise'''
                rotated[LTL] = cubeList[LTR]
                rotated[LTM] = cubeList[LMR]
                rotated[LTR] = cubeList[LBR]
                rotated[LML] = cubeList[LTM]
                rotated[LMM] = cubeList[LMM]
                rotated[LMR] = cubeList[LBM]
                rotated[LBL] = cubeList[LTL]
                rotated[LBM] = cubeList[LML]
                rotated[LBR] = cubeList[LBL]
                '''sides connected to the left face'''
                rotated[FTL] = cubeList[DTL]
                rotated[FML] = cubeList[DML]
                rotated[FBL] = cubeList[DBL]
                rotated[UTL] = cubeList[FTL]
                rotated[UML] = cubeList[FML]
                rotated[UBL] = cubeList[FBL]
                rotated[BTR] = cubeList[UBL]
                rotated[BMR] = cubeList[UML]
                rotated[BBR] = cubeList[UTL]
                rotated[DBL] = cubeList[BTR]
                rotated[DML] = cubeList[BMR]
                rotated[DTL] = cubeList[BBR]          
                self.cube = "".join(rotated)
                
            elif (i == 'U'):
                cubeList = list(rotated[:])
                '''rotate Up clockwise'''
                rotated[UTL] = cubeList[UBL]
                rotated[UTM] = cubeList[UML]
                rotated[UTR] = cubeList[UTL]
                rotated[UML] = cubeList[UBM]
                rotated[UMM] = cubeList[UMM]
                rotated[UMR] = cubeList[UTM]
                rotated[UBL] = cubeList[UBR]
                rotated[UBM] = cubeList[UMR]
                rotated[UBR] = cubeList[UTR]
                '''sides connected to the up face'''
                rotated[LTL] = cubeList[FTL]
                rotated[LTM] = cubeList[FTM]
                rotated[LTR] = cubeList[FTR]
                rotated[BTR] = cubeList[LTR]
                rotated[BTM] = cubeList[LTM]
                rotated[BTL] = cubeList[LTL]
                rotated[RTL] = cubeList[BTL]
                rotated[RTM] = cubeList[BTM]
                rotated[RTR] = cubeList[BTR]
                rotated[FTL] = cubeList[RTL]
                rotated[FTM] = cubeList[RTM]
                rotated[FTR] = cubeList[RTR]
                self.cube = "".join(rotated)   
              
            elif (i == 'u'):
                cubeList = list(rotated[:])
                '''rotate Up counterclockwise'''
                rotated[UTL] = cubeList[UTR]
                rotated[UTM] = cubeList[UMR]
                rotated[UTR] = cubeList[UBR]
                rotated[UML] = cubeList[UTM]
                rotated[UMM] = cubeList[UMM]
                rotated[UMR] = cubeList[UBM]
                rotated[UBL] = cubeList[UTL]
                rotated[UBM] = cubeList[UML]
                rotated[UBR] = cubeList[UBL]
                '''sides connected to the up face'''
                rotated[LTL] = cubeList[BTL]
                rotated[LTM] = cubeList[BTM]
                rotated[LTR] = cubeList[BTR]
                rotated[BTR] = cubeList[RTR]
                rotated[BTM] = cubeList[RTM]
                rotated[BTL] = cubeList[RTL]
                rotated[RTL] = cubeList[FTL]
                rotated[RTM] = cubeList[FTM]
                rotated[RTR] = cubeList[FTR]
                rotated[FTL] = cubeList[LTL]
                rotated[FTM] = cubeList[LTM]
                rotated[FTR] = cubeList[LTR]
                self.cube = "".join(rotated)
                
        
        self.cube = "".join(rotated)
        result['cube'] = rotated
        result['status'] = 'ok'
    
        return result  
        
    
    def get(self):
        
        return self.cube
            
        