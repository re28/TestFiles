import sys
sys.path.append('/home/pi/.local/lib/python2.7/site-packages')
import tkinter
import datetime
import gspread
import oauth2client
import json
from tkinter import *
from tkinter import ttk

class submissionBox(ttk.Frame):

	def __init__(self,master = None):
		super().__init__(master)
		self.create_widgets()

	#最初の画面（学生、管理者）
	def create_widgets(self):
		now = datetime.datetime.today()
		label_time = ttk.Label(self,text=now.date())
		label_time.grid(columnspan=2, row =0)

		#studentボタン
		label_student = ttk.Button(self,text='学生')
		label_student.grid(column=0, row =1,sticky=N+S+E+W)
		label_student.bind('<Button-1>',self.student)

		#managerボタン
		label_manager = ttk.Button(self,text='管理者')
		label_manager.grid(column=1, row =1,sticky=N+S+E+W)
		label_manager.bind('<Button-1>',self.manager)

		#フレーム自身もトップレベルウィジェットに配置
		self.grid(column = 0, row=0,sticky=N+S+E+W)

		#各行、列の引き伸ばし設定
		self.grid_rowconfigure(1,weight=1)
		self.grid_columnconfigure(0,weight=1)
		self.grid_rowconfigure(1,weight=1)
		self.grid_columnconfigure(1,weight=1)

		#トップレベルのウィジェットも引き伸ばしに対応させる
		self.master.rowconfigure(0,weight=1)
		self.master.columnconfigure(0,weight=1)

	#学生   
	def student(self,event):
		print('student')
		self.frame_student = ttk.Frame(self.master)
		self.frame_student.grid(row=0, column=0,sticky=N+S+E+W)

		now = datetime.datetime.today()
		label_time = ttk.Label(self.frame_student,text=now.date())
		label_time.grid(row=0, column=3,sticky=N+S+E+W)

		label_student = ttk.Label(self.frame_student,text='学籍番号を入力してください')
		label_student.grid(row=1, column=3, sticky=N+S+E+W)
		text = tkinter.StringVar()

		# ボタン（数字）
		self.exp_list = ['1260000']
		self.display_var=StringVar()
		self.display_var.set('1260000')
		display_label_stdnum = ttk.Label(self.frame_student,font=("",17),textvariable=self.display_var)
		display_label_stdnum.grid(row=2, column=3, sticky=N+S+E+W)

		#提出ボタン
		button_submit = ttk.Button(self.frame_student,text='提出します')
		button_submit.bind("<Button-1>",self.delete_calc_frame_student)
		button_submit.grid(row=3, column=3,sticky=N+S+E+W)

		LAYOUT =  [
		['7','8','9'],
		['4','5','6'],
		['1','2','3'],
		['0','C','Enter'],
		]

		for y, row in enumerate(LAYOUT,0):
			for x, char in enumerate(row):
				button = ttk.Button(self.frame_student, text=char)
				button.grid(row=y, column=x, sticky=N+S+E+W)
				button.bind('<Button-1>',self.calc_student)

				self.frame_student.grid_rowconfigure(0,weight=1)
				self.frame_student.grid_columnconfigure(0,weight=1)
				self.frame_student.grid_rowconfigure(1,weight=1)
				self.frame_student.grid_columnconfigure(1,weight=1)
				self.frame_student.grid_rowconfigure(2,weight=1)
				self.frame_student.grid_columnconfigure(2,weight=1)
				self.frame_student.grid_rowconfigure(3,weight=1)
				self.frame_student.grid_columnconfigure(3,weight=1)

		self.frame_student.mainloop()


	#ウィンドウを一つ前に戻す
	def delete_calc_frame_student(self,event):
		self.frame_student.destroy()

	#管理者のページ
	def manager(self,event):
		print('manager')
		self.frame_manager = ttk.Frame(self.master)
		self.frame_manager.grid(row=0, column=0,sticky=N+S+E+W)

		now = datetime.datetime.today()
		label_time = ttk.Label(self.frame_manager,text=now.date())
		label_time.grid(row=0, column=3,sticky=N+S+E+W)

		label_manager = ttk.Label(self.frame_manager,text='パスワードを入力してください')
		label_manager.grid(row=1, column=3, sticky=N+S+E+W)
		text = tkinter.StringVar()

		# ボタン（数字）
		self.exp_list = ['0000']
		self.display_var=StringVar()
		self.display_var.set('0000')
		display_label_passwd = ttk.Label(self.frame_manager,font=("",17),textvariable=self.display_var)
		display_label_passwd.grid(row=2, column=3, sticky=N+S+E+W)

		'''
		#ボタン
		button_confirmation = ttk.Button(self.frame_manager,text='確認')
		button_confirmation.bind("<Button-1>",self.number_of_students)
		button_confirmation.grid(row=3, column=3,sticky=N+S+E+W)
		'''

		LAYOUT =  [
		['7','8','9'],
		['4','5','6'],
		['1','2','3'],
		['0','C','Enter'],
		]

		for y, row in enumerate(LAYOUT,0):
			for x, char in enumerate(row):
				button = ttk.Button(self.frame_manager, text=char)
				button.grid(row=y, column=x, sticky=N+S+E+W)
				button.bind('<Button-1>',self.calc_manager) 

				self.frame_manager.grid_rowconfigure(0,weight=1)
				self.frame_manager.grid_columnconfigure(0,weight=1)
				self.frame_manager.grid_rowconfigure(1,weight=1)
				self.frame_manager.grid_columnconfigure(1,weight=1)
				self.frame_manager.grid_rowconfigure(2,weight=1)
				self.frame_manager.grid_columnconfigure(2,weight=1)
				self.frame_manager.grid_rowconfigure(3,weight=1)
				self.frame_manager.grid_columnconfigure(3,weight=1)

		self.frame_manager.mainloop()


	#人数の設定ページ
	def number_of_students(self,event):
		print('number of students')
		self.number_of_students = ttk.Frame(self.master)
		self.number_of_students.grid(row=0, column=0,sticky=N+S+E+W)

		now = datetime.datetime.today()
		label_time = ttk.Label(self.number_of_students,text=now.date())
		label_time.grid(row=0, column=3,sticky=N+S+E+W)

		label_number = ttk.Label(self.number_of_students,text='人数を設定してください')
		label_number.grid(row=1, column=3, sticky=N+S+E+W)
		text = tkinter.StringVar()

		# ボタン（数字）
		self.exp_list = ['000']
		self.display_var=StringVar()
		self.display_var.set('000')
		display_label_nof = ttk.Label(self.number_of_students,font=("",17),textvariable=self.display_var)
		display_label_nof.grid(row=2, column=3, sticky=N+S+E+W)

		button_confirm = ttk.Button(self.number_of_students,text='確定')
		button_confirm.bind("<Button-1>",self.deadline_month)
		button_confirm.grid(row=3, column=3,sticky=N+S+E+W)

		LAYOUT =  [
		['7','8','9'],
		['4','5','6'],
		['1','2','3'],
		['0','C','Enter'],
		]

		for y, row in enumerate(LAYOUT,0):
			for x, char in enumerate(row):
				button = ttk.Button(self.number_of_students, text=char)
				button.grid(row=y, column=x, sticky=N+S+E+W)
				button.bind('<Button-1>',self.calc_nof) 

				self.number_of_students.grid_rowconfigure(0,weight=1)
				self.number_of_students.grid_columnconfigure(0,weight=1)
				self.number_of_students.grid_rowconfigure(1,weight=1)
				self.number_of_students.grid_columnconfigure(1,weight=1)
				self.number_of_students.grid_rowconfigure(2,weight=1)
				self.number_of_students.grid_columnconfigure(2,weight=1)
				self.number_of_students.grid_rowconfigure(3,weight=1)
				self.number_of_students.grid_columnconfigure(3,weight=1)

		self.number_of_students.mainloop()


	#提出期限の設定
	def deadline_month(self,event):
		print('month')
		self.deadline_month = ttk.Frame(self.master)
		self.deadline_month.grid(row=0, column=0,sticky=N+S+E+W)

		now = datetime.datetime.today()
		label_time = ttk.Label(self.deadline_month,text=now.date())
		label_time.grid(row=0, column=3,sticky=N+S+E+W)

		label_deadline_month = ttk.Label(self.deadline_month,text='提出期限を設定してください（月）')
		label_deadline_month.grid(row=1, column=3, sticky=N+S+E+W)
		text = tkinter.StringVar()

		# ボタン（数字）
		self.exp_list = ['00']
		self.display_var=StringVar()
		self.display_var.set('00')
		display_label = ttk.Label(self.deadline_month,font=("",17),textvariable=self.display_var)
		display_label.grid(row=2, column=3, sticky=N+S+E+W)

		button_set = ttk.Button(self.deadline_month,text='設定')
		button_set.bind("<Button-1>",self.deadline_date)
		button_set.grid(row=3, column=3,sticky=N+S+E+W)

		LAYOUT =  [
		['7','8','9'],
		['4','5','6'],
		['1','2','3'],
		['0','C','Enter'],
		]

		for y, row in enumerate(LAYOUT,0):
			for x, char in enumerate(row):
				button = ttk.Button(self.deadline_month, text=char)
				button.grid(row=y, column=x, sticky=N+S+E+W)
				button.bind('<Button-1>',self.calc_month) 

				self.deadline_month.grid_rowconfigure(0,weight=1)
				self.deadline_month.grid_columnconfigure(0,weight=1)
				self.deadline_month.grid_rowconfigure(1,weight=1)
				self.deadline_month.grid_columnconfigure(1,weight=1)
				self.deadline_month.grid_rowconfigure(2,weight=1)
				self.deadline_month.grid_columnconfigure(2,weight=1)
				self.deadline_month.grid_rowconfigure(3,weight=1)
				self.deadline_month.grid_columnconfigure(3,weight=1)

		due_month = self.calc_month(event)

		self.deadline_month.mainloop()


	def deadline_date(self,event):
		print('date')
		self.deadline_date = ttk.Frame(self.master)
		self.deadline_date.grid(row=0, column=0,sticky=N+S+E+W)

		now = datetime.datetime.today()
		label_time = ttk.Label(self.deadline_date,text=now.date())
		label_time.grid(row=0, column=3,sticky=N+S+E+W)

		label_deadline_date = ttk.Label(self.deadline_date,text='提出期限を設定してください（日）')
		label_deadline_date.grid(row=1, column=3, sticky=N+S+E+W)
		text = tkinter.StringVar()

		self.exp_list = ['00']
		self.display_var=StringVar()
		self.display_var.set('00')
		display_label_day = ttk.Label(self.deadline_date,font=("",17),textvariable=self.display_var)
		display_label_day.grid(row=2, column=3, sticky=N+S+E+W)

		button_set = ttk.Button(self.deadline_date,text='設定')
		button_set.bind("<Button-1>",self.delete_four_frames)
		button_set.grid(row=3, column=3,sticky=N+S+E+W)

		LAYOUT =  [
		['7','8','9'],
		['4','5','6'],
		['1','2','3'],
		['0','C','Enter'],
		]

		for y, row in enumerate(LAYOUT,0):
			for x, char in enumerate(row):
				button = ttk.Button(self.deadline_date, text=char)
				button.grid(row=y, column=x, sticky=N+S+E+W)
				button.bind('<Button-1>',self.calc_date) 

				self.deadline_date.grid_rowconfigure(0,weight=1)
				self.deadline_date.grid_columnconfigure(0,weight=1)
				self.deadline_date.grid_rowconfigure(1,weight=1)
				self.deadline_date.grid_columnconfigure(1,weight=1)
				self.deadline_date.grid_rowconfigure(2,weight=1)
				self.deadline_date.grid_columnconfigure(2,weight=1)
				self.deadline_date.grid_rowconfigure(3,weight=1)
				self.deadline_date.grid_columnconfigure(3,weight=1)

		due_date = self.calc_date(event)

		self.deadline_date.mainloop()


	#ウィンドウを三つ前に戻す
	def delete_four_frames(self,event):
		self.frame_manager.destroy()
		self.number_of_students.destroy()
		self.deadline_month.destroy()
		self.deadline_date.destroy()

	#キーパッドの制御(student)
	def calc_student(self,event):
		char = event.widget['text']

		if char == 'C':
			self.exp_list = ['']
			return self.exp_list

		elif  char == 'Enter':
			stu_id = ''.join(self.exp_list)

			n = int(n)-1260000

			# ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
			from oauth2client.service_account import ServiceAccountCredentials

			# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
			scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

			# 認証情報設定
			# ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
			credentials = ServiceAccountCredentials.from_json_keyfile_name('submission-6275aa6e7761.json', scope)

			# OAuth2の資格情報を使用してGoogle APIにログインします。
			gc = gspread.authorize(credentials)

			# 共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
			SPREADSHEET_KEY = '1hBiR1qq79Rpl9atWtRaQY-gO1JOFx3tt9GFltSvNmX4'

			# 共有設定したスプレッドシートのシート1を開く
			worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

			# 提出をスプレッドシートに反映
			worksheet.update_cell(n+3, 3, '○')
			sub_num = int(worksheet.cell(2,2).value)
			sub_num = sub_num + 1
			worksheet.update_cell(2, 2, sub_num)
			all_stu = int(worksheet.cell(1,2).value)
			worksheet.update_cell(3, 2, '{}%'.format(sub_num/all_stu*100))
			#self.submission(n)

		else:
			char = self.exp_list.append(char)
			self.display_var.set(
				' '.join(self.exp_list)
				)


	#キーパッドの制御(manager)
	def calc_manager(self,event):
		char = event.widget['text']

		if char == 'C':
			self.exp_list = ['']
			return self.exp_list

		elif  char == 'Enter':
			password = ''.join(self.exp_list)
			passwd_default = '1234'
			if password == passwd_default:
				self.number_of_students(event)

		else: 
			char = self.exp_list.append(char)
			self.display_var.set(
				' '.join(self.exp_list)
				)


	#キーパッドの制御(number_of_students)
	def calc_nof(self,event):
		char = event.widget['text']

		if char == 'C':
			self.exp_list = ['']
			return self.exp_list

		elif  char == 'Enter':
			stu_num = ''.join(self.exp_list)
			self.reset_spread(int(stu_num))

		else: 
			char = self.exp_list.append(char)
			self.display_var.set(
				' '.join(self.exp_list)
				)


	def reset_spread(self,n):
		# ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
		from oauth2client.service_account import ServiceAccountCredentials

		# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

		# 認証情報設定
		# ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
		credentials = ServiceAccountCredentials.from_json_keyfile_name('submission-box-312a140faf29.json', scope)

		# OAuth2の資格情報を使用してGoogle APIにログインします。
		gc = gspread.authorize(credentials)

		# 共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
		SPREADSHEET_KEY = '1OppYg26mXWICbxQZi1zcE-E5NYwh3LPeWwjBDHp-3ro'

		# 共有設定したスプレッドシートのシート1を開く
		worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

		'''
		# スプレッドシートをリセット
		file = open("data.txt", "r", encoding="utf-8")
		lines = file.readlines()
		'''
		i = 0

		'''
		for line in lines:
			line = line.rstrip("\n")
			stu = line.rsplit(" ")
			worksheet.update_cell(i+3, 1, stu[0])
			worksheet.update_cell(i+3, 2, stu[1])
			i = i + 1
		'''

		for i in range(4, n+4):
			worksheet.update_cell(i, 3, '×')
		worksheet.update_cell(1, 1, '総数')
		worksheet.update_cell(1, 2, n)
		worksheet.update_cell(2, 1, '提出数')
		worksheet.update_cell(2, 2, 0)
		worksheet.update_cell(3, 1, '提出率')
		worksheet.update_cell(3, 2, 0)

	#キーパッドの制御(deadline_month)
	def calc_month(self,event):
		char = event.widget['text']

		if char == 'C':
			self.exp_list = ['']
			return self.exp_list

		elif  char == 'Enter':
			due_month = ''.join(self.exp_list)
			return int(due_month)

		else: 
			char = self.exp_list.append(char)
			self.display_var.set(
				' '.join(self.exp_list)
				)

	#キーパッドの制御(deadline_date)
	def calc_date(self,event):
		char = event.widget['text']

		if char == 'C':
			self.exp_list = ['']
			return self.exp_list

		elif  char == 'Enter':
			due_date = ''.join(self.exp_list)
			return int(due_date)

		else: 
			char = self.exp_list.append(char)
			self.display_var.set(
				' '.join(self.exp_list)
				)

	#スプレッドシートに出力
	def submission(n):
		n = n-1260000
		# ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
		from oauth2client.service_account import ServiceAccountCredentials

		# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

		# 認証情報設定
		# ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
		credentials = ServiceAccountCredentials.from_json_keyfile_name('submission-box-312a140faf29.json', scope)

		# OAuth2の資格情報を使用してGoogle APIにログインします。
		gc = gspread.authorize(credentials)

		# 共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
		SPREADSHEET_KEY = '1OppYg26mXWICbxQZi1zcE-E5NYwh3LPeWwjBDHp-3ro'

		# 共有設定したスプレッドシートのシート1を開く
		worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

		# 提出をスプレッドシートに反映
		worksheet.update_cell(n+3, 3, '○')
		sub_num = int(worksheet.cell(2,2).value)
		sub_num = sub_num + 1
		worksheet.update_cell(2, 2, sub_num)
		all_stu = int(worksheet.cell(1,2).value)
		worksheet.update_cell(3, 2, '{}%'.format(sub_num/all_stu*100))


def main():
	root = Tk()
	root.title('提出ボックス')
	submissionBox(root)
	root.mainloop()

if __name__ == '__main__':
	main()


