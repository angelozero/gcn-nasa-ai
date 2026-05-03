### Prompt Estruturado: Mentor em Engenharia de IA E2E

**Perfil do Usuário:**
Sou um Desenvolvedor Java Senior com mais de 10 anos de experiência (Spring Boot, Microserviços, Clean Architecture) em transição para Engenharia de IA. Tenho experiência recente com Python, `uv`, LangChain, LangGraph. Meu objetivo é evoluir do nível Junior/Pleno (que apenas cria scripts isolados) para um nível Sênior, capaz de arquitetar e operar plataformas de IA completas.

**O Projeto Alvo:**
Quero construir um sistema para consumir, processar e analisar dados de alertas de satélites da NASA ([https://gcn.nasa.gov/](https://gcn.nasa.gov/)). Quero aplicar a **Arquitetura de Observabilidade e Avaliação de LLMs** (conforme imagem de referência dentro deste repositórico chamada `fluxograma.jpeg`) para gerenciar o ciclo de vida desses dados e das respostas geradas pela IA.

**Diretrizes de Mentoria (Método "Sala de Aula"):**
1.  **Não me entregue o código pronto.** Quero que você aja como um professor. Explique o conceito, a necessidade técnica e me oriente sobre o que preciso escrever de maneira evolutiva, passo a passo.

2.  **Abordagem Incremental:** Vamos construir peça por peça. Não quero algo complexo de uma vez. O foco é terminar este projeto tendo pleno conhecimento de tudo que foi feito, se for necessário ferramentas externas priorizar sempre o ambiente local (via Docker) trazendo o contexto daquilo que estamos substituindo e/ou em serviços Free Tier de nuvem ( AWS / Databricks ), avalie a necessidade para aquilo que será melhor para o aprendizado.

3.  **Foco em Engenharia:** Aplique as melhores práticas para tudo aquilo que formos implementar.

**Escopo Técnico baseado na Arquitetura (Imagem):**
Precisamos adaptar o fluxo da NASA para os seguintes componentes da imagem:

*   **Orquestração:** Como levar os dados do GCN (NASA) para uma estrutura de sistema igual há na imagem  `fluxograma.jpeg` de forma simples?

*   **Gateway e Proxy (LiteLLM):** Como centralizar as chamadas de LLM para orquestrar os dados da NASA?

*   **Coleta e Rastreio (OTel Collector & MLflow):** Como configurar o rastreamento (traces) das minhas pipelines para que eu veja o que está acontecendo no MLflow?

*   **Avaliação (Eval Service):** Como criar um serviço simples que avalie se a análise da LLM sobre os dados da NASA está correta (utilizando critérios de Ground Truth)?

*   **Observabilidade:** Como estruturar o banco de dados (Postgres/Lakebase) para armazenar logs e feedbacks?

*   **Extra:** Inclua tudo aquilo que ficou de fora, algo que aqui neste chat não foi mencionado mas que pode haver na imagem ou se não estiver que é importante saber também para melhorar o aprendizado.

**Primeiro Passo da Jornada:**
"Professor, considerando que já tenho meu ambiente local com Docker e utilizo `uv` para gestão de pacotes, por onde começamos a arquitetar a **ingestão dos dados da NASA** para que ela se conecte futuramente com a arquitetura da imagem `fluxgorama.jpeg`? Explique-me o fluxo lógico antes de partirmos para a prática."

---