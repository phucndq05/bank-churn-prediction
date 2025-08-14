<h1 align="center">🛡️ 銀行顧客の解約（Churn）予測 & Webアプリ デモ</h1>

本プロジェクトは、銀行顧客データを分析して **解約（Churn）** を予測する **機械学習** プロジェクトです。  
解約の主な要因を特定し、信頼性の高い分類モデルを学習したうえで、**Flask** によるインタラクティブな Web アプリとして最良モデルをデプロイします。

---

## 📚 データセット
使用データは **Kaggle** の *Bank Customer Churn Prediction* データセットです（高い Usability スコア）。  
- 出典: [Kaggle Dataset Link](https://www.kaggle.com)  

---

## 🚀 特長（Key Features）
- **包括的なEDA**: KDEプロットや地図可視化（choropleth など）を用いた詳細な探索的データ分析でビジネス示唆を抽出。  
- **モデルベンチマーク**: 複数モデル（例: Logistic Regression, Random Forest）を学習・比較し、最良モデルを選定。  
- **モデル永続化**: 学習済みモデルおよびスケーラーを `joblib` で保存し、デプロイに利用。  
- **インタラクティブWeb**: **Flask** ベースのUIで新規顧客データに対するリアルタイム推論を提供。

---

## 🧰 技術スタック（Tech Stack）
- **言語**: Python  
- **主要ライブラリ**:  
  - データ処理: Pandas, NumPy  
  - 可視化: Matplotlib, Seaborn, Plotly  
  - 機械学習: Scikit-learn  
  - Webフレームワーク: Flask  
  - モデル永続化: Joblib

---

## 📋 プロジェクトワークフロー
1. **EDA（探索的データ分析）**: 初期パターンの発見とインサイト抽出。  
2. **前処理**: 欠損処理、カテゴリ特徴量のエンコード、数値特徴量のスケーリング。  
3. **学習**: 複数の分類モデル（例: Logistic Regression, Random Forest）を学習。  
4. **評価**: Accuracy / Precision / Recall / F1-Score で性能評価。  
5. **デプロイ**: 最良モデルを **Flask** Web アプリとして提供。

---

## 🚀 はじめに（Getting Started）

### 1️⃣ インストール
```bash
git clone https://github.com/phucndq05/bank-churn-prediction.git
cd bank-churn-prediction

python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### 2️⃣ データ分析（EDA）の実行
Jupyter Notebook を開いて、EDA と学習プロセスを確認します:
```bash
jupyter notebook bank_churn_analysis.ipynb
```

### 3️⃣ Webアプリの起動
```bash
python3 app.py
```
ブラウザで `http://127.0.0.1:5000` にアクセス。

---

## 📁 プロジェクト構成（Project Structure）
```
bank-churn-prediction/
├── deployment/
│   ├── model.pkl
│   └── scaler.pkl
├── templates/
│   ├── index.html
│   └── result.html
├── data/
│   └── Churn_Modelling.csv
├── app.py
├── bank_churn_analysis.ipynb
├── requirements.txt
└── README.md
```

---

## 🤖 モデル
- **例**: Logistic Regression / Random Forest など  
- **特徴量処理**: カテゴリのエンコード、数値のスケーリング  
- **評価指標**: Accuracy / Precision / Recall / F1-Score

---
