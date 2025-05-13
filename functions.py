def add_call(clients, new_client):
    clients.append(new_client)
    return clients

def get_call(clients):
    call = clients.pop(0)
    return call

def free_operator(operators):
    operator = operators[0]
    return operator

def on_call(client, operator, on_call_list):
    on_call_list[client] = operator
    return on_call_list


    