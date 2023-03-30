class rotation():
    
        def F(self,cubeList, rotated):
            '''rotating the front face'''
            rotated[2] = cubeList[0]
            rotated[5] = cubeList[1]
            rotated[8] = cubeList[2]
            rotated[1] = cubeList[3]
            rotated[4] = cubeList[4]
            rotated[7] = cubeList[5]
            rotated[0] = cubeList[6]
            rotated[3] = cubeList[7]
            rotated[6] = cubeList[8]
            '''sides connected to the front face'''
            rotated[45] = cubeList[9]
            rotated[46] = cubeList[12]
            rotated[47] = cubeList[15]
            rotated[42] = cubeList[35]
            rotated[43] = cubeList[32]
            rotated[44] = cubeList[29]
            rotated[9] = cubeList[42]
            rotated[12] = cubeList[43]
            rotated[15] = cubeList[44]
            rotated[29] = cubeList[45]
            rotated[32] = cubeList[46]
            rotated[35] = cubeList[47]
            return rotated

        def f(self,cubeList, rotated):
            '''rotating the front face'''
            rotated[6] = cubeList[0]
            rotated[3] = cubeList[1]
            rotated[0] = cubeList[2]
            rotated[7] = cubeList[3]
            rotated[4] = cubeList[4]
            rotated[1] = cubeList[5]
            rotated[8] = cubeList[6]
            rotated[5] = cubeList[7]
            rotated[2] = cubeList[8]
            '''sides connected to the front face'''
            rotated[42] = cubeList[9]
            rotated[43] = cubeList[12]
            rotated[44] = cubeList[15]
            rotated[47] = cubeList[35]
            rotated[46] = cubeList[32]
            rotated[45] = cubeList[29]
            rotated[35] = cubeList[42]
            rotated[32] = cubeList[43]
            rotated[29] = cubeList[44]
            rotated[15] = cubeList[45]
            rotated[12] = cubeList[46]
            rotated[9] = cubeList[47]
            return rotated
        
        def R(self, cubeList, rotated):
            '''rotate right clockwise'''
            rotated[9] = cubeList[15]
            rotated[10] = cubeList[12]
            rotated[11] = cubeList[9]
            rotated[12] = cubeList[16]
            rotated[13] = cubeList[13]
            rotated[14] = cubeList[10]
            rotated[15] = cubeList[17]
            rotated[16] = cubeList[14]
            rotated[17] = cubeList[11]
            '''sides connected to the right face'''
            rotated[18] = cubeList[44]
            rotated[21] = cubeList[41]
            rotated[24] = cubeList[38]
            rotated[38] = cubeList[2]
            rotated[41] = cubeList[5]
            rotated[44] = cubeList[8]
            rotated[47] = cubeList[24]
            rotated[50] = cubeList[21]
            rotated[53] = cubeList[18]
            rotated[2] = cubeList[47]
            rotated[5] = cubeList[50]
            rotated[8] = cubeList[53]
            return rotated
    
        def r(self, cubeList, rotated):
            '''rotate right counterclockwise'''
            rotated[9] = cubeList[11]
            rotated[10] = cubeList[14]
            rotated[11] = cubeList[17]
            rotated[12] = cubeList[10]
            rotated[13] = cubeList[13]
            rotated[14] = cubeList[13]
            rotated[15] = cubeList[9]
            rotated[16] = cubeList[12]
            rotated[17] = cubeList[15]
            '''sides connected to the right face'''
            rotated[2] = cubeList[38]
            rotated[5] = cubeList[41]
            rotated[8] = cubeList[44]
            rotated[18] = cubeList[53]
            rotated[21] = cubeList[50]
            rotated[24] = cubeList[47]
            rotated[38] = cubeList[24]
            rotated[41] = cubeList[21]
            rotated[44] = cubeList[18]
            rotated[47] = cubeList[2]
            rotated[50] = cubeList[5]
            rotated[53] = cubeList[8]
            return rotated

        def B(self, cubeList, rotated):
            '''rotate back clockwise'''
            rotated[18] = cubeList[24]
            rotated[19] = cubeList[21]
            rotated[20] = cubeList[18]
            rotated[21] = cubeList[25]
            rotated[22] = cubeList[22]
            rotated[23] = cubeList[19]
            rotated[24] = cubeList[26]
            rotated[25] = cubeList[23]
            rotated[26] = cubeList[20]
            '''sides connected to the back face'''
            rotated[51] = cubeList[27]
            rotated[52] = cubeList[30]
            rotated[53] = cubeList[33]
            rotated[36] = cubeList[11]
            rotated[37] = cubeList[14]
            rotated[38] = cubeList[17]
            rotated[27] = cubeList[38]
            rotated[30] = cubeList[37]
            rotated[33] = cubeList[36]
            rotated[11] = cubeList[53]
            rotated[14] = cubeList[52]
            rotated[17] = cubeList[51]
            return rotated

        def b(self, cubeList, rotated):
            '''rotate back counterclockwise'''
            rotated[18] = cubeList[20]
            rotated[19] = cubeList[23]
            rotated[20] = cubeList[26]
            rotated[21] = cubeList[19]
            rotated[22] = cubeList[22]
            rotated[23] = cubeList[25]
            rotated[24] = cubeList[18]
            rotated[25] = cubeList[21]
            rotated[26] = cubeList[24]
            '''sides connected to the back face'''
            rotated[51] = cubeList[17]
            rotated[52] = cubeList[14]
            rotated[53] = cubeList[11]
            rotated[36] = cubeList[33]
            rotated[37] = cubeList[30]
            rotated[38] = cubeList[27]
            rotated[27] = cubeList[51]
            rotated[30] = cubeList[52]
            rotated[33] = cubeList[53]
            rotated[11] = cubeList[36]
            rotated[14] = cubeList[37]
            rotated[17] = cubeList[38]
            return rotated    

        def L(self, cubeList, rotated):
            '''rotate Left clockwise'''
            rotated[27] = cubeList[33]
            rotated[28] = cubeList[30]
            rotated[29] = cubeList[27]
            rotated[30] = cubeList[34]
            rotated[31] = cubeList[31]
            rotated[32] = cubeList[28]
            rotated[33] = cubeList[35]
            rotated[34] = cubeList[32]
            rotated[35] = cubeList[29]
            '''sides connected to the left face'''
            rotated[0] = cubeList[36]
            rotated[3] = cubeList[39]
            rotated[6] = cubeList[42]
            rotated[36] = cubeList[26]
            rotated[39] = cubeList[23]
            rotated[42] = cubeList[20]
            rotated[20] = cubeList[51]
            rotated[23] = cubeList[48]
            rotated[26] = cubeList[45]
            rotated[51] = cubeList[6]
            rotated[48] = cubeList[3]
            rotated[45] = cubeList[0]
            return rotated   

        def l(self, cubeList, rotated):
            '''rotate Left counterclockwise'''
            rotated[27] = cubeList[29]
            rotated[28] = cubeList[32]
            rotated[29] = cubeList[35]
            rotated[30] = cubeList[28]
            rotated[31] = cubeList[31]
            rotated[32] = cubeList[34]
            rotated[33] = cubeList[27]
            rotated[34] = cubeList[30]
            rotated[35] = cubeList[33]
            '''sides connected to the left face'''
            rotated[0] = cubeList[45]
            rotated[3] = cubeList[48]
            rotated[6] = cubeList[51]
            rotated[36] = cubeList[0]
            rotated[39] = cubeList[3]
            rotated[42] = cubeList[6]
            rotated[20] = cubeList[42]
            rotated[23] = cubeList[39]
            rotated[26] = cubeList[36]
            rotated[51] = cubeList[20]
            rotated[48] = cubeList[23]
            rotated[45] = cubeList[26]
            return rotated   

        def U(self, cubeList, rotated):
            '''rotate Up clockwise'''
            rotated[36] = cubeList[42]
            rotated[37] = cubeList[39]
            rotated[38] = cubeList[36]
            rotated[39] = cubeList[43]
            rotated[40] = cubeList[40]
            rotated[41] = cubeList[37]
            rotated[42] = cubeList[44]
            rotated[43] = cubeList[41]
            rotated[44] = cubeList[38]
            '''sides connected to the up face'''
            rotated[27] = cubeList[0]
            rotated[28] = cubeList[1]
            rotated[29] = cubeList[2]
            rotated[20] = cubeList[29]
            rotated[19] = cubeList[28]
            rotated[18] = cubeList[27]
            rotated[9] = cubeList[18]
            rotated[10] = cubeList[19]
            rotated[11] = cubeList[20]
            rotated[0] = cubeList[9]
            rotated[1] = cubeList[10]
            rotated[2] = cubeList[11]
            return rotated   

        def u(self, cubeList, rotated):
            '''rotate Up counterclockwise'''
            rotated[36] = cubeList[38]
            rotated[37] = cubeList[41]
            rotated[38] = cubeList[44]
            rotated[39] = cubeList[37]
            rotated[40] = cubeList[40]
            rotated[41] = cubeList[43]
            rotated[42] = cubeList[36]
            rotated[43] = cubeList[39]
            rotated[44] = cubeList[42]
            '''sides connected to the up face'''
            rotated[27] = cubeList[18]
            rotated[28] = cubeList[19]
            rotated[29] = cubeList[20]
            rotated[20] = cubeList[11]
            rotated[19] = cubeList[10]
            rotated[18] = cubeList[9]
            rotated[9] = cubeList[0]
            rotated[10] = cubeList[1]
            rotated[11] = cubeList[2]
            rotated[0] = cubeList[27]
            rotated[1] = cubeList[28]
            rotated[2] = cubeList[29]
            return rotated   
        
        
        