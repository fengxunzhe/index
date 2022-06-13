
host = '192.168.58.133'

username = "administrator"

password = "Wh123456"

   try:
   
      # with方式，使用后自动close连接
      
       with SMBConnection(username, password, "", remote_name="cs", domain="WORKGROUP", use_ntlm_v2=True, is_direct_tcp=True) as conn:
       
            result = conn.connect(host, 445)  # smb协议默认端口445
            
            if result:
            
                print("登录成功")
                
                shares = conn.listShares()
                
host = '192.168.58.133'

username = "administrator"

password = "Wh123456"

    try:
    
        # with方式，使用后自动close连接
        
        with SMBConnection(username, password, "", remote_name="cs", domain="WORKGROUP", use_ntlm_v2=True, is_direct_tcp=True) as conn:
        
            result = conn.connect(host, 445)  # smb协议默认端口445
            
            if result:
            
                print("登录成功")
                
                shares = conn.listShares()
                

#### 解决SMB报错问题

###### 错误1、TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败
       在SMBConnection中加入is_direct_tcp=True

###### 错误2、无法列出共享：无法连接到 IPC$
       在SMBConnection中加入 remote_name="cs", domain="WORKGROUP",
       
###### 几种远程服务器方法
   
   1、paramiko   需安装SSH 开放22 端口   不行
   
   2、telentlib     需开启telent服务   不行
   
   3、wmic   无法回显命令行结果。执行net 命令有问题  不行
   
   4、winrm  可行
   
---------------------【SMB连接】-------------------------------------------
# -*- coding: utf-8 -*-

# 依赖安装
# pip3 install pysmb pyasn1

# 特殊提醒目录或文件名不要用smb、smb.py,否则会和引用包冲突
import os
import traceback
from smb.SMBConnection import SMBConnection
from smb.base import SharedDevice

# 全部共享文件夹目录，缓存用
shared_dirs = []


# 遍历
def walk_path(dir, path):
    dirs = []
    files = []
    print('Walking path:', path)
    os.system('pause')
    for p in conn.listPath(dir, path):
        # 排除.和..
        if p.filename != '.' and p.filename != '..':
            parentPath = path
            if not parentPath.endswith('/'):
                parentPath += '/'
            if p.isDirectory:
                # print('{}{}'.format(path,p.filename))
                # dirs.append('{}{}'.format(path,p.filename))
                dirs.append(p.filename)
                # 递归，如果单层显示，可以不用！！！
                walk_path(dir, parentPath + p.filename)
            else:
                # print('{}'.format(p.filename))
                files.append(p.filename)
        else:
            # print("特殊目录：",p.filename)
            pass
    # 排序文件夹和文件
    dirs.sort()
    files.sort()

    print('----[文件夹]----')
    for dir in dirs:
        print(dir)
    print('----[文件]----')
    for file in files:
        print(file)


   if __name__ == "__main__":

    # ip或域名
    host = 'Phu2pid1'
    username = "L10570009"
    password = "Wh123456"
    try:
        # with方式，使用后自动close连接
        with SMBConnection(username, password, "", use_ntlm_v2=True, is_direct_tcp=True, remote_name="Phu2pid1", domain="YMTC.LOCAL") as conn:
            result = conn.connect(host, 445)  # smb协议默认端口445
            if result:
                print("登录成功")
                shares = conn.listShares()


                for share in shares:
                    # 只记录共享文件夹
                    print(share.type, share.name)
                    os.system('pause')
                    if share.type == SharedDevice.DISK_TREE:
                        shared_dirs.append({'name': share.name, 'comments': share.comments})

                        # print(share.comments)  介绍
                    # 其他共享 如打印机 IPC$ 等
                    else:
                        # print(share.name)
                        # print(share.comments )
                        pass


                print("shared_dirs", shared_dirs)
                # 有共享文件夹时候才遍历
                if len(shared_dirs) > 0:
                    for dir in shared_dirs:
                        print("共享文件夹：", dir)
                        shared_folder = dir['name']
                        # 调用遍历方法
                        walk_path(dir['name'], '/')
                else:
                    print("没有发现共享文件夹")

            else:
                print("登录失败")
    except Exception as e:
        print("连接异常:")
        traceback.print_exc()
        print(e)
        
----------------------------------------------



