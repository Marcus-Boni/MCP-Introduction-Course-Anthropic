[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/marcus-boni-mcp-introduction-course-anthropic-badge.png)](https://mseep.ai/app/marcus-boni-mcp-introduction-course-anthropic)

<div align="center">

# 🤖 MCP Chat

**Um chatbot interativo de linha de comando alimentado por Anthropic Claude e Model Control Protocol**

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-1.8.0-purple.svg)](https://github.com/anthropics/mcp)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[Funcionalidades](#funcionalidades) • [Instalação](#instalação) • [Uso](#uso) • [Desenvolvimento](#desenvolvimento) • [Contribuindo](#contribuindo)

</div>

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
  - [Chat Básico](#chat-básico)
  - [Recuperação de Documentos](#recuperação-de-documentos)
  - [Execução de Comandos](#execução-de-comandos)
- [Desenvolvimento](#desenvolvimento)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Configuração](#configuração)
- [Solução de Problemas](#solução-de-problemas)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Visão Geral

MCP Chat é uma poderosa interface de linha de comando que permite interação perfeita com modelos de IA através da API Anthropic. Construído na arquitetura **Model Control Protocol (MCP)**, oferece recuperação de documentos, prompts baseados em comandos e integrações de ferramentas extensíveis para maior produtividade.

Perfeito para desenvolvedores que desejam interagir com Claude AI diretamente do terminal com recursos avançados como contexto de documentos e comandos personalizados.

## Funcionalidades

- 💬 **Interface de Chat Interativa** - Conversas em tempo real com modelos Claude AI
- 📄 **Recuperação Inteligente de Documentos** - Acesso rápido a documentos usando a sintaxe `@`
- ⚡ **Sistema de Comandos** - Execute comandos predefinidos com o prefixo `/`
- 🔧 **Integração MCP** - Sistema de ferramentas extensível via Model Control Protocol
- 🎨 **Experiência CLI Rica** - Auto-completar e interface amigável com prompt-toolkit
- 🔄 **Conversas Multi-turno** - Mantém contexto durante toda a conversa
- 🛠️ **Execução de Ferramentas** - Execute ferramentas personalizadas perfeitamente dentro do chat

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte:

| Requisito | Versão | Descrição |
|-----------|--------|-----------|
| **Python** | 3.9+ | [Download](https://www.python.org/downloads/) |
| **Chave API Anthropic** | - | [Obtenha sua chave](https://console.anthropic.com/) |

## Instalação

### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/Marcus-Boni/MCP-Introduction-Course-Anthropic.git
cd mcp-chat
```

### 2️⃣ Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env  # Ou crie manualmente
```

Adicione sua configuração:

```env
ANTHROPIC_API_KEY=sua_chave_api_aqui
CLAUDE_MODEL=claude-3-5-sonnet-20241022
USE_UV=1  # Configure como 0 para usar pip
```

### 3️⃣ Instale as Dependências

#### 🚀 Opção A: Usando uv (Recomendado)

[uv](https://github.com/astral-sh/uv) é um instalador e resolvedor de pacotes Python extremamente rápido.

```bash
# Instale o uv
pip install uv

# Crie e ative o ambiente virtual
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Instale as dependências
uv pip install -e .

# Execute a aplicação
uv run main.py
```

#### 🐍 Opção B: Usando pip

```bash
# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Instale as dependências
pip install anthropic python-dotenv prompt-toolkit "mcp[cli]==1.8.0"

# Execute a aplicação
python main.py
```

## Uso

### Chat Básico

Inicie uma conversa simplesmente digitando sua mensagem:

```
> Olá! Como você pode me ajudar hoje?
Assistente: Olá! Sou Claude, um assistente de IA. Posso te ajudar com...
```

### Recuperação de Documentos

Referencie documentos usando o símbolo `@` seguido do nome do documento:

```
> Pode explicar o conteúdo em @deposition.md?
Assistente: Com base no documento de depoimento, aqui está um resumo...

> Compare @document1.md e @document2.md
Assistente: Deixe-me comparar esses dois documentos para você...
```

**Documentos Disponíveis:**
- `deposition.md` - Documentação de testemunho
- `report.pdf` - Relatórios técnicos
- `financials.docx` - Dados financeiros
- `outlook.pdf` - Projeções futuras
- `plan.md` - Planos de projeto
- `spec.txt` - Especificações técnicas

### Execução de Comandos

Execute comandos predefinidos usando o prefixo `/`:

```
> /summarize deposition.md
Assistente: Aqui está um resumo conciso do documento...

> /format report.pdf
Assistente: Reformatando o documento em markdown...
```

**💡 Dica:** Pressione `Tab` para auto-completar comandos e documentos!

### Exemplo de Sessão

```
> Olá!
Assistente: Olá! Como posso ajudar hoje?

> @deposition.md
Assistente: Carreguei o documento de depoimento. O que você gostaria de saber?

> /summarize deposition.md
Assistente: Aqui está um resumo: Este depoimento cobre o testemunho 
de Angela Smith, P.E., sobre...

> Quais são os pontos principais?
Assistente: Os pontos principais do depoimento são...
```

### Atalhos de Teclado

| Atalho | Ação |
|--------|------|
| `Tab` | Auto-completar comandos e documentos |
| `@` | Acionar auto-completar de documentos |
| `/` | Acionar auto-completar de comandos |
| `Ctrl+C` | Sair da aplicação |

## Desenvolvimento

### Estrutura do Projeto

```
mcp-chat/
├── core/
│   ├── __init__.py       # Inicialização do módulo core
│   ├── chat.py           # Funcionalidade base de chat
│   ├── cli.py            # Implementação da interface CLI
│   ├── cli_chat.py       # Recursos de chat específicos da CLI
│   ├── claude.py         # Integração com API Claude
│   └── tools.py          # Sistema de gerenciamento de ferramentas
├── main.py               # Ponto de entrada da aplicação
├── mcp_server.py         # Implementação do servidor MCP
├── mcp_client.py         # Implementação do cliente MCP
├── pyproject.toml        # Dependências do projeto
├── .env                  # Variáveis de ambiente (criar a partir de .env.example)
├── .env.example          # Template de ambiente
├── .gitignore            # Regras do Git ignore
└── README.md             # Este arquivo
```

### Adicionando Novos Documentos

Edite `mcp_server.py` e adicione entradas ao dicionário `docs`:

```python
docs = {
    "seu-doc.md": "Conteúdo do seu documento aqui",
    "outro-doc.pdf": "Conteúdo de outro documento",
    # ...documentos existentes...
}
```

### Criando Comandos Personalizados

Adicione novos comandos de prompt em `mcp_server.py`:

```python
@mcp.prompt(
    name="seu_comando",
    description="Descrição do que seu comando faz",
)
def seu_comando(
    doc_id: str = Field(description="O ID do documento"),
) -> list[base.Message]:
    # Implementação do seu comando
    pass
```

### Estendendo com Ferramentas MCP

Crie novas ferramentas em `mcp_server.py`:

```python
@mcp.tool(
    name="sua_ferramenta",
    description="O que sua ferramenta faz",
)
def sua_ferramenta(
    param: str = Field(description="Descrição do parâmetro"),
):
    # Implementação da ferramenta
    return "Resultado"
```

## Configuração

### Variáveis de Ambiente

| Variável | Obrigatória | Padrão | Descrição |
|----------|-------------|--------|-----------|
| `ANTHROPIC_API_KEY` | ✅ | - | Sua chave API Anthropic |
| `CLAUDE_MODEL` | ✅ | - | Modelo Claude a usar |
| `USE_UV` | ❌ | `0` | Usar uv para executar (1=sim, 0=não) |

### Modelos Claude Suportados

- `claude-3-5-sonnet-20241022` (Recomendado)
- `claude-3-opus-20240229`
- `claude-3-sonnet-20240229`
- `claude-3-haiku-20240307`

## Solução de Problemas

### Problemas Comuns

**Problema: "ANTHROPIC_API_KEY cannot be empty"**
```bash
# Solução: Certifique-se de que seu arquivo .env contém uma chave API válida
echo 'ANTHROPIC_API_KEY=sua_chave_aqui' > .env
```

**Problema: Erros de importação**
```bash
# Solução: Reinstale as dependências
pip install -e .
```

**Problema: Comando não encontrado (Windows)**
```bash
# Solução: Use o caminho completo para ativar
.venv\Scripts\activate.bat
```

**Problema: Falha na conexão do servidor MCP**
```bash
# Solução: Verifique se o uv está instalado corretamente
pip install uv --upgrade
```

## Contribuindo

Contribuições são bem-vindas! Veja como você pode ajudar:

1. **Fork** o repositório
2. **Crie** uma nova branch (`git checkout -b feature/funcionalidade-incrivel`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona funcionalidade incrível'`)
4. **Push** para a branch (`git push origin feature/funcionalidade-incrivel`)
5. **Abra** um Pull Request

---

<div align="center">

⭐ Dê uma estrela neste repo se você achou útil!

</div>
