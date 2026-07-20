# SMoSA Assessment Report — {{repo}}

- **Data da avaliação:** {{date}}
- **Modo:** Brownfield
- **Pilares avaliados:** {{n_evaluated}}/9

## 1. Placar (radar)

![radar]({{radar_link}})

| Pilar | Nota (0-5) | Confiança |
|------|:----------:|:---------:|
{{score_table}}

## 2. Evidências por pilar

Para cada pilar: nota, justificativa e evidências (`arquivo:linha`) que a sustentam.

{{evidence_sections}}

## 3. Conflitos arquiteturais

Contradições observadas entre decisões/práticas (ex.: CI em staging mas deploy
manual em produção; microserviços sem service discovery).

{{conflicts}}

## 4. Propostas de intervenção (priorizadas)

| Intervenção | Pilar | Esforço | Impacto | Sobe para nível |
|-------------|-------|:-------:|:-------:|:---------------:|
{{interventions_table}}

## 5. Plano de mudança (roadmap)

Ondas priorizadas por impacto × esforço, com o alicerce antes das melhorias avançadas.

- **Onda 1 (fundamentos):** {{wave1}}
- **Onda 2 (consolidação):** {{wave2}}
- **Onda 3 (excelência):** {{wave3}}

---
_Notas são um retrato temporal, ancorado em evidências. Reavaliar após cada onda._
