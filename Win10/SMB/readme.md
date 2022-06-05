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
