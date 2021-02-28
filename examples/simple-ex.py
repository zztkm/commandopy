from commando import commando


def myprint():
    print("------------------------")
    print("Hello Commando !")
    print("------------------------")


commando.add("mkdir test")

commando.add(["touch", "test\\test.txt"])
commando.add(["touch", "test\\test2.txt"])

commando.add(myprint)

commando.add("ls test")

commando.execute()
