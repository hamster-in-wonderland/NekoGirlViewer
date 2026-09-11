import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_neko import Ui_MainWindow
import requests,json,os,re,webbrowser
import time
requests.packages.urllib3.disable_warnings()
version = '3.2.0'
class MyWindow(QMainWindow,Ui_MainWindow):
    htmlindex = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div td{
            color: white;
        }
        p{
            color: wheat;
        }
        html{
            background-color: black;
        }
        .text{
            padding: 100px;
        }
    </style>
</head>
<body>
    <p class="text">喵~</p>
    <div class="key">
    <p>快捷键列表</p>
    <table border="5">
        <tr>
            <td>上一张</td>
            <td>保存</td>
            <td>打开文件保存路径</td>
            <td>下一张</td>
        </tr>
        <tr>
            <td>左键</td>
            <td>s键</td>
            <td>o键</td>
            <td>右键或空格键</td>
        </tr>
    </table>
    </div>
</body>
</html>'''
    pictureUrlList = []
    head = {'User-Agent':'NekoViewerV2 (hamster_liu@outlook.com)'}
    idx = -1
    directory_path = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')+'/'
    os.makedirs(directory_path+'download/',exist_ok=True)
    def __init__(self):
        super(MyWindow, self).__init__()
        # self.setFixedSize(609, 478)
        self.setupUi(self)
        self.setFixedSize(489, 478)
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
以查看下载的文件

如果界面没有响应
请耐心等待''')
    def keyPressEvent(self, event):
        match event.key():
            case Qt.Key.Key_Right:
                self.nextfunc()
            case Qt.Key.Key_Left:
                self.lastfunc()
            case Qt.Key.Key_S:
                self.savefunc()
            case Qt.Key.Key_Space:
                self.nextfunc()
            case Qt.Key.Key_O:
                self.SavePathfunc()
    def savefunc(self):
        if self.idx == -1:
            self.textOutputer.setText('请先查看一张图片')
            return
        url = self.pictureUrlList[self.idx]
        filename = re.findall('/neko/(.*?).png',url)[0]+'.png'
        with open(f'{self.directory_path}download/{filename}','wb') as file:
            with requests.get(url,verify=False,headers=self.head) as response:
                file.write(response.content)
        self.textOutputer.setText(f'{time.ctime()}\n已保存图片至{self.directory_path}download/{filename}')
        return
    def ciallofunc(self):
        self.textOutputer.append(f'{time.ctime()}\nHamster：喵~')
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
            try:
                with requests.get("https://nekos.best/api/v2/neko",verify=False,headers=self.head,timeout=5) as response:
                    data = json.loads(response.text)
                data = data['results'][0]
                url = data['url']
                self.webViewer.setUrl(url)
                self.pictureUrlList.append(url)
                self.idx += 1
                self.textOutputer.setText(f'{time.ctime()}\n已获取图像url\n请等待图像加载')
            except:
                self.textOutputer.setText(f'出错了,请检查网络连接')
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
