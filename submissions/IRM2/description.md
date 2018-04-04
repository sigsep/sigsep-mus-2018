# IRM2 <!-- Your submission short name in <=4 characters -->
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

The Ideal Ratio Mask for power spectrograms (IRM2) is also known as the generalized Wiener filter.

### Notations

We write $x$ for the 3-dimensional complex array obtained by stacking the Short-Time Frequency Transforms (STFT) of left and right channels of the mixture. Its dimensions are $F\times T\times 2$, where $F,T$ stand for the number of frequency bands and time frames, respectively. Its values at Time-Frequency (TF) bin $(f,t)$ are  written $x(f,t)\in\mathbb{C}^2$, with entries $x_i(f,t)$ for $i\in\{0,1\}$. The mixture is taken as the sum of the sources _images_: $x(f,t)=\sum_j y_j(f,t)$, which correspond to the isolated instruments and are also stereo.

### Underlying theory: locally stationary Gaussian processes

The IRM2 method lies on solid theoretical grounds. It consists in assuming that all channels are independent and _locally stationary Gaussian processes_. A description of this model may be found in:

> Liutkus, Antoine, Roland Badeau, and Gäel Richard. "Gaussian processes for underdetermined source separation." IEEE Transactions on Signal Processing 59.7 (2011): 3155-3167.

Basically, this boils down to assuming all the entries of $y_j$ as independent and Gaussian. This is written: $y_{ij}(f,t)\sim\mathcal{N}_c\left(0,v_{ij}(f,t)\right)$, where $v_ij$ is the power spectrogram of $y_{ij}$, and can be understood as its energy that varies over time and frequency.


### Separation

Under this model, source estimates are computed very simply as:
$\hat{y}_{ij}(f,t)=\frac{v_j(f,t)}{\sum_j' v_{ij'}(f,t)} x(f,t),$

which is often called Ideal Ratio Mask, hence the name of this submission.

### Parameter estimation
This submission is an _oracle_, meaning that it knows the true sources to compute the optimal parameters $v_{ïj}$

Given the true sources $y_j$, the parameters are very simply estimated as the power spectrograms:

$v_{ij}(f,t)=\left|y_{ij}(f,t)\right|^2$

## References

- A. Liutkus and F.-R. Stöter, _The 2018 Signal Separation Evaluation Campaign_, Proceedings of LVA/ICA, 2018

> @inproceedings{sisec2018,
  title={The 2018 signal separation evaluation campaign},
  author={A. Liutkus and F.-R. St{\"o}ter and N. Ito},
  booktitle={International Conference on Latent Variable Analysis and Signal Separation},
  year={2018},
}
