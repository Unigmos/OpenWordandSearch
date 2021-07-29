import selenium
import subprocess
import webbrowser

#Wordのパス指定
WordPass = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
GoogledocsPass = 'https://docs.google.com/document/'

#メモ起動
try:
    subprocess.Popen(WordPass)
except:
    webbrowser.open(GoogledocsPass)

#Google起動
url = 'https://www.google.co.jp/search'
webbrowser.open(url)