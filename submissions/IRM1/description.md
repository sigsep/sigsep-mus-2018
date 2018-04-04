# IRM1 <!-- Your submission short name in <=4 characters -->
Antoine Liutkus, Fabian-Robert Stöter <!-- Authors  -->
Inria and LIRMM, University of Montpellier, France <!-- Affiliations -->
antoine.liutkus@inria.fr <!-- one corresponding mail address -->

## Additional Info

* __is_blind:__ no  <!-- if you used supervised learning, answer no -->
* __additional_training_data:__ no  <!-- if you used more data than musdb (not including data augmentation)-->

## Supplementary Material

* __Code:__ https://github.com/sigsep/sigsep-mus-oracle
* __Demos:__ Not available

## Method

### Introduction

The Ideal Ratio Mask for magnitude spectrograms (IRM2) is also known as the generalized 1-Wiener filter.

### Notations

We write $x$ for the 3-dimensional complex array obtained by stacking the Short-Time Frequency Transforms (STFT) of left and right channels of the mixture. Its dimensions are $F\times T\times 2$, where $F,T$ stand for the number of frequency bands and time frames, respectively. Its values at Time-Frequency (TF) bin $(f,t)$ are  written $x(f,t)\in\mathbb{C}^2$, with entries $x_i(f,t)$ for $i\in\{0,1\}$. The mixture is taken as the sum of the sources _images_: $x(f,t)=\sum_j y_j(f,t)$, which correspond to the isolated instruments and are also stereo.

### Underlying theory: $\alpha$-harmonizable processes

The IRM1 method has been popular for many years for source separation, where experience shows that using magnitude spectrograms works often better than using power spectrogram as advocated by the classical wide-sense stationary theory. However, no theoretical understanding of it was available until recently, where it was shown to be the optimal way to process _locally stationary $\alpha$-harmonizable processes_. A description of this theory is given in:

> Liutkus, Antoine, and Roland Badeau. "Generalized Wiener filtering with fractional power spectrograms." Acoustics, Speech and Signal Processing (ICASSP), 2015 IEEE International Conference on. IEEE, 2015.

Basically, this method boils down to assuming all the entries of $y_j$ as independent and distributed with respect to a complex isotropic $\alpha$-stable distribution. This is written: $y_{ij}(f,t)\sim\mathcal{S\alpha S}_c\left(v_{ij}(f,t)\right)$, where $v_ij$ is the _$\alpha$-spectrogram_ of $y_{ij}$, and can be understood as related to the magnitude of the source across time and frequency.

In this submission, we take $\alpha=1$, which turns out to be the Cauchy model.


### Separation

Under this model, source estimates are computed very simply as:
$\hat{y}_{ij}(f,t)=\frac{v_j(f,t)}{\sum_j' v_{ij'}(f,t)} x(f,t),$

just as in classical Wiener filtering. This is often called Ideal Ratio Mask, hence the name of this submission.

### Parameter estimation
This submission is an _oracle_, meaning that it knows the true sources to compute the optimal parameters $v_{ïj}$

Given the true sources $y_j$, the parameters are very simply estimated as the magnitude:

$v_{ij}(f,t)=\left|y_{ij}(f,t)\right|.$

As may be seen, this approach is extremely similar to classical Wiener filtering, except for the choice of magnitude spectrograms instead of power. Note that this theory works for any exponent $\alpha\in(0,2]$ for the spectrogram.

## References

- A. Liutkus and F.-R. Stöter, _The 2018 Signal Separation Evaluation Campaign_, Proceedings of LVA/ICA, 2018

> @inproceedings{sisec2018,
  title={The 2018 signal separation evaluation campaign},
  author={A. Liutkus and F.-R. St{\"o}ter and N. Ito},
  booktitle={International Conference on Latent Variable Analysis and Signal Separation},
  year={2018},
}
