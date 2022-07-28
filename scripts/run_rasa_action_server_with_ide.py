r"""This script allows use of an IDE (VS Code, Wing, Pycharm, ...) to debug custom actions:
(-) Place this script in root of Rasa bot project or same location as your actions.py
(-) Open & run it from within your IDE
"""

import os
import sys

# insert the action folder in syspath
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))

# Run the command:
#  $ rasa run actions --port 5055 --debug
sys.argv.append("run")
sys.argv.append("actions")
sys.argv.append("--actions")
sys.argv.append("actions")
sys.argv.append("--port")
sys.argv.append("5055")  # change port if needed
sys.argv.append("--debug")

if __name__ == "__main__":
    from rasa.__main__ import main

    main()
