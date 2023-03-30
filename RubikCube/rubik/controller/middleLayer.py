from rubik.model.constants import *
from rubik.model.cube import Cube

def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    ''' 
     
    rotations = []
    cubeList = list(theCube.get())
    #########################################################
    #            Declare Center of Each Face                #
    #########################################################
    DownFace = cubeList[DMM] #49
    FrontFace = cubeList[FMM] #4
    RightFace = cubeList[RMM] #13
    BackFace = cubeList[BMM] #22
    LeftFace = cubeList[LMM] #31
    UpFace = cubeList[UMM] #40 
    
    #########################################################
    #                                                       #
    #           Checking for Perfect Middle Layer           #
    #             Before Starting a Rotation                #
    #########################################################
    if (cubeList[FML]==FrontFace and cubeList[FMR]==FrontFace and cubeList[RML]==RightFace and cubeList[RMR]==RightFace and cubeList[BML]==BackFace and cubeList[BMR]==BackFace and cubeList[LML]==LeftFace and cubeList[LMR]==LeftFace):
        return "".join(rotations)
    
    #########################################################
    #                                                       #
    #           Start Rotating for Middle Layer             #
    #                                                       #
    #########################################################    
    while (cubeList[FML]!=FrontFace or cubeList[FMR]!=FrontFace or cubeList[RML]!=RightFace or cubeList[RMR]!=RightFace or cubeList[BML]!=BackFace or cubeList[BMR]!=BackFace or cubeList[LML]!=LeftFace or cubeList[LMR]!=LeftFace):
        #########################################################
        #                                                       #
        #             Start Rotating for Front Face             #
        #                                                       #
        ######################################################### 
        if cubeList[RML] == FrontFace and cubeList[FMR] == RightFace:
            theCube.rotate('URurufUF')
            rotations.append('URurufUF')
            cubeList = list(theCube.get())
            theCube.rotate('UUURurufUF')
            rotations.append('UUURurufUF')
            cubeList = list(theCube.get())
            
        if cubeList[FTM] == RightFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
            
            if cubeList[UMR] == BackFace:
                theCube.rotate('UBuburUR')
                rotations.append('UBuburUR')
                cubeList = list(theCube.get())
                
            elif cubeList[UMR] == FrontFace:
                theCube.rotate('ufUFURur')
                rotations.append('ufUFURur')
                cubeList = list(theCube.get())
                
        elif cubeList[FTM] == BackFace:
            theCube.rotate('uu')
            rotations.append('uu')
            cubeList = list(theCube.get())
            if cubeList[UTM] == LeftFace:
                theCube.rotate('ULulubUB')
                rotations.append('ULulubUB')
                cubeList = list(theCube.get())
                
            elif cubeList[UTM] == RightFace:
                theCube.rotate('urURUBub')
                rotations.append('urURUBub')
                cubeList = list(theCube.get())
                
        elif cubeList[FTM] == LeftFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
            
            if cubeList[UML] == FrontFace:
                theCube.rotate('UFufulUL')
                rotations.append('UFufulUL')
                cubeList = list(theCube.get())
                
            elif cubeList[UML] == BackFace:
                theCube.rotate('ubUBULul')
                rotations.append('ubUBULul')
                cubeList = list(theCube.get())
                
        else:
            if cubeList[UBM] == RightFace:
                theCube.rotate('URurufUF')
                rotations.append('URurufUF')
                cubeList = list(theCube.get())
                
            elif cubeList[UBM] == LeftFace:
                theCube.rotate('ulULUFuf')
                rotations.append('ulULUFuf')
                cubeList = list(theCube.get())
        #########################################################
        #                                                       #
        #             Start Rotating for Right Face             #
        #                                                       #
        #########################################################    
        if cubeList[BML] == RightFace or cubeList[RMR] == BackFace:
            theCube.rotate('UBuburUR')
            rotations.append('UBuburUR')
            cubeList = list(theCube.get())
            theCube.rotate('UUUBuburUR')
            rotations.append('UUBuburUR')
            cubeList = list(theCube.get())
        
        if cubeList[RTM] == FrontFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
            
            if cubeList[UBM] == RightFace:
                theCube.rotate('URurufUF')
                rotations.append('URurufUF')
                cubeList = list(theCube.get())
                
            elif cubeList[UBM] == LeftFace:
                theCube.rotate('ulULUFuf')
                rotations.append('ulULUFuf')
                cubeList = list(theCube.get())
                
        elif cubeList[RTM] == LeftFace:
            theCube.rotate('UU')
            rotations.append('UU')
            cubeList = list(theCube.get())
            if cubeList[UML] == FrontFace:
                theCube.rotate('UFufulUL')
                rotations.append('UFufulUL')
                cubeList = list(theCube.get())
                
            elif cubeList[UML] == BackFace:
                theCube.rotate('ubUBULul')
                rotations.append('ubUBULul')
                cubeList = list(theCube.get())
                
        elif cubeList[RTM] == BackFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
            
            if cubeList[UTM] == RightFace:
                theCube.rotate('urURUBub')
                rotations.append('urURUBub')
                cubeList = list(theCube.get())
            
            elif cubeList[UTM] == LeftFace:
                theCube.rotate('ULulubUB')
                rotations.append('ULulubUB')
                cubeList = list(theCube.get())
                
        else:
            if cubeList[UMR] == BackFace:
                theCube.rotate('UBuburUR')
                rotations.append('UBuburUR')
                cubeList = list(theCube.get())
                
            elif cubeList[UMR] == FrontFace:
                theCube.rotate('ufUFURur')
                rotations.append('ufUFURur')
                cubeList = list(theCube.get())
                
        #########################################################
        #                                                       #
        #             Start Rotating for Back Face              #
        #                                                       #
        #########################################################  
        if cubeList[LML] == BackFace or cubeList[BMR] == LeftFace:
            theCube.rotate('ULulubUB')
            rotations.append('ULulubUB')
            cubeList = list(theCube.get())
            theCube.rotate('UUULulubUB')
            rotations.append('UUULulubUB')
            cubeList = list(theCube.get())
        
        if cubeList[BTM] == LeftFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
            
            if cubeList[UML] == FrontFace:
                theCube.rotate('UFufulUL')
                rotations.append('UFufulUL')
                cubeList = list(theCube.get())
                
            elif cubeList[UML] == BackFace:
                theCube.rotate('ubUBULul')
                rotations.append('ubUBULul')
                cubeList = list(theCube.get())
                
        elif cubeList[BTM] == FrontFace:
            theCube.rotate('uu')
            rotations.append('uu')
            cubeList = list(theCube.get())
            if cubeList[UBM] == RightFace:
                theCube.rotate('URurufUF')
                rotations.append('URurufUF')
                cubeList = list(theCube.get())
                
            elif cubeList[UBM] == LeftFace:
                theCube.rotate('ulULUFuf')
                rotations.append('ulULUFuf')
                cubeList = list(theCube.get())
                
        elif cubeList[BTM] == RightFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
            
            if cubeList[UMR] == BackFace:
                theCube.rotate('UBuburUR')
                rotations.append('UBuburUR')
                cubeList = list(theCube.get())
                
            elif cubeList[UMR] == FrontFace:
                theCube.rotate('ufUFURur')
                rotations.append('ufUFURur')
                cubeList = list(theCube.get())
                
        else:
            if cubeList[UTM] == LeftFace:
                theCube.rotate('ULulubUB')
                rotations.append('ULulubUB')
                cubeList = list(theCube.get())
                
            elif cubeList[UTM] == RightFace:
                theCube.rotate('urURUBub')
                rotations.append('urURUBub')
                cubeList = list(theCube.get())
                
        #########################################################
        #                                                       #
        #             Start Rotating for Left Face              #
        #                                                       #
        #########################################################  
        if cubeList[FML] == LeftFace or cubeList[LMR] == FrontFace:
            theCube.rotate('UFufulUL')
            rotations.append('UFufulUL')
            cubeList = list(theCube.get())
            theCube.rotate('UUUFufulUL')
            rotations.append('UUUFufulUL')
            cubeList = list(theCube.get())
            
        if cubeList[LTM] == FrontFace:
            theCube.rotate('u')
            rotations.append('u')
            cubeList = list(theCube.get())
            
            if cubeList[UBM] == LeftFace:
                theCube.rotate('ulULUFuf')
                rotations.append('ulULUFuf')
                cubeList = list(theCube.get())
                
            elif cubeList[UBM] == RightFace:
                theCube.rotate('URurufUF')
                rotations.append('URurufUF')
                cubeList = list(theCube.get())
                
        elif cubeList[LTM] == RightFace:
            theCube.rotate('uu')
            rotations.append('uu')
            cubeList = list(theCube.get())
            
            if cubeList[UMR] == FrontFace:
                theCube.rotate('ufUFURur')
                rotations.append('ufUFURur')
                cubeList = list(theCube.get())
                
            elif cubeList[UMR] == BackFace:
                theCube.rotate('UBuburUR')
                rotations.append('UBuburUR')
                cubeList = list(theCube.get())
                
        elif cubeList[LTM] == BackFace:
            theCube.rotate('U')
            rotations.append('U')
            cubeList = list(theCube.get())
            
            if cubeList[UTM] == RightFace:
                theCube.rotate('urURUBub')
                rotations.append('urURUBub')
                cubeList = list(theCube.get())
            elif cubeList[UTM] == LeftFace:
                theCube.rotate('ULulubUB')
                rotations.append('ULulubUB')
                cubeList = list(theCube.get())
                
        else:
            if cubeList[UML] == BackFace:
                theCube.rotate('ubUBULul')
                rotations.append('ubUBULul')
                cubeList = list(theCube.get())
                
            elif cubeList[UML] == FrontFace:
                theCube.rotate('UFufulUL')
                rotations.append('UFufulUL')
                cubeList = list(theCube.get())
                
            
            
    
    

    print("".join(rotations))
    return "".join(rotations)       
