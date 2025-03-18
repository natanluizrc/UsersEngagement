# Listagem de Workspaces com Privilégios Administrativos

# Importa a biblioteca para fazer requisições HTTP
import requests

# Importa a função de autenticação
from _01_AuthAzureAD import get_access_token

def adm_workspaces_list():
    """
    Lista todos os workspaces do Power BI disponíveis.
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
    
    # Define a URL do endpoint da API do Power BI para listar workspaces disponíveis
    URL_WORKSPACES = "https://api.powerbi.com/v1.0/myorg/admin/groups?$top=1000"
    
    try:
        # Faz a requisição GET para obter os workspaces disponíveis
        response_adm = requests.get(URL_WORKSPACES, headers=HEADERS)
        response_adm.raise_for_status()  # Lança um erro se houver problema na requisição
        
        # Converte a resposta JSON em um dicionário Python
        workspaces = response_adm.json()
        
        # Exibe a lista de workspaces acessíveis pelo administrador
        print("Workspaces disponíveis:", workspaces)
    except requests.exceptions.RequestException as e:
        # Captura qualquer erro na requisição e exibe a mensagem de erro
        print(f"Erro ao buscar workspaces disponíveis: {e}")

# Permite testar o código executando diretamente o script _03_Adm-WorkspacesList.py
if __name__ == "__main__":
    adm_workspaces_list()