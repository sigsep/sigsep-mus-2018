# RGT1
Gerard Roma, Owen Green, Pierre Alexandre Tremblay
University of Huddersfield
g.roma@hud.ac.uk

## Additional Info

* __is_blind:__ no
* __additional_training_data:__ no

## Supplementary Material

* __Code:__ https://github.com/flucoma/LVA-ICA-2018/
* __Demos:__ http://www.flucoma.org/LVA-ICA-2018/


## Method
This system employs a Convolutional Neural Network with fully-connected output layers.
The input of the network is a slice of 11 STFT frames (about 200ms). The output is a ratio mask corresponding to one spectral frame.
We trained the network by optimizing the mean square error loss with ideal ratio masks simultaneously for four sources using the training set of the musdb dataset.



## References
- G. Roma, O. Green, P.A. Tremblay, Improving single-network single-channel separation of musical audio with convolutional layers. Proceedings of LVA/ICA, 2018
