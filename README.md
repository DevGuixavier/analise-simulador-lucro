# Análise Simulador Lucro

O projeto Análise Simulador Lucro é uma ferramenta interativa que permite simular e analisar o lucro de um negócio ao longo do tempo, com base em parâmetros como clientes iniciais, custo de aquisição de clientes (CAC), ticket médio e margem de lucro. O projeto oferece visualizações gráficas e cálculos dinâmicos para ajudar na tomada de decisões estratégicas.

## Índice

- [Descrição](#descrição)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Funcionalidades](#funcionalidades)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Descrição

Este projeto visa realizar uma análise financeira utilizando diversos parâmetros de entrada, como clientes iniciais, CAC (Custo de Aquisição de Cliente), ticket médio e margem de lucro. Ele calcula o lucro acumulado ao longo de um período e gera gráficos interativos para visualizar esses resultados de maneira clara e dinâmica.

Além disso, o projeto possui um botão chamado "Armazenar Dados", que permite salvar os dados inseridos em um banco de dados SQLite, chamado `entradas.db`. Para visualizar esse banco de dados, você precisará instalar a extensão SQLite Viewer.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Streamlit**: Framework para criação de interfaces web interativas.
- **Plotly**: Biblioteca para visualização de gráficos interativos.
- **SQLite**: Banco de dados para armazenar os dados de entrada e resultados.
- **Pandas**: Biblioteca para manipulação de dados.
- **NumPy**: Biblioteca para cálculos numéricoss
  
## Instalação

Passo a passo para instalar e rodar o projeto:

1. Clone este repositório:
   ```sh
   git clone <URL_do_repositório>
   ```

2. Entre na pasta do projeto:
   ```sh
   cd nome-do-projeto
   ```

3. Instale as dependências necessárias utilizando o pip:

   - **Streamlit**:
     ```sh
     pip install streamlit
     ```
   - **Plotly**:
     ```sh
     pip install plotly
     ```
   - **SQLite** (geralmente já vem com o Python, mas caso precise):
     ```sh
     pip install sqlite3
     ```

4. Execute o projeto:
   ```sh
   streamlit run main.py
   ```

## Como Usar

Após configurar o ambiente e instalar as dependências, você pode começar a usar o projeto da seguinte forma:

1. Execute o comando abaixo para iniciar o aplicativo Streamlit:
   ```sh
   streamlit run main.py
   ```

2. O aplicativo será aberto no seu navegador padrão, onde você poderá:
   - Inserir dados como clientes iniciais, CAC, ticket médio e margem de lucro.
   - Visualizar os resultados em tempo real, com gráficos interativos gerados pelo Plotly.
   - Armazenar Dados:
     - O projeto possui um botão chamado "Armazenar Dados" que, quando pressionado, grava os dados inseridos no banco de dados `entradas.db`.
     - Para visualizar os dados armazenados, você precisará instalar a extensão SQLite Viewer em seu navegador ou em um editor como o VS Code.

### Instruções para instalação do SQLite Viewer

- No VS Code, vá até a loja de extensões e busque por SQLite Viewer. Após instalar, você poderá abrir o arquivo `entradas.db` diretamente na interface do VS Code.
- No navegador, instale uma extensão de SQLite Viewer que permita abrir arquivos `.db` diretamente.

### Funcionalidades

Este projeto oferece as seguintes funcionalidades:

- **Cálculo de lucro acumulado**: A partir de parâmetros inseridos, o projeto calcula o lucro acumulado mês a mês.
- **Estimativa de receita mensal**: Com base no ticket médio, calcula a receita mensal gerada.
- **Dashboards interativos**: Gráficos gerados pelo Plotly para visualização dinâmica dos dados.
- **Armazenamento de dados**: Permite salvar os dados no banco de dados `entradas.db`, acessível com o SQLite Viewer.

## Contribuições

Se você deseja contribuir para este projeto, siga os passos abaixo:

1. Faça um fork deste repositório clicando no botão "Fork" no GitHub.

2. Clone o repositório forkado para sua máquina local:
   ```sh
   git clone <URL_do_repositório_forkado>
   ```

3. Crie uma nova branch para a sua modificação:
   ```sh
   git checkout -b feature-xyz
   ```

4. Faça suas alterações e commit:
   ```sh
   git commit -am 'Adicionando nova funcionalidade'
   ```

5. Envie para o repositório remoto:
   ```sh
   git push origin feature-xyz
   ```

6. Abra um Pull Request para que suas alterações sejam avaliadas e possivelmente incorporadas ao projeto principal.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
