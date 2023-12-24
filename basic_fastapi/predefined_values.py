from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"

app = FastAPI()
#If you have a path operation that receives a path parameter, but you want the possible valid 
# path parameter values to be predefined, you can use a standard Python Enum.

@app.get("/models/{modelsname}")
async def model(modelsname:ModelName):
  if modelsname == ModelName.alexnet:
    return{"Alex net":"O AlexNet é o nome de uma clássica arquitetura de rede neural convolucional desenvolvida por Krizhevsky et al. Essa arquitetura consiste de convoluções, max pooling e camadas densamente conectadas em grupos com o objetivo principal de treinar um modelo em duas GPUs (Unidades de Processamento Gráfico)"}
  
  if modelsname == ModelName.resnet:
    return{"Resnet":"Uma Rede Neural Residual é um modelo de aprendizado profundo no qual as camadas de peso aprendem funções residuais com referência às entradas da camada. Uma Rede Residual é uma rede com conexões de salto que realizam mapeamentos de identidade, mesclados com as saídas da camada por adição"}
  
  if modelsname == ModelName.lenet:
    return{"Lenet":"A LeNet consiste em sete camadas, incluindo duas camadas de convolução, duas camadas de subamostragem (também conhecidas como pooling), duas camadas totalmente conectadas e uma camada de saída.)"}
  else:
    return{"response":"Notting to show"}
  