# WK

Dominic Ward, Qiuqiang Kong

CVSSP, University of Surrey, Guildford, UK

dominic.ward[at]surrey.ac.uk

q.kong[at]surrey.ac.uk

## Additional Info

* __is_blind:__ no
* __additional_training_data:__ no

## Supplementary Material

* __Code:__ [WK-sisec-mus-2018](https://github.com/CVSSP/WK-sisec-mus-2018) (will update soon)

Please also see the python library
[untwist](https://github.com/IoSR-Surrey/untwist) where most of this work will
be incorporated for others to use in a more flexible manner.

## Method

This method is based on techniques given in the references, with some
experimentation. We used a bidirectional gated recurrent unit (BGRU) neural
network (one model per source) to estimate a time-frequency mask for each
source.

To obtain the accompaniment, the estimated bass, drums and other sources were
summed.

Specific steps are summarised below.

### Pre-Processing / Feature Derivation

1. Resample audio from 44.1 kHz to 32 kHz
2. Compute stereo STFT:

    - Window: Hamming
    - Window size: 1024
    - Hop size: 512

3. Convert stereo STFT to mono magnitude spectrogram
4. Apply a mel-frequency filter bank (128 bands)
5. Take the log of the mel-magnitude spectrogram
6. Standardise each mel band using the means and standard deviations computed
   from the training data

### Model and Training

The model is a BGRU with 3 layers and 512 units per layer. The input to the
model is a standardised log mel-magnitude spectrogram whose number of time
frames are determined by a context window. Each context window consists of
several stacked frames, which was chosen to be 11 for drums and 101 for bass,
other and vocals. Given these stacked frames, the model predicts a single
mel-frequency mask of length 128, corresponding to the centre frame of the
context window. That is, the output of the model is a mel mask. 

The loss function is defined as the absolute difference (L1-norm loss) between
the mel-magnitude spectrum (not log) of the target, and the element-wise
multiplication of the predicted mel mask and the mel-magnitude spectrum of the
mixture. Or, because that's a mouth full:

`loss = sum(| target_mel - predited_mel_mask * mixture_mel |)`

We used the Adam optimisation algorithm with a learning rate of 0.0001 to
minimise the loss function. 

Four models were trained (one per source), using batches of 100
mini-spectrograms (determined by context window) which were drawn from the
shuffled dataset (shuffling every epoch). We used a hop size of 1 frame when
drawing mini-spectrograms from the training data. There were roughly 12500
iterations of these batches per epoch.

We used the last 10 songs from the training set (100 songs) as our validation
set.

To apply the model after training, the mel-mask is interpolated to a
linear-frequency mask (see intro of [2]), which can then be multiplied with the
complex spectrum of the mixture to obtain the complex spectrum of a given
source.

### Post-processing

- For each source, we averaged the output of four models from the latter half of
    the training session. Specifically, we averaged models saved at iterations
    15, 20, 25 and 30 thousand. This was done to reduce variance in the
    estimated mask.

- Single-channel Wiener filter (see [1])

### Inverse STFT

- We applied the inverse STFT on each of the four separated complex spectra
    with overlap-add to recover the waveforms.


### Model Selection and Observations

After training the models, we computed BSS Eval measures on the validation test
to estimate performance and compare models. Although not scientifically
rigorous, we made some observations based on our validation set:

- Stacking more frames (longer context window) had a negative effect on the
    performance for drums.

- Stacking more frames had a positive effect on the remaining sources in terms
    of SDR, most notably for the vocals.

- For a low number of stacked frames, e.g. up to 11, it was hard to make a case
    for a 3-layer network given the variance in the BSS Eval measures.

- Surprisingly, Mel or ERB-inspired compressed spectra performed on par with raw
    linear magnitude spectrum. This means that the complexity of the model can
    be significantly reduced by simplifying the input representation (as
    discussed in [2]).

- Minimising the loss in linear magnitude domain (after interpolating the
    mel-mask) didn't seem to make much difference, but we didn't test
    extensively (see Eq.  6 of [2]).
    
- From listening, Wiener filtering improves general suppression of unwanted
    sources, but distorts the bass. We did experiment with multi-channel
    filtering and various smoothing techniques, but didn't manage to make
    significant improvements and ran out of time!

- Within-source model fusion is a must.

## References

1. Uhlich, S., Porcu, M., Giron, F., Enenkl, M., Kemp, T., Takahashi, N., &
   Mitsufuji, Y. (2017). Improving music source separation based on deep neural
   networks through data augmentation and network blending. 2017 IEEE
   International Conference on Acoustics, Speech and Signal Processing (ICASSP),
   261-265.

2. Weninger, F., Hershey, J.R., Roux, J.L., & Schuller, B.W. (2014).
   Discriminatively trained recurrent neural networks for single-channel speech
   separation. 2014 IEEE Global Conference on Signal and Information Processing
   (GlobalSIP), 577-581.
