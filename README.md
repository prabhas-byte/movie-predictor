# Movie Rating Prediction

A beginner-friendly machine learning regression project to predict IMDb movie ratings using features like genre, director, lead actors, year, runtime, and number of votes.

Built with Python, pandas, scikit-learn, XGBoost, matplotlib & seaborn.

### What it does
- Loads and cleans the IMDb Movies India dataset (~15k movies)
- Preprocesses genres (multi-label → one-hot / first genre), encodes director & actor names (target encoding)
- Trains Random Forest + XGBoost regression models
- Evaluates using R², MAE, RMSE (~0.50–0.62 R² typical)
- Shows visualizations: rating distribution, average rating by genre/year, top directors

### How to Run

1. Clone or download this repository
2. Place `IMDb Movies India.csv` in the same folder ![Titanic](download from Kaggle: https://www.kaggle.com/datasets/adrianmcmahon/imdb-india-movies)
3. Install required packages:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn xgboost

#### Run the Script

python filename.py

## license

MIT License – free to use, modify, and learn from this task.


