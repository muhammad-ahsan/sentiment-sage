# Sentiment Server

A machine learning model based on nltk. A dockerized REST Api which encapsulates a machine learning model and serve as standalone sentiment predictio model when given a sentence.

# Build Docker

docker build -t sample_model .

# Run Docker

docker run -p 8000:8000 sample_model

# API Interface

1. http://0.0.0.0:8000
2. http://0.0.0.0:8000/docs
3. http://0.0.0.0:8000/health
4. http://0.0.0.0:8000/predict?q=this%20is%20great


# References
1. https://www.nltk.org
1. https://www.nltk.org/nltk_data/
