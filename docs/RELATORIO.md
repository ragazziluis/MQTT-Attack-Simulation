# Relatório Técnico: Simulação de Ataques a um Sistema MQTT Utilizando MQTTool para iOS

## 1. Introdução
Neste relatório, apresentamos uma análise técnica das vulnerabilidades associadas à confidencialidade, integridade e disponibilidade de um sistema MQTT. Para tanto, utilizamos o aplicativo MQTTool para iOS e um broker público listado no site [10 Free Public & Private MQTT Brokers for Testing & Prototyping](https://mntolia.com/10-free-public-private-mqtt-brokers-for-testing-prototyping/).

## 2. Metodologia

### 2.1 Ferramentas Utilizadas
- **Aplicativo Cliente MQTT:** MQTTool para iOS.
- **Broker Público:** Selecionado da lista disponível no link mencionado acima.
- **Identificador do Cliente:** Utilizamos identificadores aleatórios e depois fixamos um identificador para observar o comportamento.
- **Tópico:** Um nome único foi criado para o tópico de comunicação.

### 2.2 Procedimento

1. **Conexão ao Broker:**
   - **Broker Selecionado:** `mqtt.eclipse.org`
   - **Porta:** 1883
   - **Identificador Aleatório:** Geramos um identificador aleatório para a conexão inicial.
   - **Tópico:** `simulacao/ataques/mqtt`

2. **Subscrição e Publicação:**
   - Realizamos a subscrição no tópico `simulacao/ataques/mqtt` usando MQTTool.
   - Publicamos mensagens no mesmo tópico, observando a recepção correta das mensagens.

3. **Teste com Identificador Fixo:**
   - Utilizamos o mesmo identificador em múltiplas conexões para verificar o comportamento do sistema.

4. **Simulação de Ataques:**
   - **Confidencialidade:** Publicamos mensagens com informações sensíveis sem criptografia.
   - **Integridade:** Alteramos mensagens durante a transmissão.
   - **Disponibilidade:** Realizamos um ataque de negação de serviço (DoS) publicando um grande volume de mensagens em curto intervalo de tempo.

## 3. Resultados

### 3.1 Conexão ao Broker
A conexão foi estabelecida com sucesso utilizando um identificador aleatório. Quando o mesmo identificador foi reutilizado em múltiplas conexões, a sessão anterior foi desconectada, evidenciando que o broker não permite múltiplas sessões simultâneas com o mesmo identificador.

### 3.2 Subscrição e Publicação
As mensagens foram publicadas e recebidas corretamente quando utilizando identificadores únicos. A sincronização entre publicação e recepção mostrou-se eficiente.

### 3.3 Teste com Identificador Fixo
Ao reutilizar o mesmo identificador, verificamos que apenas a última sessão ativa manteve-se conectada, enquanto todas as anteriores foram desconectadas, potencialmente interrompendo serviços em uso.

### 3.4 Simulação de Ataques
- **Confidencialidade:** As mensagens foram interceptadas facilmente utilizando ferramentas de captura de tráfego, pois não havia criptografia.
- **Integridade:** Conseguimos alterar mensagens durante a transmissão utilizando intermediários maliciosos (Man-in-the-Middle).
- **Disponibilidade:** O broker sofreu degradação de performance ao receber um grande volume de mensagens em curto espaço de tempo, simulando um ataque DoS.

## 4. Conclusões
A análise revelou vulnerabilidades significativas em sistemas MQTT quando não são adotadas medidas de segurança adequadas. Recomendamos as seguintes ações:
- **Confidencialidade:** Implementação de TLS para criptografia de mensagens.
- **Integridade:** Uso de assinaturas digitais para verificar a integridade das mensagens.
- **Disponibilidade:** Implementação de controles de taxa e mecanismos de autenticação robustos para mitigar ataques DoS.

## 5. Referências
- "10 Free Public & Private MQTT Brokers for Testing & Prototyping" - [mntolia.com](https://mntolia.com/10-free-public-private-mqtt-brokers-for-testing-prototyping/)
- MQTT Standard Documentation - [mqtt.org](https://mqtt.org/documentation)

Este relatório demonstra a importância de práticas de segurança na implementação de sistemas MQTT, especialmente em ambientes onde a integridade e a disponibilidade dos dados são críticas.