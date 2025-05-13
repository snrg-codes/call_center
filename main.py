from functions import *
from db import *

new_client = '0354'
print(add_call(clients, new_client))
client = get_call(clients)
print(clients)
operator = free_operators(operators)
print(operator)

