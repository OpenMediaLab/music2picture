# -*- coding: cp936 -*-
from pylab import *
import numpy as np
nSampleNum = 5120
ncount = 2048.0
df = nSampleNum / ncount
sampleTime = ncount / nSampleNum
freqLine = 1500

x = np.linspace(0,sampleTime,ncount)#ʱ����x������
sinx = np.sin(2*pi*250*x)
sinx2 = 0.5*np.sin(2*pi*500*x)
sinx3 = 0.3*np.sin(2*pi*2500*x)    #������������׼���Ҳ���

sinx += sinx2
sinx += sinx3  #����һ��ʱ����

fft = np.fft.fft(sinx)[0:freqLine]  #����fft�任�㷨����Ƶ����
fftx = np.linspace(0,df*freqLine,freqLine)  #Ƶ����x������311)
plot(x,sinx)
xlabel('time(s)')
ylabel('amplitude')
title('time domain graph')

subplot(313)
plot(fftx,abs(fft))
xlabel('freqency(Hz)')
ylabel('amplitude')
title('frequency domain graph')

show()
