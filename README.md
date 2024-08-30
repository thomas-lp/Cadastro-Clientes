# Passos de configuração - Deploy de uma aplicação Django com AWS EC2 + RDS

## Etapas após conectar na instância EC2:

### Atualizar o ubuntu:
- sudo apt-get update 

### Clonar repositório:
- git clone https://github.com/thomas-lp/Cadastro-Clientes

### Instalar o pip:
- sudo apt install python3-pip -y

### Instalar o Django:
- pip install django --break-system-packages

### Ver pastas:
- dir ou ls

### Entrar na pasta:
- cd <nome-da-pasta>

### Comandos Django:
- python3 manage.py makemigrations 
- python3 manage.py migrate
- python3 manage.py createsuperuser 
- python3 manage.py runserver

### Rodar o servidor fora do localhost:
- python3 manage.py runserver 0.0.0.0:8000

### Exibir todos os screens:
- screen -list 

### Criar screen (Para deixar a aplicação rodando permanentemente, sem cair ao fechar o terminal da instância EC2):
- screen -S <nome-do-screen> 

### Reconectar ao screen:
- screen -r <nome-do-screen>

### Encerrar screen:
- screen -X -S <nome-do-screen> quit 

### Sair do screen:
- ctrl-A + d 

### Redirecionar a porta 80 para a porta 8080 (Para evitar de digitar a prota na url):
- sudo /sbin/iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000

## Etapas após conectar na instância RDS:

### Atualizar o repositório local (após ajustar a conexão com o banco em settings.py):
- git pull origin master

### instalar psycopg2:
- pip install psycopg2-binary --break-system-packages

### Instalar postgresql-client:
- sudo apt-get install postgresql-client

### Comando pra conectar no postgres-sql:
- psql -h <token-aws-rds> -U postgres -p 5432


