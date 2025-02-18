import sqlite3
import datetime

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('academia.db')
        self.cursor = self.conn.cursor()
        self.create_tables()  # Chama o método para criar as tabelas

    def create_tables(self):
        try:
            # Tabela de clientes
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS clients (
                    cpf TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    birth_date TEXT,
                    gender TEXT,
                    marital_status TEXT,
                    email TEXT,
                    phone TEXT,
                    address TEXT,
                    workout TEXT
                )
            ''')

            # Tabela de registros de acesso dos clientes
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS access_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpf TEXT,
                    access_time TEXT,
                    FOREIGN KEY (cpf) REFERENCES clients(cpf)
                )
            ''')

            # Tabela de funcionários
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS employees (
                    employee_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL
                )
            ''')

            # Tabela de registros de entrada e saída dos funcionários
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS employee_records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_id TEXT,
                    check_in TEXT,
                    check_out TEXT,
                    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
                )
            ''')

            self.conn.commit()
            print("Tabelas criadas com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao criar tabelas: {e}")

    def register_client(self, cpf, info):
        self.cursor.execute('SELECT cpf FROM clients WHERE cpf = ?', (cpf,))
        if self.cursor.fetchone():
            return "Cliente já registrado."

        try:
            self.cursor.execute('''
                INSERT INTO clients (cpf, name, workout)
                VALUES (?, ?, ?)
            ''', (cpf, info['name'], info.get('workout', '')))
            self.conn.commit()
            return "Cliente cadastrado com sucesso."
        except sqlite3.Error as e:
            return f"Erro ao cadastrar cliente: {e}"


    def get_all_clients(self):
        try:
            self.cursor.execute('SELECT * FROM clients')
            clients = self.cursor.fetchall()
            return [{'cpf': client[0], 'name': client[1], 'workout': client[2]} for client in clients]
        except sqlite3.Error as e:
            print(f"Erro ao buscar clientes: {e}")
            return []

    def validate_access_and_register_entry(self, cpf):
        self.cursor.execute('SELECT name FROM clients WHERE cpf = ?', (cpf,))
        client = self.cursor.fetchone()
    
        if not client:
            return "Cliente não encontrado."  # Retorna uma mensagem ao invés de levantar um erro
    
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.cursor.execute('''
                INSERT INTO access_records (cpf, access_time)
                VALUES (?, ?)
            ''', (cpf, current_time))
            self.conn.commit()
            return f"Acesso permitido para {client[0]} às {current_time}."
        except sqlite3.Error as e:
            return f"Erro ao registrar acesso: {e}"


    def get_access_records(self, cpf):
        self.cursor.execute('SELECT access_time FROM access_records WHERE cpf = ?', (cpf,))
        records = self.cursor.fetchall()
        if not records:
            raise ValueError("Cliente não encontrado.")
        return [record[0] for record in records]

    def SearchWorkout(self, cpf):
        self.cursor.execute('SELECT workout FROM clients WHERE cpf = ?', (cpf,))
        workout = self.cursor.fetchone()
        if not workout:
            raise ValueError("Cliente não encontrado.")
        return workout[0] if workout[0] else 'Nenhum treino atribuído.'

    def SearchClient(self, cpf):
        self.cursor.execute('SELECT * FROM clients WHERE cpf = ?', (cpf,))
        client = self.cursor.fetchone()
        if client:
            return {'cpf': client[0], 'name': client[1], 'workout': client[2]}
        return None

    def update_client_info(self, cpf, info):
        self.cursor.execute('SELECT cpf FROM clients WHERE cpf = ?', (cpf,))
        if not self.cursor.fetchone():
            return False  # Retorna False caso o cliente não seja encontrado
    
        for key, value in info.items():
            self.cursor.execute(f'UPDATE clients SET {key} = ? WHERE cpf = ?', (value, cpf))
    
        self.conn.commit()
        return True  # Retorna True se a atualização for bem-sucedida


    def register_employee(self, employee_id, name):
        self.cursor.execute('SELECT employee_id FROM employees WHERE employee_id = ?', (employee_id,))
        if self.cursor.fetchone():
            return "Funcionário já registrado."

        try:
            self.cursor.execute('''
                INSERT INTO employees (employee_id, name)
                VALUES (?, ?)
            ''', (employee_id, name))
            self.conn.commit()
            return f"Funcionário {name} registrado com sucesso."
        except sqlite3.Error as e:
            return f"Erro ao registrar funcionário: {e}"


    def check_in(self, employee_id):
        self.cursor.execute('SELECT name FROM employees WHERE employee_id = ?', (employee_id,))
        employee = self.cursor.fetchone()
    
        if not employee:
            return "Funcionário não encontrado."  # Retorna mensagem amigável
    
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        try:
            self.cursor.execute('''
                INSERT INTO employee_records (employee_id, check_in)
                VALUES (?, ?)
            ''', (employee_id, current_time))
            self.conn.commit()
            return f"Entrada registrada para {employee[0]} às {current_time}."
        except sqlite3.Error as e:
            return f"Erro ao registrar entrada: {e}"


    def check_out(self, employee_id):
        self.cursor.execute('SELECT name FROM employees WHERE employee_id = ?', (employee_id,))
        employee = self.cursor.fetchone()
    
        if not employee:
            return "Funcionário não encontrado."  # Retorna mensagem amigável
    
        self.cursor.execute('''
            SELECT id FROM employee_records
            WHERE employee_id = ? AND check_out IS NULL
            ORDER BY check_in DESC
            LIMIT 1
        ''', (employee_id,))
        record = self.cursor.fetchone()
    
        if not record:
            return "Hora de entrada não registrada ou já finalizada."
    
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        try:
            self.cursor.execute('''
                UPDATE employee_records
                SET check_out = ?
                WHERE id = ?
            ''', (current_time, record[0]))
            self.conn.commit()
            return f"Saída registrada para {employee[0]} às {current_time}."
        except sqlite3.Error as e:
            return f"Erro ao registrar saída: {e}"


    def get_employee_data(self, employee_id):
        self.cursor.execute('SELECT * FROM employees WHERE employee_id = ?', (employee_id,))
        employee = self.cursor.fetchone()
        if not employee:
            raise ValueError("Funcionário não encontrado.")
        
        self.cursor.execute('SELECT check_in, check_out FROM employee_records WHERE employee_id = ?', (employee_id,))
        records = self.cursor.fetchall()
        return {
            'employee_id': employee[0],
            'name': employee[1],
            'records': [{'check_in': record[0], 'check_out': record[1]} for record in records]
        }

    def close(self):
        self.conn.close()