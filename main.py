from functions import *
import pymorphy2

data = create_ann("C:\\Proganiy\\annotation.csv")
data = clean(data)
print(data)