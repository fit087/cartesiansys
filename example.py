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
conexao_gl_16=SE.LCS2UCS(conexao_SE_16)
heightTractionMachine_SE=conexao_SE_16-array([0,0,16*2.54/100/2])
heightTractionMachine_gl=SE.LCS2UCS(heightTractionMachine_SE)

heightTractionMachine_utm=UTM.OCS2LCS(SE,heightTractionMachine_SE)
heightTractionMachine_utm1=UTM.UCS2LCS(heightTractionMachine_gl)



print("\nPto de Conexão (16pulg)_SE ",conexao_SE_16)
print("\nPto de Conexão (16pulg)_gl ",conexao_gl_16)
print("\nheightTractionMachine_SE ",heightTractionMachine_SE)
print("\nheightTractionMachine_gl ",heightTractionMachine_gl)

print("\nheightTractionMachine_utm ",heightTractionMachine_utm)
print("\nheightTractionMachine_utm1 ",heightTractionMachine_utm1)

# xline=SE.LCS2UCS(-SE.xaxis,True)
# yline=SE.LCS2UCS(-SE.yaxis,True)
# zline=SE.LCS2UCS(SE.zaxis,True)
LineSys=sistCoord(heightTractionMachine_gl,LS.xaxis,LS.yaxis,LS.zaxis)

PT_LineS=LineSys.UCS2LCS(PT_GL)
PT2_LineS=LineSys.UCS2LCS(PT2_gl)

print("PT_LineS= ",PT_LineS)
print("PT_LineS= ",PT_LineS[0])
print("PT2_LineS= ",PT2_LineS)
print("PT_GL= ",PT_GL)
print("LS.origem= ",LS.origem)
print("LS.origem_SE= ",SE.UCS2LCS(LS.origem))
print("LineSys.origem_SE= ",SE.UCS2LCS(LineSys.origem))

heightTractionMachine_LineSys=LineSys.UCS2LCS(heightTractionMachine_gl)

print("heightTractionMachine_LineSys= ",heightTractionMachine_LineSys)

print("LineSys.origem= ", LineSys.origem)

print("LS.xaxis,LS.yaxis,LS.zaxis= ",LS.xaxis,LS.yaxis,LS.zaxis)

#1,3347
#PT2Mauro_SL=array([0,0,1.3347])

endSt_LS=array([22.0710,0,-5.7749])
endSt_LineS=LineSys.OCS2LCS(LS,endSt_LS)
print("endSt_LineS= ", endSt_LineS)
referencesPoint_LineS=endSt_LineS
referencesPoint_LineS[0]/=2
print("referencesPoint_LineS",referencesPoint_LineS)
referencesPoint_gl=LineSys.LCS2UCS(referencesPoint_LineS)
referencesPoint_utm=UTM.OCS2LCS(LineSys,referencesPoint_LineS)
print("referencesPoint_gl",referencesPoint_gl)
print("referencesPoint_utm",referencesPoint_utm)