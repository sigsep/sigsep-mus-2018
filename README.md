# SISEC MUS 2018 Submission

This is the submission system for the Professionally-produced music task of the [2018 SiSEC](https://sisec.inria.fr/2018-professionally-produced-music-recordings/).

For the this year, we are handling the submission of the results through GitHub.
This means it will be necessary for any participant to have a github account. If you don't have experience with git, don't worry, as everything can be done from within the browser. Also we will add a full tutorial here.

## Dates

- __March 1st, 2018__: The submission system is open.
- __April 1st 2018__: Deadline for submission results.

## Submission

To submit source separation results to SISEC 2018 you need to run the following steps

### Step 1: Dataset

Download the dataset via the link on the [dataset website](https://sigsep.github.io/musdb).

### Step 2: Compute Estimates

Compute estimates using the python based [musdb tools](https://github.com/sigsep/sigsep-mus-db) or through your own custom method.

In any case, make sure, your estimates folder does follow a certain schema. Lets assume your method is called `ABCD`:

```
ABC1/  <---------------------------------- Your estimate short name (max 4 characters)
└── test/  <------------------------------ The test subfolder (do not submit the results for train)
    ├── Arise - Run Run Run/  <----------- 50 subfolders, one for each track
    │   ├── vocals.wav  <----------------- One wav file for every target you want to submit (up to 5)
    │   ├── accompaniment.wav
    │   ├── drums.wav
    │   ├── bass.wav
    │   └── other.wav
    ⋮
    └── Zeno - Signs/
```

### Step 3: Compute Evaluation Scores

Evaluate your estimate folder using the BSSEval v4 metric using the [museval package](https://github.com/sigsep/sigsep-mus-eval). We provide a docker image for the evaluation tools so that you do not need to set up a python environment.

```
ABC1/  <---------------------------------- Your estimate short name (max 4 characters)
└── test/  <------------------------------ The test subfolder (do not submit the results for train)
    ├── Arise - Run Run Run.json <-------- 50 json files that include your bsseval v4 scores
    ⋮
    └── Zeno - Signs.json
```

:warning: If you apply your separation method on the default dataset encoded in the STEM format (not converted to `wav` first), please make sure you use the same ffmpeg version for separation and evaluation. We tested several different machines and ffmpeg version and did not run into any problems, but we cannot guarantee that the decoded outputs of two different ffmpeg versions are identical and would not affect the bsseval scores. E.g. when silence > 512 samples would be added in the beginning of a target source.

### Step 4: Submission to Github

To submit your Evaluation scores, we kindly ask you to create a Pull Request on github for your submission.

The first step is to prepare your evaluation score folder so that it matches our [/submission-template/ABC1](/submission-template) directory in this repository (`ABC1` in the example above). Make sure you add the [description.md](/submission-template/ABC1/description.md) file to briefly describe your proposed method. Then put your `submission` directory into the [/submissions](/submissions) subfolder.

In the following we describe the basic steps to create this pull request with your submission through the github user interface (if you already know git, you can safely ignore many steps):

1. Create a fork of this repository by clicking on the "Fork" button at the top right of this page.
2. In your new repository, navigate to the submissions directory (after navigating, the URL should be something like https://github.com/your-github-username/sigsep-mus-2018/tree/master/submissions).
3. Click the "Upload files" button.
4. Upload your submission directory, this should upload a 51 files in total (50 json files and the `description.md`). Hit "Commit changes" at the bottom of the page.
5. Click the "New Pull Request" button.
6. On the next page, click the "Create Pull Request" button.
7. Make the pull request title the same as your submission folder, and click the "Create Pull Request" button.
8. This will take you the pull request page for your paper, with a URL like https://github.com/sigsep/sigsep-mus-2018/pull/2. Save this URL for future reference. At this point, you have finished your submission; don't close the pull request.
9. Your submission will be tested by an [automated test system](/tests). We may instruct you to update your submission with a few changes. To do so, simply follow steps 2-4 again with your updated submission directory (i.e. navigate to the submissions directory in your fork and upload your new updated folder). The pull request will be updated automatically. Once the tests pass, we will merge your submission.
10. This the merging should take place before the deadline of __April 1st 2018__.

#### Further Notes

- You can submit multiple submission directories in one pull request.
- :warning: please do not delete your estimates as we will aggregate the wav files later through a separate upload system.

## Support

If you need help with your submission, you can use our chat or contact @faroit.
[![Join the chat at https://gitter.im/sigsep-mus-2018/Lobby](https://badges.gitter.im/sigsep-mus-2018/Lobby.svg)](https://gitter.im/sigsep-mus-2018/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

### Acknowledgements

We thank [Colin Raffel](http://colinraffel.com) for the inspiration to use git for handling the SiSEC submissions.
