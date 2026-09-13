# 📱 Scanner de Rede (Wi-Fi QR Code & Barcode Reader)

Este projeto transforma seu smartphone em um leitor de código de barras e QR Code sem fio. Utilizando a câmera do seu celular, ele lê o código e simula a digitação instantânea da informação (seguida da tecla `Enter`) diretamente no seu computador, onde quer que o cursor esteja focado.

Ideal para preencher planilhas, sistemas de estoque ou qualquer software de PDV sem precisar de um leitor físico conectado por cabo.

## 🛠️ Tecnologias Utilizadas

*   **Python:** Lógica principal do servidor e simulação de teclado.
*   **Flask:** Servidor web leve para hospedar a página na rede local.
*   **PyAutoGUI:** Biblioteca para controlar o teclado do computador e digitar os dados recebidos.
*   **pyOpenSSL:** Para gerar um certificado HTTPS temporário, exigência dos navegadores móveis para liberar o acesso à câmera.
*   **HTML5-QRCode:** Biblioteca JavaScript no front-end para escanear os códigos via câmera.

## ⚙️ Pré-requisitos

*   Python 3.x instalado no computador.
*   Computador e celular conectados na **mesma rede Wi-Fi**.

## 🚀 Instalação

1. Clone ou baixe este repositório.
2. Abra o terminal na pasta do projeto e instale as dependências executando:

```bash
pip install flask pyautogui pyopenssl
```

## 📖 Como Usar

1. **Inicie o servidor no computador:**
   Rode o script Python no seu terminal:
   ```bash
   python scanner.py
   ```
   *O terminal exibirá uma mensagem informando que o servidor está rodando e mostrará qual endereço você deve acessar (ex: `https://192.168.0.10:5000`).*

2. **Acesse no Celular:**
   Abra o navegador do seu celular e digite o endereço completo (incluindo o `https://` e a porta `:5000`).
   
   ⚠️ **Aviso de Segurança (Importante):** 
   Como o certificado de segurança gerado é local (Adhoc), o navegador exibirá uma tela de alerta dizendo "Sua conexão não é particular" ou similar. 
   * No Chrome: Toque em **Avançado** e depois em **Ir para [Seu IP] (inseguro)**.
   * No Safari: Toque em **Mostrar Detalhes** e depois em **Visitar este site**.

3. **Prepare o Computador:**
   No seu PC, clique com o mouse onde você deseja que o texto seja digitado (um bloco de notas, uma célula do Excel, um campo de busca, etc). Deixe o cursor piscando.

4. **Escaneie:**
   No celular, clique no botão **Abrir Câmera**, aponte para o código e aguarde. Assim que a leitura for feita, a informação aparecerá automaticamente no seu computador!
