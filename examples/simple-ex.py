import logging

from commando import commando

logging.basicConfig(level=logging.DEBUG)

test3 = "test/test3.txt"


def myprint():
    print("------------------------")
    print("Hello Commando !")
    print("------------------------")


commando.add(["mkdir", "test"])

commando.add(["touch", "test/test.txt"])
commando.add(["touch", "test/test2.txt"])
commando.add(["touch", test3])

commando.add(myprint)

commando.add(["ls", "test"])

commando.execute()
