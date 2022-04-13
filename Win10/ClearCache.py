from pathlib import Path
import getpass
import os, re, os.path
import ctypes
from time import sleep
from progress.bar import Bar

print('清理缓存中...')
username = getpass.getuser()
print('用户名： '+username)

def getSizeInNiceString(sizeInBytes):
    """
    Convert the given byteCount into a string like: 9.9bytes/KB/MB/GB
    """
    for (cutoff, label) in [(1024*1024*1024, "GB"),
                            (1024*1024, "MB"),
                            (1024, "KB"),
                            ]:
        if sizeInBytes >= cutoff:
            return "%.1f %s" % (sizeInBytes * 1.0 / cutoff, label)

    if sizeInBytes == 1:
        return "1 byte"
    else:
        bytes = "%.1f" % (sizeInBytes or 0,)
        return (bytes[:-2] if bytes.endswith('.0') else bytes) + ' bytes'

def countFile(dir):
    tmp = 0
    try:
        for item in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, item)):
                tmp += 1
            else:
                tmp += countFile(os.path.join(dir, item))
    except:
        return tmp
    return tmp

def removefiles(Path):
    '''删除指定目录所有文件和文件夹'''
    if(os.path.exists(Path)):
        with Bar('清理中...',max=countFile(Path)) as bar:
            for root, dirs, files in os.walk(Path):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                        bar.next()
                    except:
                        bar.next()
                        pass
                          

                
'''
Test_directory = Path(r'C:\123')
Test_size=sum(f.stat().st_size for f in Test_directory.glob('**/*') if f.is_file())
print('清理补丁更新缓存： ')
print('缓存文件大小： '+getSizeInNiceString(Test_size))
removefiles(Test_directory)
'''
#cmd="start /wait \\\\ypub\\Software\\ymtc\\freeMemory.exe"
#os.system(cmd)
#print("已清理内存!")

WinUP_directory = Path(r'C:\Windows\SoftwareDistribution\Download')
WinUP_size=sum(f.stat().st_size for f in WinUP_directory.glob('**/*') if f.is_file())
print('清理补丁更新缓存： ' ,WinUP_size)
print('缓存文件大小： '+getSizeInNiceString(WinUP_size))
removefiles(WinUP_directory)


SCCM_directory = Path(r'C:\Windows\ccmcache')
SCCM_size=sum(f.stat().st_size for f in SCCM_directory.glob('**/*') if f.is_file())
print('清理SCCM缓存： ')
print('缓存文件大小： '+getSizeInNiceString(SCCM_size))
removefiles(SCCM_directory)


Google_directory = Path('C:\\Users\\'+username+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache')

Google_size=sum(f.stat().st_size for f in Google_directory.glob('**/*') if f.is_file())
print('清理谷歌浏览器缓存： ')
print('缓存文件大小：'+getSizeInNiceString(Google_size))
removefiles(Google_directory)


IE_directory = Path('C:\\Users\\'+username+'\\AppData\\Local\\Microsoft\\Windows\\INetCache')
IE_size=sum(f.stat().st_size for f in IE_directory.glob('**/*') if f.is_file())
print('清理IE浏览器缓存： ')
print('缓存文件大小：'+getSizeInNiceString(IE_size))
removefiles(IE_directory)

FireFox_directory = Path('C:\\Users\\'+username+'\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\55qckifp.default\\cache2')
FireFox_size=sum(f.stat().st_size for f in FireFox_directory.glob('**/*') if f.is_file())
print('清理火狐浏览器缓存： ')
print('缓存文件大小：'+getSizeInNiceString(FireFox_size))
removefiles(FireFox_directory)

Personal_directory = Path('C:\\Users\\'+username+'\\AppData\\Local\\Temp')
Personal_size=sum(f.stat().st_size for f in Personal_directory.glob('**/*') if f.is_file())
print('清理个人临时文件： ')
print('缓存文件大小：'+getSizeInNiceString(Personal_size))
removefiles(Personal_directory)


IUI_directory = Path('C:\\Users\\'+username+'\\AppData\\Local\\Apps\\2.0')
IUI_size=sum(f.stat().st_size for f in Personal_directory.glob('**/*') if f.is_file())
print('清理IUI临时文件： ')
print('缓存文件大小：'+getSizeInNiceString(IUI_size))
removefiles(IUI_directory)

sum_size=IUI_size+Personal_size+FireFox_size+IE_size+Google_size+SCCM_size+WinUP_size
print('已清理缓存总大小： '+getSizeInNiceString(sum_size))
ctypes.windll.user32.MessageBoxW(0, "已清理缓存： "+getSizeInNiceString(sum_size), "清理缓存", 1)

