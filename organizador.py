import os
import shutil
import sys 
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox, filedialog 
import threading 
import time

# --- Adicionar o diretório 'dependencies' ao caminho de busca de módulos do Python ---
# Isso permite que o script encontre as bibliotecas CustomTkinter e darkdetect dentro da pasta 'dependencies'
# O os.path.dirname(__file__) garante que ele procure na pasta onde o script está.
SCRIPT_DIR = os.path.dirname(__file__)
DEPENDENCIES_DIR = os.path.join(SCRIPT_DIR, "dependencies") # ONDE ESTÃO AS LIBS
if os.path.exists(DEPENDENCIES_DIR) and DEPENDENCIES_DIR not in sys.path:
    sys.path.insert(0, DEPENDENCIES_DIR) # Adiciona 'dependencies' ao início do caminho de busca

# --- Mapeamento de Extensões para Organização ---
TIPOS_DE_ARQUIVO = {
    "imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".ico"],
    "documentos": [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "musicas": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "executaveis": [".exe", ".msi", ".dmg", ".appimage"],
    "compactados": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso"],
    "codigos": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".cs", ".php", ".json", ".xml", ".yml"],
    "fontes": [".ttf", ".otf", ".woff", ".woff2"],
    "apresentacoes": [".ppt", ".pptx"], 
    "planilhas": [".xls", ".xlsx", ".ods"], 
    "outros": [] 
}

# Flag para controlar a interrupção da organização por parte do usuário
parar_organizacao_flag = threading.Event()

# --- Lógica Central de Organização de Pastas ---
def organizar_pasta(caminho_da_pasta, log_textbox, progress_bar, moved_count_label, total_files_label):
    log_textbox.configure(state="normal") 
    log_textbox.delete("1.0", ctk.END) 
    log_textbox.insert(ctk.END, f"Iniciando a jornada de organização em: '{caminho_da_pasta}'\n\n")
    log_textbox.see(ctk.END)
    log_textbox.configure(state="disabled")

    if not os.path.exists(caminho_da_pasta):
        log_textbox.configure(state="normal")
        log_textbox.insert(ctk.END, f"Erro: O destino '{caminho_da_pasta}' não foi encontrado. Por favor, verifique o caminho.\n")
        log_textbox.see(ctk.END)
        log_textbox.configure(state="disabled")
        return False

    if not os.path.isdir(caminho_da_pasta):
        log_textbox.configure(state="normal")
        log_textbox.insert(ctk.END, f"Erro: '{caminho_da_pasta}' não é uma pasta válida para organizar.\n")
        log_textbox.see(ctk.END)
        log_textbox.configure(state="disabled")
        return False

    todos_os_itens = os.listdir(caminho_da_pasta)
    arquivos_para_organizar = [item for item in todos_os_itens if os.path.isfile(os.path.join(caminho_da_pasta, item))]
    
    total_arquivos = len(arquivos_para_organizar)
    arquivos_movidos_count = 0
    arquivos_nao_movidos_count = 0
    
    progress_bar.set(0) 
    moved_count_label.configure(text=f"Movidos: 0 | Erros: 0")
    total_files_label.configure(text=f"Total: {total_arquivos}")

    if total_arquivos == 0:
        log_textbox.configure(state="normal")
        log_textbox.insert(ctk.END, "Nenhum arquivo encontrado para organizar nesta pasta. Jornada leve!\n")
        log_textbox.see(ctk.END)
        log_textbox.configure(state="disabled")
        return True

    for i, nome_arquivo in enumerate(arquivos_para_organizar):
        if parar_organizacao_flag.is_set():
            log_textbox.configure(state="normal")
            log_textbox.insert(ctk.END, "\nOrganização interrompida pelo comandante!\n")
            log_textbox.see(ctk.END)
            log_textbox.configure(state="disabled")
            break 
        
        caminho_completo_arquivo = os.path.join(caminho_da_pasta, nome_arquivo)
        
        _, extensao_arquivo = os.path.splitext(nome_arquivo)
        extensao_arquivo = extensao_arquivo.lower()

        pasta_destino_nome = "outros"

        for categoria, extensoes in TIPOS_DE_ARQUIVO.items():
            if extensao_arquivo in extensoes:
                pasta_destino_nome = categoria
                break
        
        caminho_pasta_destino = os.path.join(caminho_da_pasta, pasta_destino_nome)

        if not os.path.exists(caminho_pasta_destino):
            os.makedirs(caminho_pasta_destino)
            log_textbox.configure(state="normal")
            log_textbox.insert(ctk.END, f"Criando novo setor: '{pasta_destino_nome}'\n")
            log_textbox.see(ctk.END)
            log_textbox.configure(state="disabled")

        try:
            shutil.move(caminho_completo_arquivo, caminho_pasta_destino)
            log_textbox.configure(state="normal")
            log_textbox.insert(ctk.END, f"Movendo: '{nome_arquivo}' para o setor '{pasta_destino_nome}'\n")
            log_textbox.see(ctk.END)
            log_textbox.configure(state="disabled")
            arquivos_movidos_count += 1
        except shutil.Error as e:
            log_textbox.configure(state="normal")
            log_textbox.insert(ctk.END, f"Falha ao mover '{nome_arquivo}': {e}. Destino ocupado ou permissão negada.\n")
            log_textbox.see(ctk.END)
            log_textbox.configure(state="disabled")
            arquivos_nao_movidos_count += 1
        except Exception as e:
            log_textbox.configure(state="normal")
            log_textbox.insert(ctk.END, f"Erro inesperado com '{nome_arquivo}': {e}\n")
            log_textbox.see(ctk.END)
            log_textbox.configure(state="disabled")
            arquivos_nao_movidos_count += 1
        
        progress = (i + 1) / total_arquivos
        progress_bar.set(progress)
        moved_count_label.configure(text=f"Movidos: {arquivos_movidos_count} | Erros: {arquivos_nao_movidos_count}")
        janela.update_idletasks() 
        # time.sleep(0.005) # Pequeno delay para ver a animação em arquivos pequenos

    if not parar_organizacao_flag.is_set(): 
        log_textbox.configure(state="normal")
        log_textbox.insert(ctk.END, "\nJornada de organização finalizada com sucesso!\n")
        log_textbox.see(ctk.END)
        log_textbox.configure(state="disabled")
    
    return True

