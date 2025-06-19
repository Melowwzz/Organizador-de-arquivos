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

### 💻 **Como Usar (Guia Passo a Passo):**

Para rodar este programa, você precisará ter o Python instalado no seu computador.

**Passo 0: Preparação (Baixando o Projeto Completo)**

1.  **Baixe o Código-Fonte:**
    * Clique em "< > Code" no topo desta página do GitHub e selecione **"Download ZIP"**.
    * Ou clone o repositório via Git: `git clone [URL_DO_SEU_REPOSITORIO]`
2.  **Extraia os Arquivos:**
    * Descompacte o arquivo ZIP em uma pasta de sua preferência (ex: `C:\MeusProgramas\OrganizadorDeArquivos`). Esta será a **Pasta Principal do Projeto**.

**Passo 1: Instalando o Python (Se você ainda não tem!)**

* **Pule este passo** se você já tem o Python 3.x instalado e funcionando no seu computador.
1.  **Baixe o Instalador Oficial do Python:** Vá para: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2.  **Execute o Instalador (ATENÇÃO CRÍTICA AQUI!):**
    * Na **PRIMEIRA TELA**, **MARQUE a caixa `Add python.exe to PATH`**. Isso é **FUNDAMENTAL** para o programa funcionar.
    * Prossiga com a instalação (pode escolher "Instalação Personalizada" e marcar tudo, ou a padrão se "Add to PATH" estiver marcado).
3.  **Verifique a Instalação:** Abra o PowerShell e digite `python --version` e `pip --version`. Ambos devem mostrar as versões instaladas.

**Passo 2: Baixando as Dependências (Bibliotecas Essenciais)**

* Seu programa usa bibliotecas extras para a interface. Elas **NÃO estão no download principal do GitHub para manter o projeto leve**.
* Você deve baixá-las separadamente.

1.  **Baixe o Pacote de Dependências:**
    * Acesse este link no seu navegador: [**Baixar Pasta 'dependencies' (Google Drive)**](https://drive.google.com/drive/folders/1Y-bVFgIA3STM524cyMx8BBPU0eYiArM?usp=sharing)
    * Clique em "Fazer download" da pasta `dependencies`.
    * Salve este arquivo `.zip` na **MESMA Pasta Principal do Projeto** que você descompactou no **Passo 0**.
2.  **Extraia a Pasta `dependencies`:**
    * Vá até a Pasta Principal do Projeto.
    * Clique com o botão direito no arquivo `.zip` (`dependencies.zip`) e selecione `Extrair Tudo...`.
    * **MUITO IMPORTANTE:** Certifique-se de que a pasta **`dependencies` seja extraída DIRETAMENTE DENTRO da Pasta Principal do Projeto**, ao lado do arquivo `organizador.py`. O caminho final deve ser algo como: `C:\SeuCaminho\OrganizadorDeArquivos-main\dependencies`.
        * **O nome da pasta deve ser `dependencies` (com "d" minúsculo) para o programa encontrar as bibliotecas!**

**Passo 3: Execute o Programa!**

Agora que o Python está instalado e as dependências estão no lugar certo, é hora de voar!

1.  **Vá para a Pasta Principal do Projeto:**
    * Navegue no Explorador de Arquivos até a pasta onde você descompactou tudo (ex: `C:\MeusProgramas\OrganizadorDeArquivos`).
2.  **Execute o Programa:**
    * Basta **clicar duas vezes** no arquivo **`organizador.py`**.
    * Uma janela bonita do "Organizador de Arquivos" deve aparecer!
    * **Se não abrir ao clicar duas vezes:** Abra o PowerShell na Pasta Principal do Projeto (clique na barra de endereço na pasta e digite `powershell` e Enter). No terminal, digite: `python organizador.py` e aperte Enter.

---

### ⭐ **Solução de Problemas Rápidos:**

* **"Erro: A pasta '...' não existe."**: O caminho da pasta que você selecionou não é válido.
    * **Solução:** Clique em **`Procurar`** na UI e selecione a pasta manualmente.
* **"Erro Crítico / Permissão Negada"**: Ao tentar organizar pastas do sistema (como `C:\Windows`).
    * **Solução:** Escolha uma pasta nas suas "Minhas Documentos" ou em um drive que você tem controle total.
* **"No module named 'customtkinter'"**: As dependências não foram encontradas.
    * **Solução:** Refaça o **Passo 1 (Instalação Python)** e o **Passo 2 (Baixando Dependências)** com atenção especial aos nomes e locais das pastas.

---

### 📝 **Personalização e Contribuição:**

* **Tipos de Arquivo:** Você pode facilmente editar o dicionário `TIPOS_DE_ARQUIVO` dentro do `organizador.py` para adicionar novas categorias ou extensões que desejar organizar!
* **Temas Visuais:** Altere `ctk.set_default_color_theme("blue")` no `organizador.py` para experimentar outros temas do CustomTkinter (ex: "dark-blue", "green") ou personalize suas próprias cores!

---
