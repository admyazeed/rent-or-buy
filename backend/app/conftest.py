import os
import sys

HERE = os.path.abspath(os.path.dirname(__file__))
BACKEND_ROOT = os.path.abspath(os.path.join(HERE, ".."))

if BACKEND_ROOT not in sys.path:
    sys.path.insert(0, BACKEND_ROOT)
