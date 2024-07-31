# Sudanese-Arabic-Dialect-Encoding-Using-XLM-RoBERTa-(Zol-RoBERTa)


## Overview
Zol-RoBERTa is a specialized language model designed for sentiment analysis in the Sudanese Arabic dialect, leveraging the XLM-RoBERTa model. This project aims to enhance the understanding and processing of Sudanese Arabic by fine-tuning a pre-trained model on a Sudanese dialect corpus.

## Overview

The Zol-RoBERTa focuses on developing a comprehensive language model specifically tailored for the Sudanese Arabic dialect, a language spoken by over 40 million people. This project aims to fill a significant gap by creating a model that captures the linguistic features of the Sudanese-Arabic Dialect. This promotes inclusivity in language technology, making advanced NLP tools accessible for a wider range of users.

The model's perfomance was evaluated using Sentiment nalysis, achieving notable accuracy. However, the broader objective extends beyond sentiment analysis, aiming to enhance NLP applications across various fields, including agriculture. Here, the model can support a new generation of farmers, providing them with tools to navigate daily challenges, thereby contributing to economic and social development in Sudan. This project not only advances NLP for underrepresented languages but also fosters a more inclusive and diverse technological landscape.

### Why is this project important ?

Sentiment analysis was used as an evaluation task to measure the model's performance, but the broader objective is to enhance NLP capabilities for a variety of applications in the Sudanese Dialect. This model can support a new generation of educated but practically inexperienced farmers in agriculture by offering deep learning tools that provide insights and answers to routine farming activities. Overall, this project has the potential to drive economic and social development in Sudan.









## Dataset Used
The dataset consists of 6.5 million sentences collected from various social media platforms. This diverse dataset captures a wide range of informal language, including slang and abbreviations, reflective of how people communicate online. 

### Sentiment Analysis Dataset
For the sentiment analysis task, two datasets were primarily used:
1. **Transportation Services Dataset**: Includes 2,116 tweets discussing transportation services.
2. **Telecommunication Services Dataset**: Contains 4,712 tweets expressing opinions about telecommunication services in Sudan, categorized into positive, negative, and neutral sentiments.

**Sample of the dataset:**

<p align="center">
  <img src="images/rev_tele.png" alt="Alt text" width="400"/>
</p>

### Methodology Overview:

<p align="center">
  <img src="images/Methodology.png" alt="Alt text" width="500"/>
</p>


#### Stages:

- **Pre-training Stage:** The model underwent pre-training on a Sudanese Arabic dialect , based on the XLM-RoBERTa architecture, was pre-trained on a Sudanese Arabic dialect corpus. This phase was essential to enhance the model's understanding of the unique linguistic features of Sudanese-Arabic dialect .

- **Fine-Tuning Stage:** The pre-trained model was then fine-tuned for Sentiment Analysis, adapting it (adding two classification layers) to classify text into positive, negative, or neutral sentiments. This stage refines the model's capabilities to accurately interpret sentiment-specific features in the language.



<p align="center">
  <img src="images/fine-tuning_fin.png" alt="Alt text" width="300"/>
</p>


## Evaluation and Results

The Model's performance was assessed using metrics such as Accuracy and F1-score to ensure it meets the desired objectives for Sentiment Analysis in the Sudanese dialect.


### Performance on Sudanese Dataset
| Model         | Accuracy | F1-Score |
|---------------|----------|----------|
| XLM-RoBERTa   | 61.6%    | 47%      |
| Zol-RoBERTa   | 81.1%    | 78.7%    |


Zol-RoBERTa shows a significant improvement in sentiment analysis for the Sudanese dialect, demonstrating the value of domain-specific pre-training.


### Conclusion

"Zol-Roberta" stands as a significant step forward in NLP for the Sudanese-Arabic dialect, providing a robust tool that enhances the understanding of this underrepresented dialect. The model achieved good results, underscoring its effectiveness and enabling it to set the foundation for expanding NLP applications in various fields.

## Usage and Installation

To use the Zol-RoBERTa model , follow these steps to set up your environment:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/DuaaAlshareef/Sudanese-Arabic-Dialect-Encoding.git
