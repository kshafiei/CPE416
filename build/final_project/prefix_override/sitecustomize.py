import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/calpoly/gobilda/gobilda_ws/install/final_project'
