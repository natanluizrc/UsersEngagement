# Autenticação no Azure AD e Obtenção de Token de Acesso

# Importa a biblioteca para fazer requisições HTTP
import requests

# Importa a biblioteca para acessar variáveis de ambiente
import os

def get_access_token():
    """
    Obtém um token de acesso do Azure AD para autenticar requisições à API do Power BI.
    As credenciais são carregadas de variáveis de ambiente para maior segurança.
    """
    # Obtém as credenciais do Azure AD a partir das variáveis de ambiente (Engagement Report)
    TENANT_ID = os.getenv("Azure_TenantId")
    CLIENT_ID = os.getenv("Azure_ClientId")
    CLIENT_SECRET = os.getenv("Azure_ClientSecret")

    # Define a URL do endpoint para obtenção do token de autenticação
    URL_TOKEN = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    
    # Define o corpo da requisição para obtenção do token de acesso
    payload = {
        "grant_type": "client_credentials",  # Tipo de autenticação
        "client_id": CLIENT_ID,  # ID do aplicativo registrado no Azure AD
        "client_secret": CLIENT_SECRET,  # Segredo do cliente (client secret)
        "scope": "https://analysis.windows.net/powerbi/api/.default"  # Escopo de acesso à API do Power BI
    }
    
    try:
        # Faz a requisição HTTP POST para obter o token
        response = requests.post(URL_TOKEN, data=payload)
        response.raise_for_status()  # Lança um erro se a resposta contiver um código HTTP de erro
        
        # Extrai o token de acesso da resposta JSON
        access_token = response.json().get("access_token")
        
        # Se o token for obtido com sucesso, exibe uma mensagem e retorna o token
        if access_token:
            print("Autenticação bem-sucedida!")
            return access_token
        else:
            print("Erro: Token de acesso não obtido.")
            return None
    except requests.exceptions.RequestException as e:
        # Captura qualquer erro na requisição e exibe a mensagem de erro
        print(f"Erro na autenticação: {e}")
        return None

# Permite testar o código executando diretamente o _01_AuthAzureAD.py
if __name__ == "__main__":
    get_access_token()