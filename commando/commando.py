import logging
import subprocess
import sys
from typing import Any, Callable, List, Union

from commando.util import str_to_list

logger = logging.getLogger(__name__)

Command = Union[str, List[str], Callable[..., Any]]


class Commando:
    """Provide ths commando methods."""

    def __init__(self):
        self.__commands: List[Command] = []

    def run(self, cmd: Union[str, List[str], Callable[..., Any]]) -> Any:
        """Run your command

        Args:
            cmd (Union[str, List[str], Callable[..., Any]]): command

        Returns:
            Any | CompletedProcess[bytes]: callable return value or CompletedProcess[bytes]
        """
        # 呼び出し可能かどうかで条件分岐
        if callable(cmd):
            try:
                ret = cmd()
            except Exception:
                logger.exception("Runtime error")
                sys.exit(1)
        else:
            ret = self.__execute_subprocess_cmd(cmd)
        return ret

    def add(self, cmd: Union[str, List[str], Callable[..., Any]]):
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

        Note:
            Now do not use this method.
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

    def __execute_subprocess_cmd(self, cmd: Union[str, List[str]]):
        """execute cmd

        Args:
            cmd (str or List): Command string or list.

        Returns:
            str: string stdout.
        """
        if type(cmd) is str:
            cmd = str_to_list(cmd)

        proc = subprocess.run(cmd, check=True, capture_output=True)
        return proc
