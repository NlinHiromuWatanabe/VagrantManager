import csv
import tkinter 
from tkinter import *
from tkinter import ttk
from functools import partial
import subprocess

vagrant_list = []
# csvファイル読み込み
# withを使用するとcloseなしでもOK
with open("vagrant_machines.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    # vagrant_listに多次元リストでCSVの中身を格納
    vagrant_list = [row for row in reader]
# リストの内包表記でvagrant_listのタイトルだけ抜き出し
machine_tilte_list = [x[0] for x in vagrant_list]

# tkinter インスタンスを生成
win  = tkinter.Tk()

# titleを設定
win.title(u"Vagrant Manager")

# window サイズを設定
win.geometry("300x215")
win.resizable(width=False, height=False)

#リストボックス
# CSVのタイトルカラムを設定
txt = StringVar(value=machine_tilte_list)
# リストボックスにテキストを渡し大きさの指定
lb= Listbox(win, listvariable=txt,width=48,height=10)
# vagrantマシンのリストの長さが1以上のとき初期値にインデックス[0]を設定
if len(machine_tilte_list) > 0:
    lb.select_set(0)
lb.pack(pady=5)

def button_click(list_arr, win, command_str):
    # 初期値設定してるからありえないけど選択0だったらreturn
    if len(lb.curselection()) == 0:
        return
    # 選択しているインデックスを取得
    index = lb.curselection()[0]
    
    # CMD実行
    subprocess.run(command_str.split(), shell=True, cwd=list_arr[index][1])
    return

# ボタンの生成・コールバック関数にpartialを使って引数を渡す
up_button = tkinter.Button(win, text="起動", command = partial(button_click, vagrant_list, win, "vagrant up "))
down_button = tkinter.Button(win, text="終了", command = partial(button_click, vagrant_list, win, "vagrant halt "))
reload_button = tkinter.Button(win, text="再起動", command = partial(button_click, vagrant_list, win, "vagrant reload "))
# ボタンの大きさを指定
up_button.place(x=90,y=180)
down_button.place(x=130,y=180)
reload_button.place(x=170,y=180)
# ここまでの処理をループ
win.mainloop()