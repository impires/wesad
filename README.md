## Stress Detection from Multimodal Wearable Sensor Data using autoencoder latent features
### Dataset: WESAD 
https://archive.ics.uci.edu/ml/datasets/WESAD+%28Wearable+Stress+and+Affect+Detection%29


Run scripts in the following order (can take a while) to prepare data and extract features from the latent layer of autoencoder model: </br>
1. Preprocess and merge subject data
</br>Command: <br>
python merge_subj_data.py
My: python3 merge_subj_data.py
</br></br>
Input data path: 'data/WESAD/'</br>
Generates the following files in data folder:</br>
subj_merged_acc_w.pkl</br>
subj_merged_bvp_w.pkl</br>
subj_merged_eda_temp_w.pkl</br>
merged_chest_fltr.pkl</br></br>
2. Create autoencoder model and extract latent features
</br>Command: </br>
python extract_ae_latent_features.py
My: /opt/homebrew/bin/python3.10 /Volumes/One\ Touch/wesad-main/extract_ae_latent_features.py
</br></br>
Input files:<br>
subj_merged_acc_w.pkl</br>
subj_merged_bvp_w.pkl</br>
subj_merged_eda_temp_w.pkl</br>
merged_chest_fltr.pkl</br>
  - Uses ae_feature_extractor.py to build and train autoencoder model and extract features. </br>
  - Save extracted features leaving one subject out into pickle files in features/train and features/test directories. The number in the filename indicates which subject was left out in each fold.</br></br>
3. SVM_classifier.ipynb - Open in Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1G0dqghsFeUKa36uquWuICoLO9DAxQYFy/view?usp=sharing) </br></br>
4. MLP_classifier.ipynb - Open in Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1z9Qw9MAhgAC3c4l2s9sk-9B9NQ4zc1Z0/view?usp=sharing) </br></br>
5. RandomForest_classifier.ipynb - Open in Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1Crn0Z9yG6eO3YtjfrSwJW4bRm7Hju9Mf/view?usp=sharing) </br></br>
6. BNN_classifier.ipynb - Open in Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1NXbY48sSe5ko3Oofvu9hiLoLIrYn34f6/view?usp=sharing) </br></br>
7. AutoKeras_classifier.ipynb - Open in Google Colab: [![Open In Colab](https://drive.google.com/file/d/1-dYZwtbiMvh9DMa-M2oDVugJ0yhtvmO7/view?usp=sharing)





