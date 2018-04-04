# UHL2
Stefan Uhlich¹, Franck Giron¹, Michael Enenkl¹, Thomas Kemp¹, Naoya Takahashi², Yuki Mitsufuji²

¹Sony European Technology Center (EuTEC), Stuttgart, Germany<br/>
²Sony Corporation, Audio Technology Development Department, Tokyo, Japan

stefan.uhlich (at) eu.sony.com


## Additional Info

* __is_blind:__ no
* __additional_training_data:__ no


## Supplemental Material

* __Code:__ not available
* __Demos:__ not available


## Method

This submission blends two systems as described in [1]. The first system is
UHL1 and the second system is another set of four networks trained on
`musdb` with different random seeds. We linearly blend the raw outputs of the
two systems using

`$$\hat{s}_i(n) = 0.5 * ( \hat{s}_{i, 1}(n) + \hat{s}_{i, 2}(n)$$`

where `$i = \{`B`, `D`, `O`, `V`\}$`. From these estimates, we then compute the
power spectral densities and spatial covariance matrices of the multichannel
Wiener filter [2].


## References

- [1] S. Uhlich, M. Porcu, F. Giron, M. Enenkl, T. Kemp, N. Takahashi and Y. Mitsufuji: Improving music source separation based on deep neural networks through data augmentation and network blending, Proc. ICASSP, 2017
- [2] A. A. Nugraha, A. Liutkus, and E. Vincent. "Multichannel music separation with deep neural networks." EUSIPCO, 2016.
