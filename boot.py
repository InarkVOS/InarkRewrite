import sys,getpass,hashlib,os

if 'first' in sys.argv:
    print("Welcome to InarkOS this installer will guide you over the things you need to know about the os!")
    if os.name == "nt":
        os.system('py -m pip install -r depencies')
    else:
        os.system('python3 -m pip install -r depencies')
    print("We installed the depencies for you we can set up your user now!")
    dialog = input('Please tell me what username you want to use: ')
    print(f'Welcome {dialog}!')
    pdialog = getpass.getpass('What password do you want to use (the password doesnt show while typing)?:')
    print("Please hold on your user experience is getting set up...")
    encp = pdialog.encode()
    d = hashlib.sha256(encp)
    hash = d.hexdigest()
    os.mkdir(f'usr/{dialog}')
    writer = open(f'usr/{dialog}/pswd', 'w')
    writer.write(hash)
    writer.close()
    test = open('.btsctr', 'w')
    test.close()
    writer_1 = open(f'.linfo', 'w')
    writer_1.write(dialog)
    writer_1.close()
    hostname = input('Please tell me what hostname you want to use: ')
    writer_2 = open(f'conf/hostname', 'w')
    writer_2.write(hostname)
    writer_2.close()
elif 'nfirst' in sys.argv:
    os.remove('.linfo')
    print("Please log in.")
    dialog = input("Username: ")
    pdialog = getpass.getpass("Password: ")
    reader = open(f'usr/{dialog}/pswd', 'r')
    t = reader.read()
    encp = pdialog.encode()
    d = hashlib.sha256(encp)
    hash = d.hexdigest()
    writer_1 = open(f'.linfo', 'w')
    writer_1.write(dialog)
    writer_1.close()
    if t == hash:
        print("Welcome back!")
        from bin.commandhandler import *
    else:
        print("Wrong password!")
        sys.exit()
else:
    print("Please run the bootfile with argument: first or nfirst.")