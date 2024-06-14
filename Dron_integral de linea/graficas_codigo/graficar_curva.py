# Graficar la curva paramétrica

import matplotlib.pyplot as plt
import numpy as np
def graficar(t1_values, t2_values, t3_values, t4_values ):
 
    def x_parametric(t):
        return t
    def y_parametric(t):
        return t*0
    def z_parametric(t):
        return -0.5*np.cos(4/5*np.pi*t)+1.2
    
    # Calcular los valores de x y y para cada valor de t
    x_values = x_parametric(t1_values)
    y_values = y_parametric(t1_values)
    z_values = z_parametric(t1_values)

    def x_parametric(t):
        return 5*(t/t)
    def y_parametric(t):
        return t
    def z_parametric(t):
        return 0.7*(t/t)
    x2_values = x_parametric(t2_values)
    y2_values = y_parametric(t2_values)
    z2_values = z_parametric(t2_values)
    
    def x_parametric_2(t):
        return 5-t
    def y_parametric_2(t):
        return t/t
    def z_parametric_2(t):
        return -0.5*np.cos(4/5*np.pi*t)+1.2
    
    x3_values = x_parametric_2(t3_values)
    y3_values = y_parametric_2(t3_values)
    z3_values = z_parametric_2(t3_values)


    def x_parametric_4(t):
        return t*0
    def y_parametric_4(t):
        return 1-t
    def z_parametric_4(t):
        return 0.7*(t/t)
    x4_values = x_parametric_4(t4_values)
    y4_values = y_parametric_4(t4_values)
    z4_values = z_parametric_4(t4_values)



    #Vectores con los datos reales de vuelo

    x_medidos_1=[0, 1.25, 2.50, 3.80, 5.05, 5.05 ,5-1.25, 5-2.50, 5-3.80 ,0.5, 0 ]
    y_medidos_1=[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0]
    z_medidos_1=[0.4, 1.40, 0.40, 1.40, 0.40, 0.40, 1.30, 0.40, 1.30, 0.50, 0.40]

    z_medidos_2=[0.4, 1.40, 0.50, 1.40, 0.50, 0.50, 1.40, 0.50, 1.40, 0.5, 0.5]

    z_medidos_3=[0.3, 1.30, 0.30, 1.30, 0.30, 0.30, 1.30, 0.30, 1.30, 0.3, 0.3]
   

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Graficar los puntos en 3D
    line1, =ax.plot(x_values, y_values, z_values, linestyle='dashed' ,color='b', label='Función modelo')
    ax.plot(x2_values, y2_values, z2_values,linestyle='dashed' , color='b')
    ax.plot(x3_values, y3_values, z3_values, linestyle='dashed'  ,color='b')
    ax.plot(x4_values, y4_values, z4_values, linestyle='dashed'  ,color='b')

    line2, = ax.plot(x_medidos_1, y_medidos_1, z_medidos_1, color='m', label='Intento 2')
    line3, = ax.plot(x_medidos_1, y_medidos_1, z_medidos_2, color='#00FF00', label='Intento 3')
    line4, = ax.plot(x_medidos_1, y_medidos_1, z_medidos_3, color='r', label='Intento 5')
   
    

    # Etiquetas de los ejes
    ax.set_xlabel('X ')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Gráfica del modelo vs datos reales del vuelo')


    ax.legend(['First line'])
    ax.legend(handles=[line1, line2, line3, line4])
    # Mostrar la gráfica
    plt.show()