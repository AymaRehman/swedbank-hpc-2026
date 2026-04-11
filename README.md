<img width="402" height="277" alt="image" src="https://github.com/user-attachments/assets/3b53ded6-7a3d-4b56-9d37-f4cbd34c09f8" />## Swedbank HPC Fraud Detection Challenge
![Website Status](https://img.shields.io/website?url=https%3A%2F%2Fswedbank-fraud-detection-frontend.onrender.com&up_message=online&up_color=green&down_message=offline&down_color=red&label=Frontend%20Status)
![API Status](https://img.shields.io/website?url=https%3A%2F%2Fswedbank-fraud-detection-api.onrender.com%2Fdocs&up_message=online&up_color=blue&down_message=offline&down_color=red&label=API%20Status)

ML-powered SMS fraud detection system built with pandas, scikit-learn, fastAPI, and trained on RTU's HPC cluster. Developed in collaboration with Ģirts Bērziņš of Swedbank as part of RTU's HPC challenge 2026.

### Participants:

    Matthew Harris
    Ayma Rehman
    Klints Legranžs
    Evelīna Šadurska

### Live Demo
- [Frontend](https://swedbank-fraud-detection-frontend.onrender.com)
- 
- [API Backend](https://swedbank-fraud-detection-api.onrender.com/docs)


### Tech Stack

| Library | Purpose |
|---|---|
| numpy | Numerical operations and array handling |
| pandas | Data loading and manipulation |
| scikit-learn | ML model training and evaluation (Logistic Regression, Random Forest, etc.) |
| matplotlib | Data visualization |
| seaborn | Statistical data visualization |
| FastAPI | API endpoint |
| uvicorn | Server for running FastAPI |
| joblib | Model serialization and loading |
| streamlit | Creating the frontend |
| Docker | Containerization for consistent environments |
| Render | Cloud hosting for API and UI services |

### Deployment & Containerization
This project is containerized using **Docker** and deployed via **Render Blueprints**.

## To set up on your end...

### 1. Clone the repository
```bash
git clone https://github.com/mgharris97/swedbank-hpc-2026.git
cd swedbank-hpc-2026
```

### 2. Create and activate the virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
   On Windows: ```venv\Scripts\activate```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the dataset
Download the SMS dataset from Kaggle and place it in the `data/` folder locally on your computer 

[UC Irvine SMS Spam Collection Dataset from Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
[Latvian SMS Synthetic Dataset](https://drive.google.com/file/d/1p9OcURV15c4lnN1N7C-AYVa_qAzhDKvw/view?usp=sharing)

### 5. Preprocess the data
```bash
python src/preprocess.py
```

### 6. Train the model
```bash
python src/model.py
```
### 7. Run the api
```bash
uvicorn src.api:app --reload
```
### 8. Run the frontend
```bash
streamlit run src/frontend.py
```


### Note:
Keep in mind, every time you come back to work on this project, you need to reactivate the venv first: ```source venv/bin/activate ```

Your directory structure should look like this :)

```
.
├── data
│   ├── processed
│   └── spam.csv
├── hpc
│   ├── grid_search.md
│   ├── grid_search.sh
│   ├── results
│   └── setup.md
├── models
│   ├── model.pkl
│   └── vectorizer.pkl
├── notebooks
│   └── eda.ipynb
├── src
│   ├── api.py
│   ├── config.py
│   ├── evaluate.py
│   ├── grid_search.py
│   ├── model.py
│   ├── preprocess.py
│   └── frontend.py
├── Dockerfile
├── render.yaml
├── requirements.txt
├── LICENSE
├── Production.md
└── README.md
```

