# TAU1
Naoya Takahashi¹, Stefan Uhlich², Franck Giron², Michael Enenkl², Thomas Kemp², Nabarun Goswami³, Yuki Mitsufuji¹

¹Sony Corporation, Audio Technology Development Department, Tokyo, Japan  
²Sony European Technology Center (EuTEC), Stuttgart, Germany  
³Sony India Software Center, Bangalore, India

Naoya.Takahashi [at] sony.com


## Additional Info

* __is_blind:__ no
* __additional_training_data:__ yes


## Supplemental Material

* __Code:__ not available
* __Demos:__ not available


## Method

This submission blends two systems as described in [1]. The first system is
TAK3 (MMDenseNets[2]) and the second system is UHL3 (LSTM). We linearly blend the raw
outputs of the two systems using

$$\hat{s}_i(n) = 0.5 * ( \hat{s}_{i, 1}(n) + \hat{s}_{i, 2}(n)$$

where $i = \{`B`, `D`, `O`, `V`\}$. From these estimates, we then compute the
power spectral densities and spatial covariance matrices of the multichannel
Wiener filter(MWF) [3].

## References
1. S. Uhlich, M. Porcu, F. Giron, M. Enenkl, T. Kemp, N. Takahashi and Y. Mitsufuji: Improving music source separation based on deep neural networks through data augmentation and network blending, Proc. ICASSP, 2017
2. N. Takahashi and Y. Mitsufuji: Multi-scale multi-band DenseNets for audio source separation, Proc. WASPAA, 2017
3. A. A. Nugraha, A. Liutkus, and E. Vincent. "Multichannel music separation with deep neural networks." EUSIPCO, 2016.
