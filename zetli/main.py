import sys
from zetli.command_dispatcher import CommandDispatcher

def main():
    CommandDispatcher(sys.argv).run()