import subprocess
import webbrowser

#Wordのパス指定
WordPass = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'

#Word起動
subprocess.Popen(WordPass)

#Google起動
url = 'https://www.google.co.jp/search'
webbrowser.open(url)