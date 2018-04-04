# HPSS <!-- Your submission short name in <=4 characters -->
Derry Fitzgerald, Prem Seetharaman (implementation author), Ethan Manilow (implementation author) <!-- Authors  -->
Cork Institute of Technology, Northwestern University  <!-- Affiliations -->
ethanmanilow@u.northwestern.edu <!-- one corresponding mail address -->

## Additional Info

* __is_blind:__ yes  <!-- if you used supervised learning, answer no -->
* __additional_training_data:__ no  <!-- if you used more data than musdb (not including data augmentation)-->

## Supplementary Material

* __Code:__ https://github.com/interactiveaudiolab/nussl/blob/master/nussl/separation/hpss.py


## Method

This is the ``nussl`` implementation of Harmonic/Percussive Source Separation (HPSS). It applies
a median filter along the time axis to extract harmonic elements and a median filter across the
frequency axis to extract percussive elements.

Abstract from the paper:

    In this paper, we present a fast, simple and effective method to separate the harmonic and percussive parts of a monaural audio signal.The technique involves the use of median ﬁltering on a spectrogram of the audio signal, with median ﬁltering performed across successive frames to suppress percussive events and enhance harmonic components, while median ﬁltering is also performed across frequency bins to enhance percussive events and supress harmonic components. The two resulting median ﬁltered spectrograms are then used to generate masks which are then applied to the original spectrogram to separate the harmonic and percussive parts of the signal. We illustrate the use of the algorithm in the context of remixing audio material from commercial recordings.

## References

- Fitzgerald, Derry. "Harmonic/percussive separation using median filtering." (2010).
