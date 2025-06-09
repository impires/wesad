#!/usr/bin/env python
# coding: utf-8

from ae_feature_extractor import autoencoder
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

ae = autoencoder ()
ae.train_model_c ()
ae.extract_features()

