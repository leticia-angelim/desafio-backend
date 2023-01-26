# **Desafio Back-end**

Uma interface web que aceita upload de arquivos com padrão CNAB, normaliza os dados e armazena-os em um banco de dados relacional e exibe essas informações em tela.

<br/>

## Tecnologias utilizadas

---

- Python
- Django
- Django rest framework

<br/>

## Instalação e execução em ambientes de desenvolvimento

---

### Crie o ambiente virtual

```
python -m venv venv
```

### Ative o ambiente virtual

```bash
# linux
source venv/bin/activate

# windows
.\venv\Scripts\activate
```

### Instale as dependências

```
pip install -r requirements.txt
```

### Execute as migrações

```
python manage.py migrate
```

### Rode a aplicação

```
python manage.py runserver
```

<br/>

Arquivo para testar a aplicação: **[CNAB](https://github.com/Kenzie-Academy-Brasil-Developers/desafio-backend-m6/blob/main/CNAB.txt)**

<br/>

## Rotas

---

- Rota para fazer o upload do arquivo

  > http://127.0.0.1:8000/api/upload/

<br/>

- Rota com lista de saldo em conta por loja
  > http://127.0.0.1:8000/api/upload/list/
