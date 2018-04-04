
# HEL1 <!-- Your submission short name in <=4 characters -->
Manal Helal, Dominic Ward, Mark Plumply <!-- Authors  -->
CVSSP, Surrey University, Guildford, UK <!-- Affiliations -->
mhelal@cse.unsw.edu.au <!-- one corresponding mail address -->
dominic.ward@surrey.ac.uk
m.plumbley@surrey.ac.uk

## Additional Info

* __is_blind:__ no  <!-- if you used supervised learning, answer no -->
* __additional_training_data:__ no  <!-- if you used more data than musdb (not including data augmentation)-->

## Supplementary Material

* __Code:__
* __Demos:__ 


## Method

This is tensor flow 5 layer RNN trained neural networks using stft magnitudes and soft time masking. 

I will upload the source code, once I clean it up, and will write a paper with more details soon. It is based on a previous tensor flow implementation for 2 sources from ikala dataset: 
https://github.com/andabi/music-source-separation

extended to 4 sources from the musDB 2018 dataset, and scipy for feature extraction, and museval for evaluation.

I am working on more methods to submit soon, will write a paper then will clean up the code and upload it, and upload the demo files. After easter break will upload the demo files and update this file.

## References

- Weninger, F., Hershey, J. R., Roux, J. L., and Schuller, B., “Discriminatively trained recurrent neural networks for single-channel speech separation,” in Proc. GlobalSIP, 2014.
- P.-S. Huang, M. Kim, M. Hasegawa-Johnson, and P. Smaragdis, “Singing-Voice separation from monaural recordings using deep recurrent neural networks,” in Proc. ISMIR, 2014, pp. 477–482.  section 3-2
- Weninger, F., Hershey, J. R., Roux, J. L., and Schuller, B., “Discriminatively trained recurrent neural networks for single-channel speech separation,” in Proc. GlobalSIP, 2014." 
- H. P. S., M. Kim, M. Hasegawa-Johnson, and P. Smaragdis, “Joint optimization of masks and deep recurrent neural networks for monaural source separation,” IEEE/ACM Trans. Audio Speech and Language Processing, vol. 23, no. 12, pp. 2136 – 2147, 2015.
- P.-S. Huang, M. Kim, M. Hasegawa-Johnson, and P. Smaragdis, “Singing-Voice separation from monaural recordings using deep recurrent neural networks,” in Proc. ISMIR, 2014, pp. 477–482. 
- Emad M. Grais, Gerard Roma, Andrew J. R. Simpson, and Mark D. Plumbley, "Two Stage Single Channel Audio Source Separation using Deep Neural Networks"
