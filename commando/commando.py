import subprocess
import logging
import sys


logger = logging.getLogger(__name__)


class Commando:
    """Provide ths commando methods.
    """

    def __init__(self):
        self.__commands = []

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
                try:
                    proc = subprocess.run(cmd, check=True, capture_output=True)
                    stdout = proc.stdout.decode(sys.getfilesystemencoding())
                    # 特に表示するものがないときは logging いらんよね?
                    if stdout != "":
                        logger.info(stdout)
                except subprocess.CalledProcessError as e:
                    logger.exception(e.stderr.decode(
                        sys.getfilesystemencoding()))
                    sys.exit(1)
        # execute が完了したら commands の要素をすべて削除する
        self.__commands.clear()
