# SMoSA Assessment (`smosa-assess`)

Uma coleção de **skills + subagents do [Claude Code](https://claude.com/claude-code)**
que transforma o **[SMoSA](../README.md)** (Subway Map of Software Architecture)
num avaliador de arquitetura acionável.

Aponte-a para um ou mais repositórios e ela atribui uma **nota 0–5 por pilar**,
**fundamentada em evidências** (`arquivo:linha` ou ausência comprovada), e produz
um **radar** + **relatório** com conflitos, intervenções priorizadas e um plano
de mudança em ondas.

Isto **operacionaliza a 10ª linha do SMoSA** — *Measurement and Evaluation*
(ATAM/SAAM). Essa linha não é um pilar avaliado: é o **motor**. Os **9 pilares
avaliados** são as outras 9 linhas do mapa.

📄 **Veja uma saída de exemplo:** [`examples/sample-assessment.md`](examples/sample-assessment.md)
(sistema e dados fictícios).

---

## O modelo

Cada pilar recebe uma nota nesta escala:

| Nota | Nível |
|:----:|-------|
| **0** | Não aplicável (o artefato não tem superfície para o pilar) |
| **1** | Iniciante |
| **2** | Básico |
| **3** | Intermediário |
| **4** | Avançado |
| **5** | Excelência |

**Regras de ouro** (herdadas do método):

- **Evidência obrigatória.** Nenhuma nota sem `caminho:linha` ou ausência provada.
- **`0` = N/A, não "ruim".** Distinga "não aplicável" de "nível 1".
- **Capacidade ≠ uso.** Uma lib referenciada não conta como praticada até haver
  uma chamada real.
- **O alicerce trava o teto.** Um sinal isolado avançado não infla a nota se o
  fundamento do pilar não existe.
- **Reprodutível.** Toda nota carrega a data — é um retrato temporal.

Os **9 pilares** (= linhas do SMoSA):

`strategic-principles` · `quality-attributes` · `architectural-styles` ·
`architectural-patterns` · `cloud-distributed` · `data-architecture` ·
`security-practices` · `agile-devops` · `modeling-docs`

A fonte da verdade é [`smosa/model.yaml`](smosa/model.yaml); cada pilar tem uma
rubrica 0–5 com dimensões e sinais de evidência em [`smosa/rubric/`](smosa/rubric/).

---

## Estrutura

```
smosa-assess/
├─ smosa/
│  ├─ model.yaml              # 9 pilares + o motor (fonte da verdade)
│  ├─ rubric/*.yaml           # 9 rubricas 0–5 (dimensões + sinais de evidência)
│  └─ report-template.md      # esqueleto do relatório final
├─ agents/smosa-<pilar>.md    # 9 subagents avaliadores (1 por pilar) → saída JSON
├─ skills/
│  ├─ smosa-assess/SKILL.md   # orquestrador brownfield (fan-out dos 9 pilares)
│  └─ smosa-radar/SKILL.md    # gera o radar (SVG inline, HTML autocontido)
├─ tools/ascii_safe.py        # blindagem UTF-8 dos artefatos HTML
├─ examples/                  # radar POC + relatório de exemplo
└─ reports/                   # saídas geradas — área PRIVADA (gitignored, ver abaixo)
```

> **`reports/` é privado.** Avaliações de repositórios reais (evidências,
> citações `arquivo:linha`, achados) não devem ir para o remote. Todo conteúdo
> de `reports/` é ignorado pelo Git ([`.gitignore`](.gitignore)); só a pasta é
> versionada (via `.gitkeep`). Direcione as saídas para lá.

---

## Pré-requisitos

- **Claude Code** (CLI, app ou extensão de IDE) — as skills e agents rodam nele.
- **Python 3** — apenas para `tools/ascii_safe.py` (pós-processa o radar HTML).
- **Git** — para clonar esta coleção e apontar para os repositórios-alvo.

---

## Instalação

As skills e agents são arquivos Markdown que o Claude Code descobre em
`.claude/skills/` e `.claude/agents/`. A coleção precisa manter a pasta
`smosa/` (rubricas) e `tools/` junto, porque as skills as leem por caminho.

**1. Clone o repositório** (que contém esta coleção em `smosa-assess/`):

```bash
git clone https://github.com/<user>/smosa.git
cd smosa/smosa-assess
```

**2. Registre skills e agents no Claude Code.** Escolha o escopo:

*Escopo de projeto* — disponível apenas dentro deste repositório (recomendado):

```bash
# a partir de smosa-assess/
mkdir -p .claude
ln -s "$PWD/skills" .claude/skills
ln -s "$PWD/agents" .claude/agents
```

*Escopo pessoal* — disponível em qualquer sessão do Claude Code:

```bash
# a partir de smosa-assess/
ln -s "$PWD"/skills/*  ~/.claude/skills/
ln -s "$PWD"/agents/*  ~/.claude/agents/
```

> **Nota sobre caminhos.** As skills referenciam as rubricas por caminho relativo
> à coleção (`smosa/rubric/<pilar>.yaml`). Rode o Claude Code a partir de
> `smosa-assess/`, ou informe o caminho absoluto da coleção ao invocar — assim os
> agentes localizam as rubricas.

**3. Confirme** que as skills aparecem: numa sessão do Claude Code, digite `/` e
procure por `smosa-assess` e `smosa-radar`.

---

## Como executar (modo brownfield)

**1. Avalie um repositório.** Numa sessão do Claude Code, invoque a skill
passando o caminho do alvo:

```
/smosa-assess  /caminho/para/o/repo-alvo
```

O orquestrador faz **fan-out dos 9 pilares** (um subagent por pilar, em
paralelo). Cada agente lê sua rubrica, coleta evidências com Grep/Glob/Read e
devolve um JSON estruturado com `score`, `confidence`, `evidence`, `absence`,
`gaps`, `conflicts` e `interventions`.

**2. (Recomendado) Verificação adversarial.** Para notas de baixa confiança ou
alto impacto, peça um segundo passe que **tente refutar** cada nota relendo as
evidências. Rebaixa se a evidência não sustentar; sobe a confiança se sustentar.

**3. Gere o radar.**

```
/smosa-radar
```

Produz um **HTML autocontido** (SVG inline, sem libs externas, tema claro/escuro)
publicado como Artifact. Para **portfólio**, passe várias notas e os polígonos
são sobrepostos (um por repo).

**4. Relatório.** O orquestrador preenche
[`smosa/report-template.md`](smosa/report-template.md): tabela de notas,
evidências por pilar, conflitos, intervenções (esforço × impacto) e roadmap.
Veja o formato final em [`examples/sample-assessment.md`](examples/sample-assessment.md).

### Multi-repo (portfólio)

Passe vários caminhos. Cada repo é avaliado isoladamente; o radar sobreposto
compara a maturidade lado a lado — útil para priorizar investimento entre
serviços de um mesmo ecossistema.

---

## Encoding dos artefatos HTML (obrigatório)

O visualizador de Artifact pode servir a página **sem declarar charset**, o que
quebra acentos (mojibake windows-1252 × UTF-8). Todo HTML publicado é blindado:

- `<meta charset="utf-8">` na **primeira linha**, **e**
- conteúdo **ASCII-safe** — acentos como `&#nnn;` no HTML e `\uXXXX` nas strings JS.

Antes de publicar qualquer radar/relatório HTML, rode o pós-processador — ele
deve reportar `residual non-ASCII = 0`:

```bash
python3 tools/ascii_safe.py reports/meu-relatorio.html
```

> Documentos **Markdown** (como o relatório de exemplo) **não** precisam disso —
> o GitHub serve `.md` em UTF-8 corretamente. A regra vale só para HTML de Artifact.

---

## Estado e roadmap

- ✅ **Brownfield** ponta-a-ponta: 9 rubricas, 9 agentes, orquestrador e radar.
- ⏳ **Verificação adversarial** — prevista no orquestrador; a acionar por avaliação.
- ⏳ **Greenfield** — sessão de Q&A tipo *grill* que reusa as rubricas como
  bússola para gerar insumos iniciais (ADRs, stack, backlog). *Ainda não construído.*
- ⏳ **Pilar de IA/ML** — o `model.yaml` já aceita uma 10ª rubrica (arquitetura
  *de* sistemas de IA e *assistida* por IA).

---

_Parte do projeto [SMoSA](../README.md) · Silveira Neto, Malucelli & Reinehr,
ICEIS 2026._
