
# 🔐 Gerenciador de Acesso com QR Code

Este projeto é um sistema de gerenciamento de acesso que utiliza leitura de QR Code, interface gráfica em Python (Tkinter) e registro de data e hora para verificar permissões de entrada. Ele pode ser conectado a um Arduino ou usado de forma independente com a câmera do computador ou celular.

---

## 🎯 Funcionalidades

- Leitura de QR Code em tempo real (webcam ou celular via cabo USB)
- Interface gráfica simples com Tkinter
- Registro de acessos permitidos e negados com data e hora
- Armazenamento em um arquivo `.csv`
- Integração simulada com sistemas de controle de portas (ex: Arduino)

---

## 🖼️ Interface

A interface exibe em tempo real se o QR Code é válido, junto com data, hora e nome do usuário.

---

## 📦 Requisitos

- Python 3.x
- OpenCV (`cv2`)
- Tkinter (incluso com Python)
- `pyzbar` para ler QR Codes

Instale as dependências:

```bash
pip install opencv-python pyzbar
```

---

## 🚀 Como usar

1. Clone o repositório:

```bash
git clone https://github.com/GabrielBarrosDev/gereciador_de_acesso.git
cd gereciador_de_acesso
```

2. Execute o programa:

```bash
python leitor_qr_acesso.py
```

3. Aponte a câmera para um QR Code válido (ex: "usuario1")

---

## 📁 Estrutura

```
gerenciador_de_acesso/
├── leitor_qr_acesso.py         # Código principal
├── registros_acesso.csv        # Arquivo gerado com os registros
├── README.md                   # Este arquivo
└── ...
```

---

## 📌 Exemplo de QR Code válido

Para testes, use um QR Code com o conteúdo:

```
usuario1
```

Você pode gerar QR Codes usando sites como: [https://www.qr-code-generator.com/](https://www.qr-code-generator.com/)

---

## 💡 Dicas

- Use a câmera do celular conectada via USB usando aplicativos como **DroidCam**.
- Para Arduino físico, adapte o código Python para enviar comandos via `pyserial`.

---

## 🔧 Possibilidades de Expansão

- Integração com banco de dados
- Controle de acesso com RFID e QR Code
- Comunicação com o Arduino via Serial
- Dashboard com histórico de acessos

---

## 👨‍💻 Autor

Desenvolvido por [Gabriel Barros](https://github.com/GabrielBarrosDev)
