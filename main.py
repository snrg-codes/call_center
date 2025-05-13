from functions import *
from db import *

new_client = '0354'
print(add_call(clients, new_client))
client = get_call(clients)
print(clients)
operator = free_operator(operators)
print(operator)
on_call(client, operator, on_call_list)
print(on_call_list)


