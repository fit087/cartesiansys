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

    def ijk_UCS2LCS(self,versor):
        matrix=array([self.xaxis,self.yaxis,self.zaxis])
        #matrix=matrix.T
        pto=inner(matrix,versor)
        #pto=pto-self.origem
        return pto


    def LCS2UCS(self,pto):
        matrix=array([self.xaxis,self.yaxis,self.zaxis])
        matrix=matrix.T
        pto=inner(matrix,pto)
        pto=pto+self.origem
        return pto

    def ijk_LCS2UCS(self,versor):
        matrix=array([self.xaxis,self.yaxis,self.zaxis])
        matrix=matrix.T
        versor=inner(matrix,versor)
        #pto=pto+self.origem
        return versor

 #   def LCS2UCS(self,pto,xaxis=self.xaxis,yaxis=self.yaxis,zaxis=self.zaxis):
 #       matrix=array([xaxis,yaxis,zaxis])
 #       matrix=matrix.T
 #       pto=inner(matrix,pto)
 #       pto=pto+self.origem
 #       return pto

    def LCS2UCS2(self,pto,xaxis,yaxis,zaxis,S2S1):
        matrix=array([xaxis,yaxis,zaxis])
        matrix=matrix.T
        pto=inner(matrix,pto)
        pto=pto+S2S1
        return pto


    def OCS2LCS(self,OCS,pto):
        #Rotation
        xLOCS=self.ijk_UCS2LCS(OCS.xaxis)
        yLOCS=self.ijk_UCS2LCS(OCS.yaxis)
        zLOCS=self.ijk_UCS2LCS(OCS.zaxis)
        S2S1=self.ijk_UCS2LCS(OCS.origem-self.origem)
        #nwpto=self.LCS2UCS(pto,xLOCS,yLOCS,zLOCS)
        nwpto=self.LCS2UCS2(pto,xLOCS,yLOCS,zLOCS,S2S1)
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

SEorigin=array([0,0,-5.182])
xaxis,yaxis,zaxis=array([0,-1,0]),array([1,0,0]),array([0,0,1])
SE=sistCoord(SEorigin,xaxis,yaxis,zaxis)

Origen_do_global=array([0,0,0])

Origen_do_global_SE=SE.UCS2LCS(Origen_do_global)

print("\nOrigen_do_global_SE= ",Origen_do_global_SE)

OLS_SE=array([-60,-13.24,4.8])

print("OLS_SE= ",OLS_SE)

OLS_gl=SE.LCS2UCS(OLS_SE)

xrs_se=array([-1,0,0])
yrs_se=array([0,-1,0])
zrs_se=array([0,0,1])

xrs_gl=SE.ijk_LCS2UCS(xrs_se)
yrs_gl=SE.ijk_LCS2UCS(yrs_se)
zrs_gl=SE.ijk_LCS2UCS(zrs_se)

print("xrs,yrs,zrs_gl= ",xrs_gl,yrs_gl,zrs_gl)

LS=sistCoord(OLS_gl,xrs_gl,yrs_gl,zrs_gl)

print("\nLocalSistem LS_gl= ",OLS_gl)

PT_SL=array([-35.017,0,5.668])

print("\nPto Tangencia_LS ",PT_SL)

PT_GL=LS.LCS2UCS(PT_SL)

print("\nPto Tangencia_GL ",PT_GL)

PT_SE=SE.UCS2LCS(PT_GL)

print("\nPto Tangencia_SE ",PT_SE)


PT_seProva=SE.OCS2LCS(LS,PT_SL)

print("\nPto Tangencia_SEprova ",PT_seProva)

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