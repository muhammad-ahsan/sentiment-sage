# Sentiment Server


1. A dockerized REST API which encapsulates a machine learning model 
2. A machine learning model based on nltk.
3. Serve as standalone sentiment prediction model 
4. Given a sentence, the model provides a sentiment score based on positivity, negativity and neutrality

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
