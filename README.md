# Inteli - Instituto de Tecnologia e Liderança

### Curso: Engenharia de Software 
* Módulo 8: Arquitetura de Software
* Professor: Hermano Peixoto

# Simulação de Ataques usando MQTT

Este repositório contém a documentação e o código utilizados para simular ataques de confidencialidade, integridade e disponibilidade em um sistema MQTT.

## Estrutura do Projeto

- `docs/`: Contém o relatório técnico dessa atividade.
- `src/`: Contém os scripts/códigos utilizados para publicar, subscrever e simular ataques.
- `requirements.txt`: Lista de dependências do projeto.

## Instruções de Uso

### Pré-requisitos

- Python 3.x
- Pip

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/ragazziluis/mqtt-attack-simulation.git
    cd mqtt-attack-simulation
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

### Códigos/scripts

- `publish.py`: Script para publicar mensagens em um MQTT.
- `subscribe.py`: Script para subscrever a um MQTT e receber mensagens.
- `dos_attack.py`: Script para simular um ataque de negação de serviço (DoS).

### Uso

1. **Subscrição**:

    ```bash
    python src/subscribe.py
    ```

2. **Publicação**:

    ```bash
    python src/publish.py
    ```

3. **Ataque DoS**:

    ```bash
    python src/dos_attack.py
    ```

Para mais detalhes, consulte a [documentação completa](docs/RELATORIO.md).
