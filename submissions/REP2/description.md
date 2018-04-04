# ABC1 <!-- Your submission short name in <=4 characters -->
Zafar Raffi, Bryan Pardo, Ethan Manilow (implementation author) <!-- Authors  -->
Gracenote, Northwestern University <!-- Affiliations -->
ethanmanilow@u.northwestern.edu <!-- one corresponding mail address -->

## Additional Info

* __is_blind:__ yes  <!-- if you used supervised learning, answer no -->
* __additional_training_data:__ no  <!-- if you used more data than musdb (not including data augmentation)-->

## Supplementary Material

* __Code:__ https://github.com/interactiveaudiolab/nussl/blob/master/nussl/separation/repet_sim.py


## Method
This is the ``nussl`` implementation of the REpeating Pattern Extraction Technique algorithm using the Similarity Matrix (REPET-SIM).


From [here](http://music.cs.northwestern.edu/research.php?project=repet):

The REPET methods work well when the repeating background has periodically repeating patterns (e.g., jackhammer noise); however, the repeating patterns can also happen intermittently or without a global or local periodicity (e.g., frogs by a pond). REPET-SIM is a generalization of REPET that can also handle non-periodically repeating structures, by using a similarity matrix to identify the repeating elements. 

![](http://music.cs.northwestern.edu/includes/projects/repet/images/repet-sim.png)
Overview of REPET-SIM. Stage 1: calculation of the similarity matrix S and estimation of the repeating elements jk's. Stage 2: filtering of the mixture spectrogram V and calculation of an initial repeating spectrogram model U. Stage 3: calculation of the refined repeating spectrogram model W and derivation of the soft time-frequency mask M. 

    
## References

- Zafar Rafii and Bryan Pardo. "Audio Separation System and Method," US20130064379 A1, US 13/612,413, March 14, 2013
- Zafar Rafii and Bryan Pardo. "Music/Voice Separation using the Similarity Matrix," 13th International Society on Music Information Retrieval, Porto, Portugal, October 8-12, 2012.
