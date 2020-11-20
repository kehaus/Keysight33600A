# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:49:48 2020


Reference links
 - http://rfmw.em.keysight.com/bihelpfiles/Trueform/webhelp/US/Content/__I_SCPI/VOLTage_Subsystem.htm#VOLTage
 - Sine waveform: http://rfmw.em.keysight.com/bihelpfiles/Trueform/webhelp/US/Content/_Programming%20Examples_/01%20-%20Configure%20a%20Sine%20Wave.htm
 
 


"""
__author__ = "kha"
__version__ = "0.0.1"


from visa_baseclass import VISABaseClass

# ===========================================================================
# Keysight 33600A waveform generator
# ===========================================================================
class Keysight33600AException(Exception):
    """ """
    pass


class Keysight33600A(VISABaseClass):
    """class represents the Keysight 33600A waveform generator inside python
    
    Example
    >>> protocol = 'TCPIP'
    >>> addr = 'FDN-AWG.local
    >>> awg = Keysight33600A(protocol, addr)

    """
    
#    def __init__(self, addr):
#        
#        self.protocol = "TCPIP"
#        self.addr = addr
#        self._open()
#        
#    def _open(self):
#        rm = visa.ResourceManager()
#        full_addr = '::'.join([self.protocol, self.addr, "INSTR"])
#        self.inst = rm.open_resource(full_addr)
#        
#    def close(self):
#        self.inst.close()
#        
#    def _query(self, scpi_cmd, verbose=False):
#        """sends scpi_cmd to hardware by passing it to instrument query
#        
#        Example:
#        >>>> awg = Keysight33600A('FDN-AWG.local::inst0')
#        >>> awg._query('*IDN?')
#        ... 'Agilent Technologies,33612A,MY53401500,A.02.02-2.40-03-64-02\n'
#        
#        """
#        if verbose: print('query: ', scpi_cmd)
#        rtn = self.inst.query(scpi_cmd)
#        return rtn
#     
#    def query(self, scpi_cmds, **kwargs):
#        """sends list of scpi_cmd to instrument
#        
#        """
#        rtn = []
#        if type(scpi_cmds) == str:
#            return self._query(scpi_cmds, **kwargs)
#        elif type(scpi_cmds) == list:
#            for scpi_cmd in scpi_cmds:
#                rtn.append(
#                    self._query(scpi_cmd, **kwargs)
#                )
#        else:
#            raise Keysight33600AException(
#                'scpi_cmds filetype: {} is not valid'.format(type(scpi_cmds))
#            )
#        return rtn
#    
#    def _write(self, scpi_cmd, verbose=False):
#        """ """
#        if verbose: print('write: ', scpi_cmd)
#        rtn = self.inst.write(scpi_cmd)
#        return rtn
#    
#    def write(self, scpi_cmds, **kwargs):
#        rtn = []
#        if type(scpi_cmds) == str:
#            return self._write(scpi_cmds, **kwargs)
#        elif type(scpi_cmds) == list:
#            for scpi_cmd in scpi_cmds:
#                rtn.append(
#                    self._write(scpi_cmd, **kwargs)
#                )
#                time.sleep(0.05)
#        else:
#            raise Keysight33600AException(
#                'scpi_cmds filetype: {} is not valid'.format(type(scpi_cmds))
#            )
#        return rtn
    
    
    # ======
    # high level commands
    # ======
    
    def get_idn(self):
        scpi_cmd = '*IDN?'
        return self.query(scpi_cmd)
    
    def set_output1_on(self):
        scpi_cmd = "OUTP1 ON"
        return self.write(scpi_cmd)

    def set_output1_off(self):
        scpi_cmd = "OUTP1 OFF"
        return self.write(scpi_cmd)        
        
    def set_output2_on(self):
        scpi_cmd = "OUTP2 ON"
        return self.write(scpi_cmd)
        
    def set_output2_off(self):
        scpi_cmd = "OUTP2 OFF"
        return self.write(scpi_cmd)
    
    def set_sin_waveform(self, channel=1, freq=1e3, volt=1, offset=0, phase=0):
        """sets a sin waveform to the specified channel """
        
        src = "SOURCE{}".format(str(channel))
        scpi_cmds = [
            'FUNC SIN',
            'FREQ {:.6e}'.format(freq),
            'PHASE {}'.format(str(phase)),
            'VOLT {}'.format(str(volt)),
            'VOLT:OFFS {}'.format(str(offset))
        ]
        scpi_cmds = [src+':'+cmd for cmd in scpi_cmds]
        return self.write(scpi_cmds)
    
## =========
## first trial
## =========
#rm = visa.ResourceManager()                         #load the VISA resource manager
#addr = 'FDN-AWG.local::inst0'
#inst = rm.open_resource("TCPIP::"+addr+"::INSTR")   #connect to the device




if __name__ == "__main__":
    
    # ==========
    # test awg class
    # ==========
#    protocol = 'TCPIP'
#    addr = 'FDN-AWG.local::inst0'
#    awg = Keysight33600A(protocol, addr)

    
    pass