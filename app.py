4. import os
5. 
6. # ERRO DE SEGURANÇA: Chave de API exposta diretamente no código (Secret Leak)
7. AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
8. AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
9. 
10. def main():
11.     print("Iniciando aplicação extremamente insegura...")
12.     print(f"Conectando na AWS com a chave: {AWS_ACCESS_KEY_ID}")
13. 
14. if __name__ == "__main__":
15.     main()