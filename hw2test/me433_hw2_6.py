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

# ----------------------------------------------------

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

# added for no. 5
newa = []

for ia in range(len(ya)):
    avga = 0
    suma = 0
    for ja in range(800):
        try:
            suma = suma + ya[ia + ja]
        except:
            continue
    avga = suma/800
    newa.append(avga)

newYa = np.fft.fft(newa)/na # fft computing and normalization
newYa = newYa[range(int(na/2))]


# added for no. 6
new_averagea = []
# Aa = 0.95
# Ba = 0.05
# Aa = 0.996
# Ba = 0.004
Aa = 0.997
Ba = 0.003
# Aa = 0.998
# Ba = 0.002

for aa in range(len(ta)):
    if(aa == 0):
        # new_averaged[ad] = data1d[ad]
        new_averagea.append(data1a[aa])
    else:
        # new_averaged[ad] = Ad * new_averaged[ad-1] + Bd * data1d[ad]
        new_averagea.append(Aa * new_averagea[aa-1] + Ba * data1a[aa])
# new_averaged[i] = Ad * new_averaged[id-1] + Bd * signald[id]
newnewYa = np.fft.fft(new_averagea)/na # fft computing and normalization
newnewYa = newnewYa[range(int(na/2))]


figa, ([ax1a, ax3a], [ax2a, ax4a]) = plt.subplots(2, 2)
ax1a.title.set_text('sigA: [Signal v Time] plot (MAF; avg=800)')
ax1a.plot(ta,ya,'k')
ax1a.plot(ta,newa,'r')
ax1a.set_xlabel('Time')
ax1a.set_ylabel('Amplitude')
figa.subplots_adjust(hspace=0.5)
figa.subplots_adjust(wspace=0.5)


ax2a.loglog(frqa,abs(Ya),'k') # plotting the fft
ax2a.loglog(frqa,abs(newYa),'r') # plotting the fft
ax2a.title.set_text('sigA: [MAF] plot')
ax2a.set_xlabel('Freq (Hz)')
ax2a.set_ylabel('|Y(freq)|')

ax3a.title.set_text('sigA: filtered [Signal v Time] (IIR; A=0.997, B=0.003)')
ax3a.plot(ta,ya,'k')
ax3a.plot(ta,new_averagea,'r')
ax3a.set_xlabel('Time')
ax3a.set_ylabel('Amplitude')

ax4a.loglog(frqa,abs(Ya),'k') # plotting the fft
ax4a.loglog(frqa,abs(newnewYa),'r') # plotting the fft
ax4a.title.set_text('sigA: [IIR] plot')
ax4a.set_xlabel('Freq (Hz)')
ax4a.set_ylabel('|Y(freq)|')



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

# added for no. 5
newb = []

for ib in range(len(yb)):
    avgb = 0
    sumb = 0
    for jb in range(800):
        try:
            sumb = sumb + yb[ib + jb]
        except:
            continue
    avgb = sumb/800
    newb.append(avgb)

newYb = np.fft.fft(newb)/nb # fft computing and normalization
newYb = newYb[range(int(nb/2))]


# added for no. 6
new_averageb = []
# Ab = 0.99
# Bb = 0.01
# Ab = 0.9992
# Bb = 0.0008
Ab = 0.9995
Bb = 0.0005
# Ab = 0.9999
# Bb = 0.0001

for ab in range(len(tb)):
    if(ab == 0):
        # new_averaged[ad] = data1d[ad]
        new_averageb.append(data1b[ab])
    else:
        # new_averaged[ad] = Ad * new_averaged[ad-1] + Bd * data1d[ad]
        new_averageb.append(Ab * new_averageb[ab-1] + Bb * data1b[ab])
# new_averaged[i] = Ad * new_averaged[id-1] + Bd * signald[id]
newnewYb = np.fft.fft(new_averageb)/nb # fft computing and normalization
newnewYb = newnewYb[range(int(nb/2))]


