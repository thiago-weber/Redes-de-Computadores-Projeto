# Rastreio de pacotes de MiniDLNA com Wireshark

Material de apoio e laboratório prático da disciplina de Redes de Computadores - 2026.1.

---

## Descrição do Projeto

Este projeto implementa uma infraestrutura de rede que integra um serviço de streaming de mídia padronizado com uma aplicação própria de notificação em tempo real. 

O objetivo principal é monitorar o consumo de mídia e a integridade da comunicação entre um **Raspberry Pi 3B+** e um **desktop** dentro de uma rede local. O sistema utiliza o **Padrão de Projeto Observer**, no qual o Raspberry Pi atua monitorando alterações no diretório de mídias enquanto o computador aguarda os alertas.

---

## Pré-requisitos

*   **Ambiente Python**: Python 3 instalado em ambos os dispositivos.
*   **Raspberry Pi**: Configurado com o servidor MiniDLNA e a biblioteca `watchdog` instalada.
*   **Acesso Remoto**: Foi utilizado o RealVNC para acessar o Raspberry Pi remotamente.

---

## Instruções de Instalação e Execução

### 1. Preparação do Ambiente
Certifique-se de que ambos os dispositivos estão conectados na mesma rede local.

### 2. Configuração de Rede
No código-fonte, ajuste as configurações de **socket address**:
*   Configure o IP e a porta nos arquivos `servidor.py` e `cliente.py` conforme os dispositivos utilizados.

### 3. Execução do Laboratório
Siga a ordem correta para estabelecer o canal de comunicação orientado à conexão:

1.  **Iniciar o Servidor (Desktop)**:
    ```bash
    python servidor.py
    ```
    *O servidor entrará em modo `listen()` aguardando a conexão.*

2.  **Iniciar o Cliente (Raspberry Pi)**:
    ```bash
    python cliente.py
    ```

3.  **Teste de Notificação**:
    Adicione qualquer arquivo à pasta `/media/media/` do Raspberry Pi para disparar o alerta imediato no servidor.

4.  **Consumo de Mídia**:
    Acesse a aba **Rede** do Explorador de Arquivos do Windows para visualizar e reproduzir a mídia do Raspberry Pi via MiniDLNA.

---

## Arquitetura e Fluxo

Para viabilizar a comunicação, foi desenvolvida uma aplicação utilizando sockets TCP, garantindo a criação de um canal confiável de cadeia de bytes para a entrega das notificações.

*   **Utilização de Threads**: Implementadas no lado servidor para permitir que o processo de "escuta" na porta 5005 não seja bloqueante. Isso possibilita que o servidor gerencie múltiplas conexões simultâneas sem interromper a execução principal.
*   **Serviço MiniDLNA**: Disponibiliza o conteúdo via protocolo HTTP na porta 8200, permitindo o consumo transparente dos arquivos de mídia.

---

## Análise com Wireshark

Toda a atividade de rede foi analisada para validar os conceitos de protocolos de transporte e aplicação:
*   **Controle de Conexão**: Verificação do *handshake* *SYN/ACK*.
*   **Transferência de Dados**: Monitoramento do fluxo de notificações.
*   **Fragmentação**: Observação de grandes arquivos de mídia através da descrição *"TCP PDU Reassembled"*.

---

## Autoria

Projeto desenvolvido como laboratório prático da disciplina de Redes de Computadores pelos integrantes:
*   **Esther Freixo Chaves**
*   **Raphael Mendes Miranda Fernandes**
*   **Thiago Lucas Vianna Gomes Lehmkuhl Weber**

---

## 🔗 Fontes e Referências

*   [Raspberry Pi Media Server - MiniDLNA](https://www.instructables.com/Raspberry-Pi-Media-Server-MiniDLNA/)
*   [Instruções para configurar MiniDLNA](https://www.instructables.com/Creating-a-ReadyMedia-formerly-MiniDLNA-Media-Serv/)
*   [Python Docs (Sockets e Threads)](https://docs.python.org/3/library/socket.html)
*   [Observer Pattern in Python](https://refactoring.guru/design-patterns/observer/python/example)
*   [Watchdog Documentation](https://pythonhosted.org/watchdog/)
