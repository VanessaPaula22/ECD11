# ECD11_v2

Um projeto básico de um Perceptron de Multicamadas (MLP) para o trabalho final da disciblina de Entrega Contínua e DevOps (ECD11).

# Estrutura do Projeto
.

├── .github/workflows

│ └── python-app.yml

├── pipeline

│ └── mlp

│ │ ├── __init__.py

│ │ └── mlp.py

│ ├── __init__.py

│ └── useful_functions.py

├── test

│ ├── __init__.py

│ └── test_mlp.py

├── .gitignore

├── README.md

├── main.py

└── requirements.txt

# Documentação do Projeto
Boas práticas utilizadas:

 - Controle de versionamento através do GitHub
 - O código fonte foi organizado em diretórios, separando a lógica da aplicação dos testes automatizados
 - Convenções de commits com o uso de mensagens claras e descritivas
 - Criação de branch "dev" para o desenvolvimento.

# Diagrama do Processo de CI:
![image](https://github.com/user-attachments/assets/42ebb1a7-517f-4d35-ab67-cc31418330d9)

Descrição das etapas:

 - Início do Pipeline: O pipeline é iniciado manualmente ou automaticamente quando um novo commit ou pull-request é detectado no repositório.

 - Commit ou Pull-Request: Modificações no código são enviadas para o repositório (commit) ou sugeridas em uma nova branch (pull-request), desencadeando a execução do pipeline.

 - Dev Review: Desenvolvedores revisam o código para garantir que as mudanças atendam aos padrões de qualidade e funcionalidade antes de prosseguir.

 - Build Automatizado: O código é compilado e preparado para execução, gerando uma versão testável do projeto.

 - Instalação de Dependências: Dependências e bibliotecas necessárias para o projeto são instaladas, garantindo o ambiente adequado para testes e execução.

 - Testes Automatizados / Análise de qualidade: Scripts de teste verificam automaticamente a funcionalidade e a estabilidade do código, identificando possíveis erros. Foi utilizado o pytest como ferramenta de teste automatizado.

 - Deploy: Zip do projeto e envio à plataforma PythonAnywhere da Anaconda, através de requests http, unzip e criação de task com schedule para execução automática do código.

Print da task de execução sobre o código:
![image](https://github.com/user-attachments/assets/90195add-45e5-4aa0-b516-20be00bb7776)

Upload do repositório na plataforma de execução:
![WhatsApp Image 2024-10-27 at 12 55 48](https://github.com/user-attachments/assets/ec617b51-a41f-4eb3-9556-5f2d3686840a)


Também utilizamos o Flake8 como ferramenta de análise de qualidade de código. A ferramenta verifica o estilo do código e aponta possíveis problemas de segurança. Essa verificação acontece durante a etapa de Testes automatizados, como forma de controle de qualidade do código.

 - Deploy: O código aprovado é implantado em um ambiente de produção ou teste, tornando-o acessível aos usuários finais ou testadores.

# Execução
Como Executar:
  1. Clone o repositório
  2. Instale as dependências usando "pip install -r requirements.txt"
  3. Execute o código com "python -u main.py"

Como Rodar os Testes:
  1. Instale Pytest
  2. Execute os testes com "pytest test"
