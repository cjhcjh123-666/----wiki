# -*- coding: UTF-8 -*-
from tkinter import *
from PIL import Image, ImageTk
import pymysql
import tkinter.messagebox as tkm
from ComBoPicker import Combopicker
import pandas as pd
import pickle
import os
import re
global master,master2
master = Tk()
master.title('原神wiki数据库管理系统')
master.geometry('800x600')      # 不能有空格在800和x之间，适当设置分辨率利于设置滚动条
# 画布
canvas = Canvas(master, height=700, width=1000)
# 加载图片
im = Image.open("C:\\Users\\55151\\Desktop\\原神Wiki数据库课设\\UI\\原神.png")
image_file = ImageTk.PhotoImage(im)
# image_file = tk.PhotoImage(file='images/01.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')
# main = Frame(master)
# main.pack(expand=False, fill="both")
# COMBOPICKER1 = Combopicker(main, values=['CELL-S1', 'CELL-S2', 'CELL-S3', 'CELL-S4'])
# COMBOPICKER1.pack(anchor="w")
usr = StringVar()  # 用户名变量
pwd = StringVar()  # 密码变量
Label(master, text='用 户 名:').place(x=250,y=250)
Label(master, text='密     码:').place(x=250,y=300)
# 第一个输入框-用来输入用户名的。
# textvariable 获取文本框的内容
entry_usr_name = Entry(master, textvariable=usr)
entry_usr_name.place(x=300, y=250)
# 第二个输入框-用来输入密码的。
entry_usr_pwd = Entry(master, textvariable=pwd, show='*')
entry_usr_pwd.place(x=300, y=300)
def main():
    master.withdraw()
    master2 = Toplevel(master)
    master2.title('原神wiki数据库管理系统')
    master2.geometry('800x600')  # 不能有空格在800和x之间，适当设置分辨率利于设置滚动条
    # 画布
    canvas = Canvas(master2, height=700, width=1000)
    # 加载图片
    im = Image.open("C:\\Users\\55151\\Desktop\\原神Wiki数据库课设\\UI\\原神.png")
    image_file = ImageTk.PhotoImage(im)
    # image_file = tk.PhotoImage(file='images/01.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack(side='top')
    btn_login = Button(master2, text=' 角 色', command=lambda :juese())
    btn_login.place(x=0, y=0)  # 用place来处理按钮的位置信息。
    btn_sign_up = Button(master2, text=' 武 器 ', command=lambda:wuqi())
    btn_sign_up.place(x=250, y=0)
    btn_login = Button(master2, text=' 圣 遗 物 ', command=lambda:shengyiwu())
    btn_login.place(x=550, y=0)  # 用place来处理按钮的位置信息。
    btn_login = Button(master2, text=' 我 的 数 据', command=lambda: my())
    btn_login.place(x=250, y=200)  # 用place来处理按钮的位置信息。
    mainloop()
