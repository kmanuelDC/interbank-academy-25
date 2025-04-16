# 💰 Reporte de Transacciones - Interbank Academy 25

## 📌 Introducción

Este proyecto desarrolla una pequeña aplicación de análisis de transacciones financieras a partir de un archivo CSV. Su objetivo es generar un reporte simple y claro que detalle:

- El balance final de las transacciones.
- La transacción de mayor monto.
- El número de transacciones por tipo (Crédito y Débito).

---

## ▶️ Instrucciones de Ejecución

### 1. Clonar el repositorio (si aplica)
```bash
git clone https://github.com/kmanuelDC/interbank-academy-25.git
cd interbank-academy-25
```

### 2. Crear un archivo CSV
```bash
touch data.csv
id,tipo,monto
1,Débito,235.81
2,Débito,227.59
3,Crédito,34.28
4,Crédito,309.36
5,Crédito,418.59
.....
```

### 3.Estructura del proyecto

```
├── README.md
├── calculatorBalance.py
└── data.csv

balance_final
Agrupé los datos por tipo para calcular el balance final de manera más simple y estructurada, en solo dos pasos.

trans_max
Utilicé Pandas para obtener el registro con el monto más alto y asignarlo a una variable como un objeto completo (fila).

count
Con Pandas, también generé un objeto tipo DataFrame que muestra el conteo de transacciones agrupadas por tipo.


```

### 4.Instalar dependencias
```bash
pip install pandas
```

### 5. Ejecutar el script
```bash
python calculatorBalance.py
```