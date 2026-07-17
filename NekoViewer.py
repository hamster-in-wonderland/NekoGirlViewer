print('导入依赖',end='...',flush=True)
import requests
import json
import random
import os
from PIL import Image
import keyboard
import glob
import time
import threading
from hamsterTools.colorfulPrint import *
time.sleep(0.005)
print('完成',flush=True)



print('初始化',end='...',flush=True)
directory_path = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')+'/'
os.makedirs(directory_path+'download/',exist_ok=True)
os.makedirs(directory_path+'temp/',exist_ok=True)
requests.packages.urllib3.disable_warnings()
head = {'User-Agent':'NekoViewerV2 (hamster2010@yeah.net)'}
filepath = ''
timer = time.time()-3
picturenum = 1
print('完成',flush=True)



print('配置全局变量',end='...',flush=True)
def delete_files_in_directory(directory):
    files = glob.glob(directory + '/*')
    for file in files:
        os.remove(file)
    os.rmdir(directory)
    return
version = '2.0'
versionvisualable = '2.0 stable'
time.sleep(0.05)
print('完成',flush=True)


print('定义函数',end='...',flush=True)
def download():
    with requests.get("https://nekos.best/api/v2/neko",verify=False,headers=head) as response:
        data = json.loads(response.text)
    data = data['results'][0]
    url = data['url']
    artist = data['artist_name']
    filename = str(hex(random.randint(0, 16**32-1))[2:])+'.png'
    global filepath
    filepath = directory_path+'temp/'+filename
    with open(filepath,'wb') as file:
        with requests.get(url,headers=head,verify=False) as picture:
            file.write(picture.content)
            info = {'artist':artist,'filepath':filepath}
    return info


def show(event):
    global filepath
    global directory_path
    global timer
    global picturenum
    timepast = time.time()-timer
    if timepast < 3:
        print(f'请求过于频繁 冷却时间{round(3-timepast,2)}秒')
        return
    else:
        timer = time.time()
    delete_files_in_directory(directory_path+'temp/')
    os.makedirs(directory_path+'temp/',exist_ok=True)
    cprint(f'图片{picturenum}正在加载',color.PURPLE,end='...')
    info = download()
    img = Image.open(filepath)
    img.show(title='NekoViewer')
    cprint(f'加载完成',color.BULE)
    print(f'作者{info['artist']}')
    picturenum += 1
    return
def save(event): 
    global filepath
    global directory_path
    try:
        assert filepath != ''
    except:
        print('请先按下空格键')
    else:
        img = Image.open(filepath)
        img.save(filepath.replace('/temp/','/download/'))
        cprint(f'已保存 {filepath.replace('/temp/','/download/')}',color.RED)
print('完成',flush=True)
time.sleep(0.05)
clearscreen()




if __name__ == '__main__':
    cprint(f'''猫娘浏览器  version:{versionvisualable}
                                        By Hamster 喵~
    ''',color.CYAN)
    print('按下s保存图片，按下空格切换下一只,关闭窗口以退出')


    keyboard.on_press_key('s',callback=save,suppress=True)
    keyboard.on_press_key('space',callback=show,suppress=True)
    keyboard.wait()