def my():
    my1 = Toplevel(master)
    my1.title('原神wiki数据库管理系统')
    my1.geometry('800x600')  # 不能有空格在800和x之间，适当设置分辨率利于设置滚动条
    btn_login = Button(my1, text=' 我 的 角 色', command=lambda: showmyjuese())
    btn_login.place(x=0, y=0)  # 用place来处理按钮的位置信息。
    btn_sign_up = Button(my1, text=' 我 的 武 器 ', command=lambda: showmywuqi())
    btn_sign_up.place(x=250, y=0)
    btn_login = Button(my1, text=' 我 的 圣 遗 物 ', command=lambda: showmyshengyiwu())
    btn_login.place(x=500, y=0)  # 用place来处理按钮的位置信息。
    lb1 = Listbox(my1)
    scr1 = Scrollbar(my1)
    lb1.config(yscrollcommand=scr1.set)
    scr1.config(command=lb1.yview)
    lb1.pack(fill=Y)
    lb1.place(x=0,y=50)
    scr1.pack(fill=Y)
    scr1.place(x=130,y=50)

    lb2 = Listbox(my1)
    scr2 = Scrollbar(my1)
    lb2.config(yscrollcommand=scr2.set)
    scr2.config(command=lb2.yview)
    lb2.pack(fill=Y)
    lb2.place(x=250, y=50)
    scr2.pack(fill=Y)
    scr2.place(x=380, y=50)

    lb3 = Listbox(my1)
    scr3 = Scrollbar(my1)
    lb3.config(yscrollcommand=scr3.set)
    scr3.config(command=lb3.yview)
    lb3.pack(fill=Y)
    lb3.place(x=500, y=50)
    scr3.pack(fill=Y)
    scr3.place(x=630, y=50)

    lb4 = Listbox(my1)
    scr4 = Scrollbar(my1)
    lb4.config(yscrollcommand=scr1.set)
    scr4.config(command=lb1.yview)
    lb4.pack(fill=Y)
    lb4.place(x=0, y=380)
    scr4.pack(fill=Y)
    scr4.place(x=130, y=380)

    lb5 = Listbox(my1)
    scr5 = Scrollbar(my1)
    lb5.config(yscrollcommand=scr1.set)
    scr5.config(command=lb1.yview)
    lb5.pack(fill=Y)
    lb5.place(x=250, y=380)
    scr5.pack(fill=Y)
    scr5.place(x=380, y=380)

    lb6 = Listbox(my1)
    scr6 = Scrollbar(my1)
    lb6.config(yscrollcommand=scr1.set)
    scr6.config(command=lb1.yview)
    lb6.pack(fill=Y)
    lb6.place(x=500, y=380)
    scr6.pack(fill=Y)
    scr6.place(x=630, y=380)
    def showmyjuese():
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        cur.execute('select 角色 from yonghushuju')
        con.ping(reconnect=True)
        data = cur.fetchall()
        print(data)
        va = []
        for i in data:
            va.append(i)
        cur.close()
        con.commit()
        con.close()
        for i in va:
            lb1.insert(END, i)
    def showmywuqi():
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        cur.execute('select 武器 from yonghushuju')
        con.ping(reconnect=True)
        data = cur.fetchall()
        print(data)
        va = []
        for i in data:
            va.append(i)
        cur.close()
        con.commit()
        con.close()
        for i in va:
            lb2.insert(END, i)
    def showmyshengyiwu():
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        cur.execute('select 圣遗物 from yonghushuju')
        con.ping(reconnect=True)
        data = cur.fetchall()
        print(data)
        va = []
        for i in data:
            va.append(i)
        cur.close()
        con.commit()
        con.close()
        for i in va:
            lb3.insert(END, i)
    Label(my1, text=' 角 色 信 息').place(x=0, y=240)  # 用place来处理按钮的位置信息。
    Label(my1, text='选项：稀有度、武器类型、\n元素属性、性别、\n所在国家、90生命上限、90攻击力、\n90防御力、突破加成MAX、TAG').place(x=0, y=310)
    # 第4步，在图形化界面上设定一个文本框
    text1 = Text(my1,width=10, height=1)  # 创建文本输入框
    # 第5步，安置文本框
    text1.setvar('请输入角色名')
    text1.pack()
    text1.place(x=0,y=270)# 把Text放在window上面，显示Text这个控件
    text2 = Text(my1,width=10,height=1)  # 创建文本输入框
    text2.pack()  # 把Text放在window上面，显示Text这个控件
    text2.place(x=0,y=290)
    # 第6步，获取文本框输入
    def getTextInput1():
        result1 = text1.get("1.0", "end")  # 获取文本输入框的内容
        result1=result1[:-1]
        #result1.replace('\n','')
        result2 = text2.get("1.0", "end")
        result2=result2[:-1]
        #result2.replace('\n', '')
        #print(result1,result2)
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        sql = 'select {} from juese where 名字="{}"'.format(result2,result1)
        print(sql)
        con.ping(reconnect=True)
        cur.execute(sql)
        data = cur.fetchall()
        print(data)
        lb4.insert(END,data)
        cur.close()
        con.commit()
        con.close()
        tkm.showinfo(message='读入成功！！！')
    # Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
    # "end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。
    # 第7步，在图形化界面上设定一个button按钮（#command绑定获取文本框内容的方法）
    btnRead1 = Button(my1, height=1, width=10, text="Read", command=getTextInput1)  # command绑定获取文本框内容的方法
    # 第8步，安置按钮
    btnRead1.pack()
    btnRead1.place(x=100,y=270)# 显示按钮

    Label(my1, text=' 武 器 信 息 ').place(x=250, y=240)
    Label(my1, text='选项：类型、稀有度、获取途径、\n初始攻击力、最高攻击力、技能').place(x=250, y=330)
    # 第4步，在图形化界面上设定一个文本框
    text3 = Text(my1, width=10, height=1)  # 创建文本输入框
    # 第5步，安置文本框
    text3.pack()
    text3.place(x=250, y=270)  # 把Text放在window上面，显示Text这个控件
    text4 = Text(my1, width=10, height=1)  # 创建文本输入框
    text4.pack()  # 把Text放在window上面，显示Text这个控件
    text4.place(x=250, y=290)
    # 第6步，获取文本框输入
    def getTextInput2():
        result3 = text3.get("1.0", "end")  # 获取文本输入框的内容
        result3=result3[:-1]
        result4 = text4.get("1.0", "end")
        result4=result4[:-1]
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        sql = 'select {} from wuqi where 名称="{}"'.format(result4, result3)
        print(sql)
        con.ping(reconnect=True)
        cur.execute(sql)
        data = cur.fetchall()
        print(data)
        lb5.insert(END, data)
        cur.close()
        con.commit()
        con.close()
        tkm.showinfo(message='读入成功！！！')

    # Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
    # "end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。
    # 第7步，在图形化界面上设定一个button按钮（#command绑定获取文本框内容的方法）
    btnRead2 = Button(my1, height=1, width=10, text="Read", command=getTextInput2)  # command绑定获取文本框内容的方法
    # 第8步，安置按钮
    btnRead2.pack()
    btnRead2.place(x=350, y=270)  # 显示按钮
    Label(my1, text=' 圣 遗 物 信 息 ').place(x=500, y=240)  # 用place来处理按钮的位置信息。
    Label(my1, text='选项：最低稀有度、最高稀有度、\n获取途径、两件套效果、四件套效果').place(x=500, y=320)
    # 第4步，在图形化界面上设定一个文本框
    text5 = Text(my1, width=10, height=1)  # 创建文本输入框
    # 第5步，安置文本框
    text5.pack()
    text5.place(x=500, y=270)  # 把Text放在window上面，显示Text这个控件
    text6 = Text(my1, width=10, height=1)  # 创建文本输入框
    text6.pack()  # 把Text放在window上面，显示Text这个控件
    text6.place(x=500, y=290)

    # 第6步，获取文本框输入
    def getTextInput3():
        result5 = text5.get("1.0", "end")  # 获取文本输入框的内容
        result6 = text6.get("1.0", "end")
        result5=result5[:-1]
        result6=result6[:-1]
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        sql = 'select {} from shengyiwu where 名称="{}"'.format(result6, result5)
        print(sql)
        con.ping(reconnect=True)
        cur.execute(sql)
        data = cur.fetchall()
        print(data)
        lb6.insert(END, data)
        cur.close()
        con.commit()
        con.close()
        tkm.showinfo(message='读入成功！！！')

    # Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
    # "end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。
    # 第7步，在图形化界面上设定一个button按钮（#command绑定获取文本框内容的方法）
    btnRead3 = Button(my1, height=1, width=10, text="Read", command=getTextInput3)  # command绑定获取文本框内容的方法
    # 第8步，安置按钮
    btnRead3.pack()
    btnRead3.place(x=580, y=270)  # 显示按钮
    Label(my1, text=' 请选择 角色、武器、圣遗物').place(x=640, y=10)
    text7 = Text(my1, width=10, height=1)  # 创建文本输入框
    # 第5步，安置文本框
    text7.pack()
    text7.place(x=650, y=30)
    Label(my1, text=' 请选择要修改的项目').place(x=650, y=50)
    # 把Text放在window上面，显示Text这个控件
    text8 = Text(my1, width=10, height=1)  # 创建文本输入框
    text8.pack()  # 把Text放在window上面，显示Text这个控件
    text8.place(x=650, y=70)
    Label(my1, text=' 请输入修改结果').place(x=650, y=90)
    text9 = Text(my1, width=10, height=1)  # 创建文本输入框
    # 第5步，安置文本框
    text9.pack()
    text9.place(x=650, y=110)  # 把Text放在window上面，显示Text这个控件

    Label(my1, text=' 请输入修改目标').place(x=650, y=130)
    text10 = Text(my1, width=10, height=1)  # 创建文本输入框
    # 第5步，安置文本框
    text10.pack()
    text10.place(x=650, y=150)  # 把Text放在window上面，显示Text这个控件

    def shan1():
        a = text7.get("1.0", "end")
        a = a[:-1]
        b = text8.get("1.0", "end")
        b = b[:-1]
        c = text9.get("1.0", "end")
        c = c[:-1]
        d = text10.get("1.0", "end")
        d = d[:-1]
        print(a, b, c, d)
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        if a=='角色':
            cur.execute('delete * from juese where 名字="{}"'.format(b))
        elif a=='武器':
            cur.execute('delete * from wuqi where 名字="{}"'.format(b))
        elif a=='圣遗物':
            cur.execute('delete * from shengyiwu where 名字="{}"'.format(b))
        #cur.execute(sql1)
        con.ping(reconnect=True)
        cur.close()
        con.commit()
        con.close()
        tkm.showinfo(message='删除成功！！！')
    def gai1():
        a = text7.get("1.0", "end")
        a = a[:-1]
        b = text8.get("1.0", "end")
        b = b[:-1]
        c = text9.get("1.0", "end")
        c = c[:-1]
        d = text10.get("1.0", "end")
        d = d[:-1]
        print(a, b, c, d)
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        if a == '角色':
            print('update juese  set {}={} where {}={}'.format(b, c, b, d))
            cur.execute('update juese  set {}="{}" where {}="{}"'.format(b,c,b,d))
        elif a == '武器':
            cur.execute('update wuqi  set {}="{}" where {}="{}"'.format(a,c,a,d))
        elif a == '圣遗物':
            cur.execute('update shengyiwu  set {}="{}" where {}="{}"'.format(a,c,a,d))
        con.ping(reconnect=True)
        cur.close()
        con.commit()
        con.close()
        tkm.showinfo(message='修改成功！！！')

    shan = Button(my1, height=1, width=10, text="删", command=shan1)  # command绑定获取文本框内容的方法
    # 第8步，安置按钮
    shan.pack()
    shan.place(x=700, y=170)  # 显示按钮

    gai = Button(my1, height=1, width=10, text="改", command=gai1)  # command绑定获取文本框内容的方法
    # 第8步，安置按钮
    gai.pack()
    gai.place(x=700, y=250)  # 显示按钮




