# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:59:38 2021

@author: Alex
"""
# from IPython import get_ipython
# ipython = get_ipython()
# ipython.magic('%clear')

import sesame
import numpy as np
import matplotlib.pyplot as plt

#Constantes
h = 6.62607004e-34 #unidades de (m^2 kg)/s
kb = 1.38064852e-23 #Unidades de (m^2 kg)/(s^2 K)
me = 0.0948
mh = 0.1995
m = 9.11e-31

#Region homounion pn, unidades en cm
L = 0.1e-3    #Longitud de la celda en cm
x = np.concatenate((np.linspace(0,0.05e-3,100,endpoint=False),(np.linspace(0.05e-3, L, 50))))
T = 293.15  #Temperatura del sistema
# DEC = ((T/300.)**(3./2.))*2.8e19     #Calculo de Nc dependiente de la temperatura Silicio
# DEV = ((T/300.)**(3./2.))*1.04e19     #Calculo de Nv dependiente de la temperatura Silicio
DEC = 2.540933e19*(((me*m)/m)**(3./2.))*((T/300.)**(3./2.)) #Densidad efectiva de electrones
DEV = 2.540933e19*(((mh*m)/m)**(3./2.))*((T/300.)**(3./2.)) #Densidad efectiva de huecos

#Creacion de la malla con Sesame
sys = sesame.Builder(x)

####################################################################################################
#Detalles del material Silicio
# material = {'Nc':DEC, 'Nv':DEV, 'Eg':1.12, 'affinity':4.05, 'epsilon':11.7,
#         'mu_e':1450, 'mu_h':500, 'Et':0, 'tau_e':10e-6, 'tau_h':10e-6, 'Et':0}

#Detalles del material TiO2
material = {'Nc':DEC, 'Nv':DEV, 'Eg':2, 'affinity':4.9, 'epsilon':85,
          'mu_e':10, 'mu_h':10, 'Et':0, 'tau_e':1e-3, 'tau_h':1e-3, 'Et':0} 

sys.add_material(material)

#Extension de la union desde el contacto izquierdo en cm
junction = 50e-7

#Definicion de la region n y densidad de donadores de electrones en cm^-3
def n_region(pos):
    x = pos
    return x < junction

nD = 1e17   #Densidad de donadores (electrones)
sys.add_donor(nD, n_region) #Adiciona los donadores a la region del semiconductor (donador, region)

#Definicion de la region y densidad de aceptadores de electrones (huecos) en cm^-3
def p_region(pos):
    x = pos
    return x >= junction

nA = 1e17  #Densidad de Aceptadores (huecos)
sys.add_acceptor(nA, p_region)  #Adiciona los aceptadores a la region del semiconductor (donador, region)

# Definicion de contactos Ohmicos
sys.contact_type('Ohmic', 'Ohmic')

#Definicion de tasas de recombinacion electron-hueco en la superficie, haciendo la homounion pn
Sn_left, Sp_left, Sn_right, Sp_right = 1e7, 0, 0, 1e7  # cm/s
sys.contact_S(Sn_left, Sp_left, Sn_right, Sp_right)

######################################################################################################
#Definicion de elementos luminicos en el Silicio
# phi = 3.12e16       # flujo de fotones [1/(cm^2 s)]
# alpha = 2.3e4    # coeficiente de absorcion [1/cm]

#Definicion de elementos luminicos en el TiO2
phi = 3.12e16      # flujo de fotones [1/(cm^2 s)]
alpha = 13534.7  # coeficiente de absorcion [1/cm]
#alpha = 4.94e-3
# Definicion de la funcion de tasa de generacion dependiente de la profundidad de penetracion de la luz
# en el seminconductor, en este caso es un decaimiento exponencial
def gfcn(x):
    return phi * alpha * np.exp(-alpha * x)

sys.generation(gfcn)

#####################################################################################################
#Generacion de voltajes iniciales bias
voltages = np.linspace(0, 1.95, 50) #Genera los voltajes
j = sesame.IVcurve(sys, voltages, '1dhomo_V') #Guarda los datos de las corriente adimensionales
j = j * sys.scaling.current #Da unidades de corriente en voltios

#Graficos
# plt.plot(voltages, j*1000, '-o')
# plt.title('Curva I-V')
# plt.xlabel('Voltaje [V]')
# plt.ylabel('Densidad de Corriente [mA/cm^2]')
# plt.grid()      # Agrega reticula
# plt.show()      # Muestra la figura
# np.savetxt('curvas\jv_values215a.txt', np.column_stack((voltages, j)))


#Bandas de Energia
# sys, result = sesame.load_sim('1dhomo_V_0.gzip')  # load data file
# az = sesame.Analyzer(sys,result)                   # get Sesame analyzer object
# p1 = (0,0)
# p2 = (0.1e-3,0)
# az.band_diagram((p1,p2))                           # plot band diagram along line from p1 to p2
