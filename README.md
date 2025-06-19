# 🚀 Organizador de Arquivos - Domine o Caos Digital! 📁

Este projeto Python oferece uma ferramenta de interface gráfica (GUI) intuitiva para te ajudar a organizar automaticamente seus arquivos em pastas específicas, baseadas no tipo de arquivo. Mantenha seus downloads, documentos, imagens e muito mais sempre em ordem, sem esforço manual!

---

### ✨ **Funcionalidades Principais:**

* **Organização Inteligente:** Classifica arquivos por extensão em categorias predefinidas (Imagens, Documentos, Vídeos, Músicas, Executáveis, etc.).
* **Interface Gráfica (UI) Moderna:** Desenvolvido com [CustomTkinter](https://customtkinter.tomsonsdev.com/) para uma experiência visual agradável e tema escuro.
* **Seleção Flexível de Pasta:** Escolha **qualquer pasta** do seu sistema para organizar, não apenas a pasta Downloads.
* **Feedback em Tempo Real:** Acompanhe o processo de organização com uma barra de progresso e um log de atividades detalhado diretamente na interface.
* **Controle Total:** Inicie, pare (com cautela) e limpe o log a qualquer momento.

---

### 💻 **Como Usar:**

Para rodar este programa, você precisará ter o Python instalado no seu computador.

1.  **Baixe o Projeto Completo:**
    * Clique em "Code" (ou "Código") no topo desta página do GitHub e selecione "Download ZIP".
    * Ou clone o repositório via Git: `git clone [URL_DO_SEU_REPOSITORIO]`
2.  **Extraia os Arquivos:**
    * Descompacte o arquivo ZIP em uma pasta de sua preferência (ex: `C:\MeusProjetos\OrganizadorDeArquivos`).
3.  **Instale o Python (se necessário):**
    * Se você ainda não tem Python 3.x instalado, baixe e instale a versão mais recente em [python.org/downloads/](https://www.python.org/downloads/). **É fundamental marcar a opção "Add Python.exe to PATH" durante a instalação!**
4.  **Instale as Dependências (ou use as pré-empacotadas):**
    * **Opção 1 (Recomendado - Usar as Dependências Incluídas):**
        * Este projeto já vem com as bibliotecas necessárias na pasta `dependencies/`. Você não precisa fazer nada!
    * **Opção 2 (Manual - Se a Opção 1 não funcionar ou para Devs):**
        * Abra o terminal (ou PowerShell) na pasta do projeto e instale as bibliotecas listadas em `requirements.txt`:
            `pip install -r requirements.txt`
5.  **Execute o Programa:**
    * **No Windows:** Vá até a pasta do projeto e execute o `organizador.py` diretamente clicando duas vezes nele.
    * **Via Terminal:** Abra o terminal na pasta do projeto e execute: `python organizador.py`

---

### 📥 **Download das Dependências (Alternativo):**

Caso a pasta `dependencies` não esteja incluída no download principal do GitHub, ou se houver algum problema, você pode baixá-las separadamente aqui:

[**Baixar Pasta 'dependencies' (Google Drive)**](https://drive.google.com/drive/folders/1Y-bVFgIA3STM524cyMx8BBPUU0eYiArM?usp=sharing)

---

### 📝 **Personalização e Contribuição:**

* **Tipos de Arquivo:** Você pode facilmente editar o dicionário `TIPOS_DE_ARQUIVO` dentro do `organizador.py` para adicionar novas categorias ou extensões que desejar organizar!
* **Temas Visuais:** Altere `ctk.set_default_color_theme("blue")` no `organizador.py` para experimentar outros temas do CustomTkinter (ex: "dark-blue", "green") ou personalize suas próprias cores!

