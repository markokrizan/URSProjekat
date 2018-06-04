'''
Created on Jun 4, 2018

@author: Freeman
'''

import os
cur_path = os.getcwd()
ignore_set = set(["__init__.py", "count_sourcelines.py"])

loclist = []

for pydir, _, pyfiles in os.walk(cur_path):
    for pyfile in pyfiles:
        if pyfile.endswith(".py") and pyfile not in ignore_set:
            totalpath = os.path.join(pydir, pyfile)
            loclist.append( ( len(open(totalpath, "r").read().splitlines()),
                               totalpath.split(cur_path)[1]) )

for linenumbercount, filename in loclist: 
    print (str(linenumbercount) + " linije u " +  str(filename))

#print ("\nTotal: %s lines (%s)" % sum([x[0] for x in loclist]), cur_path)
print('\nUkupno: ' + str(sum([x[0] for x in loclist])) + " linije u " + str(cur_path))
