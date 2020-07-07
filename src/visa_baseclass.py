# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:19:34 2020

@author: Administrator
"""
__author__ = "kha"
__version__ = "0.0.1"


import time

import visa


# ===========================================================================
# VISA Exception class
# ===========================================================================
class VISABaseClassException(Exception):
    """ """
    pass

# ===========================================================================
# VISA base class
# ===========================================================================
class VISABaseClass():
    """Implements basic query and write commands to communicate via VISA 
    resource manager
    
    This base class impplements various communication functions like query and 
    write to handle hardware communication via the VISA resourcemanager. This
    class can be used as a parent class for specific hardware classes"""
    
    def __init__(self, protocol, addr):
        self.protocol = protocol
        self.addr = addr
        self._open()
        
    def _open(self):
        rm = visa.ResourceManager()
        full_addr = '::'.join([self.protocol, self.addr, "INSTR"])
        self.inst = rm.open_resource(full_addr)
        
    def close(self):
        self.inst.close()
        
    def _query(self, scpi_cmd, verbose=False):
        """sends scpi_cmd to hardware by passing it to instrument query
        
        Example:
        >>>> awg = Keysight33600A('FDN-AWG.local::inst0')
        >>> awg._query('*IDN?')
        ... 'Agilent Technologies,33612A,MY53401500,A.02.02-2.40-03-64-02\n'
        
        """
        if verbose: print('query: ', scpi_cmd)
        rtn = self.inst.query(scpi_cmd)
        
        if rtn[-1] == '\n':   # remove newline character if present
            rtn = rtn[:-1]
        
        return rtn
     
    def query(self, scpi_cmds, **kwargs):
        """sends list of scpi_cmd to instrument
        
        """
        rtn = []
        if type(scpi_cmds) == str:
            return self._query(scpi_cmds, **kwargs)
        elif type(scpi_cmds) == list:
            for scpi_cmd in scpi_cmds:
                rtn.append(
                    self._query(scpi_cmd, **kwargs)
                )
        else:
            raise VISABaseClassException(
                'scpi_cmds filetype: {} is not valid'.format(type(scpi_cmds))
            )
        
        return rtn
    
    def _write(self, scpi_cmd, verbose=False):
        """sends scpi command to hardaware py passing it to instrument write"""
        if verbose: print('write: ', scpi_cmd)
        rtn = self.inst.write(scpi_cmd)
        return rtn
    
    def write(self, scpi_cmds, **kwargs):
        rtn = []
        if type(scpi_cmds) == str:
            return self._write(scpi_cmds, **kwargs)
        elif type(scpi_cmds) == list:
            for scpi_cmd in scpi_cmds:
                rtn.append(
                    self._write(scpi_cmd, **kwargs)
                )
                time.sleep(0.05)
        else:
            raise VISABaseClassException(
                'scpi_cmds filetype: {} is not valid'.format(type(scpi_cmds))
            )
        return rtn
    
    def read_raw(self):
        return self.inst.read_raw()
    
    def get_chunk_size(self):
        return self.inst.chunk_size
    
    def set_chunk_size(self, chunk_size):
        self.inst.chunk_size = chunk_size