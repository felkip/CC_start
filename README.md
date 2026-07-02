# CS Start

Aplicação para ajudar pessoas que estão pensando em entrar ou começando o curso de Ciência da Computação.

## Tecnologias

- **Python** - Linguagem de programação
- **Streamlit** - Framework web
- **PostgreSQL** - Banco de dados

## Estrutura do Projeto

```
CS Start/
├── app/                 # Módulos da aplicação
│   ├── auth.py         # Sistema de autenticação
│   ├── quiz.py         # Lógica do quiz de perfil
│   └── roadmap.py      # Roadmap sugerido por perfil
├── config/             # Configurações
│   └── db_config.py    # Configuração do banco de dados
├── database/           # Scripts SQL
│   └── schema.sql      # Schema do banco
├── static/             # Arquivos estáticos (CSS, imagens)
├── main.py             # Aplicação principal (Streamlit)
├── plano_quiz.md       # Plano inicial do quiz
├── plano_roadmap.md    # Plano inicial do roadmap
├── requirements.txt    # Dependências Python
├── tests/              # Testes básicos da aplicação
├── .env.example        # Exemplo de variáveis de ambiente
└── README.md           # Este arquivo
```

## Funcionalidades

### ✅ Implementadas
- **Login e Cadastro** - Sistema de autenticação com senhas criptografadas
- **Quiz de Perfil** - Perguntas simples para identificar afinidade com computação
- **Roadmap de Estudos** - Sugestão de tópicos com base no resultado do quiz

### 🔄 Em Desenvolvimento
- **Melhorias visuais** - Interface mais sofisticada
- **Recomendações personalizadas** - Sugestões mais completas

## Instalação

### 1. Clonar o projeto
```bash
cd "C:\Users\lfcar\OneDrive\Desktop\CC"
```

### 2. Criar ambiente virtual
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar banco de dados

#### Opção A: PostgreSQL Local
1. Instale PostgreSQL (https://www.postgresql.org/download/)
2. Abra o pgAdmin ou psql
3. Execute o arquivo `database/schema.sql`
4. Copie `.env.example` para `.env` e configure as credenciais

#### Opção B: Supabase (PostgreSQL em Nuvem)
1. Crie uma conta em https://supabase.com
2. Execute o arquivo `database/schema.sql` no editor SQL
3. Copie a connection string para `.env`

### 5. Executar a aplicação
```bash
streamlit run main.py
```

A aplicação abrirá em `http://localhost:8501`

## Regras do Projeto

- ✅ Código simples
- ✅ Priorizar funcionamento
- ✅ Uma funcionalidade por vez
- ✅ Manter arquivos organizados

## Próximas Tarefas

- [x] Implementar Quiz de Perfil
- [x] Implementar Roadmap de estudos
- [ ] Adicionar interface visual melhorada
- [ ] Implementar sistema de recomendações

