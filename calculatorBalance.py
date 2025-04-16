import pandas as pd

# Lectura csv
df = pd.read_csv('data.csv')

# Agrupacion por tipo
gr = df.groupby("tipo")["monto"].sum()
balance_final = gr["Crédito"] - gr["Débito"]

# Transacción más alta
trans_max = df.loc[df["monto"].idxmax()]

# Conteo de transacciones
count = df["tipo"].value_counts()

#print(conteo)

# Impresión
print(f"""
Reporte de Transacciones
---------------------------------------------
Balance Final: {balance_final:.2f}
Transacción de Mayor Monto: ID:{trans_max["id"]} - monto:{trans_max["monto"]}1
Conteo de Transacciones: {count.get('Crédito', 0)} Débito: {count.get('Débito', 0)}""")