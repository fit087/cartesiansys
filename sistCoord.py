# -*- coding: latin1 -*-
from numpy import array
from numpy import inner
class sistCoord:
    """Cartesian Coordinate System: make cartesian coordinate objects with 
    the origin and the axis"""
    def __init__(self,origem,xaxis,yaxis,zaxis):
        self.origem=origem
        self.xaxis=xaxis
        self.yaxis=yaxis
        self.zaxis=zaxis
    
    def UCS2LCS(self,pto,ijk=False):
        """From Universal Coordinate System to Local Coordinate System 
        if ijk=True: pto is a versor and then don't need translation only rotation"""
        matrix=array([self.xaxis,self.yaxis,self.zaxis])
        #matrix=matrix.T
        pto=inner(matrix,pto)
        if not ijk:
            pto=pto-self.origem
        return pto

        
    def LCS2UCS(self,pto,ijk=False):
        """From Local Coordinate System to Universal Coordinate System
        if ijk=True: pto is a versor and then don't need translation only rotation"""
        matrix=array([self.xaxis,self.yaxis,self.zaxis])
        matrix=matrix.T
        pto=inner(matrix,pto)
        if not ijk:
            pto=pto+self.origem
        return pto        


    def LCS2UCS2(self,pto,xaxis,yaxis,zaxis,S2S1):
        matrix=array([xaxis,yaxis,zaxis])
        matrix=matrix.T
        pto=inner(matrix,pto)
        pto=pto+S2S1
        return pto


    def OCS2LCS(self,OCS,pto):
        """From Another Coordinate System to the Local Coordinate System"""
        
        xLOCS=self.UCS2LCS(OCS.xaxis,True)
        yLOCS=self.UCS2LCS(OCS.yaxis,True)
        zLOCS=self.UCS2LCS(OCS.zaxis,True)
        S2S1=self.UCS2LCS(OCS.origem-self.origem,True)
    
        nwpto=self.LCS2UCS2(pto,xLOCS,yLOCS,zLOCS,S2S1)
        return nwpto
