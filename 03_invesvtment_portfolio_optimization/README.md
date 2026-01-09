# Investment Portfolio Optimization with Integer Programming

A binary integer programming solution for capital budgeting with complex logical constraints.

## 📋 Problem Description

Optimize investment selection to maximize expected profit while satisfying budget and logical business constraints.

### Investment Universe

- **7 potential investments** with varying costs ($3-$12) and profits ($1-$5)
- **Budget constraint:** $30 available
- **Complex logical rules:** mutual exclusivity, dependencies, either-or conditions

### Business Constraints

1. Must select at least one investment
2. Investments 1 and 3 are mutually exclusive
3. Investment 4 requires investment 2
4. Must choose both investments 1 and 5, or neither
5. Diversification requirement with two options

## 🎯 Solution Approach

**Technique:** Binary Integer Programming with Big-M formulation

**Solver:** CVXPY with CBC/GLPK

**Complexity:** NP-hard (integer programming with logical constraints)

## 📊 Results

- **Optimal Profit:** Maximized within constraints
- **Budget Utilization:** Efficient allocation
- **Constraints:** All satisfied and verified
- **ROI:** Balanced portfolio selection

## 🚀 Usage
```bash
pip install -r requirements.txt
jupyter notebook investment_optimization.ipynb
```

## 🛠️ Technologies

- Python 3.8+
- CVXPY (optimization modeling)
- NumPy, Pandas (data processing)
- Matplotlib, Seaborn (visualization)

## 📈 Key Features

- Complete mathematical formulation
- Constraint verification
- Visual solution analysis
- Business insights and recommendations

## 🎓 Skills Demonstrated

- Integer programming
- Constraint modeling (logical constraints)
- Optimization problem formulation
- Big-M method
- Financial analysis
- Decision science

## 📚 Applications

- Capital budgeting
- Project selection
- Resource allocation
- Portfolio management
- Strategic planning

## 👤 Author

Randall - Graduate coursework in optimization and operations research
```

**Save it**

---

### **2. Create requirements.txt**

### 3. [Investment Portfolio Optimization](./03_investment_portfolio_optimization/)
Binary integer programming solution for capital budgeting with complex logical constraints.

**Technologies:** Python, CVXPY, Integer Programming, Constraint Modeling  
**Techniques:** Big-M formulation, logical constraints, decision optimization  
**Highlights:** Constraint verification, ROI analysis, business insights

---

**Right-click** → **New File** → `requirements.txt`
```
cvxpy>=1.3.0
numpy>=1.23.0
pandas>=1.5.0
matplotlib>=3.6.0
seaborn>=0.12.0
jupyter>=1.0.0