# import library dari file logic.py
from logic import *

# mendeklarasikan simbol logis
rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")


knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

# mengetahui keluaran berdasarkan logika yang sudah dibuat
print(model_check(knowledge, dumbledore))
