# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, Menu
from DatabaseManager import DatabaseManager
from RegisterClient import RegisterClient
from SendWorkout import SendWorkout
import sqlite3

class Interface:
    def __init__(self):
        self.database_manager = DatabaseManager()
        self.register_client = RegisterClient(self.database_manager)
        self.send_workout = SendWorkout(self.database_manager)
        self.employee_manager = DatabaseManager()

        self.window = tk.Tk()
        self.window.geometry("1024x768")
        self.window.title("Smart Fyt Sistema")

        self.register_icon = tk.PhotoImage(file="Imagens/Cliente.png").subsample(5, 5)
        self.send_icon = tk.PhotoImage(file="Imagens/Passartreino.png").subsample(5, 5)
        self.find_icon = tk.PhotoImage(file="Imagens/Pesquisar.png").subsample(5, 5)
        self.treino_icon = tk.PhotoImage(file="Imagens/Treino.png").subsample(5, 5)
        self.validate_icon = tk.PhotoImage(file="Imagens/Verificar.png").subsample(5, 5)
        self.funcionario_icon = tk.PhotoImage(file="Imagens/Funcionario.png").subsample(5, 5)
        self.check_icon = tk.PhotoImage(file="Imagens/Check.png").subsample(5, 5)


        self.create_menu_bar()
        self.create_toolbar()


        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.create_logo() 
        self.window.mainloop()

    def create_menu_bar(self):
        menu_bar = Menu(self.window)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Sair", command=self.window.quit)
        menu_bar.add_cascade(label="Arquivo", menu=file_menu)

        register_menu = Menu(menu_bar, tearoff=0)
        register_menu.add_command(label="Registrar Cliente", command=self.SelectRegisterClient)
        menu_bar.add_cascade(label="Cadastros", menu=register_menu)

        workout_menu = Menu(menu_bar, tearoff=0)
        workout_menu.add_command(label="Enviar Treino", command=self.SelectSendWorkout)
        menu_bar.add_cascade(label="Treinos", menu=workout_menu)

        access_menu = Menu(menu_bar, tearoff=0)
        access_menu.add_command(label="Validar Acesso", command=self.SelectValidateAccess)
        menu_bar.add_cascade(label="Acesso", menu=access_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Sobre", command=self.show_about)
        menu_bar.add_cascade(label="Ajuda", menu=help_menu)

        self.window.config(menu=menu_bar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.window, bd=1, relief=tk.RAISED)

        buttons = [
            ("Registrar Cliente", self.register_icon, self.SelectRegisterClient),
            ("Enviar Treino", self.send_icon, self.SelectSendWorkout),
            ("Procurar Cliente", self.find_icon, self.SelectFindClient),
            ("Checar Treino", self.treino_icon, self.SelectCheckWorkout),
            ("Validar Acesso", self.validate_icon, self.SelectValidateAccess),
            ("Registrar Funcionario", self.funcionario_icon, self.SelectRegisterEmployee),
            ("Horario Funcionario", self.check_icon, self.SelectCheckInOut)
        ]

        for text, icon, command in buttons:
            btn = tk.Button(toolbar, text=text, image=icon, compound="top", command=command, width=100)
            btn.pack(side=tk.LEFT, padx=0, pady=0)

        toolbar.pack(side=tk.TOP, fill=tk.X)

    def create_logo(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        logo_frame = tk.Frame(self.main_frame)
        logo_frame.pack(expand=True)

        tk.Label(logo_frame, text="Smart Fyt", font=("Helvetica", 48, "bold"), fg="blue").pack()
        tk.Label(logo_frame, text="Saúde e Treino", font=("Helvetica", 24), fg="gray").pack()

    def show_about(self):
        messagebox.showinfo("Sobre", "Smart Fyt Sistema\nVersão 1.0\nFitTech Solutions")

    def SelectRegisterClient(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="Nome Completo *").grid(row=0, column=0, padx=(10, 5), pady=10, sticky="w")
        entry_name = tk.Entry(self.main_frame, width=40)
        entry_name.grid(row=0, column=1, padx=(5, 10), pady=10)


        tk.Label(self.main_frame, text="CPF *").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        entry_cpf = tk.Entry(self.main_frame, width=40)
        entry_cpf.grid(row=1, column=1, padx=(10, 0), pady=10)

        tk.Label(self.main_frame, text="Data de Nascimento *").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        entry_birth_date = tk.Entry(self.main_frame, width=40)
        entry_birth_date.grid(row=2, column=1, padx=(10, 0), pady=10)

        tk.Label(self.main_frame, text="Sexo *").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        entry_gender = tk.Entry(self.main_frame, width=40)
        entry_gender.grid(row=3, column=1, padx=(10, 0), pady=10)

        tk.Label(self.main_frame, text="Estado Civil *").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        entry_marital_status = tk.Entry(self.main_frame, width=40)
        entry_marital_status.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.main_frame, text="E-mail *").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        entry_email = tk.Entry(self.main_frame, width=40)
        entry_email.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(self.main_frame, text="Telefone *").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        entry_phone = tk.Entry(self.main_frame, width=40)
        entry_phone.grid(row=6, column=1, padx=10, pady=10)

        tk.Label(self.main_frame, text="Endereço *").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        entry_address = tk.Entry(self.main_frame, width=40)
        entry_address.grid(row=7, column=1, padx=10, pady=10)

        self.message_label = tk.Label(self.main_frame, text="", font=("Helvetica", 10, "bold"))
        self.message_label.grid(row=9, column=0, columnspan=2, pady=10, sticky="w")


        tk.Button(self.main_frame, text="Salvar", command=lambda: self.save_client(entry_name, entry_cpf, entry_birth_date, entry_gender, entry_marital_status, entry_email, entry_phone, entry_address)).grid(row=8, column=1, pady=20)

    def save_client(self, entry_name, entry_cpf, entry_birth_date, entry_gender, entry_marital_status, entry_email, entry_phone, entry_address):
        name = entry_name.get()
        cpf = entry_cpf.get()
        birth_date = entry_birth_date.get()
        gender = entry_gender.get()
        marital_status = entry_marital_status.get()
        email = entry_email.get()
        phone = entry_phone.get()
        address = entry_address.get()

        if not all([name, cpf, birth_date, gender, marital_status, email, phone, address]):
            self.message_label.config(text="Todos os campos são obrigatórios.", fg="red")
            return

        client_info = {
            "name": name,
            "birth_date": birth_date,
            "gender": gender,
            "marital_status": marital_status,
            "email": email,
            "phone": phone,
            "address": address,
            "workout": None
        }

        try:
            self.database_manager.register_client(cpf, client_info)
            self.message_label.config(text="Cliente cadastrado com sucesso.", fg="green")
        except sqlite3.Error as e:
            self.message_label.config(text=f"Erro ao cadastrar cliente: {e}", fg="red")

    def display_message(self, message, color):
        self.message_label.config(text=message, fg=color)
        self.message_label.config(wraplength=400)


    def SelectSendWorkout(self):
        """ Tela de envio de treino corrigida """
        # Limpa a interface principal antes de criar os elementos
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Criar um frame centralizado para organizar os elementos corretamente
        form_frame = tk.Frame(self.main_frame)
        form_frame.pack(pady=20)

        # CPF Label e Entry
        tk.Label(form_frame, text="CPF:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_cpf = tk.Entry(form_frame, width=30)
        entry_cpf.grid(row=0, column=1, padx=10, pady=5)

        # Treino Label e Entry
        tk.Label(form_frame, text="Treino:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_workout = tk.Entry(form_frame, width=40)
        entry_workout.grid(row=1, column=1, padx=10, pady=5)

        # Mensagem de status (Para exibir erros/sucessos)
        self.message_label = tk.Label(form_frame, text="", fg="red")
        self.message_label.grid(row=3, column=0, columnspan=2, pady=5)

        # Botão de Enviar Treino
        tk.Button(
            form_frame, text="Enviar Treino",
            command=lambda: self.send_workout_to_client(entry_cpf, entry_workout)
        ).grid(row=2, column=1, pady=10)

    def send_workout_to_client(self, entry_cpf, entry_workout):
        """ Função para enviar treino ao cliente """
        cpf = entry_cpf.get().strip()
        workout = entry_workout.get().strip()

        if not cpf or not workout:
            self.message_label.config(text="Todos os campos são obrigatórios.", fg="red")
            return

        try:
            success = self.database_manager.update_client_info(cpf, {'workout': workout})
            if success:
                self.message_label.config(text="Treino enviado com sucesso.", fg="green")
            else:
                self.message_label.config(text="Cliente não encontrado.", fg="red")
        except sqlite3.Error as e:
            self.message_label.config(text=f"Erro ao enviar treino: {e}", fg="red")



    def display_client_list(self):
        for widget in self.client_list_frame.winfo_children():
            if widget.winfo_class() == 'Label' and widget.cget("font") != ("Arial", 12, "bold"):
                widget.destroy()

        try:
            clients = self.database_manager.get_all_clients()
            if not clients:
                tk.Label(self.client_list_frame, text="Nenhum cliente cadastrado.", fg="gray").pack()
            else:
                for client in clients:
                    client_info = f"{client['name']} - CPF: {client['cpf']}"
                    tk.Label(self.client_list_frame, text=client_info, font=("Arial", 10)).pack(anchor="w")
        except Exception as e:
            self.message_label.config(text=f"Erro ao buscar clientes: {e}", fg="red")


    def find_client(self, entry_cpf):
        """ Busca um cliente pelo CPF e exibe apenas o Nome diretamente do banco de dados """
        # Limpa mensagens antigas
        self.message_label.config(text="", fg="red")

        # Remove widgets antigos antes de exibir os novos dados
        for widget in self.client_data_frame.winfo_children():
            widget.destroy()

        cpf = entry_cpf.get().strip()
        if not cpf:
            self.message_label.config(text="CPF é obrigatório.", fg="red")
            return

        try:
            # Executa a busca diretamente no banco de dados
            self.database_manager.cursor.execute('SELECT name FROM clients WHERE cpf = ?', (cpf,))
            client = self.database_manager.cursor.fetchone()

            if client is None:
                self.message_label.config(text="Cliente não encontrado.", fg="red")
                return

            self.message_label.config(text="Cliente encontrado com sucesso.", fg="green")

            # Exibe apenas o Nome
            tk.Label(self.client_data_frame, text="Nome:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", padx=5)
            tk.Label(self.client_data_frame, text=client[0]).grid(row=0, column=1, sticky="w", padx=5)

        except Exception as e:
            self.message_label.config(text=f"Erro ao buscar cliente: {e}", fg="red")






    def SelectFindClient(self):
        """ Tela de busca de clientes corrigida """
        # Limpa a interface principal antes de criar os elementos
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Frame principal para organizar os elementos
        container_frame = tk.Frame(self.main_frame)
        container_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Frame para o formulário de busca
        form_frame = tk.Frame(container_frame)
        form_frame.pack(side=tk.LEFT, padx=20, pady=10, fill=tk.Y)

        # Frame para exibir a lista de clientes
        self.client_list_frame = tk.Frame(container_frame)
        self.client_list_frame.pack(side=tk.RIGHT, padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Título da lista de clientes
        tk.Label(self.client_list_frame, text="Clientes Cadastrados", font=("Arial", 12, "bold")).pack()

        # Inicializa a exibição da lista de clientes
        self.display_client_list()

        # Campos de entrada e botões
        tk.Label(form_frame, text="CPF:").pack(anchor="w", padx=5, pady=5)
        entry_cpf = tk.Entry(form_frame, width=30)
        entry_cpf.pack(padx=5, pady=5)

        # Mensagem de erro/sucesso
        self.message_label = tk.Label(form_frame, text="", fg="red")
        self.message_label.pack(pady=5)

        # Frame para exibir os dados do cliente encontrado
        self.client_data_frame = tk.Frame(form_frame)
        self.client_data_frame.pack(pady=10)

        # Botão de pesquisa
        tk.Button(
            form_frame, text="Procurar",
            command=lambda: self.find_client(entry_cpf)
        ).pack(pady=10)


    def display_client_list(self):
        """ Exibe a lista de clientes na tela """
        # Remove widgets antigos antes de atualizar a lista
        for widget in self.client_list_frame.winfo_children():
            widget.destroy()

        # Adiciona um título à lista
        tk.Label(self.client_list_frame, text="Clientes Cadastrados", font=("Arial", 12, "bold")).pack()

        try:
            # Busca todos os clientes no banco de dados
            clients = self.database_manager.get_all_clients()

            if not clients:
                tk.Label(self.client_list_frame, text="Nenhum cliente cadastrado.", fg="gray").pack()
            else:
                for client in clients:
                    client_info = f"{client['name']} - CPF: {client['cpf']}"
                    tk.Label(self.client_list_frame, text=client_info, font=("Arial", 10)).pack(anchor="w")
        except Exception as e:
            self.message_label.config(text=f"Erro ao buscar clientes: {e}", fg="red")


    def SelectCheckWorkout(self):
        """ Tela para checar treino de um cliente pelo CPF """
        # Limpa a interface principal antes de criar os elementos
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Criar um frame para organizar os elementos
        form_frame = tk.Frame(self.main_frame)
        form_frame.pack(pady=20)

        # CPF Label e Entry
        tk.Label(form_frame, text="CPF:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_cpf = tk.Entry(form_frame, width=30)
        entry_cpf.grid(row=0, column=1, padx=10, pady=5)

        # Mensagem de erro/sucesso
        self.message_label = tk.Label(form_frame, text="", fg="red")
        self.message_label.grid(row=2, column=0, columnspan=2, pady=5)

        # Botão de Checar Treino
        tk.Button(
            form_frame, text="Checar",
            command=lambda: self.check_workout(entry_cpf)
        ).grid(row=1, column=1, pady=10)

        # Criando frame onde será exibido o treino do cliente
        self.workout_data_frame = tk.Frame(self.main_frame)
        self.workout_data_frame.pack(pady=10)


    def check_workout(self, entry_cpf):
        """ Busca e exibe o treino do cliente """
        # Limpa mensagens antigas
        self.message_label.config(text="", fg="red")

        # Limpa a exibição anterior do treino
        for widget in self.workout_data_frame.winfo_children():
            widget.destroy()

        cpf = entry_cpf.get().strip()
        if not cpf:
            self.message_label.config(text="CPF é obrigatório.", fg="red")
            return

        try:
            workout = self.database_manager.SearchWorkout(cpf)

            if workout is None or workout.strip() == "":
                self.message_label.config(text="Nenhum treino atribuído para este cliente.", fg="red")
                return

            self.message_label.config(text="Treino encontrado.", fg="green")

            # Exibindo os dados do treino corretamente no frame
            tk.Label(self.workout_data_frame, text="Treino:", font=("Arial", 10, "bold")).pack(anchor="w", padx=5)
            tk.Label(self.workout_data_frame, text=workout, wraplength=400, justify="left").pack(anchor="w", padx=5)

            # Garante que o frame seja atualizado na interface
            self.workout_data_frame.pack(pady=10)

        except ValueError as e:
            self.message_label.config(text=str(e), fg="red")




    def SelectValidateAccess(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="CPF:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_cpf = tk.Entry(self.main_frame, width=30)
        entry_cpf.grid(row=0, column=1, padx=10, pady=10)

        self.message_label = tk.Label(self.main_frame, text="", fg="red")
        self.message_label.grid(row=3, column=1, pady=5)

        tk.Button(self.main_frame, text="Validar", command=lambda: self.validate_access(entry_cpf)).grid(row=1, column=1, pady=10)

        self.access_records_frame = tk.Frame(self.main_frame)
        self.access_records_frame.grid(row=4, column=0, columnspan=2, pady=10)

    def validate_access(self, entry_cpf):
        cpf = entry_cpf.get()
        if not cpf:
            self.message_label.config(text="CPF é obrigatório.", fg="red")
            return

        try:
            result = self.database_manager.validate_access_and_register_entry(cpf)
            self.message_label.config(text=result, fg="green")

            self.display_access_records(cpf)
        except sqlite3.Error as e:
            self.message_label.config(text=f"Erro ao validar acesso: {e}", fg="red")

    def display_access_records(self, cpf):
        for widget in self.access_records_frame.winfo_children():
            widget.destroy()

        try:
            records = self.database_manager.get_access_records(cpf)
            tk.Label(self.access_records_frame, text="Historico de Acessos:", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

            if not records:
               tk.Label(self.access_records_frame, text="Nenhum acesso registrado.", fg="gray").grid(row=1, column=0, columnspan=2, pady=5)
            else:
                for i, record in enumerate(records):
                    tk.Label(self.access_records_frame, text=f"Acesso {i+1}: {record}").grid(row=i+1, column=0, sticky="w")

        except ValueError as e:
            self.message_label.config(text=str(e), fg="red")

    def SelectRegisterEmployee(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="ID do Funcionário:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_id = tk.Entry(self.main_frame, width=30)
        entry_id.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.main_frame, text="Nome do Funcionário:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        entry_name = tk.Entry(self.main_frame, width=30)
        entry_name.grid(row=1, column=1, padx=10, pady=10)

        self.message_label = tk.Label(self.main_frame, text="", fg="red")
        self.message_label.grid(row=3, column=1, pady=5)

        tk.Button(self.main_frame, text="Registrar", command=lambda: self.register_employee(entry_id, entry_name)).grid(row=2, column=1, pady=10)

    def register_employee(self, entry_id, entry_name):
        employee_id = entry_id.get()
        employee_name = entry_name.get()

        if not employee_id or not employee_name:
            self.message_label.config(text="Todos os campos são obrigatórios.", fg="red")
            return

        try:
            result = self.employee_manager.register_employee(employee_id, employee_name)
            self.message_label.config(text=result, fg="green")
        except sqlite3.Error as e:
            self.message_label.config(text=f"Erro ao registrar funcionário: {e}", fg="red")
    
    def SelectCheckInOut(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="ID do Funcionário:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entry_id = tk.Entry(self.main_frame, width=30)
        entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.message_label = tk.Label(self.main_frame, text="", fg="red")
        self.message_label.grid(row=3, column=1, pady=5)

        tk.Button(self.main_frame, text="Registrar Entrada", command=lambda: self.check_in(entry_id)).grid(row=1, column=0, pady=10)
        tk.Button(self.main_frame, text="Registrar Saída", command=lambda: self.check_out(entry_id)).grid(row=1, column=1, pady=10)
        tk.Button(self.main_frame, text="Ver Registros", command=lambda: self.display_employee_records(entry_id)).grid(row=2, column=1, pady=10)

    
        self.records_frame = tk.Frame(self.main_frame)
        self.records_frame.grid(row=4, column=0, columnspan=2, pady=10)

    def check_in(self, entry_id):
        employee_id = entry_id.get()
        if not employee_id:
            self.message_label.config(text="ID do funcionário é obrigatório.", fg="red")
            return

        try:
            result = self.employee_manager.check_in(employee_id)
            self.message_label.config(text=result, fg="green")
        except sqlite3.Error as e:
            self.message_label.config(text=f"Erro ao registrar entrada: {e}", fg="red")

    def check_out(self, entry_id):
        employee_id = entry_id.get()
        if not employee_id:
            self.message_label.config(text="ID do funcionário é obrigatório.", fg="red")
            return

        try:
            result = self.employee_manager.check_out(employee_id)
            self.message_label.config(text=result, fg="green")
        except sqlite3.Error as e:
            self.message_label.config(text=f"Erro ao registrar saída: {e}", fg="red")

    def display_employee_records(self, entry_id):
        for widget in self.records_frame.winfo_children():
            widget.destroy()

        employee_id = entry_id.get()
        if not employee_id:
            self.message_label.config(text="ID do funcionário é obrigatório.", fg="red")
            return

        try:
            employee_data = self.employee_manager.get_employee_data(employee_id)
            records = employee_data['records']

            tk.Label(self.records_frame, text=f"Registros de {employee_data['name']}:").grid(row=0, column=0, columnspan=2, pady=5)

            if not records:
                tk.Label(self.records_frame, text="Nenhum registro encontrado.", fg="gray").grid(row=1, column=0, columnspan=2, pady=5)
            else:
                for i, record in enumerate(records):
                    check_in = record['check_in'] or "Sem entrada"
                    check_out = record['check_out'] or "Sem saída"
                    tk.Label(self.records_frame, text=f"Entrada: {check_in} | Saída: {check_out}").grid(row=i+1, column=0, columnspan=2, sticky="w")
        except ValueError as e:
            self.message_label.config(text=str(e), fg="red")


if __name__ == "__main__":
    Interface()
