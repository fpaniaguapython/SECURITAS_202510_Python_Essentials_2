class Cliente:
    # Constructor
    def __init__(self, nombre, email, saldo, activo=True): 
        # Atributos de instancia
        self.nombre = nombre
        self.email = email
        self.saldo = saldo
        self.activo = activo

    # Método de instancia
    def incrementar_saldo(self, incremento):
        self.saldo+=incremento

    def __str__(self):
        return f'Nombre:{self.nombre}. Email:{self.email}. Saldo:{self.saldo}'
    
    def __repr__(self):
        return f'Nombre:{self.nombre}. Email:{self.email}. Saldo:{self.saldo}'

# Instanciación o creación de la instancia o del objeto
jose_david = Cliente('José David', 'jose.david@gmail.com', 10_000)
alejandro = Cliente('Alejandro', 'alejandro@hotmail.com', 5_000)
arancha = Cliente('Arancha', 'arancha@microsoft.com', 12_000)

# Guardar las instancias una lista
clientes = [jose_david, alejandro, arancha]

# Ordenar la lista de clientes por el saldo
def ponderar_saldo(cliente : Cliente) -> int:
    return cliente.saldo

def ponderar_email(cliente : Cliente) -> str:
    return cliente.email.lower()

def ponderar_nombre(cliente : Cliente) -> int:
    return len(cliente.nombre)

#print(sorted(clientes, key=ponderar_saldo))
#print(sorted(clientes, key=ponderar_email))
#print(sorted(clientes, key=ponderar_nombre))

#print(sorted(clientes, key=lambda cliente : cliente.saldo))
print(sorted(clientes, key=lambda cliente : len(cliente.email)))