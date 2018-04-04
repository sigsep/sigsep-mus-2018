# HPLP <!-- Your submission short name in <=4 characters -->
Ethan Manilow (Implementation author)  <!-- Authors  -->
Northwestern University <!-- Affiliations -->
ethanmanilow@u.northwestern.edu <!-- one corresponding mail address -->

## Additional Info

* __is_blind:__ yes  <!-- if you used supervised learning, answer no -->
* __additional_training_data:__ no  <!-- if you used more data than musdb (not including data augmentation)-->

## Supplementary Material

* __Code:__ https://github.com/interactiveaudiolab/nussl/blob/master/nussl/separation/high_low_pass_filter.py
* __Demo:__ https://github.com/interactiveaudiolab/nussl/blob/master/demos/demo_high_low_pass_filter.py


## Method

This is a simple high pass/low pass filter mask implemented in ``nussl``. After computing the STFT,
we find the closest frequency index to the desired filter cutoff and every frequency higher than that
index is considered foreground (or vocals) and every value below that index is considered background
(or accompaniment). We make two hard masks: the foreground mask is all ones above the cutoff index and
zeros below, the background mask is all zeros above the cutoff index and ones below.

This is a benchmark algorithm, hopefully more advanced methods can beat this one!

For this implementation we selected the closest frequency to 100Hz, which turned out to be ~107Hz.

## References

None
