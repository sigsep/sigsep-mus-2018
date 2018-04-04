# MWF <!-- Your submission short name in <=4 characters -->
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

The Multichannel Wiener Filter (MWF) exploiting the Local Gaussian Model (LGM) has been initially proposed in the following paper:

> Duong, Ngoc QK, Emmanuel Vincent, and Rémi Gribonval. "Under-determined reverberant audio source separation using a full-rank spatial covariance model." IEEE Transactions on Audio, Speech, and Language Processing 18.7 (2010): 1830-1840.

Its core feature is to extend the single channel Wiener filter by exploiting interchannel correlations of the sources.

### Notations

We write $x$ for the 3-dimensional complex array obtained by stacking the Short-Time Frequency Transforms (STFT) of left and right channels of the mixture. Its dimensions are $F\times T\times 2$, where $F,T$ stand for the number of frequency bands and time frames, respectively. Its values at Time-Frequency (TF) bin $(f,t)$ are  written $x(f,t)\in\mathbb{C}^2$. The mixture is taken as the sum of the sources _images_: $x(f,t)=\sum_j y_j(f,t)$, which correspond to the isolated instruments and are also stereo.

### The local Gaussian model

The local Gaussian model assumes $y_j(f,t)\in\mathbb{C}^2$ is a circularly-symmetric Gaussian random vector, as described in:

> Gallager, Robert G. "Circularly-symmetric Gaussian random vectors." Technical report, MIT (2008).

This is written: $y_j(f,t)\sim\mathcal{N}_c\left(0,v_j(f,t)R_j(f)\right)$, where:
* $v_j(f,t)$ is the _Power Spectral Density_ (PSD) of source $j$ at TF bin $(f,t)$. It can be understood as the _energy_ at that TF bin.
* $R_j(f)$ is the _Spatial Covariance Matrix_ (SCM) of source $j$ at frequency $f$. It is a $2\times 2$ matrix that encodes the _correlations_ between left and right channels for this source at that frequency. The SCM can be understood as encoding how much one channel gives any information about the other through correlations. Note that in the LGM, the SCM is assumed to be constant over time, which basically means we expect all sources to have a consistant spatial configuration throughout the song.

The LGM model can be shown to generalize several previously proposed models, such as the linear instantaneous and the convolutive, that assume some deterministic relationship between left and right channels. Its strength is to relax such approaches by introducing some stochasticity: channels are only assumed _correlated_, and not necessarily either _independent_ or _deterministically related_.

### Separation
One advantage of the LGM is that it allows for straightforward separation, if we have the true parameters $v_j$ and $R_j$. In short, each source is estimated as:

$\hat{y}_j(f,t)=v_j(f,t)R_j(f)\left[\sum_j' v_{j'}(f,t)R_{j'}(f)\right]^\dagger x(f,t),$

where $\cdot^\dagger$ denotes pseudo inversion. This operation is denoted as Multichannel Wiener Filtering, and is the one implemented here.

### Parameter estimation
This submission is an _oracle_, meaning that it knows the true sources to compute the optimal parameters $v_j$ and $R_j$. This submission is therefore intended as an upper bound on performance that can be attained by methods based on multichannel filtering.

Given the true sources $y_j$, the parameters are estimated through the method discussed in the aforementioned paper by N. Duong, replacing the estimated sources by their true values.

## References

- A. Liutkus and F.-R. Stöter, _The 2018 Signal Separation Evaluation Campaign_, Proceedings of LVA/ICA, 2018
> @inproceedings{sisec2018,
  title={The 2018 signal separation evaluation campaign},
  author={A. Liutkus and F.-R. St{\"o}ter and N. Ito},
  booktitle={International Conference on Latent Variable Analysis and Signal Separation},
  year={2018},
}