def juese():
    juese1=Toplevel(master)
    juese1.title('原神wiki数据库管理系统')
    juese1.geometry('800x600')  # 不能有空格在800和x之间，适当设置分辨率利于设置滚动条
    con = pymysql.connect(host='localhost', user='root',
                          passwd='cjhcjh123', charset='utf8')
    cur = con.cursor()
    cur.execute('use yuanshenwiki')
    cur.execute('select 名字 from juese')
    con.ping(reconnect=True)
    data = cur.fetchall()
    print(data)
    va = []
    for i in data:
        va.append(i)
    cur.close()
    con.commit()
    con.close()
    Label(juese1, text='请选择你所需要的角色数据').pack(side='left')
    lb = Listbox(juese1)
    scr = Scrollbar(juese1)
    lb.config(yscrollcommand=scr.set)
    scr.config(command=lb.yview)
    lb.pack(fill=Y)
    lb.place(x=0, y=50)
    scr.pack(fill=Y)
    scr.place(x=130, y=50)
    for i in va:
        lb.insert(END, i)
    # 第4步，在图形化界面上设定一个文本框
    textExample = Text(juese1, height=1)  # 创建文本输入框
    # 第5步，安置文本框
    textExample.pack()  # 把Text放在window上面，显示Text这个控件
    # 第6步，获取文本框输入
    def getTextInput():
        result1=[]
        result = textExample.get("1.0", "end")  # 获取文本输入框的内容
        result1.append(result)
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        sql = 'insert into yonghushuju(角色) values (%s)'
        con.ping(reconnect=True)
        cur.executemany(sql, result1)
        cur.close()
        con.commit()
        con.close()
        tkm.showinfo(message='读入成功！！！')
    # Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
    # "end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。
    # 第7步，在图形化界面上设定一个button按钮（#command绑定获取文本框内容的方法）
    btnRead = Button(juese1, height=1, width=10, text="Read", command=getTextInput)  # command绑定获取文本框内容的方法
    # 第8步，安置按钮
    btnRead.pack()  # 显示按钮
    canvas = Canvas(juese1, height=700, width=1000)
    # 加载图片
    im = Image.open("C:\\Users\\55151\\Desktop\\原神Wiki数据库课设\\UI\\原神.png")
    image_file = ImageTk.PhotoImage(im)
    # image_file = tk.PhotoImage(file='images/01.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack(side='top')
    mainloop()
