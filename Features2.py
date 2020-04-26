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

def features2():
    data = xlrd.open_workbook(r'data.xls')
    sh1= data.sheet_by_name('温度')
    sh= data.sheet_by_name('挠度')
    sh2= data.sheet_by_name('应变')
    root2 = Tk()
    root2.title("数据可视化")
    root2.geometry("600x700")
    f = Figure(figsize=(2.52, 2.56), dpi=100)#figsize定义图像大小，dpi定义像素
    f_plot1 = f.add_subplot(111)#定义画布中的位置
    canvs1 = FigureCanvasTkAgg(f, root2)#f是定义的图像，root是tkinter中画布的定义位置
    canvs1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    def draw_D_T():
        f_plot1.clear()
        d1 = ord(user_text.get())
        if d1>82:
            str1 = messagebox.showinfo(title='提示',message = '输入范围错误，请重新输入')
            if str1 == 'ok':
                return
        test_VD1 = d1-65
        if test_VD1<18:
            col_test_VD1 = sh.col_values(test_VD1)
            s_test=pd.Series(col_test_VD1[1:])
            corr_nm1 = []
            open('D_T.txt', 'w').close()
            for j in range(1,12):
                col3 = sh1.col_values(j) 
                s3=pd.Series(col3[1:])
                corr_test=s_test.corr(s3) 
                if corr_test<0:
                    corr_nm1.append(-corr_test)
                else :
                    corr_nm1.append(corr_test)
                if chVarDis.get()==1:
                    result2txt=str('位移'+str(user_text.get())  +'测点&温度'+str(j) +'测点的相关系数:'+str(corr_nm1[j-1]))          # data是前面运行出的数据，先将其转为字符串才能写入
                    with open('D_T.txt','a',encoding='utf8') as file_handle:   # .txt可以不自己新建,代码会自动新建
                        file_handle.write(result2txt)     # 写入
                        file_handle.write('\n')         # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
                    if j==11:
                        subprocess.Popen("D_T.txt")
            f_plot1.set(title='Displacement&temprature',xlabel='Displacement&temperature',ylabel='corr_num')
            f_plot1.bar(x= [1,2,3,4,5,6,7,8,9,10,11],height = corr_nm1,width = (0.5),)
            canvs1.draw()

    def draw_D_Y():
        f_plot1.clear()
        d2 = ord(user_text1.get())
        if d2>77:
            str1 = messagebox.showinfo(title='提示',message = '输入范围错误，请重新输入')
            if str1 == 'ok':
                return
        test_VD2 = d2-65
        if test_VD2<18:
            col_test_VD2 = sh.col_values(test_VD2)
            s_test1=pd.Series(col_test_VD2[1:])
            corr_nm2 = []
            X=[]
            open('D_Y.txt', 'w').close()
            for i in range(0,44):
                X.insert(i,i)
                col_y = sh2.col_values(i) 
                s_y=pd.Series(col_y[1:])
                corr_test1=s_test1.corr(s_y) 
                if corr_test1<0:
                    corr_nm2.append(-corr_test1)
                else :
                    corr_nm2.append(corr_test1)
                if chvarUn.get()==1:
                    result2txt=str('位移'+str(user_text1.get())  +'测点&应变'+str(i+1) +'测点的相关系数:'+str(corr_nm2[i]))          # data是前面运行出的数据，先将其转为字符串才能写入
                    with open('D_Y.txt','a',encoding='utf8') as file_handle:   # .txt可以不自己新建,代码会自动新建
                        file_handle.write(result2txt)     # 写入
                        file_handle.write('\n')         # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
                    if i==43:
                        subprocess.Popen("D_S.txt")
            f_plot1.set(title='Displacement&strain',xlabel='Displacement&Strain',ylabel='corr_num')
            f_plot1.bar(x=X,height=corr_nm2,width=0.5,)
            canvs1.draw()

    def draw_Y_T():
        f_plot1.clear()
        if user_text2.get().isdigit():
            test_YB1 = int(user_text2.get())-1
        else :
            messagebox.showinfo(title='提示',message = '输入的测试点超出范围，请重新输入！')
        if test_YB1 < 44 and test_YB1 >=0:
            col_test_YB1 = sh2.col_values(test_YB1)
            s_test2=pd.Series(col_test_YB1[1:])
            corr_nm3 = []
            X=[]
            open('S_T.txt', 'w').close()
            for k in range(1,12):
                X.insert(k-1,k-1)
                col_yt = sh.col_values(k) 
                s_yt=pd.Series(col_yt[1:])
                corr_test2=s_test2.corr(s_yt) 
                if corr_test2<0:
                    corr_nm3.append(-corr_test2)
                else :
                    corr_nm3.append(corr_test2)
                if chvarEn.get()==1:
                    result2txt=str('应变'+str(user_text2.get())  +'测点&温度'+str(k) +'测点的相关系数:'+str(corr_nm3[k-1]))          # data是前面运行出的数据，先将其转为字符串才能写入
                    with open('S_T.txt','a',encoding='utf8') as file_handle:   # .txt可以不自己新建,代码会自动新建
                        file_handle.write(result2txt)     # 写入
                        file_handle.write('\n')         # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
                    if k==11:
                        subprocess.Popen("Data_show.txt")
            f_plot1.set(title='Strain&Temprature',                                    xlabel='Strain&temperature',ylabel='corr_num')
            f_plot1.bar(x=X,height=corr_nm3,width=0.5,)             
            canvs1.draw()
        else:
            str1 = messagebox.showinfo(title='提示',message = '输入范围错误，请重新输入')
            if str1 == 'ok':
                return






    
    Label(root2,text="*位移点A-R,温度点A-M,应变点1-44*",font=50).pack()
    Label(root2,text="选择温度",font=20).pack()
    user_text=Entry(root2)
    user_text.pack()
    # 复选框
    chVarDis =IntVar(root2)   # 用来获取复选框是否被勾选，通过chVarDis.get()来获取其的状态,其状态值为int类型 勾选为1  未勾选为0
    check1 = Checkbutton(root2, text="在TXT中显示具体相关系数", variable=chVarDis)    # text为该复选框后面显示的名称, variable将该复选框的状态赋值给一个变量，当state='disabled'时，该复选框为灰色，不能点的状态
    check1.deselect()     # 该复选框是否勾选,select为勾选, deselect为不勾选
    check1.pack()
    #check1.grid(column=0, row=4, sticky=W)       # sticky=tk.W  当该列中其他行或该行中的其他列的某一个功能拉长这列的宽度或高度时，设定该值可以保证本行保持左对齐，N：北/上对齐  S：南/下对齐  W：西/左对齐  E：东/右对齐
    Button(root2, text='选择测试点', command=draw_D_T).pack()
    Label(root2,text="选择位移",font=20).pack()
    user_text1=Entry(root2)
    user_text1.pack()
    chvarUn =IntVar(root2)
    check2 =Checkbutton(root2, text="在TXT中显示具体相关系数", variable=chvarUn)
    check2.deselect()
    check2.pack()
    #check2.grid(column=1, row=4, sticky=W)
    Button(root2,text='选择测试点',command=draw_D_Y).pack()
    Label(root2,text="选择应变",font=20).pack()
    user_text2=Entry(root2)
    user_text2.pack()
    chvarEn =IntVar(root2)
    #check3.grid(column=2, row=4, sticky=W)
    check3 =Checkbutton(root2, text="在TXT中显示具体相关系数", variable=chvarEn)
    check3.deselect() 
    check3.pack()
    Button(root2, text='选择测试点',command=draw_Y_T).pack()
    root2.mainloop()

    