 # MDL1 <!-- Your submission short name in <=4 characters -->
Stylianos Ioannis Mimilakis¹ and Konstantinos Drossos² <!-- Authors  -->

¹Fraunhofer-IDMT, Ilmenau, Germany

²Tampere University of Technology, Tampere, Finland <!-- Affiliations -->

Contact: mis [at] idmt.fraunhofer.de <!-- one corresponding mail address -->

## Additional Info

* __is_blind:__ no  <!-- if you used supervised learning, answer no -->
* __additional_training_data:__ no  <!-- if you used more data than musdb (not including data augmentation)-->

## Supplemental Material

* __Code:__ https://github.com/Js-Mim/mss_pytorch

## Method

Task: Singing voice separation.

We used the Masker and Denoiser (MaD) architecture presented in the references below. Our method operates on single-channel
mixture magnitude spectrograms and yields single-channel estimates for the singing voice. The accompaniment source is estimated by time-domain subtraction. To avoid the computational complexities of the recurrent inference, we introduced to the overall cost a unit matrix norm penalty for the latent representation of the target source time-frequency mask (denoted as "H_j_dec" in our paper). In MDL1 a scalar of 2e-7 is applied to the aforementioned matrix norm. For training we only used the training subset of MUSDB18, without any augmentation, normalisation or dropout. At test time, we applied our method to each available mixture channel independently.


More details can be found here:
https://js-mim.github.io/mss_pytorch/

## References

1 S.I. Mimilakis, K. Drossos, T. Virtanen, and G. Schuller: A recurrent encoder-decoder approach with skip-filtering connections for monaural singing voice separation, in Proc. IEEE International Workshop on Machine Learning for Signal Processing (MLSP), September 2017.

2 S.I. Mimilakis, K. Drossos, J.F. Santos, G. Schuller, T. Virtanen, and Y. Bengio: Monaural singing voice separation with skip-filtering connections and recurrent inference of time-frequency mask, in Proc. IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), April 2018.
