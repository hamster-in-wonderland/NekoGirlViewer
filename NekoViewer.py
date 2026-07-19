import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_neko import Ui_MainWindow
from PySide6.QtGui import QIcon
import requests,json,os,re,webbrowser

requests.packages.urllib3.disable_warnings()
version = '3.1.0'
class MyWindow(QMainWindow,Ui_MainWindow):
    htmlindex = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            background-color: black;
        }
        p{
            color:white;
            padding: 150px;
        }
    </style>
</head>
<body>
    <p>喵~</p>
</body>
</html>'''
    pictureUrlList = []
    head = {'User-Agent':'NekoViewerV2 (hamster_liu@outlook.com)'}
    idx = -1
    directory_path = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')+'/'
    os.makedirs(directory_path+'download/',exist_ok=True)
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setFixedSize(609, 478)
        self.setupUi(self)
        self.webViewer.page().profile().setHttpUserAgent('NekoViewerV3FilledWithQtEdit (hamster_liu@outlook.com)')
        self.webViewer.setHtml(self.htmlindex)
        self.save.clicked.connect(self.savefunc)
        self.next.clicked.connect(self.nextfunc)
        self.last.clicked.connect(self.lastfunc)
        self.ciallo.triggered.connect(self.ciallofunc)
        self.About_Hamster_label.triggered.connect(self.hamsterfunc)
        self.SavePath.triggered.connect(self.SavePathfunc)
        self.textOutputer.setText('''NekoViewer已成功启动

        
在菜单栏中选择
neko > 打开保存路径
以查看下载的文件''')

    def savefunc(self):
        if self.idx == -1:
            self.textOutputer.setText('请先查看一张图片')
            return
        url = self.pictureUrlList[self.idx]
        filename = re.findall('/neko/(.*?).png',url)[0]+'.png'
        with open(f'{self.directory_path}download/{filename}','wb') as file:
            with requests.get(url,verify=False,headers=self.head) as response:
                file.write(response.content)
        self.textOutputer.setText(f'已保存图片至{self.directory_path}download/{filename}')
        return
    def ciallofunc(self):
        self.textOutputer.append('Hamster：喵~')
        return
    def hamsterfunc(self):
        webbrowser.open('https://space.bilibili.com/3706996599556932')
        return
    def SavePathfunc(self):
        os.system(f'start {self.directory_path}download/')
        return
    def nextfunc(self):
        if self.idx == len(self.pictureUrlList)-1:
            self.textOutputer.setText('正在加载')
            with requests.get("https://nekos.best/api/v2/neko",verify=False,headers=self.head,timeout=5) as response:
                data = json.loads(response.text)
            data = data['results'][0]
            url = data['url']
            self.webViewer.setUrl(url)
            self.pictureUrlList.append(url)
            self.idx += 1
            self.textOutputer.setText('已获取图像url')
        else:
            self.idx += 1
            self.webViewer.setUrl(self.pictureUrlList[self.idx])
        return
    def lastfunc(self):
        if self.idx > 0:
            self.idx -= 1
            self.webViewer.setUrl(self.pictureUrlList[self.idx])
        else:
            self.textOutputer.setText('已经是最后一张了')
        return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
