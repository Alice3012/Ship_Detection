%function [] = HeatMP(x)
x='C:\Users\79266\Desktop\диплом\Программа\sled22 Маска 10 шаг 1 26 3.csv'
df = csvread(x);
%load patients

h = heatmap(transpose(df), 'Colormap', parula, 'GridVisible','off')
%grid off;
%set(gca,'visible','off');
%filenm = 
%saveas(h, x);