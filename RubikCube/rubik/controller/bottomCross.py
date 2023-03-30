from rubik.model.constants import *
from rubik.model.cube import Cube

def solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
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
    #              Checking for Perfect Cube                #
    #                                                       #
    #########################################################
    if (cubeList[DTM] == DownFace and cubeList[DML] == DownFace and cubeList[DMR] == DownFace and cubeList[DBM] == DownFace):
        return "".join(rotations)
    
    
    
    
    
    
    #########################################################
    #                                                       #
    #          Start Rotating for Down Face Cross           #
    #                                                       #
    #########################################################
    while (cubeList[DTM] != DownFace or cubeList[DML] != DownFace or cubeList[DMR] != DownFace or cubeList[DBM] != DownFace):
        #########################################################
        #                                                       #
        #        Checking for Daisy Pedal on Down Face          #
        #                                                       #
        #########################################################
        if cubeList[DTM] == DownFace:
            if cubeList[FBM] != FrontFace:
                theCube.rotate('FF')
                rotations.append('FF')
                cubeList = list(theCube.get())
                #rotate'FF'
                if cubeList[FTM] == RightFace:
                    theCube.rotate('urr')
                    rotations.append('urr')
                    cubeList = list(theCube.get())
                    #rotate'urr'
                elif cubeList[FTM] == LeftFace:
                    theCube.rotate('ULL')
                    rotations.append('ULL')
                    cubeList = list(theCube.get())
                    #rotate'ULL'
                else:
                    theCube.rotate('uuBB')
                    rotations.append('uuBB')
                    cubeList = list(theCube.get())
                    #rotate'uuBB'
        
        if cubeList[DML] == DownFace:
            if cubeList[LBM] != LeftFace:
                theCube.rotate('ll')
                rotations.append('ll')
                cubeList = list(theCube.get())
                #rotate'll'
                if cubeList[LTL] == FrontFace:
                    theCube.rotate('uFF')
                    rotations.append('uFF')
                    cubeList = list(theCube.get())
                    #rotate'uFF'
                elif cubeList[LTL] == RightFace:
                    theCube.rotate('uuRR')
                    rotations.append('uuRR')
                    cubeList = list(theCube.get())
                    #rotate'uuRR'
                else:
                    theCube.rotate('UBB')
                    rotations.append('UBB')
                    cubeList = list(theCube.get())
                    #rotate'UBB'
        
        if cubeList[DMR] == DownFace:
            if cubeList[RBM] != RightFace:
                theCube.rotate('RR')
                rotations.append('RR')
                cubeList = list(theCube.get())
                #rotate'RR'
                if cubeList[RTM] == FrontFace:
                    theCube.rotate('UFF')
                    rotations.append('UFF')
                    cubeList = list(theCube.get())
                    #rotate'UFF'
                elif cubeList[RTM] == LeftFace:
                    theCube.rotate('UULL')
                    rotations.append('UULL')
                    cubeList = list(theCube.get())
                    #rotate'UULL'
                else:
                    theCube.rotate('uBB')
                    rotations.append('uBB')
                    cubeList = list(theCube.get())
                    #rotate'uBB'
        
        if cubeList[DBM] == DownFace:
            if cubeList[BBM] != BackFace:
                theCube.rotate('BB')
                rotations.append('BB')
                cubeList = list(theCube.get())
                #rotate'BB'
                if cubeList[BTM] == RightFace:
                    theCube.rotate('URR')
                    rotations.append('URR')
                    cubeList = list(theCube.get())
                    #rotate'URR'
                elif cubeList[BTM] == FrontFace:
                    theCube.rotate('UUFF')
                    rotations.append('UUFF')
                    cubeList = list(theCube.get())
                    #rotate'UUFF'
                else:
                    theCube.rotate('uLL')
                    rotations.append('uLL')
                    cubeList = list(theCube.get())
                    #rotate'uLL'
        
        #########################################################
        #                                                       #
        #          Checking for Daisy Pedal on Up Face          #
        #                                                       #
        #########################################################
        if cubeList[UTM] == DownFace:
            if cubeList[BTM] == RightFace:
                theCube.rotate('URR')
                rotations.append('URR')
                cubeList = list(theCube.get())
                #rotate'URR'
            elif cubeList[BTM] == FrontFace:
                theCube.rotate('UU')
                rotations.append('UU')
                cubeList = list(theCube.get())
                #rotate'UU;
            elif cubeList[BTM] == LeftFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                #rotate'u'
            else:
                theCube.rotate('BB')
                rotations.append('BB')
                cubeList = list(theCube.get())
                #rotate'BB'
        
        if cubeList[UML] == DownFace:
            if cubeList[LTM] == FrontFace:
                theCube.rotate('uFF')
                rotations.append('uFF')
                cubeList = list(theCube.get())
                #rotate'uFF'
            elif cubeList[LTM] == RightFace:
                theCube.rotate('uu')
                rotations.append('uu')
                cubeList = list(theCube.get())
                #rotate'uu'
            elif cubeList[LTM] == BackFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                #rotate'U'
            else:
                theCube.rotate('LL')
                rotations.append('LL')
                cubeList = list(theCube.get())
                #rotate'LL'
        
        if cubeList[UMR] == DownFace:
            if cubeList[RTM] == FrontFace:
                theCube.rotate('UFF')
                rotations.append('UFF')
                cubeList = list(theCube.get())
                #rotate'UFF'
            elif cubeList[RTM] == LeftFace:
                theCube.rotate('UULL')
                rotations.append('UULL')
                cubeList = list(theCube.get())
                #rotate'UULL'
            elif cubeList[RTM] == BackFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                #rotate'u'
            else:
                theCube.rotate('RR')
                rotations.append('RR')
                cubeList = list(theCube.get())
        
        if cubeList[UBM] == DownFace:
            if cubeList[FTM] == RightFace:
                theCube.rotate('urr')
                rotations.append('urr')
                cubeList = list(theCube.get())
                #rotate'urr'
            elif cubeList[FTM] == LeftFace:
                theCube.rotate('U')
                rotations.append('U')
                cubeList = list(theCube.get())
                #rotate'U'
            elif cubeList[FTM] == BackFace:
                theCube.rotate('UUBB')
                rotations.append('UUBB')
                cubeList = list(theCube.get())
                #rotate'UUBB'
            else:
                theCube.rotate('FF')
                rotations.append('FF')
                cubeList = list(theCube.get())
                #rotate'FF'
                
        #########################################################
        #                                                       #
        #        Checking for Daisy Pedal on Front Face         #
        #                                                       #
        #########################################################
        if cubeList[FTM] == DownFace:
            if cubeList[UBM] == RightFace:
                theCube.rotate('uBUbrr')
                rotations.append('uBUbrr')
                cubeList = list(theCube.get())
                #rotate'uBUbrr'
            elif cubeList[UBM] == LeftFace:
                theCube.rotate('ULFUfll')
                rotations.append('ULFUfll')
                cubeList = list(theCube.get())
                #rotate'ULFUfll'
            elif cubeList[UBM] == BackFace:
                theCube.rotate('UUBBLUlbb')
                rotations.append('UUBBLUlbb')
                cubeList = list(theCube.get())
                #rotate'UUBBLUlbb'
            else:
                theCube.rotate('FRUrff')
                rotations.append('FRUrff')
                cubeList = list(theCube.get())
                #rotate'FRUrff'
        
        if cubeList[FML] == DownFace:
            if cubeList[LMR] == RightFace:
                theCube.rotate('FuRBUbrr')
                rotations.append('FuRBUbrr')
                cubeList = list(theCube.get())
                #rotate'FuRBUbrr'
            elif cubeList[LMR] == BackFace:
                theCube.rotate('FuuBLUlbb')
                rotations.append('FuuBLUlbb')
                cubeList = list(theCube.get())
                #rotate'FuuBLUlbb'
            elif cubeList[LMR] == LeftFace:
                theCube.rotate('FULFUfll')
                rotations.append('FULFUfll')
                cubeList = list(theCube.get())
                #rotate'FULFUfll'
            else:
                theCube.rotate('FFRUrff')
                rotations.append('FFRUrff')
                cubeList = list(theCube.get())
                #rotate'FFRUrff'
        
        if cubeList[FMR] == DownFace:
            if cubeList[RML] == BackFace:
                theCube.rotate('RRBBLUlbb')
                rotations.append('RRBBLUlbb')
                cubeList = list(theCube.get())
                #rotate'RRBBLUlbb'
            elif cubeList[RML] == LeftFace:
                theCube.rotate('fULFUfll')
                rotations.append('fULFUfll')
                cubeList = list(theCube.get())
                #rotate'fULFUfll'
            elif cubeList[RML] == RightFace:
                theCube.rotate('fuRBUbrr')
                rotations.append('fuRBUbrr')
                cubeList = list(theCube.get())
                #rotate'fuRBUbrr'
            else:
                theCube.rotate('RUrff')
                rotations.append('RUrff')
                cubeList = list(theCube.get())
                #rotate'RUrff'
        
        if cubeList[FBM] == DownFace:
            if cubeList[DTM] == LeftFace:
                theCube.rotate('FFULFUfLL')
                rotations.append('FFULFUfLL')
                cubeList = list(theCube.get())
                #rotate'FFULFUfLL'
            elif cubeList[DTM] == BackFace:
                theCube.rotate('FFuuBLUlbb')
                rotations.append('FFuuBLUlbb')
                cubeList = list(theCube.get())
                #rotate'FFuuBLUlbb'
            elif cubeList[DTM] == RightFace:
                theCube.rotate('FFuRBUbrr')
                rotations.append('FFuRBUbrr')
                cubeList = list(theCube.get())
                #rotate'FFuRBUbrr'
            else:
                theCube.rotate('fRUrff')
                rotations.append('fRUrff')
                cubeList = list(theCube.get())
                #rotate'fRUrff'
        
        #########################################################
        #                                                       #
        #        Checking for Daisy Pedal on Right Face         #
        #                                                       #
        #########################################################
        if cubeList[RTM] == DownFace:
            if cubeList[UMR] == FrontFace:
                theCube.rotate('UFRUrFF')
                rotations.append('UFRUrFF')
                cubeList = list(theCube.get())
                #rotate'UFRUrFF'
            elif cubeList[UMR] == LeftFace:
                theCube.rotate('UU')
                rotations.append('UU')
                cubeList = list(theCube.get())
                #rotate'UU'
            elif cubeList[UMR] == BackFace:
                theCube.rotate('u')
                rotations.append('u')
                cubeList = list(theCube.get())
                #rotate'u'
            else:
                theCube.rotate('RBUbrr')
                rotations.append('RBUbrr')
                cubeList = list(theCube.get())
                #rotate'RBUbrr'
        
        if cubeList[RML] == DownFace:
            if cubeList[FMR] == FrontFace:
                theCube.rotate('FF')
                rotations.append('FF')
                cubeList = list(theCube.get())
                #rotate'FF'
            elif cubeList[FMR] == LeftFace:
                theCube.rotate('fUFUBLLFUfLL')
                rotations.append('fUFUBLLFUfLL')
                cubeList = list(theCube.get())
                #rotate'fUFUBLLFUfLL'
            elif cubeList[FMR] == BackFace:
                theCube.rotate('RurBLUlbb')
                rotations.append('RurBLUlbb')
                cubeList = list(theCube.get())
                #rotate'RurBLUlbb'
            else:
                theCube.rotate('RRBUbrr')
                rotations.append('RRBUbrr')
                cubeList = list(theCube.get())
                #rotate'RRBUbrr'
        
        if cubeList[RMR] == DownFace:
            if cubeList[BML] == FrontFace:
                theCube.rotate('BUFF')
                rotations.append('BUFF')
                cubeList = list(theCube.get())
                #rotate'BUFF'
            elif cubeList[BML] == BackFace:
                theCube.rotate('b')
                rotations.append('b')
                cubeList = list(theCube.get())
                #rotate'b'
            elif cubeList[BML] == LeftFace:
                theCube.rotate('BUUFF')
                rotations.append('BUUFF')
                cubeList = list(theCube.get())
                #rotate'BUUFF'
            else:
                theCube.rotate('BUbrr')
                rotations.append('BUbrr')
                cubeList = list(theCube.get())
                #rotate'BUbrr'
        
        if cubeList[RBM] == DownFace:
            if cubeList[DMR] == LeftFace:
                theCube.rotate('RRUULFUfLL')
                rotations.append('RRUULFUfLL')
                cubeList = list(theCube.get())
                #rotate'RRUULFUfLL'
            elif cubeList[DMR] == FrontFace:
                theCube.rotate('RRUFRUrff')
                rotations.append('RRUFRUrff')
                cubeList = list(theCube.get())
                #rotate'RRUFRUrff'
            elif cubeList[DMR] == BackFace:
                theCube.rotate('RRurrBLUlbb')
                rotations.append('RRurrBLUlbb')
                cubeList = list(theCube.get())
                #rotate'RRurrBLUlbb'
            else:
                theCube.rotate('rBUbrr')
                rotations.append('rBUbrr')
                cubeList = list(theCube.get())
                #rotate'rBUbrr'
        
        #########################################################
        #                                                       #
        #        Checking for Daisy Pedal on Back Face          #
        #                                                       #
        #########################################################
        if cubeList[BTM] == DownFace:
            if cubeList[UTM] == RightFace:
                theCube.rotate('URBUbrr')
                rotations.append('URBUbrr')
                cubeList = list(theCube.get())
                #rotate'URBUbrr'
            elif cubeList[UTM] == FrontFace:
                theCube.rotate('UUFRUrff')
                rotations.append('UUFRUrff')
                cubeList = list(theCube.get())
                #rotate'UUFRUrff'
            elif cubeList[UTM] == LeftFace:
                theCube.rotate('uLFfll')
                rotations.append('uLFUfll')
                cubeList = list(theCube.get())
                #rotate'uLFUfll'
            else:
                theCube.rotate('BLUlbb')
                rotations.append('BLUlbb')
                cubeList = list(theCube.get())
                #rotate'BLUlbb'
        
        if cubeList[BML] == DownFace:
            if cubeList[RMR] == RightFace:
                theCube.rotate('R')
                rotations.append('R')
                cubeList = list(theCube.get())
                #rotate'R'
            elif cubeList[RMR] == FrontFace:
                theCube.rotate('rrRUrff')
                rotations.append('rrRUrff')
                cubeList = list(theCube.get())
                #rotate'rrRUrff'
            elif cubeList[RMR] == LeftFace:
                theCube.rotate('rURfFUfll')
                rotations.append('rURfFUfll')
                cubeList = list(theCube.get())
                #rotate'rURfFUfll'
            else:
                theCube.rotate('BBLUlbb')
                rotations.append('BBLUlbb')
                cubeList = list(theCube.get())
                #rotate'BBLUlbb'
        
        if cubeList[BMR] == DownFace:
            if cubeList[LML] == RightFace:
                theCube.rotate('LulFRRBUbrr')
                rotations.append('LulFRRBUbrr')
                cubeList = list(theCube.get())
                #rotate'LulFRRBUbrr'
            elif cubeList[LML] == FrontFace:
                theCube.rotate('LulurRUrff')
                rotations.append('LulurRUrff')
                cubeList = list(theCube.get())
                #rotate'LulurRUrff'
            elif cubeList[LML] == LeftFace:
                theCube.rotate('l')
                rotations.append('l')
                cubeList = list(theCube.get())
                #rotate'LulfFUfll'
            else:
                theCube.rotate('LUlbb')
                rotations.append('LUlbb')
                cubeList = list(theCube.get())
                #rotate'LUlbb'
        
        if cubeList[BBM] == DownFace:
            if cubeList[DBM] == RightFace:
                theCube.rotate('BBURBUbrr')
                rotations.append('BBURBUbrr')
                cubeList = list(theCube.get())
                #rotate'BBURBUbrr'
            elif cubeList[DBM] == FrontFace:
                theCube.rotate('BBUUFRUrff')
                rotations.append('BBUUFRUrff')
                cubeList = list(theCube.get())
                #rotate'BBUUFRUrff'
            elif cubeList[DBM] == LeftFace:
                theCube.rotate('BBuLFUfll')
                rotations.append('BBuLFUfll')
                cubeList = list(theCube.get())
                #rotate'BBuLFUfll'
            else:
                theCube.rotate('bLUlbb')
                rotations.append('bLUlbb')
                cubeList = list(theCube.get())
                #rotate'bLUlbb'
        
        #########################################################
        #                                                       #
        #         Checking for Daisy Pedal on Left Face         #
        #                                                       #
        #########################################################
        if cubeList[LTM] == DownFace:
            if cubeList[UML] == FrontFace:
                theCube.rotate('uFRUrff')
                rotations.append('uFRUrff')
                cubeList = list(theCube.get())
                #rotate'uFRUrff'
            elif cubeList[UML] == RightFace:
                theCube.rotate('uuRBUbrr')
                rotations.append('uuRBUbrr')
                cubeList = list(theCube.get())
                #rotate'uuRBUbrr'
            elif cubeList[UML] == BackFace:
                theCube.rotate('UBLUlbb')
                rotations.append('UBLUlbb')
                cubeList = list(theCube.get())
                #rotate'UBLUlbb'
            else:
                theCube.rotate('LFUfll')
                rotations.append('LFUfll')
                cubeList = list(theCube.get())
                #rotate'LFUfll'
        
        if cubeList[LML] == DownFace:
            if cubeList[BMR] == BackFace:
                theCube.rotate('LUBLUlbb')
                rotations.append('LUBLUlbb')
                cubeList = list(theCube.get())
                #rotate'LUBLUlbb'
            elif cubeList[BMR] == RightFace:
                theCube.rotate('LuuRBUbrr')
                rotations.append('LuuRBUbrr')
                cubeList = list(theCube.get())
                #rotate'LuuRBUbrr'
            elif cubeList[BMR] == FrontFace:
                theCube.rotate('LuFRUrff')
                rotations.append('LuFRUrff')
                cubeList = list(theCube.get())
                #rotate'LuFRUrff'
            else:
                theCube.rotate('LLFUfll')
                rotations.append('LLFUfll')
                cubeList = list(theCube.get())
                #rotate'LLFUfll'
        
        if cubeList[LMR] == DownFace:
            if cubeList[FML] == FrontFace:
                theCube.rotate('FurRUrff')
                rotations.append('FurRUrff')
                cubeList = list(theCube.get())
                #rotate'FurRUrff'
            elif cubeList[FML] == RightFace:
                theCube.rotate('FuubBUbrr')
                rotations.append('FuubBUbrr')
                cubeList = list(theCube.get())
                #rotate'FuubBUbrr'
            elif cubeList[FML] == BackFace:
                theCube.rotate('FUlLUlbb')
                rotations.append('FUlLUlbb')
                cubeList = list(theCube.get())
                #rotate'FUlLUlbb'
            else:
                theCube.rotate('FUfll')
                rotations.append('FUfll')
                cubeList = list(theCube.get())
                #rotate'FUfll'
        
        if cubeList[LBM] == DownFace:
            if cubeList[DML] == FrontFace:
                theCube.rotate('lluFRUrff')
                rotations.append('lluFRUrff')
                cubeList = list(theCube.get())
                #rotate'lluFRUrff'
            elif cubeList[DML] == RightFace:
                theCube.rotate('lluuRBUbrr')
                rotations.append('lluuRBUbrr')
                cubeList = list(theCube.get())
                #rotate'lluuRBUbrr'
            elif cubeList[DML] == BackFace:
                theCube.rotate('llUBLUbb')
                rotations.append('llUBLUlbb')
                cubeList = list(theCube.get())
                #rotate'llUBLUlbb'
            else:
                theCube.rotate('lFUfll')
                rotations.append('lFUfll')
                cubeList = list(theCube.get())
                #rotate'lFUfll
    
    print("".join(rotations))
    return "".join(rotations)    



