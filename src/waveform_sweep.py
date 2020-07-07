# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:08:07 2020

@author: Administrator
"""

import time

import numpy as np

from keysight33600a import Keysight33600A
from sds1202XE_code import get_waveform, get_both_waveforms, save_wf
from sds1202xe import SDS1202XE


protocol = 'TCPIP'
addr = 'FDN-AWG.local::inst0'
awg = Keysight33600A(protocol, addr)

protocol = 'USB0'
addr = '0xF4ED::0xEE3A::SDS1ECDX2R3290'
sds = SDS1202XE(protocol, addr)


# =======
# sweep waveforms
# =======

freq_lst = [100,200,300,400,500,600,700,800,900]+[1000,2000,3000,4000,5000,6000,7000,8000,9000]+[10000,11000,12000,13000,14000,15000,16000]

#freq_lst = np.linspace(1000,20000, 21)

for freq in freq_lst:
    awg.set_output1_on()
    awg.set_sin_waveform(channel=1, freq=freq, volt=10, phase=0)
#    time.sleep(10)
    t1,v1, t2, v2 = sds.acquire_both_waveform()
    save_wf(t1, v1, '20-07-03_ch1_wf-sin_freq-{:.3e}.json'.format(freq))
    save_wf(t2, v2, '20-07-03_ch2_wf-sin_freq-{:.3e}.json'.format(freq))
#    time.sleep(1)
    print('freq: ', freq)

awg.set_output1_off()