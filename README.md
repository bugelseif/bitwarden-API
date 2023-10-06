# Exemplo para uso da API Bitwarden

- criar venv
- ativar venv
- instalar coockiecutter
- baixar template botcity web bot
- adicionar dependencia do bitwarden no requirements
- instalar dependencias
- setar webdriver
- carregar secrets Bitwarden no sistema
- conectar API Bitwarden
- desenvolver lógica para acessar e preencher o form
- verificar os resultados


## Onde pegar as chaves?
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
