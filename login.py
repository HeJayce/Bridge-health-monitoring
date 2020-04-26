# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox
import pickle
import Features1
import Features2
#窗口
window=tk.Tk()
window.title('欢迎进入桥梁健康检测系统')
window.geometry('450x300')
#标签 用户名密码
tk.Label(window,text='用户名:').place(x=100,y=150)
tk.Label(window,text='密码:').place(x=100,y=190)
#用户名输入框
var_usr_name=tk.StringVar()
entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)
#密码输入框
var_usr_pwd=tk.StringVar()
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=190)
 
#登录函数
def usr_log_in():
    #输入框获取用户名密码
    usr_name=var_usr_name.get()
    usr_pwd=var_usr_pwd.get()
    #从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle','rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle','wb') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    #判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            '''
            tk.messagebox.showinfo(title='welcome',
                                   message='欢迎您：'+usr_name)
                                   '''
            usr_sign_quit()
            face()
            
        else:
            tk.messagebox.showerror(message='密码错误')
    #用户名密码不能为空
    elif usr_name=='' or usr_pwd=='' :
        tk.messagebox.showerror(message='用户名或密码为空')
    #不在数据库中弹出是否注册的框
    else:
        is_signup=tk.messagebox.askyesno('欢迎','您还没有注册，是否现在注册')
        if is_signup:
            usr_sign_up()
#注册函数
def usr_sign_up():
    #确认注册时的相应函数
    def signtowcg():
        nn=new_name.get()
        np=new_pwd.get()
        npf=new_pwd_confirm.get()
        try:
            with open('usr_info.pickle','rb') as usr_file:
                exist_usr_info=pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info={}                      
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误','用户名已存在')
        elif np =='' or nn=='':
            tk.messagebox.showerror('错误','用户名或密码为空')
        elif np !=npf:
            tk.messagebox.showerror('错误','密码前后不一致')
        else:
            exist_usr_info[nn]=np
            with open('usr_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo('欢迎','注册成功')
            #注册成功关闭注册框
            window_sign_up.destroy()
    #新建注册界面
    window_sign_up=tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    #用户名变量及标签、输入框
    new_name=tk.StringVar()
    tk.Label(window_sign_up,text='用户名：').place(x=10,y=10)
    tk.Entry(window_sign_up,textvariable=new_name).place(x=150,y=10)
    #密码变量及标签、输入框
    new_pwd=tk.StringVar()
    tk.Label(window_sign_up,text='请输入密码：').place(x=10,y=50)
    tk.Entry(window_sign_up,textvariable=new_pwd,show='*').place(x=150,y=50)    
    #重复密码变量及标签、输入框
    new_pwd_confirm=tk.StringVar()
    tk.Label(window_sign_up,text='请再次输入密码：').place(x=10,y=90)
    tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*').place(x=150,y=90)    
    #确认注册按钮及位置
    bt_confirm_sign_up=tk.Button(window_sign_up,text='确认注册',
                                 command=signtowcg)
    bt_confirm_sign_up.place(x=150,y=130)
#退出的函数
def usr_sign_quit():
    window.destroy()



def face():
    window=tk.Tk()
    window.title('桥梁监测信息关联分析可视化系统')
    window.geometry('800x470')
    bt_login=tk.Button(window,text='数据可视化（周期估算）',command=Features1.features1)
    bt_login.place(x=350,y=180)
    bt_logup=tk.Button(window,text='选择互相关（相关系数）',command=Features2.features2)
    bt_logup.place(x=350,y=230)
    #主循环
    window.mainloop()


#登录 注册按钮
bt_login=tk.Button(window,text='登录',command=usr_log_in)
bt_login.place(x=140,y=230)
bt_logup=tk.Button(window,text='注册',command=usr_sign_up)
bt_logup.place(x=210,y=230)
bt_logquit=tk.Button(window,text='退出',command=usr_sign_quit)
bt_logquit.place(x=280,y=230)
#主循环
window.mainloop()