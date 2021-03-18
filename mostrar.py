import numpy as np
import pptk #visualizador 3D
from open3d import *
import cv2

# 240x180
def get_np_array_from_lines( lines, is_verts, width = 240, height = 180, roi = []):
    datos = []
    cont = 0
    for line in lines:
        if cont == 0:
            cont += 1
        else:
            data = line.strip()
            datos.append(data)
    objetivo = np.array(datos).reshape(int(height), int(width))
    listObjetivo = []
    #219,70 -   403,205
    #216, 1 -   398,82
    #175, 34 -  277, 273
    # for fila in objetivo[int((roi[1]+60)/2):int((roi[3]-25)/2), int((roi[0]+4)/2):int((roi[2]-20)/2)]:
    for fila in objetivo:
    # for fila in objetivo:
        for i in fila:
            list_temp = i.split(',')
            z = float(list_temp[2])
            # if z > 0.3 and z < 0.7:
                # print(float(list_temp[0]), float(list_temp[1]), z)
            listObjetivo.append([float(list_temp[0]), float(list_temp[1]), z])
    return (np.array(listObjetivo), int(width), int(height), np.array(datos))

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
            # if z > 0.3 and z < 0.7:
                # print(float(list_temp[0]), float(list_temp[1]), z)
            datos.append([float(list_temp[0]), float(list_temp[1]), z])
    return (np.array(datos), int(width), int(height), np.array(datos))

def get_np_array_from_lines_color( lines, is_verts, width = 240, height = 180, roi = []):
    datos = []
    cont = 0
    for line in lines:
        if cont == 0:
            cont += 1
        else:
            data = line.strip()
            list_temp = data.split(',')
            datos.append([int(list_temp[2])/255, int(list_temp[1])/255, int(list_temp[0])/255])
    return (np.array(datos), int(width), int(height), np.array(datos))

ubicacion = 'C:/Users/steven/Documents/Git/Investigacion/Capturas/Nueva/Sin sistema de sujecion/'
file_open_vert = ubicacion +'out15-03-2021-15-10-13_40-22_full_S_PtoP.txt'
fic = open(file_open_vert, "r")

# [175, 38, 274, 267]
# out07-03-2021-15-51-46_4-17_third_M1

# (nuevoObj, width, height, datos) = get_np_array_from_lines(fic.readlines(), True, 240, 180, [120, 40, 245, 278])
(nuevoObj, width, height, datos) = get_np_array_from_lines_nueva(fic.readlines(), True, 240, 180, [120, 40, 245, 278])
fic.close()

#=====================================================
# file_open_jpg = "C:/Users/Angel Sappa/Documents/Capturas/D435i/NewMultiple/"+"out07-03-2021-15-52-28_4-17_third_M4_2D.jpg"
# v_img = cv2.imread(file_open_jpg)

# pcd = PointCloud()
# # open3d.geometry.crop_point_cloud(input, min_bound, max_bound)
# pcd.points = Vector3dVector(nuevoObj)
# print(type(v_img))
# color_interest = v_img[int((40)/2):int((278)/2), int((120)/2):int((245)/2)].reshape(-1,3)
# pcd.colors = Vector3dVector(color_interest)
# # print(pcd)
# # pcd = geometry.crop_point_cloud(pcd, np.array([0,0,0]), np.array([403,205,1]))
# draw_geometries([pcd])
#=====================================================

# downpcd = voxel_down_sample(pcd, voxel_size = 0.005)
# draw_geometries([downpcd])

file_open_vert = ubicacion +'out15-03-2021-15-10-13_40-22_full_S_colorPtoP.txt'
fic = open(file_open_vert, "r")
(nuevoObj_col, width, height, datos_2) = get_np_array_from_lines_color(fic.readlines(), True, 240, 180, [120, 40, 245, 278])
fic.close()

# nueva = np.asarray(v_img)
# print(type(nueva))
# rgb = pptk.rand((240*180), 3)
# print(type(rgb))
# v = pptk.viewer(nuevoObj, rgb)
v = pptk.viewer(nuevoObj, nuevoObj_col)
v.set(point_size=0.0001)
