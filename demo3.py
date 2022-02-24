ctionary in python
data = {1:'Ram', 2: 'Krishn', 3: 'Surya'}
data
{1: 'Ram', 2: 'Krishn', 3: 'Surya'}
data[3]
'Surya'
data.get(1)
'Ram'

print(data.get(2))
Krishn

data.get(1, 'Not Found')
'Ram'

data.get(4, 'Not Found')
'Not Found'

keys = ['Arun', 'Krishn', 'Ram']
values = ['Python', 'Java', 'Javascript']

data = zip(keys, values)
data
<zip object at 0x000002E67FD800C0>

data = dict(zip(keys, values))
data
{'Arun': 'Python', 'Krishn': 'Java', 'Ram': 'Javascript'}

data['Krishn']
'Java'

data['Avantika'] = 'C++'
data
{'Arun': 'Python', 'Krishn': 'Java', 'Ram': 'Javascript', 'Avantika': 'C++'}

del data['Arun']
data
{'Krishn': 'Java', 'Ram': 'Javascript', 'Avantika': 'C++'}

prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE', 'NETBEANS', 'JEE': 'ECLIPSE'}}
SyntaxError: expression expected after dictionary key and ':'

prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java' : {'JSE': 'NETBEANS', 'JEE': 'ECLIPSE'}
        prog
        prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE', 'Neatbeans', 'JEE': 'Eclipse'}
                    
            SyntaxError: invalid syntax. Perhaps you forgot a comma?
            prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE': 'NETBEANS', 'JEE': 'ECLIPSE'}
                prog






                KeyboardInterrupt
                prog['JS']
                        
                Traceback (most recent call last):
                  File "<pyshell#152>", line 1, in <module>
                      prog['JS']
                      NameError: name 'prog' is not defined
                      prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE', 'NETBEANS', 'JEE': 'ECLIPSE'}}
                              
                      SyntaxError: expression expected after dictionary key and ':'
                      prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE': 'NETBEANS', 'JEE': 'ECLIPSE'}}
                              
                      prog
                              
                      {'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE': 'NETBEANS', 'JEE': 'ECLIPSE'}}
                      prog['JS']
                              
                      'Atom'

                      prog['Python'][1]
                              
                      'Sublime'

                      prog['Java']
                              
                      {'JSE': 'NETBEANS', 'JEE': 'ECLIPSE'}

                      prog['Java']['JEE']
                        
                      'ECLIPSE'
