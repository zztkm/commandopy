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
            subprocess.run(cmd, shell=True)
