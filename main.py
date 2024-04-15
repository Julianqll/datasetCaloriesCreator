import random

alturas = []
pesos = []
sexos = []
nivelesActividad = []
edades = []
calorias = []
for i in range(30):
  # alturas 
  alturas.append(round(random.uniform(150.0, 200.0),2))
  # pesos
  pesos.append(round(random.uniform(50.0, 100.0),2))
  #edades
  edades.append(random.randint(18, 50))
  #0 = Hombre, 1 = Mujer
  sexos.append(random.randint(0,1))
  #0 = Sedentario, 1 = Ligero, 2 = Moderado, 3 = Activo, 4 = Muy   Activo
  nivelesActividad.append(random.randint(0,5))
  
  #calculo de el bmr
  bmr = 0
  if sexos[i] == 0:
    bmr = 10 * pesos[i] + 6.25 * alturas[i] - 5 * edades[i] + 5
  else:
    bmr = 10 * pesos[i] + 6.25 *  alturas[i] - 5 * edades[i] - 161
  #calculo de las calorias
  caloriasCalculo = 0
  match nivelesActividad[i]:
    case 0:
      caloriasCalculo = bmr * 1.2
    case 1:
      caloriasCalculo = bmr * 1.4
    case 2:
      caloriasCalculo = bmr * 1.6
    case 3:
      caloriasCalculo = bmr * 1.75
    case 4:
      caloriasCalculo = bmr * 2.0
    case 5:
      caloriasCalculo = bmr * 2.3
  calorias.append(caloriasCalculo)
  #resumen
  print("Persona #", i+1)
  print("Altura: ", alturas[i])
  print("Peso: ", pesos[i])
  print("Edad: ", edades[i])
  print("Sexo: ", sexos[i])
  print("Nivel de actividad: ", nivelesActividad[i])
  print("Calorias: ", calorias[i])
  print("BMR: ", bmr)
