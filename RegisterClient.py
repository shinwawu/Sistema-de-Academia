"""
Classe responsável por registrar clientes no sistema.
"""

class RegisterClient:
    def __init__(self, database_manager):
        self.database_manager = database_manager

    def SetClientName(self, cpf, name):
        """
        Define o nome do cliente e registra no sistema.
        """
        if not cpf or not name:
            raise ValueError("CPF e Nome são obrigatórios.")
        self.database_manager.RegisterClient(cpf, {
            "name": name,
            "birth_date": None,
            "gender": None,
            "marital_status": None,
            "email": None,
            "phone": None,
            "address": None,
            "workout": None
        })

    def SetClientInfo(self, cpf, info):

        required_fields = ["name", "birth_date", "gender", "marital_status", "email", "phone", "address"]

        if not cpf or not all(field in info and info[field] for field in required_fields):
            raise ValueError("CPF e todas as informações obrigatórias devem ser fornecidas.")


        if self.database_manager.SearchClient(cpf) is None:
            self.database_manager.register_client(cpf, info) 
        else:
            self.database_manager.update_client_info(cpf, info) 

