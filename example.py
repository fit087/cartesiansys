# -*- coding: latin1 -*-
#import sistCoord
from sistCoord import *
#from numpy import array


print ("\n************Translacao entre Sistemas Coordenados**************\n")

#CriaÃ§Ã£o do Sist Estrutural
SEorigin=array([0,0,-5.182])
xaxis,yaxis,zaxis=array([0,-1,0]),array([1,0,0]),array([0,0,1])
#Sist Estrutural
SE=sistCoord(SEorigin,xaxis,yaxis,zaxis)

print("\nSEo= ",SEorigin)

#Provando Pontos 1
Origen_do_global=array([0,0,0])

Origen_do_global_SE=SE.UCS2LCS(Origen_do_global)

#print("\nOrigen_do_global_SE= ",Origen_do_global_SE)





#CriaÃ§Ã£o do Sist Local
#Provando Pontos 2
OLS_SE=array([-60,-13.24,4.8])

print("SistLocal_SE= ",OLS_SE)

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

#Sistema Coordenado UTM
Ogl_UTM=-array([536414.0,8580327.0,0])
ExUTM_gl,NyUTM_gl,zUTM_gl=array([1,0,0]),array([0,1,0]),array([0,0,1])
UTM=sistCoord(Ogl_UTM,ExUTM_gl,NyUTM_gl,zUTM_gl)

#Calculo do PT2 o Segundo Ponto de Tangencia
PT2_SL=array([0,0,1.3347])
PT2_gl=LS.LCS2UCS(PT2_SL)
print("\nPto Tangencia 2_LS ",PT2_SL)
print("\nPto Tangencia 2_LS ",PT2_gl)


#Ponto de Conexão (Maq. Tração) no SistemaEstrutural. Metodo OCS2LCS
print ("\n---Ponto de Conexao (Maq. Tracao)---\n")

conexao_SE_16=array([5,-13.24,10.84],dtype=float)
conexao_gl_16=SE.LCS2UCS(conexao)
heightTractionMachine_SE=conexao_SE_16-array([0,0,16*2.54/100/2])
heightTractionMachine_gl=SE.LCS2UCS(heightTractionMachine_SE)

print("\nPto de Conexão (16pulg)_SE ",conexao_SE_16)
print("\nPto de Conexão (16pulg)_gl ",conexao_gl_16)
print("\nheightTractionMachine_SE ",heightTractionMachine_SE)
print("\nheightTractionMachine_gl ",heightTractionMachine_gl)
