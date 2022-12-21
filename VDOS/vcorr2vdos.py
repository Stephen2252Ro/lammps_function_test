#!/usr/bin/env python

import collections

import numpy.fft as npfft
import scipy.fftpack as spfftp
import pandas as pd

def vcorr2vdat(vcorr_dat, vdos_dat, dt):

    df = pd.read_csv(vcorr_dat, delim_whitespace=True)
    data = collections.OrderedDict()

    # compute frequencies
    data["freq"] = npfft.rfftfreq(len(df)*2-2, d=dt)

    # skip TimeStep
    for column in df.columns[1:]:

        # use Discrete Cosine Transform because velocity correlation is even
        fft = spfftp.dct(df[column].values, type=1)
        data[column] = fft

    dfout = pd.DataFrame(data=data)
    dfout.to_csv(vdos_dat, sep=" ", index=False)


def main():

    # velocity correlation input
    vcorr_dat = "vcorr.dat"

    # VDOS output
    vdos_dat  = "vdos.dat"

    # time step
    dt = 1e-15

    vcorr2vdat(vcorr_dat, vdos_dat, dt)

if __name__ == "__main__": main()
