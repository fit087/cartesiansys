from numpy import array
from numpy import inner
class sistCoord:
    def __init__(self,origem,xaxis,yaxis,zaxis):
        self.origem=origem
        self.xaxis=xaxis
        self.yaxis=yaxis
        self.zaxis=zaxis
        
    def UCS2LCS(self,pto):
        matrix=array([self.xaxis,self.yaxis,self.zaxis])
        #matrix=matrix.T
        pto=inner(matrix,pto)
        pto=pto-self.origem
        return pto
        
    def LCS2UCS(self,pto):
        matrix=array([self.xaxis,self.yaxis,self.zaxis])
        matrix=matrix.T
        pto=inner(matrix,pto)
        pto=pto+self.origem
        return pto

 #   def LCS2UCS(self,pto,xaxis=self.xaxis,yaxis=self.yaxis,zaxis=self.zaxis):
 #       matrix=array([xaxis,yaxis,zaxis])
 #       matrix=matrix.T
 #       pto=inner(matrix,pto)
 #       pto=pto+self.origem
 #       return pto

    def LCS2UCS2(self,pto,xaxis,yaxis,zaxis):
        matrix=array([xaxis,yaxis,zaxis])
        matrix=matrix.T
        pto=inner(matrix,pto)
        pto=pto+self.origem
        return pto


    def OCS2LCS(self,OCS,pto):
        #Rotation
        xLOCS=self.UCS2LCS(OCS.xaxis)
        yLOCS=self.UCS2LCS(OCS.yaxis)
        zLOCS=self.UCS2LCS(OCS.zaxis)
        #nwpto=self.LCS2UCS(pto,xLOCS,yLOCS,zLOCS)
        nwpto=self.LCS2UCS2(pto,xLOCS,yLOCS,zLOCS)
        #only translation
        #pto+=OCS
        return nwpto
        
#class pto(array):
#class pto:
#    def __init__(self,coord,sistCoord):
#        self.coord=coord
#        self.sistCoord=sistCoord
        
origen=array([1,1,1])

xaxis=array([1,0,0])

yaxis=array([0,1,0])     
        
zaxis=array([0,0,1])#origen=array([0,0,0])




#origen=array([0,0,0])
#
##origen=array([1,1,1])
#
#xaxis=array([4.0/5,3.0/5,0])
#
#yaxis=array([-3.0/5,4.0/5,0])
#
#zaxis=array([0,0,1])


local=sistCoord(origen,xaxis,yaxis,zaxis)

pto=array([1,1,0])

ptoGl=local.LCS2UCS(pto)

print ("local.LCS2UCS(pto)= ",ptoGl)

ptoGl=local.UCS2LCS(ptoGl)

print ("local.UCS2LCS(pto)= ",ptoGl)


#xaxis=array([1.0/2**0.5,1.0/2**0.5,0])
#
#yaxis=array([-1.0/2**0.5,1.0/2**0.5,0])
#
#zaxis=array([0,0,1])


local1=sistCoord(origen,xaxis,yaxis,zaxis)

pto=array([1,1,0])

ptoGl=local1.LCS2UCS(pto)

print ("local1.LCS2UCS(pto)= ",ptoGl)

ptoGl=local1.UCS2LCS(ptoGl)

print ("local1.UCS2LCS(pto)= ",ptoGl)



print ("************Translacao entre Sistemas Coordenados************** ")



#sistLocal=sistCoord(origen,xaxis,yaxis,zaxis)        

#pto1=pto([1,5,4],sistLocal)



#a=array([1,2,3])

#print (a)


#Transformador

#class sistCoord:
#    def __init__(self,origem,xaxis,yaxis,zaxis):
#        self.origem=origem
#        self.xaxis=xaxis
#        self.yaxis=yaxis
#        self.zaxis=zaxis


#Pto siempre guarda solo em coordenada global
#o guarda coordenadas e sistema de coordenadas