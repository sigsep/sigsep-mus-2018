# UHL3
Stefan Uhlich¹, Franck Giron¹, Michael Enenkl¹, Thomas Kemp¹, Naoya Takahashi², Yuki Mitsufuji²

¹Sony European Technology Center (EuTEC), Stuttgart, Germany<br/>
²Sony Corporation, Audio Technology Development Department, Tokyo, Japan

stefan.uhlich (at) eu.sony.com

## Additional Info

* __is_blind:__ no
* __additional_training_data:__ yes


## Supplemental Material

* __Code:__ not available
* __Demos:__ not available


## Method

This submission uses a bi-directional LSTM network as described in [1] with
three BLSTM layers, each having 500 cells. For each instrument, a network is
trained which predicts the target instrument amplitude from the mixture
amplitude in the STFT domain (frame size: 4096, hop size: 1024). The raw
output of each network is then combined by a multichannel Wiener filter as
described in [2] where we estimate the power spectral densities and spatial
covariance matrices from the DNN outputs.

The network is trained on an internal database with 804 songs. We used the
full `train` part of `musdb` as validation set, which is again used to
perform early stopping and hyperparameter selection (LSTM layer dropout
rate, regularization strength).


## References

- [1] S. Uhlich, M. Porcu, F. Giron, M. Enenkl, T. Kemp, N. Takahashi and Y. Mitsufuji. "Improving music source separation based on deep neural networks through data augmentation and network blending", Proc. ICASSP, 2017.
- [2] A. A. Nugraha, A. Liutkus, and E. Vincent. "Multichannel music separation with deep neural networks." EUSIPCO, 2016.