# --- Funções de Ação da Interface de Usuário (UI) ---

def selecionar_pasta():
    caminho_selecionado = filedialog.askdirectory(title="Selecione o setor para organizar")
    if caminho_selecionado:
        entry_caminho.delete(0, ctk.END)
        entry_caminho.insert(0, caminho_selecionado)

def executar_organizacao_thread():
    caminho_da_pasta = entry_caminho.get()
    
    if not caminho_da_pasta:
        messagebox.showwarning("Atenção, Comandante!", "Por favor, insira ou selecione o setor a ser organizado.")
        return

    parar_organizacao_flag.clear() 
    botao_organizar.configure(state=ctk.DISABLED, text="Organizando...") 
    botao_parar.configure(state=ctk.NORMAL)
    botao_limpar_log.configure(state=ctk.DISABLED) 
    
    log_textbox.configure(state="normal")
    log_textbox.insert(ctk.END, f"Verificando setor e permissões...\n")
    log_textbox.see(ctk.END)
    log_textbox.configure(state="disabled")

    thread = threading.Thread(target=run_organization_in_thread, args=(caminho_da_pasta,))
    thread.start()

def run_organization_in_thread(caminho_da_pasta):
    sucesso = organizar_pasta(caminho_da_pasta, log_textbox, progress_bar, moved_count_label, total_files_label)
    
    janela.after(100, lambda: botao_organizar.configure(state=ctk.NORMAL, text="Iniciar Jornada!")) 
    janela.after(100, lambda: botao_parar.configure(state=ctk.DISABLED))
    janela.after(100, lambda: botao_limpar_log.configure(state=ctk.NORMAL))

    if sucesso and not parar_organizacao_flag.is_set():
        messagebox.showinfo("Jornada Concluída", "Sua pasta foi organizada! Verifique o log de bordo para mais detalhes.")
    elif parar_organizacao_flag.is_set():
        messagebox.showinfo("Jornada Interrompida", "A organização foi interrompida pelo comandante. Respeitamos suas ordens!")
    else:
        messagebox.showerror("Alerta Crítico", "Ocorreu um erro durante a organização. Consulte o log para investigar a anomalia.")

def limpar_log():
    log_textbox.configure(state="normal") 
    log_textbox.delete("1.0", ctk.END)
    log_textbox.insert(ctk.END, "Log de bordo limpo. Pronto para nova jornada.\n")
    log_textbox.see(ctk.END)
    log_textbox.configure(state="disabled") 
    progress_bar.set(0)
    moved_count_label.configure(text="Movidos: 0 | Erros: 0")
    total_files_label.configure(text="Total: 0")

def parar_organizacao():
    parar_organizacao_flag.set() 
    botao_parar.configure(state=ctk.DISABLED, text="Parando...") 

# --- Configuração da Interface Gráfica (UI) ---
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul/roxo, mais próximo da sua vibe

janela = ctk.CTk() 
janela.title("Organizador de Arquivos") 
janela.geometry("650x650") 
janela.resizable(False, False)

# Centraliza a janela na tela
janela.update_idletasks()
x = (janela.winfo_screenwidth() - janela.winfo_width()) // 2
y = (janela.winfo_screenheight() - janela.winfo_height()) // 2
janela.geometry(f"+{x}+{y}")

