# Aula 01 - Backend - Python

## Subindo o container com Python 
- Dockerfile
    ```Dockerfile
    FROM python:3.12

    ENTRYPOINT ["tail", "-f", "/dev/null"]
    ```
- docker-compose.yml
    ```docker-compose.yml
    version: '3'
    services:
    app:
        build: .
        volumes:
        - ./src:/app
    ```
 
- Após dos arquivos criados, rode o comando:
    ```
    docker-compose up -d --build
    ```


### Rodando os comandos em Python

-
- Item 2
  - Subitem 2.1
  - Subitem 2.2
- Item 3