figb, ([ax1b, ax3b], [ax2b, ax4b]) = plt.subplots(2, 2)
ax1b.title.set_text('sigB: [Signal v Time] plot (MAF; avg=800)')
ax1b.plot(tb,yb,'k')
ax1b.plot(tb,newb,'r')
ax1b.set_xlabel('Time')
ax1b.set_ylabel('Amplitude')
figb.subplots_adjust(hspace=0.5)
figb.subplots_adjust(wspace=0.5)


ax2b.loglog(frqb,abs(Yb),'k') # plotting the fft
ax2b.loglog(frqb,abs(newYb),'r') # plotting the fft
ax2b.title.set_text('sigB: [MAF] plot')
ax2b.set_xlabel('Freq (Hz)')
ax2b.set_ylabel('|Y(freq)|')

ax3b.title.set_text('sigB: filtered [Signal v Time] (IIR; A=0.9995, B=0.0005)')
ax3b.plot(tb,yb,'k')
ax3b.plot(tb,new_averageb,'r')
ax3b.set_xlabel('Time')
ax3b.set_ylabel('Amplitude')

ax4b.loglog(frqb,abs(Yb),'k') # plotting the fft
ax4b.loglog(frqb,abs(newnewYb),'r') # plotting the fft
ax4b.title.set_text('sigB: [IIR] plot')
ax4b.set_xlabel('Freq (Hz)')
ax4b.set_ylabel('|Y(freq)|')



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

# added for no. 5
newc = []

for ic in range(len(yc)):
    avgc = 0
    sumc = 0
    for jc in range(2800):
        try:
            sumc = sumc + yc[ic + jc]
        except:
            continue
    avgc = sumc/2800
    newc.append(avgc)

newYc = np.fft.fft(newc)/nc # fft computing and normalization
newYc = newYc[range(int(nc/2))]


# added for no. 6
new_averagec = []
# Ac = 0.95
# Bc = 0.05
Ac = 0.99
Bc = 0.01

for ac in range(len(tc)):
    if(ac == 0):
        # new_averaged[ad] = data1d[ad]
        new_averagec.append(data1c[ac])
    else:
        # new_averaged[ad] = Ad * new_averaged[ad-1] + Bd * data1d[ad]
        new_averagec.append(Ac * new_averagec[ac-1] + Bc * data1c[ac])
# new_averaged[i] = Ad * new_averaged[id-1] + Bd * signald[id]
newnewYc = np.fft.fft(new_averagec)/nc # fft computing and normalization
newnewYc = newnewYc[range(int(nc/2))]


figc, ([ax1c, ax3c], [ax2c, ax4c]) = plt.subplots(2, 2)
ax1c.title.set_text('sigC: [Signal v Time] plot (MAF; avg=2800)')
ax1c.plot(tc,yc,'k')
ax1c.plot(tc,newc,'r')
ax1c.set_xlabel('Time')
ax1c.set_ylabel('Amplitude')
figc.subplots_adjust(hspace=0.5)
figc.subplots_adjust(wspace=0.5)


ax2c.loglog(frqc,abs(Yc),'k') # plotting the fft
ax2c.loglog(frqc,abs(newYc),'r') # plotting the fft
ax2c.title.set_text('sigC: [MAF] plot')
ax2c.set_xlabel('Freq (Hz)')
ax2c.set_ylabel('|Y(freq)|')

ax3c.title.set_text('sigC: filtered [Signal v Time] (IIR; A=0.99, B=0.01)')
ax3c.plot(tc,yc,'k')
ax3c.plot(tc,new_averagec,'r')
ax3c.set_xlabel('Time')
ax3c.set_ylabel('Amplitude')

ax4c.loglog(frqc,abs(Yc),'k') # plotting the fft
ax4c.loglog(frqc,abs(newnewYc),'r') # plotting the fft
ax4c.title.set_text('sigC: [IIR] plot')
ax4c.set_xlabel('Freq (Hz)')
ax4c.set_ylabel('|Y(freq)|')



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

