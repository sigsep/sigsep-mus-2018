# RPCA <!-- Your submission short name in <=4 characters -->
Po-Sen Huang, Scott Deeann Chen, Paris Smaragdis, Mark Hasegawa-Johnson, Prem Seetharaman (Implementation Author), Ethan Manilow (Implementation Author) <!-- Authors  -->
University of Illinois, Northwestern University <!-- Affiliations -->
ethanmanilow@u.northwestern.edu <!-- one corresponding mail address -->

## Additional Info

* __is_blind:__ yes  <!-- if you used supervised learning, answer no -->
* __additional_training_data:__ no  <!-- if you used more data than musdb (not including data augmentation)-->

## Supplementary Material

* __Code:__ http://github.com/my/repo
* __Demos:__ http://www.demo.com


## Method

The ``nussl`` implementation of RPCA for audio source separation.

Abstract from the original paper:

    Separating singing voices from music accompaniment is
    an important task in many applications, such as music infor-
    mation retrieval, lyric recognition and alignment. Music ac-
    companiment can be assumed to be in a low-rank subspace,
    because of its repetition structure; on the other hand, singing
    voices can be regarded as relatively sparse within songs. In
    this paper, based on this assumption, we propose using ro-
    bust principal component analysis for singing-voice separa-
    tion from music accompaniment. Moreover, we examine the
    separation result by using a binary time-frequency masking
    method. Evaluations on the MIR-1K dataset show that this
    method can achieve around 1∼1.4 dB higher GNSDR com-
    pared with two state-of-the-art approaches without using prior
    training or requiring particular features.

## References

- Huang, Po-Sen, et al. "Singing-voice separation from monaural recordings using robust principal component analysis." Acoustics, Speech and Signal Processing (ICASSP), 2012 IEEE International Conference on. IEEE, 2012.
