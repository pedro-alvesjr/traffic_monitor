# Traffic Monitor API

API REST desenvolvida com Django e Django REST Framework para monitorização de tráfego rodoviário em segmentos de estrada locais.

## Funcionalidades

- CRUD completo para segmentos de estrada (`RoadSegment`)
- CRUD completo para leituras de velocidade média (`TrafficReading`)
- Cálculo dinâmico da **intensidade de tráfego** com base na velocidade
- Contagem do total de leituras por segmento
- Permissões por tipo de utilizador:
  - **Admin**: pode criar, editar e apagar
  - **Anônimo**: apenas leitura
- Interface de administração via Django Admin
- Documentação interativa da API em `/api/docs`

## Como executar o projeto

### Pré-requisitos

- Python 3.12 ou superior
- pip

### Instalação

# 1. Clone o repositório
git clone https://github.com/pedro-alvesjr/traffic_monitor
cd traffic_monitor

# 2. (Opcional) Crie e ative um ambiente virtual
python -m venv venv
venv\Scripts\activate  # No Windows
# ou
source venv/bin/activate  # No Linux/macOS

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Aplique as migrações
python manage.py migrate

# 5. Crie um superusuário
python manage.py createsuperuser

# 6. Inicie o servidor de desenvolvimento
python manage.py runserver
```

### Acessos úteis:

- API (segmentos): [`/api/roadsegments/`]
- API (leituras): [`/api/readings/`]
- Documentação Swagger: [`/api/docs/`]
- Django Admin: [`/admin/`]
