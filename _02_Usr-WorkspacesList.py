# Listagem de Workspaces sem Privilégios Administrativos

# Importa a biblioteca para fazer requisições HTTP
import requests

# Importa a função de autenticação
from _01_AuthAzureAD import get_access_token  

def usr_workspaces_list():
    """
    Lista todos os workspaces do Power BI acessíveis.
    """
    # Obtém o token de acesso chamando a função get_access_token()
    access_token = get_access_token()
    
    # Se a autenticação falhar, encerra a execução da função
    if not access_token:
        return
    
    # Define os cabeçalhos da requisição, incluindo o token de autenticação
    HEADERS = {
        "Authorization": f"Bearer {access_token}",  # Inclui o token no cabeçalho da requisição
        "Content-Type": "application/json"  # Define o formato dos dados esperados na resposta
    }
    
    # Define a URL do endpoint da API do Power BI para listar workspaces acessíveis
    URL_WORKSPACES = "https://api.powerbi.com/v1.0/myorg/groups"
    
    try:
        # Faz a requisição GET para obter os workspaces acessíveis
        response_usr = requests.get(URL_WORKSPACES, headers=HEADERS)
        response_usr.raise_for_status()  # Lança um erro se houver problema na requisição
        
        # Converte a resposta JSON em um dicionário Python
        workspaces = response_usr.json()
        
        # Exibe a lista de workspaces acessíveis pelo usuário
        print("Workspaces acessíveis:", workspaces)
    except requests.exceptions.RequestException as e:
        # Captura qualquer erro na requisição e exibe a mensagem de erro
        print(f"Erro ao buscar workspaces acessíveis: {e}")

# Permite testar o código executando diretamente o script _02_Usr-WorkspacesList.py
if __name__ == "__main__":
    usr_workspaces_list()