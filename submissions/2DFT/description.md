# 2DFT <!-- Your submission short name in <=4 characters -->
Prem Seetharaman, Fatemeh Pishdadian, Bryan Pardo, Ethan Manilow (implementation author) <!-- Authors  -->
Northwestern University <!-- Affiliations -->
ethanmanilow@u.northwestern.edu <!-- one corresponding mail address -->

## Additional Info

* __is_blind:__ yes  <!-- if you used supervised learning, answer no -->
* __additional_training_data:__ no  <!-- if you used more data than musdb (not including data augmentation)-->

## Supplementary Material

* __Code:__ https://github.com/interactiveaudiolab/nussl/blob/master/nussl/separation/ft2d.py
* __Demos:__ https://interactiveaudiolab.github.io/demos/2dft


## Method

This is the ``nussl`` implementation of foreground/background separation using the 2D Fourier Transform.

Abstract from original paper:

    Audio source separation is the act of isolating sound sources
    in an audio scene.  One application of source separation is
    singing voice extraction.   In this work,  we present a novel
    approach for music/voice separation that uses the 2D Fourier
    Transform  (2DFT).  Our  approach  leverages  how  periodic
    patterns manifest in the 2D Fourier Transform and is con-
    nected to research in biological auditory systems as well as
    image processing.  We find that our system is very simple to
    describe and implement and competitive with existing unsu-
    pervised source separation approaches that leverage similar
    assumptions.


## References

- Prem Seetharaman, Fatemeh Pishdadian, and Bryan Pardo. Music/voice separation using the 2d fourier transform. In Applications of Signal Processing to Au- dio and Acoustics (WASPAA), 2017 IEEE Workshop on, pages 36–40. IEEE, 2017.
