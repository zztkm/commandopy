import subprocess


class Commando:

    def __init__(self):
        self.__commands = []

    def add(self, cmd):
        self.__commands.append(cmd)

    def list(self):
        return self.__commands

    def execute(self):
        commands = self.__commands
        for cmd in commands:

            # 呼び出し可能かどうかで条件分岐
            if callable(cmd):
                # 返り値は特に受け取らない
                cmd()
            else:
                subprocess.run(cmd, check=True)
