# pi-2025.5.3
Projeto Integrador do curso Programador de Sistemas, do SENAC Castanhal

Henrique Diomedes [GitHub](https://github.com/HenriqueDiomedes).
[Vitoria Gabriela](https://github.com/Flower891/)
[Larry Cris](https://github.com/Larry53560746/logica-de-prog-python.git)
[jamilly oliveira](https://github.com/jamillyoliveira000/logica-de-prog-python.git)
[Gusdcarv21](https://github.com/gusdcarv21)
[Bianca](https://github.com/Klaay001/)
[Alana](https://github.com/Alana691)
[NOILIUG](https://github.com/NOILIUG)

## ---------------------------------------------------------
# Orientações para configuração do servidor do laboratório
## 1. Acesso ao servidor via ssh

O servidor poderá ser acessado por qualquer dispositivos que esteja na rede local do laboratório de informática.
Senha: Programador@2025
Senha de acesso root: PiTi@2025 

```shell
> ssh surpote@172.16.0.42 
```

## 2. Navegação até a pasta do projeto
O caminho para o projeto é o seguinte

``
/home/surpote/www
``

Para navegar até o diretório use o comando *cd*

## 3. Execução do servidor
Após o acesso ao servidor você poderá executar o projeto executando o comando próprio do DJango


```shell
python3 manage.py runserver 0.0.0.0:8000
```

O sistema deve permanecer executando para que o usoário possa acessar o sistema
Para que qualquer pessoa possa acessar deverá digitar acessar o seguinte endereço disponível somente na rede local (LAN ou WLAN)

[https://lojado20.senac.br/](https://lojado20.senac.br/)
