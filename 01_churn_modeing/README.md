# Churn Prediction Model with XGBoost

This project was part of the BCG Advanced Analytics virtual internship. The purpose of this assigned analysis was to attempt to predict churn over a dataset of customers and prices introducing key analytics and visualization concepts.

This internship was completed in the summer of 2021, my intention was to refactor the analysis code with a more updated approach to the visualizations.

## 📊 Overview

This project implements an optimized XGBoost classifier to predict customer churn in the energy/utility sector. The analysis includes:

- Data preprocessing and feature engineering
- Baseline and optimized model comparison
- Hyperparameter tuning with Optuna
- Comprehensive model evaluation (ROC-AUC, confusion matrices, precision-recall curves)
- Feature importance analysis
- SHAP (SHapley Additive exPlanations) values for model interpretability

## ✨ Features

- **Data Processing**: Aggregates time-series price data and engineers features from dates
- **Model Optimization**: Uses Optuna for efficient Bayesian hyperparameter optimization
- **Visualization**: Includes 30+ visualizations for model performance and interpretation
- **Explainability**: SHAP analysis for understanding individual predictions

## 🔧 Requirements
```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
scikit-learn>=1.2.0
xgboost>=2.0.0
optuna>=3.0.0
shap>=0.42.0
jupyter>=1.0.0
```

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR-USERNAME/churn-prediction-xgboost.git
cd churn-prediction-xgboost
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Place your data files (`client_data.csv` and `price_data.csv`) in the project directory

## 📖 Usage

1. Open the Jupyter notebook:
```bash
jupyter notebook churn_prediction_improved.ipynb
```

2. Update the `DATA_DIR` path in Section 2 if needed

3. Run all cells in order

## 📈 Model Performance

- **Baseline Model**: ~0.68 ROC-AUC
- **Optimized Model**: ~0.72+ ROC-AUC (after hyperparameter tuning)
- **Cross-Validation**: 5-fold stratified CV with detailed performance metrics

## 📁 Project Structure
```
├── churn_prediction_improved.ipynb  # Main analysis notebook
├── client_data.csv                   # Customer data (not included)
├── price_data.csv                    # Price history data (not included)
├── models/                           # Saved models directory
├── .gitignore                        # Git ignore file
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

## 📊 Key Visualizations

- ROC-AUC curves with cross-validation
- Feature importance (multiple methods)
- Partial dependence plots
- SHAP summary, waterfall, and beeswarm plots
- Confusion matrices
- Precision-recall curves
- Final performance dashboard

## 🛠️ Technical Details

### Data Processing
- Merges client data with aggregated price history
- Engineers date-based features (tenure, days since modification, etc.)
- One-hot encodes categorical variables
- Handles missing values

### Model Training
- Baseline XGBoost with sensible defaults
- Optuna-based hyperparameter optimization
- Stratified k-fold cross-validation
- Early stopping to prevent overfitting

### Evaluation Metrics
- Accuracy, Precision, Recall
- ROC-AUC score
- Precision-Recall curves
- Confusion matrices

## 👤 Author

**Your Name**
- GitHub: [@RandallEsc](https://github.com/Randallesc)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/RandallEscalante)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Data sourced from [mention source if applicable]
- Built with Python, XGBoost, and SHAP
- Inspired by best practices in ML interpretability

## 📝 Notes

This is a learning project demonstrating:
- End-to-end machine learning workflow
- Model optimization techniques
- ML interpretability with SHAP
- Professional project documentation
```

6. **Save**: `Ctrl + S`

---

### **Step 3: Create `requirements.txt`**

1. **Right-click** in Explorer again
2. **Select "New File"**
3. **Name it**: `requirements.txt`
4. **Press Enter**
5. **Paste this content**:
```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
scikit-learn>=1.2.0
xgboost>=2.0.0
optuna>=3.0.0
shap>=0.42.0
<<<<<<< HEAD
jupyter>=1.0.0
=======
jupyter>=1.0.0
>>>>>>> 16f6357f4f81a33ca40683d5bcb493d37e8866f2
