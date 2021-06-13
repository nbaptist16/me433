import csv
import matplotlib.pyplot as plt
import numpy as np

# import data A - D
ta = [] # column 0
data1a = [] # column 1

tb = [] # column 0
data1b = [] # column 1

tc = [] # column 0
data1c = [] # column 1

td = [] # column 0
data1d = [] # column 1

with open('sigA.csv') as fa:
    # open the csv file
    readera = csv.reader(fa)
    for rowa in readera:
        # read the rows 1 one by one
        ta.append(float(rowa[0])) # leftmost column
        data1a.append(float(rowa[1])) # second column
sratea = len(data1a)/(ta[-1] - ta[0])

with open('sigB.csv') as fb:
    # open the csv file
    readerb = csv.reader(fb)
    for rowb in readerb:
        # read the rows 1 one by one
        tb.append(float(rowb[0])) # leftmost column
        data1b.append(float(rowb[1])) # second column
srateb = len(data1b)/(tb[-1] - tb[0])

with open('sigC.csv') as fc:
    # open the csv file
    readerc = csv.reader(fc)
    for rowc in readerc:
        # read the rows 1 one by one
        tc.append(float(rowc[0])) # leftmost column
        data1c.append(float(rowc[1])) # second column
sratec = len(data1c)/(tc[-1] - tc[0])

with open('sigD.csv') as fd:
    # open the csv file
    readerd = csv.reader(fd)
    for rowd in readerd:
        # read the rows 1 one by one
        td.append(float(rowd[0])) # leftmost column
        data1d.append(float(rowd[1])) # second column
srated = len(data1d)/(td[-1] - td[0])


# dt = 1.0/10000.0 # 10kHz
# t = np.arange(0.0, 1.0, dt) # 10s
# # a constant plus 100Hz and 1000Hz
# s = 4.0 * np.sin(2 * np.pi * 100 * t) + 0.25 * np.sin(2 * np.pi * 1000 * t) + 25

# Fs = 10000 # sample rate
# Ts = 1.0/Fs; # sampling interval
# ts = np.arange(0,t[-1],Ts) # time vector
# y = s # the data to make the fft from
# n = len(y) # length of the signal
# k = np.arange(n)
# T = n/Fs
# frq = k/T # two sides frequency range
# frq = frq[range(int(n/2))] # one side frequency range
# Y = np.fft.fft(y)/n # fft computing and normalization
# Y = Y[range(int(n/2))]

# fig, (ax1, ax2) = plt.subplots(2, 1)
# ax1.plot(t,y,'b')
# ax1.set_xlabel('Time')
# ax1.set_ylabel('Amplitude')
# ax2.loglog(frq,abs(Y),'b') # plotting the fft
# ax2.set_xlabel('Freq (Hz)')
# ax2.set_ylabel('|Y(freq)|')
# plt.show()



# plot sigA
Fsa = sratea
Tsa = 1.0/Fsa; # sampling interval
tsa = np.arange(0,ta[-1],Tsa) # time vector
ya = data1a # the data to make the fft from
na = len(ya) # length of the signal
ka = np.arange(na)
Ta = na/Fsa
frqa = ka/Ta # two sides frequency range
frqa = frqa[range(int(na/2))] # one side frequency range
Ya = np.fft.fft(ya)/na # fft computing and normalization
Ya = Ya[range(int(na/2))]

figa, (ax1a, ax2a) = plt.subplots(2, 1)
# plt.title("sigA: [Signal v Time] and [FFT] plots")
ax1a.title.set_text('sigA: [Signal v Time] plot')
ax1a.plot(ta,ya,'b')
ax1a.set_xlabel('Time')
ax1a.set_ylabel('Amplitude')
figa.subplots_adjust(hspace=0.5)

ax2a.loglog(frqa,abs(Ya),'b') # plotting the fft
ax2a.title.set_text('sigA: [FFT] plot')
ax2a.set_xlabel('Freq (Hz)')
ax2a.set_ylabel('|Y(freq)|')



# plot sigB
Fsb = srateb
Tsb = 1.0/Fsb; # sampling interval
tsb = np.arange(0,tb[-1],Tsb) # time vector
yb = data1b # the data to make the fft from
nb = len(yb) # length of the signal
kb = np.arange(nb)
Tb = nb/Fsb
frqb = kb/Tb # two sides frequency range
frqb = frqb[range(int(nb/2))] # one side frequency range
Yb = np.fft.fft(yb)/nb # fft computing and normalization
Yb = Yb[range(int(nb/2))]

figb, (ax1b, ax2b) = plt.subplots(2, 1)
ax1b.title.set_text('sigB: [Signal v Time] plot')
ax1b.plot(tb,yb,'b')
ax1b.set_xlabel('Time')
ax1b.set_ylabel('Amplitude')
figb.subplots_adjust(hspace=0.5)

ax2b.loglog(frqb,abs(Yb),'b') # plotting the fft
ax2b.title.set_text('sigB: [FFT] plot')
ax2b.set_xlabel('Freq (Hz)')
ax2b.set_ylabel('|Y(freq)|')



# plot sigC
Fsc = sratec
Tsc = 1.0/Fsc; # sampling interval
tsc = np.arange(0,tc[-1],Tsc) # time vector
yc = data1c # the data to make the fft from
nc = len(yc) # length of the signal
kc = np.arange(nc)
Tc = nc/Fsc
frqc = kc/Tc # two sides frequency range
frqc = frqc[range(int(nc/2))] # one side frequency range
Yc = np.fft.fft(yc)/nc # fft computing and normalization
Yc = Yc[range(int(nc/2))]

figc, (ax1c, ax2c) = plt.subplots(2, 1)
ax1c.title.set_text('sigC: [Signal v Time] plot')
ax1c.plot(tc,yc,'b')
ax1c.set_xlabel('Time')
ax1c.set_ylabel('Amplitude')
figc.subplots_adjust(hspace=0.5)

ax2c.loglog(frqc,abs(Yc),'b') # plotting the fft
ax2c.title.set_text('sigC: [FFT] plot')
ax2c.set_xlabel('Freq (Hz)')
ax2c.set_ylabel('|Y(freq)|')



# plot sigD
Fsd = srated
Tsd = 1.0/Fsd; # sampling interval
tsd = np.arange(0,td[-1],Tsd) # time vector
yd = data1d # the data to make the fft from
nd = len(yd) # length of the signal
kd = np.arange(nd)
Td = nd/Fsd
frqd = kd/Td # two sides frequency range
frqd = frqd[range(int(nd/2))] # one side frequency range
Yd = np.fft.fft(yd)/nd # fft computing and normalization
Yd = Yd[range(int(nd/2))]

figd, (ax1d, ax2d) = plt.subplots(2, 1)
ax1d.title.set_text('sigD: [Signal v Time] plot')
ax1d.plot(td,yd,'b')
ax1d.set_xlabel('Time')
ax1d.set_ylabel('Amplitude')
figd.subplots_adjust(hspace=0.5)

ax2d.loglog(frqd,abs(Yd),'b') # plotting the fft
ax2d.title.set_text('sigD: [FFT] plot')
ax2d.set_xlabel('Freq (Hz)')
ax2d.set_ylabel('|Y(freq)|')

plt.show()