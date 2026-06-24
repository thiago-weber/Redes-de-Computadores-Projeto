# Redes-de-Computadores-Projeto
Projeto para a disciplina de Redes de Computadores - 2026.1


O projeto consiste em utilizar um dispositivo para consumir mídia presente em um Raspberry Pi 3b+, através da conexão na rede.

<br>
<br>

Utiliza o MiniDLNA configurado no Raspberry Pi e uma aplicação própria para controle da conexão cliente-servidor, 
permitindo que o dispositivo conectado seja notificado no momento que um novo arquivo for adicionado a pasta do Raspberry Pi.

Padrão Observer: o Raspberry Pi fica monitorando a pasta de mídias, enquanto o computador aguarda as notificações através de threads.

Utiliza-se os sockets e conexão TCP para criar um canal confiável para entrega de pacotes.

Além disso, utiliza-se o Wireshark para monitoramento dos pacotes.

Pré-requisitos:

Python;

Python + biblioteca watchdog + miniDLNA instalado no Raspberry Pi;


Ordem de instalação:

1 - Conectar os dispositivos na mesma rede

2 - Configurar o IP e a porta de ambos os dispositivos nos arquivos servidor.py e cliente.py.

3 - Executar o arquivo servidor.py.

4 - Executar o arquivo cliente.py.

5 - Agora que a conexão foi feita, cada arquivo adicionado a pasta "/media/media/" do Raspberry Pi será notificado para o servidor.

6 - Acessando a aba Rede do Explorador de Arquivo do Windows, é possível visualizar a mídia do Raspberry Pi.


Integrantes:

Esther Freixo Chaves

Raphael Mendes Miranda Fernandes

Thiago Lucas Vianna Gomes Lehmkuhl Weber



Fonte:

https://www.instructables.com/Raspberry-Pi-Media-Server-MiniDLNA/

https://www.instructables.com/Creating-a-ReadyMedia-formerly-MiniDLNA-Media-Serv/

Python docs

https://refactoring.guru/design-patterns/observer/python/example

https://pythonhosted.org/watchdog/api.html
