import os
import sys
import argparse
import platform

system_type = platform.system()
python_version = platform.python_version()
m, s, _ = python_version.split('.')
path = f'{os.path.dirname(os.path.abspath(__file__))}/{system_type.lower()}/{m}{s}'
print(os.path.exists(path))