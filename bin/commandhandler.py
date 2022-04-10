import configparser
import platform
import os
config = configparser.ConfigParser()
config.read('apps.ini')

def as_dict():
    dictionary = {}
    for section in config.sections():
        dictionary[section] = {}
        for option in config.options(section):
            dictionary[section][option] = config.get(section, option)
    return dictionary

d = as_dict()

def getProp(property,app):
    prop = d.get(app)
    prop2 = prop.get(property)
    return prop2
def Exists(app):
    if config.has_section(app.lower()):
        return True
    else:
        return False
def openapp(app, args):
    if app == "exit":
        try:
            code = int(args[0])
        except:
            code = 0
        exit(code)
    elif app == "rlprompt":
        init_prompt()
    if Exists(app):
        python = "python" if platform.system() == "Windows" else "python3"
        os.system(f'{python} {getProp("path", app)}')
    else:
        print('Command or application not found!')
def init_prompt():
    reader = open('.linfo', 'r')
    username = reader.read()
    reader.close()
    reader1 = open('conf/hostname', 'r')
    hostname = reader1.read()
    reader1.close()
    global prompt
    prompt = f'{username}@{hostname}> '
init_prompt()
while True:
    inp = input(prompt)
    inp_transformed = inp.split(' ',1)
    inp_onlyargs = inp.split(' ')
    inp_onlyargs.pop(0)
    openapp(inp_transformed[0],inp_onlyargs)