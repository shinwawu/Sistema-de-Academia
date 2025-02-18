"""
Classe responsável por enviar treinos para clientes.
"""

class SendWorkout:
    def __init__(self, database_manager):
        self.database_manager = database_manager

    def GetClient(self, cpf):
        """
        Busca um cliente no sistema.
        """
        client = self.database_manager.SearchClient(cpf)
        if not client:
            raise ValueError("Cliente não encontrado.")
        return client

    def WriteWorkout(self, cpf, workout):

        if not workout:
            raise ValueError("Treino não pode ser vazio.")
    
    
        client = self.database_manager.SearchClient(cpf)
        if client is None:
            raise ValueError("Cliente não encontrado.")

    
        client["workout"] = workout
        self.database_manager.update_client_info(cpf, client)  


    def SendWorkout(self, cpf, workout):
        """
        Método principal para associar o treino ao cliente.
        """
        self.WriteWorkout(cpf, workout)
