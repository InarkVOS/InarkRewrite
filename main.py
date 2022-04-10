import os
import platform
python = "python3"
if platform.system() == "Windows": python = "python"
if os.path.exists('.btsctr'):
    os.system(f'{python} boot.py nfirst')
else:
    os.system(f'{python} boot.py first')