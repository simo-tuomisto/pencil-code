# $Id: param.py,v 1.1 2007-11-16 13:57:04 joishi Exp $
"""
param.py -- reads parameters from the f90 namelists
Author: J. Oishi (joishi@amnh.org)

REQUIRES: nl2python perl script (based on Wolfgang Dobler's nl2idl script)

todo: think about single/double precision; make things into numpy arrays?
"""
import numpy as N
import os

def read_param(datadir='data/',param2=False):

    if (not datadir.endswith('/')): datadir += '/'
    datadir = os.path.expanduser(datadir)

    if (param2):
        filen = datadir+'/param2.nml'
    else:
        filen = datadir+'/param.nml'

    # will need to read dim.dat to deal with precision, should that be necessary
    #dim = read_dim(datadir)

    # execute output of nl2python script
    if (not os.path.exists(filen)):
        print "read_param: no such file",filen
        return -1
    
    cmd = 'nl2python '+filen
    script = os.popen(cmd).read()
    print script;
    if (len(script) != 0):
        exec(script)
    else:
        print "read_param: nl2python returned nothing! is $PENCIL_HOME/bin in the path?"
        return -1
    
    ret = Params() # par is the name of the class

    return ret

if __name__ == '__main__':
   print self.__doc__ 
