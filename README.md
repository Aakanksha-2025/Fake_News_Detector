# Fake_New_Detector
A machine learning–based model that detects whether a news article is real or fake.
---
## Features
- Text Preprocessing
- TF-IDF vectorization
- Trained ML model
- Flask API for prediction

---
## Project Structure
```
fake-news-detector/
⤷data
  ⤷[link given below]
⤷prepare_data.py
⤷preprocess_data.py
⤷train_model.py
⤷test_model.py
⤷api.py
⤷model.pkl
⤷vectorizer.pkl
```
## Dataset
*[https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset]*
1. Download dataset from Kaggle link
2. Place Fake.csv and True.csv inside _/data_ folder
3. Run prepare_data.py

## Installation
1. Clone the repository
   ```
   git clone https://github.com/Aakanksha-2025/Fake_News_Detector.git
   cd Fake_News_Detector
   ```
2. Install Dependencies
   ```
   pip install -r requirements.txt
   ```

## Running the API

```
python api.py
```

_API runs at:_
```
http://127.0.0.1:5000
```

## Example Request

```
curl -Method POST http://127.0.0.1:5000/predict `
-Headers @{"Content-Type"="application/json"} `
-Body '{"text":"Aliens are controlling world leaders"}'
```
