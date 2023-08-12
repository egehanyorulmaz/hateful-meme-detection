# Detecting Hateful Memes on Social Media

## Overview
This project aims to develop a model that can accurately detect hate speech in memes shared on social media platforms. It utilizes a dataset published by Meta, consisting of 10,000 labeled samples of hate speech and non-hate speech memes. The goal is to leverage both text and image analysis to identify hateful memes, based on the assumption that relying solely on either modality would be insufficient.

## Data
- The dataset contains 10,000 labeled samples of memes
- 64.1% are non-hateful and 35.9% are hateful
- Includes both the text and image of each meme

## Methodology
- Text features extracted using FastText word embeddings
- Image features extracted from a ResNet-18 CNN model pre-trained on ImageNet
- Unimodal models developed using text-only and image-only features
- Multimodal model combining text and image features
- Models optimized using Keras Tuner and evaluated on a test set

## Results
- Multimodal model underperformed likely due to challenges in integrating diverse features
- Visual cues prove more useful than text for hate speech detection in memes

## Future Work
- Collect more diverse data from additional platforms
- Improve integration of text and image features
- Apply dimensionality reduction techniques
- Explore other word embeddings like BERT
- Enhance context modeling between text and images

## Reference
- [Dataset source]()
- Details on methodology and experiments available in [this paper]()
