-- Tabela de usuários
CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome_usuario VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    criado_em TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de resultados de quiz
CREATE TABLE resultados_quiz (
    id_quiz SERIAL PRIMARY KEY,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    categoria VARCHAR(100),
    pontuacao INTEGER,
    concluido_em TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de progresso do roadmap
CREATE TABLE progresso_roadmap (
    id_roadmap SERIAL PRIMARY KEY,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    topico VARCHAR(200),
    status VARCHAR(20) DEFAULT 'pendente' CHECK (status IN ('pendente', 'em_andamento', 'concluido')),
    iniciado_em TIMESTAMPTZ,
    concluido_em TIMESTAMPTZ,
    criado_em TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Índices para melhor performance (Apenas os que não são criados automaticamente)
CREATE INDEX idx_resultados_quiz_usuario_id ON resultados_quiz(usuario_id);
CREATE INDEX idx_progresso_roadmap_usuario_id ON progresso_roadmap(usuario_id);
