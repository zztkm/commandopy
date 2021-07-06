import logging
import subprocess
import sys

from commando.util import str_to_list

logger = logging.getLogger(__name__)


class Commando:
    """Provide ths commando methods.
    """

    def __init__(self):
        self.__commands = []

    def run(self, cmd: str) -> str:
        """[summary]

        Args:
            cmd (str): Command string.

        Returns:
            str: stdout.
        """
        return self.__execute_subprocess_cmd(cmd)

    def add(self, cmd):
        """Add command

        Args:
            cmd (str or callable): Command string or callable you want to execute.
        """
        self.__commands.append(cmd)

    def list(self):
        """return commands list

        Returns:
            list: List of added commands.
        """
        return self.__commands

    def execute(self):
        """Execute the added command.
        """
        commands = self.__commands
        for cmd in commands:
            logger.debug(cmd)
            # 呼び出し可能かどうかで条件分岐
            if callable(cmd):
                try:
                    cmd()
                except Exception:
                    logger.exception("Runtime error")
                    sys.exit(1)
            else:
                stdout = self.__execute_subprocess_cmd(cmd)
                print(stdout)
        # execute が完了したら commands の要素をすべて削除する
        self.__commands.clear()

    def __execute_subprocess_cmd(self, cmd) -> str:
        """execute cmd

        Args:
            cmd (str or List): Command string or list.

        Returns:
            str: string stdout.
        """
        if type(cmd) is str:
            cmd = str_to_list(cmd)
        try:
            proc = subprocess.run(cmd, check=True, capture_output=True)
            stdout = proc.stdout.decode(sys.getfilesystemencoding())
            stderr = proc.stderr.decode(sys.getfilesystemencoding())
            if stderr != "":
                logger.info(stderr)
            return stdout
        except subprocess.CalledProcessError as e:
            # logging stderr
            logger.exception(e.stderr.decode(
                sys.getfilesystemencoding()))
            sys.exit(e.returncode)
