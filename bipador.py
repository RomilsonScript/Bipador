from flask import Flask, request, render_template_string
import pyautogui

app = Flask(__name__)

# Página HTML que será aberta no celular
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Leitor QR/Código de Barras</title>
    <script src="https://unpkg.com/html5-qrcode"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 30px; background: #f4f4f4;}
        #reader { width: 100%; max-width: 400px; margin: auto; background: white; padding: 10px; border-radius: 8px;}
        button { padding: 15px 30px; font-size: 18px; margin-bottom: 20px; background: #007bff; color: white; border: none; border-radius: 5px;}
        p { font-size: 18px; font-weight: bold; color: green; }
    </style>
</head>
<body>
    <h2>Scanner de Rede</h2>
    <button id="startButton">Abrir Câmera</button>
    <div id="reader"></div>
    <p id="result"></p>

    <script>
        const html5QrCode = new Html5Qrcode("reader");
        const startButton = document.getElementById("startButton");
        const resultDisplay = document.getElementById("result");

        startButton.addEventListener("click", () => {
            // Tenta usar a câmera traseira do celular
            html5QrCode.start(
                { facingMode: "environment" },
                { fps: 10, qrbox: { width: 250, height: 250 } },
                (decodedText, decodedResult) => {
                    // Para a câmera assim que ler
                    html5QrCode.stop();
                    resultDisplay.innerText = "Enviado: " + decodedText;

                    // Envia o resultado via POST para o Python
                    fetch('/scan', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ texto: decodedText })
                    });
                },
                (errorMessage) => { }
            ).catch(err => { alert("Erro na câmera: " + err); });
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    texto = data.get('texto', '')
    if texto:
        # Digita o texto onde o cursor estiver focado
        pyautogui.write(texto)
        # Aperta Enter (comportamento padrão de leitores físicos)
        pyautogui.press('enter')
    return {"status": "sucesso"}

if __name__ == '__main__':
    # ssl_context='adhoc' gera um HTTPS temporário para o celular permitir a câmera
    print("Servidor rodando! Acesse https://<SEU_IP_NA_REDE>:5000 no celular.")
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')