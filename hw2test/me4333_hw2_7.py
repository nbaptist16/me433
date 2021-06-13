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
# from no. 3// sample rate: 10000.20000400008 Hz

with open('sigB.csv') as fb:
    # open the csv file
    readerb = csv.reader(fb)
    for rowb in readerb:
        # read the rows 1 one by one
        tb.append(float(rowb[0])) # leftmost column
        data1b.append(float(rowb[1])) # second column
srateb = len(data1b)/(tb[-1] - tb[0])
# from no. 3// sample rate: 3300.2000121219467 Hz

with open('sigC.csv') as fc:
    # open the csv file
    readerc = csv.reader(fc)
    for rowc in readerc:
        # read the rows 1 one by one
        tc.append(float(rowc[0])) # leftmost column
        data1c.append(float(rowc[1])) # second column
sratec = len(data1c)/(tc[-1] - tc[0])
# from no. 3// sample rate: 2500.1250062503127 Hz

with open('sigD.csv') as fd:
    # open the csv file
    readerd = csv.reader(fd)
    for rowd in readerd:
        # read the rows 1 one by one
        td.append(float(rowd[0])) # leftmost column
        data1d.append(float(rowd[1])) # second column
srated = len(data1d)/(td[-1] - td[0])
# from no. 3// sample rate: 400.0833506980621 Hz

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
        new_averagea.append(data1a[aa])
    else:
        new_averagea.append(Aa * new_averagea[aa-1] + Ba * data1a[aa])
newnewYa = np.fft.fft(new_averagea)/na # fft computing and normalization
newnewYa = newnewYa[range(int(na/2))]


# added for no. 7
preva = []
fira = []
finala = 0

weightsa = [
    -0.000000000000000001,
    0.000265691843213905,
    0.001274437135254747,
    0.003460582784404648,
    0.007377744495833180,
    0.013579044221082859,
    0.022431363735207877,
    0.033916389549532834,
    0.047486166290078791,
    0.062033526304542452,
    0.076008757243869074,
    0.087671422560238535,
    0.095423650140959923,
    0.098142447391562235,
    0.095423650140959937,
    0.087671422560238563,
    0.076008757243869088,
    0.062033526304542466,
    0.047486166290078805,
    0.033916389549532862,
    0.022431363735207873,
    0.013579044221082859,
    0.007377744495833206,
    0.003460582784404654,
    0.001274437135254745,
    0.000265691843213905,
    -0.000000000000000001,
]


preva = []
fira = []

for ba in range(len(weightsa)):
    preva.append(0)

for ca in range(len(ta)):
    preva.append(data1a[ca])
    preva.pop(0)
    compa = 0
    for da in range(len(preva)):
        compa = compa + preva[da] * weightsa[da]
    fira.append(compa)

newnewnewYa = np.fft.fft(fira)/na # fft computing and normalization
newnewnewYa = newnewnewYa[range(int(na/2))]


figa, ([ax1a, ax3a], [ax2a, ax4a]) = plt.subplots(2, 2)
ax1a.title.set_text('sigA: [Signal v Time] plot (MAF; avg=1000)')
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

ax3a.title.set_text('sigA: filtered [Signal v Time] (FIR; fL=250, bL=1742.42)')
ax3a.plot(ta,ya,'k')
ax3a.plot(ta,fira,'r')
ax3a.set_xlabel('Time')
ax3a.set_ylabel('Amplitude')

ax4a.loglog(frqa,abs(Ya),'k') # plotting the fft
ax4a.loglog(frqa,abs(newnewnewYa),'r') # plotting the fft
ax4a.title.set_text('sigA: [FIR] plot')
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
        new_averageb.append(data1b[ab])
    else:
        new_averageb.append(Ab * new_averageb[ab-1] + Bb * data1b[ab])
newnewYb = np.fft.fft(new_averageb)/nb # fft computing and normalization
newnewYb = newnewYb[range(int(nb/2))]


# added for no. 7
prevb = []
firb = []
finalb = 0

weightsb = [
    -0.000000000000000001,
    0.000265691843213905,
    0.001274437135254747,
    0.003460582784404648,
    0.007377744495833180,
    0.013579044221082859,
    0.022431363735207877,
    0.033916389549532834,
    0.047486166290078791,
    0.062033526304542452,
    0.076008757243869074,
    0.087671422560238535,
    0.095423650140959923,
    0.098142447391562235,
    0.095423650140959937,
    0.087671422560238563,
    0.076008757243869088,
    0.062033526304542466,
    0.047486166290078805,
    0.033916389549532862,
    0.022431363735207873,
    0.013579044221082859,
    0.007377744495833206,
    0.003460582784404654,
    0.001274437135254745,
    0.000265691843213905,
    -0.000000000000000001,
]


prevb = []
firb = []

for bb in range(len(weightsb)):
    prevb.append(0)

for cb in range(len(tb)):
    prevb.append(data1b[cb])
    prevb.pop(0)
    compb = 0
    for db in range(len(prevb)):
        compb = compb + prevb[db] * weightsb[db]
    firb.append(compb)

newnewnewYb = np.fft.fft(firb)/nb # fft computing and normalization
newnewnewYb = newnewnewYb[range(int(nb/2))]


figb, ([ax1b, ax3b], [ax2b, ax4b]) = plt.subplots(2, 2)
ax1b.title.set_text('sigB: [Signal v Time] plot (MAF; avg=1000)')
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

