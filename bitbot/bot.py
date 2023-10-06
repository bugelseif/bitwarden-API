# Import Web Bot
from botcity.web import WebBot, Browser, By

# Import integração com BotCity Maestro SDK
from botcity.maestro import *

# Desativa os erros se não estivermos conectados ao Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Import variáveis de ambiente
import os

# Import Bitwarden
from ta_bitwarden_cli import ta_bitwarden_cli as ta


def main():
    # Runner passa a url do servidor, o id da tarefa que está sendo executada,
    # o token de acesso e os parâmetros que esta tarefa recebe (quando aplicável).
    maestro = BotMaestroSDK.from_sys_args()
    # Busca o BotExecution com detalhes da tarefa, incluindo parâmetros
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # Conecta ao Bitwarden
    bitwarden_credentials = {
        "password": os.getenv("BIT_PASSWORD"),
        "client_id": os.getenv("BIT_CLIENTID"),
        "client_secret": os.getenv("BIT_CLIENTSECRET"),
    }

    # Procura item no cofre
    item = {
        "voult": "automation"
    }

    # Inicializa Bitwarden
    bit = ta.Bitwarden(bitwarden_credentials)

    # Inicializa web bot
    bot = WebBot()

    # Configura se deseja ou não executar no modo headless
    bot.headless = False

    # Define o navegador que será utilizado
    bot.browser = Browser.FIREFOX

    # Define o caminho do driver do navegador
    bot.driver_path = r'resources\geckodriver.exe'

    try:
        # Abre a página
        bot.browse("https://practice-automation.com/form-fields/")

        # Digita nome que está no cofre
        name_input = bot.find_element("g1103-name", By.ID)
        name_input.send_keys(bit.get_credentials(item)["voult"]["login"])
        
        # Seleciona a bebida
        drink = bot.find_element(
            "label.grunion-checkbox-multiple-label:nth-child(4) > input:nth-child(1)",
            By.CSS_SELECTOR
            )
        drink.click()

        # Seleciona a cor
        color = bot.find_element(
            "label.grunion-radio-label:nth-child(1) > input:nth-child(1)",
            By.CSS_SELECTOR
            )
        color.click()

        # Digita email
        email = bot.find_element("email", By.ID)
        email.send_keys(bit.get_credentials(item)["voult"]["email"])

        # Digita mensagem
        message = bot.find_element("contact-form-comment-message", By.ID)
        message.send_keys(bit.get_credentials(item)["voult"]["note"])

        # Clica em submit
        submit = bot.find_element(
            "p.contact-submit:nth-child(2) > button:nth-child(1)",
            By.CSS_SELECTOR
            )
        submit.click()

        # Verifica se o nome está correto
        verify_name = bot.find_element(
            "div.field-value:nth-child(5)",
            By.CSS_SELECTOR
            )
        assert verify_name.text == bit.get_credentials(item)["voult"]["login"]

        # Verifica se a mensagem está correta
        verify_note = bot.find_element(
            "div.field-value:nth-child(25)",
            By.CSS_SELECTOR
            )
        assert verify_note.text == bit.get_credentials(item)["voult"]["note"]
        
        # Verifica se o email está correto
        verify_email = bot.find_element(
            "div.field-value:nth-child(21)",
            By.CSS_SELECTOR
            )
        assert verify_email.text == bit.get_credentials(item)["voult"]["email"]
        
        finish = "Success"

    except Exception as e:
        print(e)
        finish = "Failed"
    
    finally:
        print(finish)
        # Aguarda 3 segundos
        bot.wait(3000)

        # Finaliza e limpa o navegador
        bot.stop_browser()


if __name__ == '__main__':
    main()