def wuqi():
    wuqi1 = Toplevel(master)
    wuqi1.title('原神wiki数据库管理系统')
    wuqi1.geometry('800x600')  # 不能有空格在800和x之间，适当设置分辨率利于设置滚动条
    con = pymysql.connect(host='localhost', user='root',
                          passwd='cjhcjh123', charset='utf8')
    cur = con.cursor()
    cur.execute('use yuanshenwiki')
    cur.execute('select 名称 from wuqi')
    con.ping(reconnect=True)
    data = cur.fetchall()
    print(data)
    va = []
    for i in data:
        va.append(i)
    Label(wuqi1, text='请选择你所需要的武器数据').pack(side='left')
    cur.close()
    con.commit()
    con.close()
    lb = Listbox(wuqi1)
    scr = Scrollbar(wuqi1)
    lb.config(yscrollcommand=scr.set)
    scr.config(command=lb.yview)
    lb.pack(fill=Y)
    lb.place(x=0, y=50)
    scr.pack(fill=Y)
    scr.place(x=130, y=50)
    for i in va:
        lb.insert(END, i)
    # 第4步，在图形化界面上设定一个文本框
    textExample = Text(wuqi1, height=1)  # 创建文本输入框
    # 第5步，安置文本框
    textExample.pack()  # 把Text放在window上面，显示Text这个控件

    # 第6步，获取文本框输入
    def getTextInput():
        result1 = []
        result = textExample.get("1.0", "end")  # 获取文本输入框的内容
        result1.append(result)
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        sql = 'insert into yonghushuju(武器) values (%s)'
        con.ping(reconnect=True)
        cur.executemany(sql, result1)
        cur.close()
        con.commit()
        con.close()
        tkm.showinfo(message='读入成功！！！')
    # Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
    # "end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。
    # 第7步，在图形化界面上设定一个button按钮（#command绑定获取文本框内容的方法）
    btnRead = Button(wuqi1, height=1, width=10, text="Read", command=getTextInput)  # command绑定获取文本框内容的方法
    # 第8步，安置按钮
    btnRead.pack()  # 显示按钮

    # 画布
    canvas = Canvas(wuqi1, height=700, width=1000)
    # 加载图片
    im = Image.open("C:\\Users\\55151\\Desktop\\原神Wiki数据库课设\\UI\\原神.png")
    image_file = ImageTk.PhotoImage(im)
    # image_file = tk.PhotoImage(file='images/01.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack(side='top')
    mainloop()
