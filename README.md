# Advanced Analytics in Python

A portfolio of data science and machine learning projects demonstrating advanced analytical techniques, optimization algorithms, and predictive modeling.

---

## 📂 Projects

### 1. [Customer Churn Prediction with XGBoost](./01_churn_prediction/)

Predicting customer churn in the energy/utility sector using XGBoost with hyperparameter optimization and SHAP interpretability.

**Key Features:**
- Hyperparameter tuning with Optuna (Bayesian optimization)
- Feature engineering from time-series price data
- SHAP analysis for model explainability
- 30+ visualizations including ROC curves, confusion matrices, and feature importance

**Technologies:** Python, XGBoost, Optuna, SHAP, scikit-learn  
**Performance:** ROC-AUC improved from 0.68 (baseline) to 0.72+ (optimized)

**Techniques:**
- Stratified k-fold cross-validation
- Time-series aggregation
- One-hot encoding
- Partial dependence plots

---

### 2. [Cutting Stock Problem - Column Generation Algorithm](./02_cutting_stock_column_generation/)

Implementation of the column generation algorithm to solve the cutting stock optimization problem using linear programming.

**Key Features:**
- Complete column generation implementation
- Interactive visualizations of cutting patterns
- Step-by-step algorithm walkthrough
- Dual price analysis and reduced cost calculations

**Technologies:** Python, CVXPY, Linear Programming, Integer Programming  
**Performance:** Optimal solution converged in 2 iterations

**Techniques:**
- Column generation
- Restricted master problem (RMP)
- Pricing problem (knapsack)
- Duality theory
- Integer programming

---

## 🎯 About This Repository

This repository showcases advanced analytical skills across multiple domains:

- **Machine Learning:** Predictive modeling, feature engineering, hyperparameter optimization
- **Optimization:** Linear programming, column generation, integer programming
- **Statistics:** Cross-validation, hypothesis testing, model evaluation
- **Visualization:** matplotlib, seaborn, SHAP plots
- **Software Engineering:** Clean code, documentation, version control

---

## 🛠️ Technologies & Tools

**Languages:** Python

**Machine Learning:** scikit-learn, XGBoost, Optuna

**Optimization:** CVXPY, NumPy

**Data Analysis:** Pandas, NumPy

**Visualization:** Matplotlib, Seaborn, SHAP

**Development:** Jupyter Notebooks, Git, VS Code

---

## 📊 Skills Demonstrated

### Data Science
- Feature engineering and selection
- Model training and evaluation
- Hyperparameter optimization
- Cross-validation techniques
- Ensemble methods

### Optimization
- Linear programming formulation
- Column generation algorithms
- Dual problem analysis
- Integer programming
- Decomposition methods

### Communication
- Clear documentation
- Professional visualizations
- Reproducible analysis
- Technical writing

---

## 🚀 Getting Started

Each project folder contains:
- Complete Jupyter notebook with analysis
- Project-specific README with detailed documentation
- requirements.txt for dependencies
- Data (where applicable and not proprietary)

### Installation

Clone the repository:
```bash
git clone https://github.com/Randallesc/Advanced_Analytics_in_Python.git
cd Advanced_Analytics_in_Python
```

Navigate to a project folder and install dependencies:
```bash
cd 01_churn_prediction
pip install -r requirements.txt
```

Run the notebook:
```bash
jupyter notebook
```

---

## 📈 Project Structure
```
Advanced_Analytics_in_Python/
│
├── 01_churn_prediction/
│   ├── churn_model.ipynb
│   ├── README.md
│   ├── requirements.txt
│   └── data/
│
├── 02_cutting_stock_column_generation/
│   ├── cutting_stock_analysis.ipynb
│   ├── README.md
│   └── requirements.txt
│
├── .gitignore
└── README.md (this file)
```

---

## 🎓 Background

These projects were developed as part of graduate-level coursework in:
- Advanced Analytics
- Operations Research
- Machine Learning
- Optimization Methods

They demonstrate practical application of theoretical concepts to real-world problems.

---

## 📫 Contact

**Randall**  
GitHub: [@Randallesc](https://github.com/Randallesc)

---

## 📄 License

MIT License - Feel free to use these projects for educational purposes.

---

## 🔜 Future Projects

Planned additions:
- Time series forecasting
- Natural language processing
- Deep learning applications
- Network optimization
- Simulation modeling

---

**⭐ If you find these projects helpful, please consider starring the repository!**