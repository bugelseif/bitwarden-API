# Exemplo de uso da API Bitwarden

## Objetivo
Este repositório tem como objetivo demonstrar o uso da API Bitwarden para acesso a senhas e outas informações armazenadas na plataforma e usá-las de forma segura no preenchimento de formulários web.

## Pré-requisitos
Para executar o código é necessário ter instalado:

- Python 3.8^
- Pip
- Virtualenv (opcional)

## Como usar
Abaixo uma lista de passos para executar o código:

- Criar venv (opcional)
- Ativar venv (opcional)
- Instalar dependências
- Buscar chaves Bitwarden
- Atribuir chaves à variáveis de ambiente
- Executar código

## Onde pegar as chaves na Bitwarden?
Após fazer signup na Bitwarden, seguimos alguns passos:

- Acessar o menu do usuário e selecionar _Account settings_

![menu do usuário](img/menu_user.png)
- Acessar a opção _Security_ no menu lateral de configurações

![menu de configurações](img/menu_settings.png)
- Selecionar a aba _Keys_ e clicar em _View API Key_
 
![aba de chaves](img/aba_keys.png)
- Confirmar a senha do usuário

![senha do usuário](img/window_confirm_password.png)
- Copiar a chaves de acesso

![chave de acesso](img/keys.png)
- Utilizá-las como _Variáveis de Ambiente_ no sistema
