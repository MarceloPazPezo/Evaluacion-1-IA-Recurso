import pandas as pd
import numpy as np
import json

cantidad = 15
# Definir los rangos para cada campo
dept_range = (1, 45)
temperature_range = (-15, 35)
type_range = (1, 3)
size_range = (50000, 500000)
event_type_range = (1, 5)
season_range = (1, 4)

# Generar los datos aleatorios
data = {
    "Dept": np.random.randint(dept_range[0], dept_range[1] + 1, cantidad),
    "Temperature": np.random.uniform(temperature_range[0], temperature_range[1], cantidad).round(2),
    "Type": np.random.randint(type_range[0], type_range[1] + 1, cantidad),
    "Size": np.random.randint(size_range[0], size_range[1] + 1, cantidad),
    "Event_Type": np.random.randint(event_type_range[0], event_type_range[1] + 1, cantidad),
    "Season": np.random.randint(season_range[0], season_range[1] + 1, cantidad)
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Convertir DataFrame a diccionario
data_dict = df.to_dict(orient='records')

# Guardar en un archivo JSON
with open('./data/entrada_cat.json', 'w') as f:
    json.dump(data_dict, f, indent=4)

print("Datos guardados en entrada_cat.json")
