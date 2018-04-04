# REP1 <!-- Your submission short name in <=4 characters -->
Zafar Raffi, Bryan Pardo, Ethan Manilow (implementation author) <!-- Authors  -->
Gracenote, Northwestern University <!-- Affiliations -->
ethanmanilow@u.northwestern.edu <!-- one corresponding mail address -->

## Additional Info

* __is_blind:__ yes  <!-- if you used supervised learning, answer no -->
* __additional_training_data:__ no  <!-- if you used more data than musdb (not including data augmentation)-->

## Supplementary Material

* __Code:__ https://github.com/interactiveaudiolab/nussl/blob/master/nussl/separation/repet.py
* __Demos:__ https://interactiveaudiolab.github.io/nussl/getting_started/repet.html


## Method
This is the ``nussl`` implementation of the original REpeating Pattern Extraction 
Technique (REPET) algorithm using the beat spectrum.

From [here](http://music.cs.northwestern.edu/research.php?project=repet):

The original REPET aims at identifying and extracting the repeating patterns in an audio mixture, by estimating a period of the underlying repeating structure and modeling a segment of the periodically repeating background. 

![](http://music.cs.northwestern.edu/includes/projects/repet/images/repet.png)
Overview of the original REPET. Stage 1: calculation of the beat spectrum b and estimation of a repeating period p. Stage 2: segmentation of the mixture spectrogram V and calculation of the repeating segment model S. Stage 3: calculation of the repeating spectrogram model W and derivation of the soft time-frequency mask M. 

## References

- Zafar Rafii and Bryan Pardo. "Audio Separation System and Method," US20130064379 A1, US 13/612,413, March 14, 2013
- Zafar Rafii, Antoine Liutkus, and Bryan Pardo. "REPET for Background/Foreground Separation in Audio," Blind Source Separation, chapter 14, pages 395--411, Springer Berlin Heidelberg, 2014.
- Zafar Rafii and Bryan Pardo. "REpeating Pattern Extraction Technique (REPET): A Simple Method for Music/Voice Separation," IEEE Transactions on Audio, Speech, and Language Processing, Volume 21, Issue 1, pp. 71--82, January, 2013.
- 
