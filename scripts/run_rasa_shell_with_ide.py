"""This script allows use of an IDE (VS Code, Wing, Pycharm, ...) to run the rasa shell command:
(-) Place this script in root of Rasa bot project
(-) Open & run it from within your IDE
(-) In Wing, use External Console for better experience.
"""

import os
import sys

# insert path of this script in syspath so custom modules will be found
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))

# run the command:
#  $ rasa shell --enable-api --debug
sys.argv.append("shell")
sys.argv.append("--debug")


if __name__ == "__main__":
    from rasa.__main__ import main

    main()