ax3b.title.set_text('sigB: filtered [Signal v Time] (FIR; fL=82.5, bL=575)')
ax3b.plot(tb,yb,'k')
ax3b.plot(tb,firb,'r')
ax3b.set_xlabel('Time')
ax3b.set_ylabel('Amplitude')

ax4b.loglog(frqb,abs(Yb),'k') # plotting the fft
ax4b.loglog(frqb,abs(newnewnewYb),'r') # plotting the fft
ax4b.title.set_text('sigB: [FIR] plot')
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
        new_averagec.append(data1c[ac])
    else:
        new_averagec.append(Ac * new_averagec[ac-1] + Bc * data1c[ac])
newnewYc = np.fft.fft(new_averagec)/nc # fft computing and normalization
newnewYc = newnewYc[range(int(nc/2))]


# added for no. 7
prevc = []
firc = []
finalc = 0

weightsc = [
    0.000000000000000000,
    0.000000000000000000,
    0.000029412503785741,
    0.000143088637100500,
    0.000414391758664981,
    0.000938598194322230,
    0.001832440381703737,
    0.003228375620623675,
    0.005263050628105823,
    0.008060551386337687,
    0.011712181582797984,
    0.016255483308549635,
    0.021655802219589432,
    0.027793765028907336,
    0.034461524943121824,
    0.041369585492577222,
    0.048164576583843988,
    0.054456745370034115,
    0.059854395729234705,
    0.064001317688274453,
    0.066612598946205137,
    0.067504227992439630,
    0.066612598946205151,
    0.064001317688274481,
    0.059854395729234726,
    0.054456745370034101,
    0.048164576583843974,
    0.041369585492577229,
    0.034461524943121845,
    0.027793765028907333,
    0.021655802219589442,
    0.016255483308549649,
    0.011712181582797984,
    0.008060551386337690,
    0.005263050628105817,
    0.003228375620623682,
    0.001832440381703738,
    0.000938598194322229,
    0.000414391758664982,
    0.000143088637100500,
    0.000029412503785741,
    0.000000000000000000,
    0.000000000000000000,
]


prevc = []
firc = []

for bc in range(len(weightsc)):
    prevc.append(0)

for cc in range(len(tc)):
    prevc.append(data1c[cc])
    prevc.pop(0)
    compc = 0
    for dc in range(len(prevc)):
        compc = compc + prevc[dc] * weightsc[dc]
    firc.append(compc)

newnewnewYc = np.fft.fft(firc)/nc # fft computing and normalization
newnewnewYc = newnewnewYc[range(int(nc/2))]


figc, ([ax1c, ax3c], [ax2c, ax4c]) = plt.subplots(2, 2)
ax1c.title.set_text('sigC: [Signal v Time] plot (MAF; avg=1000)')
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

ax3c.title.set_text('sigC: filtered [Signal v Time] (FIR; fL=62.5, bL=275)')
ax3c.plot(tc,yc,'k')
ax3c.plot(tc,firc,'r')
ax3c.set_xlabel('Time')
ax3c.set_ylabel('Amplitude')

ax4c.loglog(frqc,abs(Yc),'k') # plotting the fft
ax4c.loglog(frqc,abs(newnewnewYc),'r') # plotting the fft
ax4c.title.set_text('sigC: [FIR] plot')
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
        new_averaged.append(data1d[ad])
    else:
        new_averaged.append(Ad * new_averaged[ad-1] + Bd * data1d[ad])
newnewYd = np.fft.fft(new_averaged)/nd # fft computing and normalization
newnewYd = newnewYd[range(int(nd/2))]


# added for no. 7
prevd = []
fird = []
finald = 0

weightsd = [
    -0.000000000000000001,
    0.001184048940411622,
    0.005638626576572929,
    0.015264466670668006,
    0.031773674080497513,
    0.055235844554924626,
    0.083022909324854871,
    0.109915929304955057,
    0.129569907497824488,
    0.136789186098581456,
    0.129569907497824488,
    0.109915929304955098,
    0.083022909324854913,
    0.055235844554924626,
    0.031773674080497534,
    0.015264466670668038,
    0.005638626576572936,
    0.001184048940411623,
    -0.000000000000000001,
]


prevd = []
fird = []

for bd in range(len(weightsd)):
    prevd.append(0)

for cd in range(len(td)):
    prevd.append(data1d[cd])
    prevd.pop(0)
    compd = 0
    for dd in range(len(prevd)):
        compd = compd + prevd[dd] * weightsd[dd]
    fird.append(compd)

newnewnewYd = np.fft.fft(fird)/nd # fft computing and normalization
newnewnewYd = newnewnewYd[range(int(nd/2))]


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

ax3d.title.set_text('sigD: filtered [Signal v Time] (FIR; fL=10, bL=100)')
ax3d.plot(td,yd,'k')
ax3d.plot(td,fird,'r')
ax3d.set_xlabel('Time')
ax3d.set_ylabel('Amplitude')

ax4d.loglog(frqd,abs(Yd),'k') # plotting the fft
ax4d.loglog(frqd,abs(newnewnewYd),'r') # plotting the fft
ax4d.title.set_text('sigD: [FIR] plot')
ax4d.set_xlabel('Freq (Hz)')
ax4d.set_ylabel('|Y(freq)|')


plt.show()