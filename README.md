# 💰 Django Cotação App - Dólar e Criptomoedas

Este é um aplicativo Django que consome duas APIs públicas para exibir a cotação atual do Dólar (USD/BRL) e de duas criptomoedas (Bitcoin e Ethereum). Os dados podem ser visualizados via navegador e exportados em formato PDF com data e hora da cotação.

---

## 📦 Funcionalidades

- 📈 Cotação atualizada do Dólar em Reais (R$)
- 💹 Cotação de Bitcoin (BTC) e Ethereum (ETH)
- 🧾 Geração de relatório em PDF com data e hora
- 🖥️ Interface HTML com Bootstrap
- 🗃️ Backend com Django e banco de dados SQL Server

---

## 🚀 Tecnologias Utilizadas

- **Django 5.2.4**
- **Python 3.10+**
- **SQL Server Express** com `pyodbc`
- **Bootstrap 5**
- **WeasyPrint** (para geração de PDF)
- **APIs Públicas**:
  - [https://economia.awesomeapi.com.br/last/USD-BRL](https://economia.awesomeapi.com.br/last/USD-BRL)
  - [https://api.coingecko.com/api/v3/simple/price](https://api.coingecko.com/api/v3/simple/price)

---

## ⚙️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Se não houver `requirements.txt`, crie com:

```bash
pip install django==5.2.4 weasyprint pyodbc requests
pip freeze > requirements.txt
```

### 4. Configure o banco de dados SQL Server

No arquivo `settings.py` do seu projeto Django, configure a seção `DATABASES` assim:

```python
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'nome_do_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
```

> Certifique-se de que o SQL Server e o ODBC Driver estejam corretamente instalados.

### 5. Realize as migrações do banco

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. (Opcional) Crie um superusuário

```bash
python manage.py createsuperuser
```

### 7. Execute o servidor local

```bash
python manage.py runserver
```

Abra no navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📄 Observações

### Geração de PDF com WeasyPrint

- No **Windows**, instale o GTK+ via:  
  [https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer)

- No **Linux**, execute:

```bash
sudo apt install libpangocairo-1.0-0 libpangoft2-1.0-0 libcairo2
```

### Limites das APIs

As APIs públicas utilizadas possuem limites de requisição. Evite fazer muitas chamadas em curto tempo para não ser bloqueado temporariamente.

---

## 📂 Estrutura do Projeto (exemplo)

```
moedas_project/
├── moedas_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── cotacoes/
│   ├── templates/
│   │   ├── index.html
│   │   └── relatorio.html
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
├── manage.py
```

---

## ✅ Licença

Este projeto é livre para fins acadêmicos e educacionais. Compartilhe com os créditos ao autor.https://github.com/moisesmania
