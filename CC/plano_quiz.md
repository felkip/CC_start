# Plano do Quiz de Perfil

## Objetivo
Criar uma versão simples do quiz de perfil para identificar a afinidade do usuário com Ciência da Computação e oferecer uma primeira orientação de estudo.

## Escopo inicial (MVP)
- Mostrar um quiz com 5 perguntas simples.
- Cada pergunta terá 3 opções de resposta.
- A resposta escolhida adiciona pontos a um perfil de afinidade.
- No final, exibir um resultado simples, como:
  - Mais próximo de programação
  - Curioso sobre tecnologia
  - Ainda está começando

## Fluxo da tela
1. O usuário entra na aplicação.
2. Clica em "Quiz de Perfil".
3. Responde às perguntas uma por uma.
4. Recebe um resultado resumido.
5. Pode continuar para um roadmap inicial ou voltar ao início.

## Estrutura proposta
- Criar uma tela simples no Streamlit.
- Guardar as perguntas em uma lista no código.
- Calcular pontuação com base nas respostas.
- Exibir o resultado final de forma clara.

## Perguntas iniciais sugeridas
- Você gosta de resolver problemas lógicos?
- Já tentou aprender programação antes?
- Gosta de mexer com tecnologia e aplicativos?
- Prefere aprender com exemplos práticos ou teoria?
- Você acha interessante criar soluções do zero?

## Lógica do resultado
- Cada resposta soma pontos para uma categoria.
- Ao final, a categoria com maior pontuação define o perfil.
- O resultado pode ser mostrado em uma mensagem simples e amigável.

## Próximos passos
1. Criar a interface do quiz no Streamlit.
2. Definir as perguntas e as opções.
3. Implementar a lógica de pontuação.
4. Exibir o resultado final.
5. Depois, conectar o resultado a uma sugestão de roadmap.

## Observação
A ideia é começar simples, com algo funcional e fácil de testar antes de evoluir para uma versão mais completa.