def shengyiwu():
    shengyiwu1 = Toplevel(master)
    shengyiwu1.title('原神wiki数据库管理系统')
    shengyiwu1.geometry('800x600')  # 不能有空格在800和x之间，适当设置分辨率利于设置滚动条
    con = pymysql.connect(host='localhost', user='root',
                          passwd='cjhcjh123', charset='utf8')
    cur = con.cursor()
    cur.execute('use yuanshenwiki')
    cur.execute('select 名称 from shengyiwu')
    con.ping(reconnect=True)
    data = cur.fetchall()
    print(data)
    va = []
    for i in data:
        va.append(i)
    Label(shengyiwu1, text='请选择你所需要的圣遗物数据').pack(side='left')
    cur.close()
    con.commit()
    con.close()
    lb = Listbox(shengyiwu1)
    scr = Scrollbar(shengyiwu1)
    lb.config(yscrollcommand=scr.set)
    scr.config(command=lb.yview)
    lb.pack(fill=Y)
    lb.place(x=0, y=50)
    scr.pack(fill=Y)
    scr.place(x=130, y=50)
    for i in va:
        lb.insert(END, i)
    # 第4步，在图形化界面上设定一个文本框
    textExample = Text(shengyiwu1, height=1)  # 创建文本输入框
    # 第5步，安置文本框
    textExample.pack()  # 把Text放在window上面，显示Text这个控件

    # 第6步，获取文本框输入
    def getTextInput():
        result1 = []
        result = textExample.get("1.0", "end")  # 获取文本输入框的内容
        result1.append(result)
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        sql = 'insert into yonghushuju(圣遗物) values (%s)'
        con.ping(reconnect=True)
        cur.executemany(sql, result1)
        cur.close()
        con.commit()
        con.close()
        tkm.showinfo(message='读入成功！！！')
    # Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
    # "end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。
    # 第7步，在图形化界面上设定一个button按钮（#command绑定获取文本框内容的方法）
    btnRead = Button(shengyiwu1, height=1, width=10, text="Read", command=getTextInput)  # command绑定获取文本框内容的方法
    # 第8步，安置按钮
    btnRead.pack()  # 显示按钮
    # 画布
    canvas = Canvas(shengyiwu1, height=700, width=1000)
    # 加载图片
    im = Image.open("C:\\Users\\55151\\Desktop\\原神Wiki数据库课设\\UI\\原神.png")
    image_file = ImageTk.PhotoImage(im)
    # image_file = tk.PhotoImage(file='images/01.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack(side='top')
    mainloop()
