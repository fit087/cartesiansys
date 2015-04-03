# -*- coding: latin1 -*-
#import sistCoord
from sistCoord import *
#from numpy import array


print ("\n************Translacao entre Sistemas Coordenados**************\n")

#Criação do Sist Estrutural
SEorigin=array([0,0,-5.182])
xaxis,yaxis,zaxis=array([0,-1,0]),array([1,0,0]),array([0,0,1])
SE=sistCoord(SEorigin,xaxis,yaxis,zaxis)


#Provando Pontos 1
Origen_do_global=array([0,0,0])

Origen_do_global_SE=SE.UCS2LCS(Origen_do_global)

print("\nOrigen_do_global_SE= ",Origen_do_global_SE)



#Criação do Sist Local
#Provando Pontos 2
OLS_SE=array([-60,-13.24,4.8])

print("OLS_SE= ",OLS_SE)

#Origem LocalSystem em SE ---> Origem LocalSystem em global
OLS_gl=SE.LCS2UCS(OLS_SE)
print("\nLocalSistem LS_gl= ",OLS_gl)

#Eixos do sistema Local no SEstructural
xrs_se=array([-1,0,0])
yrs_se=array([0,-1,0])
zrs_se=array([0,0,1])

#Eixos do sistema Local no Global (Ers_SE--->Ers_gl)
xrs_gl=SE.LCS2UCS(xrs_se,True)
yrs_gl=SE.LCS2UCS(yrs_se,True)
zrs_gl=SE.LCS2UCS(zrs_se,True)



print("xrs,yrs,zrs_gl= ",xrs_gl,yrs_gl,zrs_gl)

LS=sistCoord(OLS_gl,xrs_gl,yrs_gl,zrs_gl)


#Ponto de Tangencia no SistemaLocal
PT_SL=array([-35.017,0,5.668])

print("\nPto Tangencia_LS ",PT_SL)

#Ponto de Tangencia no SistemaGlobal
PT_GL=LS.LCS2UCS(PT_SL)

print("\nPto Tangencia_GL ",PT_GL)

#Ponto de Tangencia no SistemaEstrutural
PT_SE=SE.UCS2LCS(PT_GL)

print("\nPto Tangencia_SE ",PT_SE)


#Ponto de Tangencia no SistemaEstrutural. Metodo OCS2LCS
print ("\n---Metodo OCS2LCS---\n")

PT_seProva=SE.OCS2LCS(LS,PT_SL)

print("\nPto Tangencia_SEprova ",PT_seProva)

Ogl_UTM=array([10,20,0])
ExUTM_gl,NyUTM_gl,zUTM_gl=array([1,0,0]),array([0,1,0]),array([0,0,1])


