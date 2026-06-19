A simple note taking CLI tool to manage tasks, should work regardless of the OS you're using.

Install:

`uv tool install git+https://github.com/waikoo/zetli`

`pipx install git+https://github.com/waikoo/zetli`


Usage:
```
zetli add drink water # adds a task called "drink water" (no need to use "", but you also can use them if you want to)
zetli done 1          # deletes task with id #1
zetli boom            # deletes all tasks
zetli OR zetli show   # shows all tasks
```
