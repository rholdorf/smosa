---
name: csaaf-assess
description: >
  Avalia a maturidade arquitetural de um repositório (ou coleção de
  repositórios) nos 9 pilares do SMoSA, atribuindo notas 0-5 fundamentadas em
  evidências, e produz radar(es) + relatório com conflitos, intervenções e
  plano de mudança. Modo BROWNFIELD (lê código real). Use quando o usuário
  quer avaliar, auditar ou comparar a arquitetura de repositórios existentes.
---

# CSAAF Assessment — Brownfield

Operacionaliza a linha "Measurement and Evaluation" do SMoSA: uma avaliação
baseada em evidências, no espírito de ATAM/SAAM.

## Pilares (9)
strategic-principles · quality-attributes · architectural-styles ·
architectural-patterns · cloud-distributed · data-architecture ·
security-practices · **agile-devops** · modeling-docs

> Os 9 pilares estão implementados. Cada agente segue o mesmo contrato de
> saída (JSON com `score` + `evidence`); ver `smosa/model.yaml` e as rubricas.

## Fluxo

1. **Fase 0 — Discovery (obrigatória).** Antes de pontuar, invoque o agente
   `csaaf-discovery` sobre o(s) caminho(s). Ele é **read-only** e stack-agnóstico
   (detecta .NET/Python/Node/…) e devolve o **mapa do sistema**: forma do alvo
   (repo único · multi-repo que forma UM sistema · portfólio), inventário
   pretendido, topologia declarada, classificação por arquétipo, **completude**
   (o que é esperado vs. o que está fisicamente presente) e os **caveats de
   ausência falsa**. Esse mapa vira o **contexto compartilhado** das fases
   seguintes e decide o **escopo** (avaliar como um sistema ou por repo).
2. **Avaliação (fan-out).** Para cada um dos 9 pilares, invoque o agente
   avaliador correspondente (ex.: `csaaf-security-practices`), **passando o mapa
   da Fase 0** no prompt. Rode os pilares em paralelo. Cada agente devolve o JSON
   estruturado com `score` + `evidence`.
   - Multi-repo que forma um sistema: avalie o conjunto como UM alvo (as costuras
     — orquestrador, filas, libs compartilhadas — são evidência de primeira classe).
   - Portfólio: repita por repositório; guarde os resultados por repo.
   - **Ausência falsa:** trate como "não avaliado", nunca como nota baixa, tudo
     que o mapa marcou como não-materializado/não-clonado (ver caveats da Fase 0).
3. **(Recomendado) Verificação adversarial.** Invoque o agente `csaaf-verify`
   (um cético por pilar) para notas de baixa confiança ou alto impacto — e no
   outlier mais alto. Ele re-abre as evidências e tenta REFUTAR a nota nos dois
   sentidos. Aplique o veredito: rebaixe se a evidência não sustentar, suba a
   confiança se sustentar. _Comprovadamente valioso: num sistema real corrigiu
   ~0,3 ponto de otimismo e pegou uma nota inflada que o 1º passe deixou passar._
4. **Radares.** Invoque a skill `csaaf-radar` com o vetor de notas (um radar
   por repo + um radar sobreposto/agregado se houver vários).
5. **Relatório.** Preencha `smosa/report-template.md` com: tabela de notas,
   evidências por pilar, conflitos arquiteturais, propostas de intervenção
   priorizadas (esforço × impacto) e plano de mudança (roadmap por ondas). Saída
   para `reports/` (privado/gitignored).

## Regras de ouro
- **Evidência obrigatória.** Nenhuma nota sem `path:linha` ou ausência provada.
- **0 = N/A**, não "ruim". Distinga "não aplicável" de "nível 1 (iniciante)".
- **Não inflar.** O alicerce de cada pilar trava o teto (ver `scoring_guidance`).
- **Ausência ≠ não-baixado.** Só registre "ausência provada" quando o mapa da
  Fase 0 confirmar que o código está presente e mesmo assim o sinal não existe.
  Código não clonado/não materializado é "não avaliado", nunca nota baixa.
- **Reprodutível.** Registre a data da avaliação; notas são um retrato temporal.
