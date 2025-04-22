
# 🎯 Overfitting em Modelos de Machine Learning

Overfitting (ou sobreajuste) ocorre quando um modelo de machine learning aprende os **detalhes e ruídos** do conjunto de treino a ponto de **comprometer sua capacidade de generalização** para novos dados.

---

## 🔍 Como Identificar Overfitting

- **Alta acurácia no treino** vs. **baixa acurácia na validação/teste**
- Modelo realiza previsões perfeitas nos dados de treino
- Complexidade desnecessária no modelo (muitos parâmetros)
- Gap grande entre métricas de treino e teste (ex: `accuracy_train = 1.00`, `accuracy_test = 0.76`)

---

## 🛡️ Estratégias para Prevenir Overfitting

1. **Cross-Validation**  
   Validação cruzada k-fold ajuda a garantir que o modelo generalize para diferentes subconjuntos dos dados.

2. **Regularização (L1, L2)**  
   Penaliza coeficientes exagerados, forçando simplificação do modelo.

3. **Redução de complexidade**  
   - Para árvores: limitar profundidade ou número de folhas
   - Para redes neurais: reduzir camadas ou neurônios

4. **Remoção de variáveis redundantes ou irrelevantes**

5. **Aumento de dados (data augmentation)**

6. **Uso de mais dados ou técnicas como ensemble (RandomForest, Gradient Boosting)**

---

## 🧪 Diagnóstico prático

- Plots de aprendizado (learning curves)
- Comparação entre métricas de treino e validação
- Usar métricas mais robustas (como ROC AUC, F1-score)

---

## 📚 Referências Bibliográficas

- Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* (2ª ed.).
- Chollet, F. (2018). *Deep Learning with Python*. Manning Publications.
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*.
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*.

---

> 💡 Dica prática: se seu modelo tiver **acurácia perfeita em treino**, **desconfie**. Provavelmente ele está apenas decorando os dados!