# Frame principal com gradiente (simula um visual mais profundo)
main_frame = ctk.CTkFrame(janela, fg_color=("gray20", "#1e293b"), corner_radius=15) 
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Título da Aplicação
label_titulo = ctk.CTkLabel(main_frame, 
                            text="Organizador de Arquivos", 
                            font=ctk.CTkFont("Inter", 32, "bold"), 
                            text_color="#89d9ff") 
label_titulo.pack(pady=(25, 25))

# Frame para a entrada e botões de seleção
path_input_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
path_input_frame.pack(pady=(0, 15), fill="x", padx=25) 

label_instrucao = ctk.CTkLabel(path_input_frame, 
                               text="Selecione o setor para organizar:", 
                               font=ctk.CTkFont("Inter", 14), 
                               text_color="#e0e0e0") 
label_instrucao.pack(pady=(0, 8), anchor="w")

entry_caminho = ctk.CTkEntry(path_input_frame, 
                             width=450, 
                             height=35, 
                             font=ctk.CTkFont("Consolas", 12), 
                             text_color="#f0f0f0",
                             fg_color="#36393f", 
                             border_color="#5865f2", 
                             border_width=2, 
                             corner_radius=8) 
entry_caminho.pack(side="left", fill="x", expand=True, padx=(0, 15))

# Tenta preencher a pasta Downloads por padrão
user_home_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
if os.path.exists(user_home_downloads):
    entry_caminho.insert(0, user_home_downloads)

botao_selecionar = ctk.CTkButton(path_input_frame,
                                 text="Procurar", 
                                 command=selecionar_pasta,
                                 font=ctk.CTkFont("Inter", 14, "bold"),
                                 fg_color="#5865f2", 
                                 hover_color="#424cd9",
                                 text_color="#ffffff",
                                 corner_radius=8, 
                                 width=120, 
                                 height=35) 
botao_selecionar.pack(side="right")

# Frame para botões de controle (Organizar/Parar/Limpar)
control_buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
control_buttons_frame.pack(pady=(20, 15)) 

botao_organizar = ctk.CTkButton(control_buttons_frame, 
                                text="Iniciar Jornada!", 
                                command=executar_organizacao_thread, 
                                font=ctk.CTkFont("Inter", 16, "bold"), 
                                fg_color="#28a745", 
                                hover_color="#218838",
                                text_color="#ffffff",
                                corner_radius=8, 
                                width=180, 
                                height=45)
botao_organizar.pack(side="left", padx=10)

botao_parar = ctk.CTkButton(control_buttons_frame,
                            text="Parar",
                            command=parar_organizacao,
                            font=ctk.CTkFont("Inter", 16, "bold"),
                            fg_color="#dc3545", 
                            hover_color="#c82333",
                            text_color="#ffffff",
                            corner_radius=8,
                            state=ctk.DISABLED, 
                            width=120, 
                            height=45)
botao_parar.pack(side="left", padx=10)

botao_limpar_log = ctk.CTkButton(control_buttons_frame,
                                 text="Limpar Log",
                                 command=limpar_log,
                                 font=ctk.CTkFont("Inter", 14), 
                                 fg_color="#6c757d", 
                                 hover_color="#5a6268",
                                 text_color="#ffffff",
                                 corner_radius=8,
                                 width=120, 
                                 height=45)
botao_limpar_log.pack(side="left", padx=10)

# Frame para a barra de progresso e contadores
progress_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
progress_frame.pack(pady=10, fill="x", padx=25)

progress_bar = ctk.CTkProgressBar(progress_frame, 
                                  orientation="horizontal", 
                                  mode="determinate", 
                                  height=15, 
                                  corner_radius=8,
                                  fg_color="#36393f", 
                                  progress_color="#00aaff") 
progress_bar.set(0)
progress_bar.pack(fill="x", pady=5)

# Labels para contagem de arquivos
count_labels_frame = ctk.CTkFrame(progress_frame, fg_color="transparent")
count_labels_frame.pack(fill="x", pady=(5, 0)) 

moved_count_label = ctk.CTkLabel(count_labels_frame, 
                                 text="Movidos: 0 | Erros: 0", 
                                 font=ctk.CTkFont("Inter", 12, "bold"), 
                                 text_color="#f0f0f0")
moved_count_label.pack(side="left")

total_files_label = ctk.CTkLabel(count_labels_frame, 
                                 text="Total: 0", 
                                 font=ctk.CTkFont("Inter", 12, "bold"), 
                                 text_color="#f0f0f0")
total_files_label.pack(side="right")

# Área de Log (TextBox)
log_textbox = ctk.CTkTextbox(main_frame, 
                             width=600, 
                             height=200, 
                             font=ctk.CTkFont("Consolas", 11), 
                             text_color="#00ff00", 
                             fg_color="#12121e", 
                             border_color="#5865f2",
                             border_width=1,
                             corner_radius=8, 
                             wrap="word",
                             state="disabled") 
log_textbox.pack(pady=(15, 0), padx=25, fill="both", expand=True) 

janela.mainloop()