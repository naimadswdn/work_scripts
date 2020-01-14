Set of tools to make our work easier and faster :) 

Requirements: \
Python 3.6 (or newest) \
Git

Python packages:\
wmi \
pywin32\
pandas\
cx_Oracle\
xlwt\
pyodbc\

How to set up environment?

Go to your python directory (for me it is C:\Python36) and open cmd. 

Run below command: 

```cmd
python.exe -m venv env
```

where env is the location of newly created virtual enviroment. \
In my exaxmple I replaced env with C:\Users\xxx\Documents\venv:

```cmd
python.exe -m venv C:\Users\xxx\Documents\venv
```

Then, using cmd go the the newly created virtual environment directory and install packages: 


```cmd
cd C:\Users\xxx\Documents\venv\Scripts
pip.exe install wmi pywin32 pandas cx_Oracle xlwt pyodbc
```

After that your virtual enviroment is ready and you can active it by running active script: 

```cmd
C:\Users\xxx\Documents\venv\Scripts>activate
```

To clone repository content run:

```cmd
git clone xxx
```
