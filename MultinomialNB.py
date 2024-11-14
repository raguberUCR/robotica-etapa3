from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from Nao_Vocabulary import nao_vocabulary

# Definir las frases de ejemplo para cada categoría
saludo_nao = nao_vocabulary["saludo_nao"]
reanudar_lectura = nao_vocabulary["reanudar_lectura"]
despedida_nao = nao_vocabulary["despedida_nao"]

# Aquí añadimos otras categorías: navegación, lectura, etc.

# Etiquetas de las categorías (0 = saludo, 1 = despedida, etc.)
etiquetas = (
    ['saludo_nao'] * len(saludo_nao) +  # Etiquetas para saludo_nao
    ['despedida_nao'] * len(despedida_nao) +  # Etiquetas para despedida_nao
    ['reanudar_lectura'] * len(reanudar_lectura)  # Etiquetas para reanudar_lectura
)

# Combinar todas las frases en un solo conjunto de datos
frases = saludo_nao + despedida_nao + reanudar_lectura

# Crear un modelo con un pipeline de TF-IDF y Naive Bayes
modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Entrenar el modelo
modelo.fit(frases, etiquetas)

consulta_usuario = "sigue adelante"
prediccion = modelo.predict([consulta_usuario])

print(f"Categoría predicha: {prediccion[0]}")

from sklearn.model_selection import train_test_split

# Dividir el conjunto de datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(frases, etiquetas, test_size=0.2, random_state=42)

# Crear el pipeline del modelo
modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Realizar predicciones con el conjunto de prueba
y_pred = modelo.predict(X_test)

# Calcular las métricas de evaluación
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
conf_matrix = confusion_matrix(y_test, y_pred)

# Imprimir los resultados
print(f"Precisión (accuracy): {accuracy:.4f}")
print(f"Precisión (precision): {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print("Matriz de confusión:")
print(conf_matrix)