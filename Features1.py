import matplotlib
import subprocess
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import xlrd
import tkinter.messagebox as messagebox
import pandas as pd
import numpy as np

def features1():
    data = xlrd.open_workbook(r'data.xls')
    sh1= data.sheet_by_name('温度')
    sh= data.sheet_by_name('挠度')
    sh2= data.sheet_by_name('应变')
    root2 = Tk()
    root2.title("数据可视化")
    root2.geometry("500x800")
    f = Figure(figsize=(2.52, 2.56), dpi=100)#figsize定义图像大小，dpi定义像素
    f_plot = f.add_subplot(111)#定义画布中的位置
    canvs = FigureCanvasTkAgg(f, root2)#f是定义的图像，root是tkinter中画布的定义位置
    canvs.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def draw_T():  
            f_plot.clear()
            t =ord(user_text.get()) #用字母表示时
            if t>77:
                str1 = messagebox.showinfo(title='提示',message = '输入范围错误，请重新输入')
                if str1 == 'ok':
                    return
            test_TEM = t-65
            if test_TEM<13:
                col_test_TEM = sh1.col_values(test_TEM)
                x=np.arange(0,1078,1)
                y=np.array(col_test_TEM[1:])                               
                f_plot.set(title='temprature_GUI',xlabel='time/10min',ylabel='Temprature')
                f_plot.plot(x,y)                                                                
                canvs.draw() 
        
    def draw_D() :
        f_plot.clear()
        d =ord(user_text1.get())#用字母表示时
        if d>82:
            str1 = messagebox.showinfo(title='提示',message = '输入范围错误，请重新输入')
            if str1 == 'ok':
                return
        test_VD = d-65
        if test_VD<18:
            col_test_VD = sh.col_values(test_VD)
            x=np.arange(0,1078,1)
            y=np.array(col_test_VD[1:])
            f_plot.set(title='Displacement_GUI',xlabel='time/10min',ylabel='Displacement')
            f_plot.plot(x,y)
            canvs.draw()

    def draw_Y():
        f_plot.clear()
        #y = ord(var.get())  #用字母表示时
        if user_text2.get().isdigit():
            test_YB = int(user_text2.get())-1
        else :
            messagebox.showinfo(title='提示',message = '输入的测试点超出范围，请重新输入！')
        if test_YB<44 and test_YB>=0:
            col_test_YB = sh2.col_values(test_YB)
            x=np.arange(0,1078,1)
            y=np.array(col_test_YB[1:])
            f_plot.set(title='Strain_GUI',xlabel='time/10min',ylabel='Strain')
            f_plot.plot(x,y)
            canvs.draw()
        else:
            str1 = messagebox.showinfo(title='提示',message = '输入范围错误，请重新输入')
            if str1 == 'ok':
                return

    Label(root2,text="*位移点A-R,温度点A-M,应变点1-44*",font=50).pack()

    Label(root2,text="选择位移",font=20).pack()
    user_text1=Entry(root2)
    user_text1.pack()
    Button(root2,text='选择测试点',command=draw_D).pack()

    Label(root2,text="选择应变",font=20).pack()
    user_text2=Entry(root2)
    user_text2.pack()
    Button(root2, text='选择测试点',command=draw_Y).pack()

    Label(root2,text="选择温度",font=20).pack()
    user_text=Entry(root2)
    user_text.pack()
    Button(root2, text='选择测试点', command=draw_T).pack()

    root2.mainloop()
   