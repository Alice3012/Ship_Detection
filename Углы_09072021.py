import numpy as np
from PIL import Image
#import pyautogui as pag
import pandas as pd
import time
#import os
import seaborn as sns
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
#import cv2
import PySimpleGUI as sg
import warnings
warnings.filterwarnings("ignore")
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def data_gen():
    fig1=plt.figure(dpi=125)
    x = np.round(10*np.random.random(20),3)
    y = np.round(10 * np.random.random(20), 3)
    p1 = plt.scatter(x,y,edgecolor='k')
    plt.ylabel('Y-Values')
    plt.xlabel('X-Values')
    plt.title('Scatter plot')
    figure_x,figure_y,figure_w,figure_h=fig1.bbox.bounds
    return (x,y,fig1,figure_x,figure_y,figure_w,figure_h)


def draw_figure(figure):
    figure_canvas_agg=FigureCanvasTkAgg(figure)
    figure_canvas_agg.draw()
    return figure_canvas_agg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Название фотографии: '), sg.InputText(), sg.FileBrowse()], #0 1 2
            [sg.Text('Размер маски'),sg.InputText()],# 3
            [sg.Text('Шаг'),sg.InputText()], # 4
            [sg.Text('Введите углы. Вводить можно либо сам угол (26, например), либо угол + 180 (26+180), либо сразу сумму (206). Примеры: alpha  26, beta 0; alpha 26+180, beta 26; alpha=206, beta= 26') ],
            [sg.Text('Первый угол '), sg.InputText()],#5
            [sg.Text('Второй угол  '), sg.InputText()],#6
            [sg.Text('Цвет RGB '), sg.Checkbox('Red'),sg.Checkbox('Green'),sg.Checkbox('Blue')], # 7 8 9
            [sg.Output(size=(150, 20))],
            [sg.Button('Ok'), sg.Button('Cancel')] ,
            [sg.Button('Generate',enable_events=True,key='-GENERATE-',font='Helvetica 16')],
            [sg.Canvas(size=(50,50),key='-CANVAS-',pad=(20,20))]]

