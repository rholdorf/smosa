---
name: csaaf-radar
description: >
  Gera diagrama(s) de radar a partir do vetor de notas 0-5 dos 9 pilares do
  SMoSA. Um radar por repositório, e um radar sobreposto para comparar vários
  repositórios (portfólio). Use ao final de uma avaliação csaaf-assess.
---

# CSAAF Radar

## Entrada
Um array de resultados, um por repositório:
```json
[
  {"repo": "nome", "date": "YYYY-MM-DD",
   "scores": {"strategic-principles": 3, "quality-attributes": 2, "architectural-styles": 4,
              "architectural-patterns": 3, "cloud-distributed": 2, "data-architecture": 1,
              "security-practices": 3, "agile-devops": 4, "modeling-docs": 2}}
]
```
Pilares ainda não avaliados: use `null` (renderizados como eixo tracejado "não avaliado").

## Saída
Um **artefato HTML autocontido** (ferramenta Artifact). Restrições:
- **CSP bloqueia hosts externos** — proibido Chart.js/D3 via CDN. Desenhe o
  radar com **SVG inline + JS vanilla** (sem libs externas).
- Escala radial fixa **0..5** com anéis rotulados; cores dos pilares vindas de
  `smosa/model.yaml`.
- Multi-repo: sobreponha os polígonos (um por repo) com legenda; ofereça também
  "small multiples" (um radar por repo) se forem muitos.
- Tema claro/escuro via `prefers-color-scheme`.
- Cada vértice mostra o rótulo do pilar e a nota; tooltip com a justificativa.

## Passos
1. Normalize as notas para o intervalo 0..5 (clamp).
2. Gere os 9 eixos igualmente espaçados (ângulo = i * 2π/9), raio = nota/5.
3. Escreva o HTML em disco e publique com Artifact (favicon 📡, título estável).

## Encoding (OBRIGATÓRIO — evita mojibake windows-1252 × UTF-8)
O visualizador pode servir a página sem declarar charset; então acentos quebram.
Blinde SEMPRE:
- **Primeira linha do arquivo**: `<meta charset="utf-8">`.
- **Conteúdo à prova de charset**: prefira saída ASCII-only — caracteres
  acentuados como entidades `&#nnn;` no HTML e `\uXXXX` nas strings JS. Assim
  renderiza correto independentemente do charset assumido.
- Pós-processador de referência (ASCII-escape HTML vs JS separadamente):
  `csaaf/tools/ascii_safe.py <arquivo.html>` — deve reportar
  `residual non-ASCII = 0` antes de publicar.
