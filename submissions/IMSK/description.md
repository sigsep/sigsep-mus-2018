# IMSK <!-- Your submission short name in <=4 characters -->
Ethan Manilow (implementation author) <!-- Authors  -->
Northwestern University <!-- Affiliations -->
ethanmanilow@northwestern.edu <!-- one corresponding mail address -->

## Additional Info

* __is_blind:__ no  <!-- if you used supervised learning, answer no -->
* __additional_training_data:__ no  <!-- if you used more data than musdb (not including data augmentation)-->

## Supplementary Material

* __Code:__ https://github.com/interactiveaudiolab/nussl/blob/master/nussl/separation/ideal_mask.py


## Method

This is the ``nussl`` implementation of the ideal mask. Ideal mask generates a mask for the mixture
based on the known reference sources. This is the best any mask-based algorithm could ever hope
to achieve because it uses ground truth to calculate the masks. 

This is used a benchmark algorithm. This implementation makes soft masks.

## References

None
