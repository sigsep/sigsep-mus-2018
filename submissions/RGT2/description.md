# RGT2
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
The input of the network is a slice of 11 STFT frames (about 200ms). The output is a binary mask corresponding to one spectral frame.
We trained the network by optimizing the negative log likelihood loss from a 2D softmax output layer. The target vector was encoded with class labels corresponding to the source with highest magnitude for each time-frequency bin.


## References
- G. Roma, O. Green, P.A. Tremblay, Improving single-network single-channel separation of musical audio with convolutional layers. Proceedings of LVA/ICA, 2018
