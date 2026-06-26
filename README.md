# Rastreio de pacotes de MiniDLNA com Wireshark
Projeto para a disciplina de Redes de Computadores - 2026.1


Este projeto implementa uma infraestrutura de rede que integra um serviço de streaming de mídia padronizado com uma aplicação própria de notificação em tempo real.

<br>

O objetivo principal é monitorar o consumo de mídia e a integridade da comunicação entre um Raspberry Pi 3B+ e um desktop dentro de uma rede local.

O projeto utiliza o padrão Observer, no qual o Raspberry Pi atua monitorando alterações no diretório de mídias enquanto o computador aguarda os alertas. 
Para viabilizar essa comunicação, foi desenvolvida uma aplicação utilizando sockets TCP, garantindo a criação de um canal confiável de cadeia de bytes 
onde as notificações são entregues de forma confiável.


Também foi utilizado threads no lado servidor. Isso permite que o processo de "escuta" da porta 5005 não seja bloqueante, possibilitando 
que o servidor gerencie múltiplas conexões simultâneas sem interromper a execução principal. Em paralelo, o serviço MiniDLNA disponibiliza 
o conteúdo via protocolo HTTP na porta 8200, permitindo que o Desktop consuma os arquivos de mídia de forma transparente.

<br>

Toda a atividade de rede, incluindo o controle de conexão (handshake SYN/ACK), a transferência de dados e
a fragmentação de grandes arquivos de mídia (TCP PDU Reassembled), é analisada via Wireshark conforme vídeo.

<br>

Foi utilizado o RealVNC para acessar o Raspberry Pi remotamente.

<br>

Pré-requisitos:


Python;

Raspberry Pi com miniDLNA, Python e bilbioteca watchdog instalados;

<br>

Instruções:


1 - Conectar os dispositivos na mesma rede local;

2 - Configurar IP e porta nos arquivos servidor.py e cliente.py conforme os dispositivos utilizados;

3 - Executar o arquivo servidor.py para colocá-lo em modo listen();

4 - Executar o arquivo cliente.py;

5 - Agora que a conexão foi feita, cada arquivo adicionado a pasta "/media/media/" do Raspberry Pi será notificado para o servidor.

6 - Acessando a aba Rede do Explorador de Arquivo do Windows, é possível visualizar e reproduzir a mídia do Raspberry Pi.

<br>

Integrantes:


Esther Freixo Chaves

Raphael Mendes Miranda Fernandes

Thiago Lucas Vianna Gomes Lehmkuhl Weber

<br>

Fonte:

[Raspberry Pi Media Server - MiniDLNA](https://www.instructables.com/Raspberry-Pi-Media-Server-MiniDLNA/)

[Creating a ReadyMedia (formerly MiniDLNA) Media Server With a Raspberry Pi](https://www.instructables.com/Creating-a-ReadyMedia-formerly-MiniDLNA-Media-Serv/)

Python docs (Sockets e Threads)

[Observer in Python](https://refactoring.guru/design-patterns/observer/python/example)

[Watchdog documentation](https://pythonhosted.org/watchdog/api.html)
