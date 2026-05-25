import os

# CORREÇÃO: Removendo a chave mock e usando variável de ambiente
# No mundo real, essa chave estaria no GitHub Secrets ou em um Vault (GCP Secret Manager)
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID", "CHAVE_NAO_CONFIGURADA")

def main():
    print("Aplicação rodando de forma segura...")
    if AWS_ACCESS_KEY == "CHAVE_NAO_CONFIGURADA":
        print("Aviso: Variável de ambiente não encontrada.")
    else:
        print("Conectado com sucesso (Identidade protegida).")

if __name__ == "__main__":
    main()