# IBM1 <!-- Your submission short name in <=4 characters -->
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

The Ideal Binary Mask (IBM) is a hard-assignment method that design a filter as a binary classification problem. This version computes the mask based on a ratio of magnitude spectrograms.

### Notations

We write $x$ for the 3-dimensional complex array obtained by stacking the Short-Time Frequency Transforms (STFT) of left and right channels of the mixture. Its dimensions are $F\times T\times 2$, where $F,T$ stand for the number of frequency bands and time frames, respectively. Its values at Time-Frequency (TF) bin $(f,t)$ are  written $x(f,t)\in\mathbb{C}^2$, with entries $x_i(f,t)$ for $i\in\{0,1\}$. The mixture is taken as the sum of the sources _images_: $x(f,t)=\sum_j y_j(f,t)$, which correspond to the isolated instruments and are also stereo.

### Filtering method

The IBM method computes source estimates by processing independently left and right channels of the mixture and multiplying it by a _binary mask_ $M(f,t)\in\{0,1\}$:
$\hat{y}_{ij}(f,t)=M_{ij}(f,t) x(f,t),$

where $M(f,t)$ is the parameter to be estimated. A classical reference for the IBM is for instance:
> Wang, DeLiang. "On ideal binary mask as the computational goal of auditory scene analysis." Speech separation by humans and machines. Springer, Boston, MA, 2005. 181-197.

### Binary mask estimation
This submission is an _oracle_, meaning that it knows the true sources to compute the binary mask.

Given the true sources $y_j$, the mask is computed very simply as:

$M_{ij}(f,t)=\frac{v_{ij}(f,t)}{\sum_j' v_{ij'}(f,t)}>0.5,$

where $v_{ij}(f,t)=\left|y_{ij}(f,t)\right|$ is the _magnitude spectrogram_ of $y_ij$ at time frequency bin $(t,f)$, hence the name IRM1 for this submission, in contrast of IRM2 that computes a ratio of _power_ spectrograms.

## References

- A. Liutkus and F.-R. Stöter, _The 2018 Signal Separation Evaluation Campaign_, Proceedings of LVA/ICA, 2018

> @inproceedings{sisec2018,
  title={The 2018 signal separation evaluation campaign},
  author={A. Liutkus and F.-R. St{\"o}ter and N. Ito},
  booktitle={International Conference on Latent Variable Analysis and Signal Separation},
  year={2018},
}
