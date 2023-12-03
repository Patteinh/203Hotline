#!/usr/bin/env python3
import sys
from src.utils import *
from src.check_errors import *
from src.hotline import *

if __name__ == '__main__':
    try:
        check_args(len(sys.argv), sys.argv)
        hotline(int(sys.argv[1]), None if len(sys.argv) == 2 else int(sys.argv[2]))
    except Exception as message:
        print(message, file=sys.stderr)
        sys.exit(84)