# Fire Station Location Optimization using SOCP

Optimal facility location using Second-Order Cone Programming to minimize emergency response time.

## 📋 Problem Description

Given n villages with known coordinates, determine the optimal location for a fire station that minimizes the maximum distance (worst-case response time) to any village.

### Problem Characteristics

- **Objective:** Minimax (minimize maximum distance)
- **Type:** Second-Order Cone Programming (SOCP)
- **Constraints:** Euclidean distance constraints
- **Villages:** 20 randomly generated locations
- **Area:** 10 × 10 square units

## 🎯 Why Minimax?

Unlike minimizing average distance (which gives the centroid), minimax optimization ensures:
- **Equity:** No village is too far from emergency services
- **Fairness:** All communities receive similar service quality
- **Worst-Case Optimization:** Critical for emergency response planning

## 📐 Mathematical Formulation

**Decision Variables:**
- (x, y): Fire station coordinates
- t: Maximum distance to any village

**Objective:**
```
minimize t
```

**Constraints (for each village i):**
```
‖(x, y) - (xᵢ, yᵢ)‖₂ ≤ t
```

This is a **second-order cone constraint**, making it a convex SOCP problem with guaranteed global optimum.

## 📊 Key Results

- **Optimal Solution:** Fire station location that minimizes worst-case distance
- **Equity Achieved:** Multiple villages share the maximum distance
- **Performance:** ~20-40% reduction in max distance vs naive approaches
- **Computational Efficiency:** Solves in seconds

## 🚀 Usage
```bash
pip install -r requirements.txt
jupyter notebook fire_station_optimization.ipynb
```

## 📈 Features

- Complete SOCP formulation and solution
- Interactive visualizations with coverage circles
- Comparison with alternative strategies (centroid, bounding box)
- Sensitivity analysis (varying number of villages)
- What-if scenarios (adding new villages)
- Distance distribution analysis

## 🛠️ Technologies

- **Python 3.8+**
- **CVXPY** - Convex optimization modeling
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation
- **Matplotlib** - Visualization

## 🎓 Skills Demonstrated

- Second-Order Cone Programming
- Convex optimization
- Facility location problems
- Minimax optimization
- Geometric optimization
- Sensitivity analysis
- Spatial analysis and visualization

## 📚 Applications

- **Emergency Services:** Fire stations, ambulances, police
- **Healthcare:** Hospitals, clinics, urgent care centers
- **Infrastructure:** Cell towers, power substations
- **Retail:** Distribution centers, service hubs
- **Public Services:** Schools, libraries, community centers

## 🔍 Key Insights

1. **Minimax vs Average:** Minimax ensures equity, while average minimization (centroid) can leave some villages underserved

2. **Critical Villages:** The optimal solution typically has 2-3 villages at exactly the maximum distance, forming a "critical set"

3. **Sensitivity:** Optimal location is sensitive to outlying villages - one remote village can significantly shift the optimal placement

4. **Scalability:** SOCP efficiently handles 5-100+ villages

## 📖 Theory

**Second-Order Cone Programming** is a class of convex optimization problems that generalize linear and quadratic programming:
```
minimize   cᵀx
subject to ‖Aᵢx + bᵢ‖₂ ≤ cᵢᵀx + dᵢ  for i = 1, ..., m
```

Euclidean distances naturally fit this framework, making SOCP ideal for geometric optimization problems.

## 🔗 Extensions

- Multiple fire stations (k-center problem)
- Weighted villages (by population)
- Road network distances (not just Euclidean)
- Coverage constraints (maximum acceptable distance)
- Budget constraints (balancing stations vs coverage)

## 👤 Author

Randall - Graduate coursework in optimization and operations research

## 📄 License

MIT License
```

**Save it**

---

### **2. Create requirements.txt**

**Right-click** → **New File** → `requirements.txt`
```
cvxpy>=1.3.0
numpy>=1.23.0
pandas>=1.5.0
matplotlib>=3.6.0
seaborn>=0.12.0
jupyter>=1.0.0
clarabel>=0.5.0