def usr_login():
    usr_name = usr.get()
    usr_pwd = pwd.get()
    #print(usr_name,usr_pwd)
    con = pymysql.connect(host='localhost', user='root',
                          passwd='cjhcjh123', charset='utf8')
    cur = con.cursor()
    cur.execute('use yuanshenwiki')
    cur.execute('select 账号,密码 from yonghuxinxi')
    con.ping(reconnect=True)
    data = cur.fetchall()
    data=dict(data)
    cur.close()
    con.commit()
    con.close()
    if usr_name in data:
        if usr_pwd==data[usr_name]:
            tkm.showinfo(
                title='欢迎来到提瓦特的世界', message=usr_name + '：!登陆成功！')

            main()
        else:
            tkm.showinfo(message='错误提示：密码不对，请重试')
    else:
        is_sign_up = tkm.askyesno('提示', '你还没有注册，请先注册')
        print(is_sign_up)
        if is_sign_up:
            usr_sign_up()
# 注册按钮
def usr_sign_up():
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        con = pymysql.connect(host='localhost', user='root',
                              passwd='cjhcjh123', charset='utf8')
        cur = con.cursor()
        cur.execute('use yuanshenwiki')
        cur.execute('select 账号 from yonghuxinxi')
        con.ping(reconnect=True)
        data=cur.fetchall()
        print(data)
        if np != npf:
            tkm.showerror('错误提示', '密码和确认密码必须一样')
        elif nn in data:
            tkm.showerror('错误提示', '用户名早就注册了！')
        else:
            sqlSentence = 'insert into yonghuxinxi(账号,密码) values (%s,%s)'
            record = (nn, np)
            print(record)
            cur.executemany(sqlSentence, [record])
            tkm.showinfo('欢迎', '你已经成功注册了')
            window_sign_up.destroy()
        # 结束,关闭
        cur.close()
        con.commit()
        con.close()
    # 点击注册之后，会弹出这个窗口界面。
    window_sign_up = Toplevel(master)
    window_sign_up.title('欢迎注册')
    window_sign_up.geometry('360x200')  # 中间是x，而不是*号

    # 用户名框--这里输入用户名框。
    new_name = StringVar()
    new_name.set('')  # 设置的是默认值
    Label(window_sign_up, text='用户名').place(x=10, y=10)
    entry_new_name = Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=100, y=10)

    # 新密码框--这里输入注册时候的密码
    new_pwd = StringVar()
    Label(window_sign_up, text='密  码').place(x=10, y=50)
    entry_usr_pwd = Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=100, y=50)
    # 密码确认框
    new_pwd_confirm = StringVar()
    Label(window_sign_up, text='确认密码').place(x=10, y=90)
    entry_usr_pwd_confirm = Entry(
        window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=100, y=90)

    btn_confirm_sign_up = Button(
        window_sign_up, text=' 注  册 ', command=sign_to_Mofan_Python)
    btn_confirm_sign_up.place(x=120, y=130)
# 创建注册和登录按钮
btn_login = Button(master, text=' 登  录 ', command=usr_login)
btn_login.place(x=250, y=350)  # 用place来处理按钮的位置信息。
btn_sign_up = Button(master, text=' 注  册 ', command=usr_sign_up)
btn_sign_up.place(x=400, y=350)
mainloop()
