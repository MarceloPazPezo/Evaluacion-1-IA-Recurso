import pandas as pd
import numpy as np
import json

cantidad = 15
# Definir los rangos para cada campo
is_holiday_range = (0, 1)
dept_range = (1, 45)
temperature_range = (-15, 35)
type_range = (1, 3)
size_range = (50000, 500000)

# Generar los datos aleatorios
data = {
    "IsHoliday": np.random.randint(is_holiday_range[0], is_holiday_range[1] + 1, cantidad),
    "Dept": np.random.randint(dept_range[0], dept_range[1] + 1, cantidad),
    "Temperature": np.random.uniform(temperature_range[0], temperature_range[1], cantidad).round(2),
    "Type": np.random.randint(type_range[0], type_range[1] + 1, cantidad),
    "Size": np.random.randint(size_range[0], size_range[1] + 1, cantidad),
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Convertir DataFrame a diccionario
data_dict = df.to_dict(orient='records')

# Guardar en un archivo JSON
with open('./data/entrada_num.json', 'w') as f:
    json.dump(data_dict, f, indent=4)

print("Datos guardados en entrada_num.json")
