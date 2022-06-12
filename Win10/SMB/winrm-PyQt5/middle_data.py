import winrm
from winrm.protocol import Protocol


class Pane(winrm.Session, object):  # 继承父类，修改代码，解决编码问题

    def __init__(self, target, auth, **kwargs):
        super().__init__(target, auth, **kwargs)
        username, password = auth
        self.url = self._build_url(target, kwargs.get('transport', 'plaintext'))
        self.protocol = Protocol(self.url,
                                 username=username, password=password, **kwargs)

    def run_cmd(self, command, args=()):
        # TODO optimize perf. Do not call open/close shell every time
        shell_id = self.protocol.open_shell(codepage=936)
        command_id = self.protocol.run_command(shell_id, command, args)
        rs = winrm.Response(self.protocol.get_command_output(shell_id, command_id))
        self.protocol.cleanup_command(shell_id, command_id)
        self.protocol.close_shell(shell_id)
        return rs

    def res_Online(self):

        pass



if __name__ == '__main__':

    """s = Pane('192.168.58.133:5985', auth=('administrator', 'Wh123456'), transport='ntlm')

    # s = winrm.Session('192.168.58.133:5985', auth=('administrator', 'Wh123456'), transport='ntlm')
    # r = s.run_cmd('ipconfig', ['/all'])
    r = s.run_cmd('openfiles')  # Openfiles /?

    code = r.status_code

    content = r.std_out if code == 0 else r.std_err
    import chardet

    try:
        print(chardet.detect(content))  # 检测server的编码格式
        result = content.decode("GB2312")
        print(result)
    except:
        result = content.decode("GBK")"""