#!/usr/bin/env python

import numpy as np
import os
import glob

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0) # only difference


LINES = []
LINES.append("filename,prob_en,prob_fr")
for _file_path in glob.glob("data/test_images/*.jpg"):
    probs = softmax(np.random.rand(2))
    LINES.append("{},{},{}".format(
        os.path.basename(_file_path),
        probs[0],
        probs[1]
    ))

fp = open("random_prediction.csv", "w")
fp.write("\n".join(LINES))
fp.close()

