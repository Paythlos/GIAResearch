# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:59:38 2021

@author: Alex
"""
from IPython import get_ipython
ipython = get_ipython()
ipython.magic('%clear')

import sesame
import numpy as np
import matplotlib.pyplot as plt

#Region heterounion pn, unidades en cm
L = 3e-4    #Longitud de la celda
x = np.concatenate((np.linspace(0,1e-4,100,endpoint=False),(np.linspace(1e-4, L, 50))))

#Creacion de la malla con Sesame
sys = sesame.Builder(x)

####################################################################################################
#Detalles del material
material = {'Nc':8e17, 'Nv':1.8e19, 'Eg':1.5, 'affinity':3.9, 'epsilon':9.4,
        'mu_e':100, 'mu_h':100, 'Et':0, 'tau_e':10e-9, 'tau_h':10e-9, 'Et':0}

sys.add_material(material)

#Extension de la union desde el contacto izquierdo en cm
junction = 50e-7 

#Definicion de la region n y densidad de donadores de electrones en cm^-3
def n_region(pos):
    x = pos
    return x < junction

nD = 1e17   #Densidad de donadores
sys.add_donor(nD, n_region) #Adiciona los donadores a la region del semiconductor (donador, region)

#Definicion de la region y densidad de aceptadores de electrones en cm^-3
def p_region(pos):
    x = pos
    return x >= junction

nA = 1e15 #Densidad de Aceptadores
sys.add_acceptor(nA, p_region)  #Adiciona los aceptadores a la region del semiconductor (donador, region)

# Definicion de contactos Ohmicos
sys.contact_type('Ohmic', 'Ohmic')

#Definicion de tasas de recombinacion electron-hueco en la superficie, haciendo la homounion pn
Sn_left, Sp_left, Sn_right, Sp_right = 1e7, 0, 0, 1e7  # cm/s
sys.contact_S(Sn_left, Sp_left, Sn_right, Sp_right)

######################################################################################################
#Definicion de elementos luminicos
phi = 1e17       # flujo de fotones [1/(cm^2 s)]
alpha = 2.3e4    # coeficiente de absorcion [1/cm]

# Definicion de la funcion de tasa de generacion dependiente de la profundidad de penetracion de la luz
# en el seminconductor, en este caso es un decaimiento exponencial
def gfcn(x):
    return phi * alpha * np.exp(-alpha * x)

sys.generation(gfcn)

#####################################################################################################
#Generacion de voltajes iniciales bias
voltages = np.linspace(0, 0.95, 40) #Genera los voltajes
j = sesame.IVcurve(sys, voltages, '1dhomo_V') #Guarda los datos de las corriente adimensionales
j = j * sys.scaling.current #Da unidades de corriente en voltios

#Graficos
plt.plot(voltages, j, '-o')
plt.title('Curva I-V')
plt.xlabel('Voltaje [V]')
plt.ylabel('Densidad de Corriente [A/cm^2]')
plt.grid()      # Agrega reticula
plt.show()      # Muestra la figura

#Bandas de Energia 
sys, result = sesame.load_sim('1dhomo_V_0.gzip')  # load data file
az = sesame.Analyzer(sys,result)                   # get Sesame analyzer object
p1 = (0,0)
p2 = (3e-4,0)
az.band_diagram((p1,p2))                           # plot band diagram along line from p1 to p2