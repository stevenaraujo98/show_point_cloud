import numpy as np
import pptk #visualizador 3D
import cv2
import glob

# 240x180
def get_np_array_from_lines_nueva( lines, is_verts, width = 240, height = 180, roi = []):
    datos = []
    cont = 0
    for line in lines:
        if cont == 0:
            cont += 1
        else:
            data = line.strip()
            list_temp = data.split(',')
            z = float(list_temp[2])
            if z > 0.1 and z < 0.5:
                datos.append([float(list_temp[0]), float(list_temp[1]), z])
    return (np.array(datos), int(width), int(height), np.array(datos))

# ubicacion = 'C:/Users/steve/Documents/Git/Investigacion/Capturas/Objetos diferentes/640X480/'
# ubicacion = 'C:/Users/steve/Documents/Git/Investigacion/Capturas/Objetos diferentes/848X480/'
# ubicacion = 'C:/Users/steve/Documents/Git/Investigacion/Capturas/Objetos diferentes/1280X720/'
ubicacion = 'C:/Users/steve/Documents/Git/Investigacion/Capturas/Objetos diferentes/1920X1080/'

list_image_path = []
list_image_path.extend(glob.glob(ubicacion+'*_full_S.txt'))

for i in list_image_path:
    fic = open(i, "r")
    (nuevoObj, width, height, datos) = get_np_array_from_lines_nueva(fic.readlines(), True, 240, 320)
    fic.close()

    v = pptk.viewer(nuevoObj)
    v.set(point_size=0.0001)

    # fic = open(i, "w")
    # fic.write('320x240\n')
    # for j in nuevoObj:
    #     fic.write(str(j[0]) + ',' + str(j[1]) + ',' + str(j[2]) + '\n')
    # fic.close()

# ================================================================================
# file_open_vert = ubicacion +'out01-05-2021-13-40-40_3.2-46.7_full_S.txt'
# fic = open(file_open_vert, "r")

# (nuevoObj, width, height, datos) = get_np_array_from_lines_nueva(fic.readlines(), True, 240, 320)
# fic.close()

# v = pptk.viewer(nuevoObj)
# v.set(point_size=0.0001)

# fic = open(file_open_vert, "w")
# fic.write('320x240\n')
# for j in nuevoObj:
#     fic.write(str(j[0]) + ',' + str(j[1]) + ',' + str(j[2]) + '\n')
# fic.close()
