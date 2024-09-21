# Sentiment Analysis on Customer Review

This repository contains a project for performing Aspect-Based Sentiment Analysis (ABSA) on customer reviews, specifically utilizing the YELP dataset. The goal of this project is to extract sentiments for various aspects from customer reviews, allowing for more detailed analysis of user opinions.

## Project Overview

- **Kaggle Notebook**: [Aspect-Based Sentiment Analysis on Customer Review](https://www.kaggle.com/code/shreyanshmanavshukla/aspect-based-sentiment-analysis-on-customer-review)
- **Dataset**: [YELP Dataset](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset)
- **Running APP**: [Aspect-Based Sentiment Analysis on Hugging Face Spaces](https://huggingface.co/spaces/ShuklaShreyansh/Aspect-Based_Sentiment_Analysis)

### Key Features:
- Sentiment analysis based on customer reviews.
- Aspect-based extraction: Different categories of sentiment (e.g., service, food quality, atmosphere).
- Uses an LSTM-based model for sentiment classification.
  
## Model Information

The model used for sentiment analysis is an LSTM (Long Short-Term Memory) network trained on the YELP dataset. The trained model is saved as `lstm_senti.h5`. The model performs aspect-based sentiment analysis by categorizing sentiments for specific review aspects.

### Model Training

The model was trained using the [aspect-based-sentiment-analysis-on-customer-review.ipynb](aspect-based-sentiment-analysis-on-customer-review.ipynb) notebook, which is available in this repository. The notebook contains all the steps required to preprocess the data, train the model, and evaluate its performance.

## Dataset

The YELP dataset is a large-scale dataset that contains millions of customer reviews. It's widely used in sentiment analysis projects. You can download the dataset from Kaggle [here](https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset).

## Running the Project

### Prerequisites:
- Python 3.10+
- `tensorflow`, `keras`, `numpy`, `pandas`, `gradio`

### Installation:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