# added for no. 5
newd = []

for id in range(len(yd)):
    avgd = 0
    sumd = 0
    for jd in range(1000):
        try:
            sumd = sumd + yd[id + jd]
        except:
            continue
    avgd = sumd/1000
    newd.append(avgd)

newYd = np.fft.fft(newd)/nd # fft computing and normalization
newYd = newYd[range(int(nd/2))]


# added for no. 6
new_averaged = []
# Ad = 0.95
# Bd = 0.05
Ad = 0.97
Bd = 0.03
# Ad = 0.975
# Bd = 0.025
# Ad = 0.98
# Bd = 0.02

for ad in range(len(td)):
    if(ad == 0):
        # new_averaged[ad] = data1d[ad]
        new_averaged.append(data1d[ad])
    else:
        # new_averaged[ad] = Ad * new_averaged[ad-1] + Bd * data1d[ad]
        new_averaged.append(Ad * new_averaged[ad-1] + Bd * data1d[ad])
# new_averaged[i] = Ad * new_averaged[id-1] + Bd * signald[id]
newnewYd = np.fft.fft(new_averaged)/nd # fft computing and normalization
newnewYd = newnewYd[range(int(nd/2))]


figd, ([ax1d, ax3d], [ax2d, ax4d]) = plt.subplots(2, 2)
ax1d.title.set_text('sigD: [Signal v Time] plot (MAF; avg=1000)')
ax1d.plot(td,yd,'k')
ax1d.plot(td,newd,'r')
ax1d.set_xlabel('Time')
ax1d.set_ylabel('Amplitude')
figd.subplots_adjust(hspace=0.5)
figd.subplots_adjust(wspace=0.5)


ax2d.loglog(frqd,abs(Yd),'k') # plotting the fft
ax2d.loglog(frqd,abs(newYd),'r') # plotting the fft
ax2d.title.set_text('sigD: [MAF] plot')
ax2d.set_xlabel('Freq (Hz)')
ax2d.set_ylabel('|Y(freq)|')

ax3d.title.set_text('sigD: filtered [Signal v Time] (IIR; A=0.97, B=0.03)')
ax3d.plot(td,yd,'k')
ax3d.plot(td,new_averaged,'r')
ax3d.set_xlabel('Time')
ax3d.set_ylabel('Amplitude')

ax4d.loglog(frqd,abs(Yd),'k') # plotting the fft
ax4d.loglog(frqd,abs(newnewYd),'r') # plotting the fft
ax4d.title.set_text('sigD: [IIR] plot')
ax4d.set_xlabel('Freq (Hz)')
ax4d.set_ylabel('|Y(freq)|')

# 

# # figd, ([ax1d, ax3d], [ax2d, ax4d]) = plt.subplots(2, 1)
# figd, (ax1d, ax2d) = plt.subplots(2, 1)
# ax1d.title.set_text('sigD: [Signal v Time] plot (A = 0.95; B = 0.05)')
# ax1d.plot(td,yd,'k')
# ax1d.set_xlabel('Time')
# ax1d.set_ylabel('Amplitude')
# # ax3d.plot(td,newd,'r')
# ax1d.plot(td,new_averaged,'r')
# figd.subplots_adjust(hspace=0.5)
# figd.subplots_adjust(wspace=0.5)


# ax2d.loglog(frqd,abs(Yd),'k') # plotting the fft
# ax2d.title.set_text('sigD: unfiltered [FFT] plot')
# ax2d.set_xlabel('Freq (Hz)')
# ax2d.set_ylabel('|Y(freq)|')
# # ax4d.loglog(frqd,abs(newYd),'r') # plotting the fft
# ax2d.loglog(frqd,abs(newnewYd),'r') # plotting the fft

plt.show()