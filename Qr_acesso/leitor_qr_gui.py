import cv2
from pyzbar.pyzbar import decode
import tkinter as tk
from datetime import datetime
import csv
import threading
import time

# Lista de QR Codes autorizados
autorizados = ['usuario123', 'admin789', 'funcionario456']

def registrar_acesso(codigo, status):
    with open('registros_acesso.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), codigo, status])

def iniciar_leitura():
    cap = cv2.VideoCapture(1)

    while True:
        success, frame = cap.read()
        if not success:
            continue

        for code in decode(frame):
            qr_data = code.data.decode('utf-8')

            if qr_data in autorizados:
                status = "Acesso Permitido"
                cor = "green"
                simular_porta(True)
            else:
                status = "Acesso Negado"
                cor = "red"
                simular_porta(False)

            registrar_acesso(qr_data, status)
            atualizar_interface(qr_data, status, cor)
            time.sleep(2)
            cap.release()
            return

        cv2.imshow("Leitor QR", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def atualizar_interface(usuario, status, cor):
    label_resultado.config(text=f"{status}: {usuario}", fg=cor)

def simular_porta(acesso_liberado):
    if acesso_liberado:
        canvas.itemconfig(porta_led, fill="green")
        label_porta.config(text="🔓 Porta Aberta")
    else:
        canvas.itemconfig(porta_led, fill="red")
        label_porta.config(text="🔒 Acesso Bloqueado")

def iniciar_thread():
    threading.Thread(target=iniciar_leitura).start()

# Interface gráfica
janela = tk.Tk()
janela.title("Controle de Acesso Simulado - Câmera IP")
janela.geometry("400x300")

label_titulo = tk.Label(janela, text="Leitor de QR Code", font=("Arial", 18))
label_titulo.pack(pady=10)

btn_ler = tk.Button(janela, text="Ler QR Code", command=iniciar_thread, font=("Arial", 14))
btn_ler.pack(pady=10)

label_resultado = tk.Label(janela, text="", font=("Arial", 14))
label_resultado.pack(pady=10)

canvas = tk.Canvas(janela, width=100, height=100)
porta_led = canvas.create_oval(20, 20, 80, 80, fill="gray")
canvas.pack()

label_porta = tk.Label(janela, text="Estado da Porta", font=("Arial", 12))
label_porta.pack(pady=10)

janela.mainloop()
