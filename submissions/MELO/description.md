# MELO <!-- Your submission short name in <=4 characters -->
Justin Salamon, Prem Seetharaman (Implementation Author), Ethan Manilow (Implementation Author) <!-- Authors  -->
New York University, Northwestern University <!-- Affiliations -->
ethanmanilow@northwestern.edu <!-- one corresponding mail address -->

## Additional Info

* __is_blind:__ yes  <!-- if you used supervised learning, answer no -->
* __additional_training_data:__ no  <!-- if you used more data than musdb (not including data augmentation)-->

## Supplementary Material

* __Code:__ https://github.com/interactiveaudiolab/nussl/blob/master/nussl/separation/melodia.py


## Method

This is the ``nussl`` implementation of masking using pitch tracking. The pitch tracking algorithm
used is the Melodia pitch tracker from Salamon & Gómez. Using the pitch, we create a mask on the 
mixture. The abstract for Melodia is below:

    We present a novel system for the automatic extraction of the main melody from polyphonic music recordings. Our approach is based on the creation and characterization of pitch contours, time continuous sequences of pitch candidates grouped using auditory streaming cues. We define a set of contour characteristics and show that by studying their distributions we can devise rules to distinguish between melodic and non-melodic contours. This leads to the development of new voicing detection, octave error minimization and melody selection techniques. A comparative evaluation of the proposed approach shows that it outperforms current state-of-the-art melody extraction systems in terms of overall accuracy. Further evaluation of the algorithm is provided in the form of a qualitative error analysis and the study of the effect of key parameters and algorithmic components on system performance. Finally, we conduct a glass ceiling analysis to study the current limitations of the method, and possible directions for future work are proposed.

## References

- Salamon, Justin, and Emilia Gómez. "Melody extraction from polyphonic music signals using pitch contour characteristics." IEEE Transactions on Audio, Speech, and Language Processing 20.6 (2012): 1759-1770.
