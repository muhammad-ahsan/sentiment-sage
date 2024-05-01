import uvicorn
from fastapi import FastAPI

from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = FastAPI()
model_path = "nltk_data/vader_lexicon.zip/vader_lexicon/vader_lexicon.txt"
model = SentimentIntensityAnalyzer(lexicon_file=model_path)


@app.get("/")
async def root():
    return {"message": "Welcome to sentiment-sage. Your mood reader ;)"}


@app.get("/predict")
async def predict(q: str):
    return model.polarity_scores(q)


@app.get("/health")
async def health():
    return {"message": "Congratulations, I am healthy :) "}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
