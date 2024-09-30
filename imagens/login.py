import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def autenticar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    # Aqui você pode adicionar a lógica de autenticação
    if usuario == "Joao Faquira" and senha == "1991":
        messagebox.showinfo("Login", "Autenticado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Criando a janela principal
root = tk.Tk()
root.title("Departamento Património e Logística")

# Definindo o tamanho da janela
root.geometry("350x450")

# Adicionando o título da tela
label_titulo = tk.Label(root, text="Departamento Património e Logística", font=("Arial", 16))
label_titulo.pack(pady=10)

# Carregando o timbre da universidade
imagem = Image.open("E:/curso-informatica-2020/4ano/II Semestre/Fundamentos do HTML5/ProtifolioFaquira/novo.PNG")
imagem = imagem.resize((100, 100), Image.Resampling.LANCZOS)
timbre = ImageTk.PhotoImage(imagem)

# Adicionando o timbre à tela
label_timbre = tk.Label(root, image=timbre)
label_timbre.pack(pady=10)

# Campo de usuário
label_usuario = tk.Label(root, text="Usuário:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(root)
entry_usuario.pack(pady=5)

# Campo de senha
label_senha = tk.Label(root, text="Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=5)

# Botão de autenticação
botao_autenticar = tk.Button(root, text="Autenticar", command=autenticar)
botao_autenticar.pack(pady=20)

# Executando a aplicação
root.mainloop()
