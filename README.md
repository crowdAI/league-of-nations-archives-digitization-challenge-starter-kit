# league-of-nations-archives-digitization-challenge-starter-kit
![CrowdAI-Logo](https://github.com/crowdAI/crowdai/raw/master/app/assets/images/misc/crowdai-logo-smile.svg?sanitize=true)

This is a starter kit for the [League of Nations archives digitization challenge](https://www.crowdai.org/challenges/league-of-nations-archives-digitization-challenge) on 
[crowdAI](https://www.crowdai.org).

# Problem Statement
This challenge is an image classification problem, where in the training set you are given 4692 images belonging to either `english` or `french`, and then you are provided 14216 images in the test set, where you are supposed to predict the class the said image belongs to.

# Dataset
The datasets are available in the [Dataset section of the challenge page](https://www.crowdai.org/challenges/league-of-nations-archives-digitization-challenge/dataset_files), and on following the links, you will have two files : 

* `train.tar.gz`
* `test.tar.gz`

`train.tar.gz` expands into a folder containing two subfolders, of the form : 

```
.
└── train
    ├── en
    └── fr
```
The folders `en` and `fr` have `.jpg` images belonging to the respective class.
For the rest of this starter kit you are encourage to download both the files, and extract them and place them in the `data/` directory.

# Author
Sharada Mohanty <sharada.mohanty@epfl.ch>
