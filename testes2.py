from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações
DEEPSEEK_URL = "https://www.deepseek.com"  # URL atual do DeepSeek
CONSULTA = "Explique quantum computing em 3 linhas."

def consulta_automatizada():
    # Configurar o ChromeDriver automaticamente
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(DEEPSEEK_URL)

    try:
        # Aguardar até que o campo de input esteja disponível
        input_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )
        
        # Digitar a consulta e enviar
        input_box.send_keys(CONSULTA)
        input_box.send_keys(Keys.RETURN)

        # Aguardar a resposta (ajuste o tempo conforme necessário)
        time.sleep(15)

        # Capturar a última resposta (ajuste o seletor conforme o site)
        respostas = driver.find_elements(By.CSS_SELECTOR, "[class*='response']")
        if respostas:
            print("\nResposta do DeepSeek:")
            print(respostas[-1].text)  # Pega a última resposta
        else:
            print("Resposta não encontrada.")

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        driver.quit()

#if __name__ == "__main__":
consulta_automatizada()