import numpy as np
from PIL import Image
#import pyautogui as pag
import pandas as pd
import time
import os
import seaborn as sns
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import cv2
import PySimpleGUI as sg
import warnings
warnings.filterwarnings("ignore")
import math


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Название фотографии: '), sg.InputText(), sg.FileBrowse()], #0
            [sg.Text('Размер маски'),sg.InputText()],# 1
            [sg.Text('Шаг'),sg.InputText()], # 2
            [sg.Text('Цвет RGB '), sg.Checkbox('Red'),sg.Checkbox('Green'),sg.Checkbox('Blue')], # 3,4,5
            [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Diplom', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Ok' and values[0]:
        nnn=0
        try:
            #path='/Users/79266/Desktop/Diplom/'
            image = Image.open(values[0])
            imr=np.asarray(image)
            width=len(imr[0])
            height=len(imr)
            name=os.path.basename(values[0])
            path=values[0].replace(name,'')
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
        try:
            if values[3]==True:
                color=1
            if values[4]==True:
                color=2
            if values[5]==True:
                color=3
        except:
            print('Не выбран цвет')
            nnn=nnn+1
        if nnn==0:
            pix = image.load()
            # start_time=time.time()

            def program(alpha, width, height, step,color):
                def quety(alpha, i_k, j_k, k,color):
                    delta_plus=[]
                    delta_minus=[]
                    if str.replace(alpha, ' ', '') == '0':
                        delta_plus = [pix[i + 1, j][color - 1] - pix[i, j][color - 1] for i in range(i_k, k + i_k - 1)
                                      for j in range(j_k, k + j_k - 1)]
                        delta_minus = [pix[i - 1, j][color - 1] - pix[i, j][color - 1] for i in range(i_k, k + i_k - 1)
                                      for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '26':
                        delta_plus = [(pix[i + 2, j - 1][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i - 2, j + 1][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '45':
                        delta_plus = [(pix[i + 1, j - 1][color - 1] - pix[i, j][color - 1]) / (2 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i - 1, j + 1][color - 1] - pix[i, j][color - 1]) / (2 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '64':
                        delta_plus = [(pix[i + 1, j - 2][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i - 1, j + 2][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '90':
                        delta_plus = [pix[i, j - 1][color - 1] - pix[i, j][color - 1] for i in range(i_k, k + i_k - 1)
                                      for j in range(j_k, k + j_k - 1)]
                        delta_minus = [pix[i, j + 1][color - 1] - pix[i, j][color - 1] for i in range(i_k, k + i_k - 1)
                                      for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '116':
                        delta_plus = [(pix[i - 1, j - 2][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i + 1, j + 2][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '135':
                        delta_plus = [(pix[i - 1, j - 1][color - 1] - pix[i, j][color - 1]) / (2 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i + 1, j + 1][color - 1] - pix[i, j][color - 1]) / (2 ** 0.5) for i in
                                       range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '154':
                        delta_plus = [(pix[i - 2, j - 1][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1)
                                      for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i + 2, j + 1][color - 1] - pix[i, j][color - 1]) / (5 ** 0.5) for i in range(i_k, k + i_k - 1)
                                      for j in range(j_k, k + j_k - 1)]

                    '''
                        углы на клетках 3х3
                    '''

                    if str.replace(alpha, ' ', '') == '18':
                        delta_plus = [(pix[i + 3, j - 1][color - 1] - pix[i, j][color - 1]) / (10 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i - 3, j + 1][color - 1] - pix[i, j][color - 1]) / (10 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '34':
                        delta_plus = [(pix[i + 3, j - 2][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i - 3, j + 2][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '56':
                        delta_plus = [(pix[i + 2, j - 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i - 2, j + 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '72':
                        delta_plus = [(pix[i + 1, j - 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i - 1, j + 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '108':
                        delta_plus = [(pix[i - 1, j - 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i + 1, j + 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '124':
                        delta_plus = [(pix[i - 2, j - 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i + 2, j + 3][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '146':
                        delta_plus = [(pix[i - 3, j - 2][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i + 3, j + 2][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '162':
                        delta_plus = [(pix[i - 3, j - 1][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i + 3, j + 1][color - 1] - pix[i, j][color - 1]) / (13 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    '''
                        углы на клетках 4х4
                    '''
                    if str.replace(alpha, ' ', '') == '14':
                        delta_plus = [(pix[i + 1, j - 4][color - 1] - pix[i, j][color - 1]) / (17 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i - 1, j + 4][color - 1] - pix[i, j][color - 1]) / (17 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '37':
                        delta_plus = [(pix[i + 3, j - 4][color - 1] - pix[i, j][color - 1]) / (25 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i - 3, j + 4][color - 1] - pix[i, j][color - 1]) / (25 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '53':
                        delta_plus = [(pix[i + 4, j - 3][color - 1] - pix[i, j][color - 1]) / (25 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i - 4, j + 3][color - 1] - pix[i, j][color - 1]) / (25 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '76':
                        delta_plus = [(pix[i + 4, j - 1][color - 1] - pix[i, j][color - 1]) / (17 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i - 4, j + 1][color - 1] - pix[i, j][color - 1]) / (17 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]

                    if str.replace(alpha, ' ', '') == '-45': # 0 -45
                        delta_plus = [(pix[i + 1, j][color - 1] - pix[i, j][color - 1]) / (17 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for
                                 j in range(j_k, k + j_k - 1)]
                        delta_minus = [(pix[i + 1, j + 1][color - 1] - pix[i, j][color - 1]) / (17 ** 0.5) for i in
                                 range(i_k, k + i_k - 1) for j in range(j_k, k + j_k - 1)]
                    return delta_plus, delta_minus

                #q = np.zeros((round((height - k) / step), round((width - k) / step)))
                q=[]
                i_n=0
                for i_k in range(4, width - k -4, step):
                    j_n=0
                    for j_k in range(4, height - k -4 , step):
                        #delta_plus, delta_minus = quety(alpha, i_k, j_k, k,1)
                        #q_0 = np.array(pearsonr(delta_plus, delta_minus))
                        #delta_plus, delta_minus = quety(alpha, i_k, j_k, k,2)
                        #q_1 = np.array(pearsonr(delta_plus, delta_minus))
                        delta_plus, delta_minus = quety(alpha, i_k, j_k, k, color)
                        q_2 = np.array(pearsonr(delta_plus, delta_minus))

                        def nvl(a):
                            if pd.isnull(a):
                                return 0
                            else:
                                return a

                        q.append([nvl(q_2[0]),i_n, j_n])
                        j_n+=1
                    i_n+=1
                q = pd.DataFrame(q, columns=['Корреляция', 'x', 'y'])
                #q['y'] = np.array(q['y'])[::-1]
                #q['x'] = np.array(q['x'])[::-1]
                try:
                    matrix = np.zeros([np.array(q['x'])[-1] + 1, np.array(q['y'])[-1] + 1])
                    matrix[np.array(q['x'])[:], np.array(q['y'])[:]] = np.array(q['Корреляция'])[:]
                except:
                    print('Error')


                #swim_1 = sns.heatmap(matrix.transpose(), cmap='viridis', cbar=True, center=0,cmap=sns.diverging_palette(20, 220, n=200), square=True)

               # my_colors = ['navy', 'blue', 'yellow', 'powderblue', 'skyblue', 'skyblue', 'powderblue', 'yellow', 'blue', 'navy']
                my_colors = ['midnightblue','navy', 'mediumblue','royalblue','dodgerblue', 'skyblue', 'springgreen', 'aquamarine', 'yellow','aquamarine', 'springgreen', 'skyblue',
                             'dodgerblue', 'royalblue','mediumblue','navy','midnightblue']

                fig,ax = plt.subplots(1,1)
                #swim_1 = \
                sns.heatmap(matrix.transpose(),
                                     #center=-0.2,
                                     cmap=my_colors
                                     ,square=True, ax=ax)
                colorbar = ax.collections[0].colorbar
                M_max=matrix.max()
                M_min = matrix.min()
                M = abs(M_max) + abs(M_min)
                #colorbar.set_ticks([1/5 * M, 2/5 * M, 3/5 * M, 4/5 * M, M])
                #colorbar.set_ticklabels([1/10 * M, 2/10 * M, 3/10 * M, 4/10 * M, 5/10 * M, 6/10 * M, 7/10 * M,  8/10 * M, 9/10 * M, M])

                #fig = swim_1.get_figure()
                name_0 = values[0].split('/')
                name = name_0[len(name_0) - 1].replace('.jpg','').replace('.png','')
                str_res = name+ ' Маска ' + str(k) + ' шаг ' + str(step) + ' ' + alpha + ' ' + str(color) + '.jpg'
                #print(str_res)
                #print(path)
                try:

                    fig.savefig(path+str_res, dpi=300)
                    #cv2.imwrite(os.path.join(path,str_res),swim_1)
                    #cv2.waitKey(0)
                    pd.DataFrame(matrix).to_csv(str_res.replace('.jpg','')+'.csv', index = False
                                                , header = False)
                    print('Результат сохранен: ', str_res)
                except:
                    print('Не удалось сохранить файл')


            #program('-45', width, height, step, color)

            program('0', width, height, step, color)
            program('26',width,height,step,color)
            program('45', width, height, step, color)
            program('64', width, height, step, color)
            program('90', width, height, step, color)
            program('116', width, height, step, color)
            program('135', width, height, step, color)
            program('154', width, height, step, color)

            #program('18', width, height, step, color)
            #program('34', width, height, step, color)
            #program('56', width, height, step, color)
            #program('72', width, height, step, color)
            #program('108', width, height, step, color)
            #program('124', width, height, step, color)
            #program('146', width, height, step, color)
            #program('162', width, height, step, color)
            #program('14', width, height, step, color)
            #program('37', width, height, step, color)
            #program('53', width, height, step, color)
            print('Complete')
        else:
            print('Некорректные данные для продолжения')
window.close()