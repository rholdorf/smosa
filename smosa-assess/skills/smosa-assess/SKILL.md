---
name: smosa-assess
description: >
  Avalia a maturidade arquitetural de um repositório (ou coleção de
  repositórios) nos 9 pilares do SMoSA, atribuindo notas 0-5 fundamentadas em
  evidências, e produz radar(es) + relatório com conflitos, intervenções e
  plano de mudança. Modo BROWNFIELD (lê código real). Use quando o usuário
  quer avaliar, auditar ou comparar a arquitetura de repositórios existentes.
---

# SMoSA Assessment — Brownfield

Operacionaliza a linha "Measurement and Evaluation" do SMoSA: uma avaliação
baseada em evidências, no espírito de ATAM/SAAM.

## Pilares (9)
strategic-principles · quality-attributes · architectural-styles ·
architectural-patterns · cloud-distributed · data-architecture ·
security-practices · **agile-devops** · modeling-docs

> Estado atual (fatia vertical): apenas **agile-devops** implementado. Os
> demais agentes seguem o mesmo contrato assim que suas rubricas existirem.

## Fluxo

1. **Descoberta.** Receba 1..N caminhos de repositório. Para cada um, mapeie a
   estrutura de topo e detecte o tipo de artefato.
2. **Avaliação (fan-out).** Para cada pilar com rubrica `implemented`, invoque
   o agente avaliador correspondente (ex.: `smosa-agile-devops`) sobre o repo.
   Rode os pilares em paralelo. Cada agente devolve o JSON estruturado com
   `score` + `evidence` (ver `smosa/model.yaml` e as rubricas).
   - Multi-repo: repita por repositório; guarde os resultados por repo.
3. **(Opcional, recomendado) Verificação adversarial.** Para notas de baixa
   confiança ou alto impacto, rode um segundo passe que tenta REFUTAR a nota
   relendo as evidências. Rebaixe se a evidência não sustentar.
4. **Radares.** Invoque a skill `smosa-radar` com o vetor de notas (um radar
   por repo + um radar sobreposto/agregado se houver vários).
5. **Relatório.** Preencha `smosa/report-template.md` com: tabela de notas,
   evidências por pilar, conflitos arquiteturais, propostas de intervenção
   priorizadas (esforço × impacto) e plano de mudança (roadmap por ondas).

## Regras de ouro
- **Evidência obrigatória.** Nenhuma nota sem `path:linha` ou ausência provada.
- **0 = N/A**, não "ruim". Distinga "não aplicável" de "nível 1 (iniciante)".
- **Não inflar.** O alicerce de cada pilar trava o teto (ver `scoring_guidance`).
- **Reprodutível.** Registre a data da avaliação; notas são um retrato temporal.