# Create the Window
window = sg.Window('Diplom', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Ok':
        if values[0]:
            nnn=0
            try:
                path='/Users/79266/Desktop/Diplom/'
                image = Image.open(values[0])
                imr=np.asarray(image)
                width=len(imr[0])
                height=len(imr)
                print(f'Ширина: {width}, высота: {height}')
            except:
                print('Введено некорректное название')
                nnn=nnn+1
            try:
                k=int(values[1])
            except:
                print('Не выбран размер маски')
                nnn=nnn+1
            try:
                step = int(values[2])
            except:
                print('Не выбран шаг')
                nnn=nnn+1
            if values[3] in ('0','180','26','26+180','45','45+180','64','64+180','90','90+180','116','116+180'
                             ,'135','135+180','154','154+180','206','334','296','270','244','225','315','18'
                             ,'198','18+180','34','34+180','214','56','56+180','236'
                             ,'72','72+180','252','14','14+180','194'
                             ,'37','37+180','217','53','53+180','233'
                             ,'76','76+180','256'):
                alpha = values[3]
            else:
                print('Выбран некорректный угол alpha')
                nnn=nnn+1
            if values[4] in ('0','180','26','26+180','45','45+180','64','64+180','90','90+180','116','116+180'
                             ,'135','135+180','154','154+180','206','334','296','270','244','225','315','18'
                             ,'198','18+180','34','34+180','214','56','56+180','236'
                             , '72', '72+180','252','14','14+180','194'
                             ,'37','37+180','217','53','53+180','233'
                             ,'76','76+180','256'):
                beta = values[4]
            else:
                print('Выбран некорректный угол beta')
                nnn=nnn+1
            try:
                if values[5]==True:
                    color=1
                if values[6]==True:
                    color=2
                if values[7]==True:
                    color=3
            except:
                print('Не выбран цвет')
                nnn=nnn+1
            if nnn==0:
                pix = image.load()
                # start_time=time.time()
                q = np.ones((round((height - k) / step), round((width - k) / step)))
                n=0

                def quety(alpha, i_k, j_k, k):
                    delta = []
                    if str.replace(alpha, ' ', '') == '0':
                        delta = [pix[i + 1, j][color - 1] - pix[i, j][color - 1] for i in range(i_k, k + i_k - 1) for j in
                                 range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '180':
                        delta = [pix[i - 1, j][color - 1] - pix[i, j][color - 1] for i in range(i_k, k + i_k - 1) for j in
                                 range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '26':
                        delta = [(pix[i - 2, j + 1][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '206') | (str.replace(alpha, ' ', '') == '26+180'):
                        delta = [(pix[i + 2, j - 1][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '154':
                        delta = [(pix[i + 2, j + 1][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '154+180') | (str.replace(alpha, ' ', '') == '334'):
                        delta = [(pix[i - 2, j - 1][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '116':
                        delta = [(pix[i + 1, j + 2][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '116+180') | (str.replace(alpha, ' ', '') == '296'):
                        delta = [(pix[i - 1, j - 2][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '90':
                        delta = [pix[i, j + 1][color - 1] - pix[i, j][color - 1] for i in range(i_k, k + i_k - 1) for j in
                                 range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '90+180') | (str.replace(alpha, ' ', '') == '270'):
                        delta = [pix[i, j - 1][color - 1] - pix[i, j][color - 1] for i in range(i_k, k + i_k - 1) for j in
                                 range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '64':
                        delta = [(pix[i - 1, j + 2][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '64+180') | (str.replace(alpha, ' ', '') == '244'):
                        delta = [(pix[i + 1, j - 2][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '45':
                        delta = [(pix[i - 1, j + 1][color - 1] - pix[i, j][color - 1]) / (2 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '45+180') | (str.replace(alpha, ' ', '') == '225'):
                        delta = [(pix[i + 1, j - 1][color - 1] - pix[i, j][color - 1]) / (2 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '135':
                        delta = [(pix[i + 1, j + 1][color - 1] - pix[i, j][color - 1]) / (2 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '135+180') | (str.replace(alpha, ' ', '') == '315'):
                        delta_minus = [(pix[i - 1, j - 1][color - 1] - pix[i, j][color - 1]) / (2 ** 0.5) for i in
                                       range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '18':
                        delta = [(pix[i + 3, j - 1][color - 1] - pix[i, j][color - 1]) / (10 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '18+180') | (str.replace(alpha, ' ', '') == '198'):
                        delta = [(pix[i - 3, j + 1][color - 1] - pix[i, j][color - 1]) / (10 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for  j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '34':
                        delta = [(pix[i + 3, j + 2][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '34+180') | (str.replace(alpha, ' ', '') == '214'):
                        delta = [(pix[i - 3, j - 2][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '56':
                        delta = [(pix[i + 2, j + 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '56+180') | (str.replace(alpha, ' ', '') == '236'):
                        delta = [(pix[i - 2, j - 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '72':
                        delta = [(pix[i + 1, j + 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '72+180') | (str.replace(alpha, ' ', '') == '252'):
                        delta = [(pix[i - 1, j - 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '14':
                        delta = [(pix[i + 1, j + 4][color - 1] - pix[i, j][color - 1]) / (17 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '14+180') | (str.replace(alpha, ' ', '') == '194'):
                        delta = [(pix[i - 1, j - 4][color - 1] - pix[i, j][color - 1]) / (17 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '37':
                        delta = [(pix[i + 3, j + 4][color - 1] - pix[i, j][color - 1]) / (25 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '37+180') | (str.replace(alpha, ' ', '') == '217'):
                        delta = [(pix[i - 3, j - 4][color - 1] - pix[i, j][color - 1]) / (25 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '53':
                        delta = [(pix[i + 4, j + 3][color - 1] - pix[i, j][color - 1]) / (25 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '53+180') | (str.replace(alpha, ' ', '') == '233'):
                        delta = [(pix[i - 4, j - 3][color - 1] - pix[i, j][color - 1]) / (25 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                    elif str.replace(alpha, ' ', '') == '76':
                        delta = [(pix[i + 4, j + 1][color - 1] - pix[i, j][color - 1]) / (17 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                    elif (str.replace(alpha, ' ', '') == '76+180') | (str.replace(alpha, ' ', '') == '256'):
                        delta = [(pix[i - 4, j - 1][color - 1] - pix[i, j][color - 1]) / (17 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                    return delta


                for i_k in range(4, width - k-4, step):
                    for j_k in range(4, height - k-4, step):
                        delta_plus = quety(alpha, i_k, j_k, k)
                        #print([x for x in delta_plus])
                        delta_minus = quety(beta, i_k, j_k, k)
                        q_0 = np.array(pearsonr(delta_plus, delta_minus))
                        if pd.notnull(q_0[0]):
                            q[math.floor(j_k / step)-3, math.floor(i_k / step)-3] = q_0[0]
                        n = n + 1  # количество итераций
                plt.figure(figsize=(16, 9))
                swim = sns.heatmap(q, cmap='viridis', cbar=True)
                fig = swim.get_figure()
                name_0=values[0].split('/')
                name=name_0[len(name_0)-1]
                str_res='Маска '+str(k)+' шаг '+str(step) + ' ' + alpha + ' ' + beta + ' '+ str(color) +' '+ name
                #path=''
                #for elem in range(0,len(name)-3):
                 #   path=path+name_0[elem]+'/'
                #path=path+name_0[len(name_0)-2]
                try:
                    fig.savefig(str_res)
                    print('Результат сохранен в папке с программой под названием: ', str_res)
                except:
                    print('Не удалось сохранить файл')
                print(f'Количество итераций: {n}')
                print(f'Можете продолжать работу, изменив некоторые параметры в полях.')
                print()
                print()
        else:
            print('Некорректные данные для продолжения')
fig.show()
#window.close()