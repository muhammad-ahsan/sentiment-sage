import uvicorn
from fastapi import FastAPI

from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = FastAPI()
model = SentimentIntensityAnalyzer(lexicon_file="nltk_data/vader_lexicon.zip/vader_lexicon/vader_lexicon.txt")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/predict")
async def predict(q: str):
    return model.polarity_scores(q)


@app.get("/health")
async def health():
    return {"message": "Congratulations, I am healthy :) "}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
