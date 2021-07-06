import logging

from commando import commando as cmd

logging.basicConfig(level=logging.DEBUG)

print(cmd.run(["ls", "commando"]))
