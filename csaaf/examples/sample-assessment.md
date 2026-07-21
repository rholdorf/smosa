# CSAAF Assessment Report — Helios Commerce Platform

> **Documento de exemplo.** Sistema e evidências **fictícios**, criados para
> ilustrar a saída da coleção `csaaf`. Nenhum `arquivo:linha` abaixo
> aponta para código real — servem apenas para demonstrar o *formato* de uma
> avaliação fundamentada em evidências.

- **Data da avaliação:** 2026-07-20
- **Modo:** Brownfield (leitura de código real)
- **Pilares avaliados:** 9/9
- **Média geral:** **3,1 / 5 — Intermediário**

**Alvo (fictício):** *Helios Commerce Platform* — plataforma SaaS B2B de
e-commerce. Microserviços poliglotas (`catalog-service` e `orders-service` em
Go, `storefront-bff` em Node/TypeScript), mensageria **Kafka** (event-driven),
**PostgreSQL** por serviço + **Redis** para cache, deploy em **AWS EKS** via
**Terraform**, pipeline em **GitHub Actions**, observabilidade com
**OpenTelemetry + Prometheus/Grafana**.

---

## 1. Placar (radar)

Escala: `0` N/A · `1` Iniciante · `2` Básico · `3` Intermediário · `4` Avançado · `5` Excelência.

```
Estilos Arquiteturais    ████████░░  4  Avançado
Qualidade & Técnicas     ████████░░  4  Avançado
Nuvem & Distribuída      ████████░░  4  Avançado
Ágil & DevOps            ████████░░  4  Avançado
Princípios Estratégicos  ██████░░░░  3  Intermediário
Padrões Arquiteturais    ██████░░░░  3  Intermediário
Arquitetura de Dados     ██████░░░░  3  Intermediário
Segurança                ████░░░░░░  2  Básico
Modelagem & Doc.         ██░░░░░░░░  1  Iniciante
```

| Pilar | Nota (0-5) | Confiança |
|------|:----------:|:---------:|
| Architectural Styles | 4 | alta |
| Quality Attributes and Techniques | 4 | alta |
| Cloud and Distributed Architecture | 4 | alta |
| Agile and DevOps Practices | 4 | alta |
| Strategic Principles and Decisions | 3 | média |
| Architectural Patterns | 3 | alta |
| Data Architecture | 3 | média |
| Security Practices | 2 | média |
| Modeling and Documentation | 1 | alta |

> Um radar visual interativo (SVG, tema claro/escuro, multi-repo) é gerado pela
> skill [`csaaf-radar`](../skills/csaaf-radar/SKILL.md) como artefato HTML. As
> barras acima são a versão portável para GitHub.

---

## 2. Evidências por pilar

### Architectural Styles — 4 (confiança alta)
Microserviços com fronteiras claras por domínio, um **BFF** dedicado ao
storefront e comunicação **event-driven** via Kafka. Falta apenas descoberta de
serviço explícita (resolvida por DNS do k8s) para tender a 5.

- `deploy/k8s/catalog-service.yaml:1-40` — serviço isolado, deploy próprio (microserviço).
- `services/storefront-bff/src/gateway.ts:12-88` — BFF agrega catalog + pricing para o front.
- `services/orders-service/internal/events/publisher.go:23-51` — publica `OrderPlaced` em tópico Kafka (EDA).
- **Ausência:** nenhum registro/descoberta de serviço além de DNS do cluster.

### Quality Attributes and Techniques — 4 (confiança alta)
Resiliência e observabilidade de primeira classe: retries com backoff, health
probes, tracing distribuído. Sem autoscaling comprovado, o que trava o 5.

- `services/orders-service/internal/http/middleware/retry.go:14-46` — retry com backoff exponencial.
- `deploy/k8s/orders-service.yaml:52-71` — `livenessProbe` e `readinessProbe` configurados.
- `services/catalog-service/internal/telemetry/otel.go:9-63` — spans OpenTelemetry exportados.
- **Ausência:** nenhum `HorizontalPodAutoscaler` em `deploy/k8s/`.

### Cloud and Distributed Architecture — 4 (confiança alta)
Infra declarativa (Terraform), cluster gerenciado EKS, mensageria e persistência
poliglota. Consistência eventual assumida no fluxo de pedidos.

- `infra/terraform/eks.tf:1-120` — cluster EKS versionado como código.
- `infra/terraform/msk.tf:1-58` — broker Kafka gerenciado (AWS MSK).
- `services/orders-service/internal/saga/checkout.go:30-140` — coordenação distribuída de checkout.
- **Ausência:** sem estratégia multi-região; RTO/RPO não documentados.

### Agile and DevOps Practices — 4 (confiança alta)
CI/CD automatizado, IaC, versionamento de imagens. Falta *progressive delivery*
(canário/blue-green) e métricas DORA para chegar a 5.

- `.github/workflows/ci.yml:1-96` — build, testes e push de imagem por serviço.
- `infra/terraform/` — infraestrutura como código (Terraform).
- `.github/workflows/release.yml:20-44` — tag semântica gera imagem imutável.
- **Ausência:** deploy de produção descrito como `kubectl apply` manual (ver §3).

### Strategic Principles and Decisions — 3 (confiança média)
Camadas bem separadas e fronteiras por domínio, mas modelos majoritariamente
anêmicos e sem DDD tático ou ADRs que registrem o *porquê* das decisões.

- `services/orders-service/internal/{domain,app,infra}/` — separação de camadas clara.
- `services/catalog-service/internal/domain/product.go:8-24` — struct anêmica (só getters/setters).
- **Ausência:** nenhum diretório `docs/adr/` nem agregados/invariantes de domínio.

### Architectural Patterns — 3 (confiança alta)
Circuit breaker e Saga presentes e corretos, mas **sem CQRS/Event Sourcing** —
leitura e escrita compartilham o mesmo modelo relacional.

- `services/storefront-bff/src/resilience/breaker.ts:5-40` — circuit breaker no BFF.
- `services/orders-service/internal/saga/checkout.go:30-140` — Saga de checkout orquestrada.
- **Ausência:** `grep -ri "commandhandler\|queryhandler" services/` → 0 resultados (sem CQRS).

### Data Architecture — 3 (confiança média)
Persistência poliglota, índices e migrations versionadas. Sem trilha analítica
(warehouse/lake), CDC ou governança de dados.

- `services/catalog-service/migrations/0007_add_gin_index.sql:1-6` — índice deliberado.
- `services/orders-service/migrations/` — migrations versionadas e sequenciais.
- **Ausência:** nenhum pipeline ETL/streaming analítico; sem catálogo/lineage de dados.

### Security Practices — 2 (confiança média)
Validação de entrada e emissão de JWT presentes, mas a **verificação** de
autorização não aparece no código dos serviços e há segredo versionado — higiene
que trava em 2.

- `services/storefront-bff/src/auth/token.ts:10-38` — emite JWT no login.
- `services/catalog-service/config/appsettings.staging.json:14` — connection string com senha **versionada** (higiene).
- **Ausência:** middleware de authz (equivalente a `[Authorize]`) não encontrado nos serviços downstream.
- **Incerteza:** a verificação de token pode viver no gateway de borda (Envoy) fora deste repo — a nota sobe se confirmada.

### Modeling and Documentation — 1 (confiança alta)
Documentação mínima: um README raiz genérico e nenhum diagrama, ADR ou contrato
de API publicado. Novos integrantes dependem de leitura de código.

- `README.md:1-30` — visão geral de uma página, sem diagramas.
- **Ausência:** sem `docs/`, sem C4/UML, sem ADRs, sem spec OpenAPI publicada.

---

## 3. Conflitos arquiteturais

1. **EDA declarada, integração síncrona na prática.** `orders-service` publica
   `OrderPlaced` em Kafka (`publisher.go:23`), mas `notifications-worker` faz
   *polling* REST no orders-service (`poller.go:18`) em vez de assinar o tópico —
   acoplamento que a arquitetura event-driven pretendia eliminar.
2. **CI automatizado × deploy manual.** O pipeline testa e publica imagens
   (`ci.yml`), porém a promoção para produção é um `kubectl apply` manual
   documentado no README — quebra a cadeia de entrega contínua e a rastreabilidade.
3. **Resiliência desigual.** `orders-service` tem retry+breaker; `catalog-service`
   chama o `pricing-service` sem timeout nem breaker (`client.go:22`), criando um
   ponto de falha em cascata sob latência.

---

## 4. Propostas de intervenção (priorizadas)

| Intervenção | Pilar | Esforço | Impacto | Sobe para nível |
|-------------|-------|:-------:|:-------:|:---------------:|
| Externalizar segredos (AWS Secrets Manager) e remover senha versionada | Security | S | alto | 3 |
| Adicionar middleware de authz nos serviços (ou confirmar no gateway) | Security | M | alto | 3 |
| Publicar ADRs + diagrama C4 nível 2 dos serviços | Modeling & Doc. | S | alto | 3 |
| Fazer `notifications-worker` assinar o tópico Kafka (remover polling) | Styles / Patterns | M | médio | — |
| Adicionar HPA e testar sob carga | Quality Attributes | M | médio | 5 |
| Progressive delivery (canário) + coleta de métricas DORA | Agile & DevOps | L | médio | 5 |

---

## 5. Plano de mudança (roadmap)

Ondas priorizadas por impacto × esforço — o alicerce (segurança e documentação)
antes das melhorias avançadas.

- **Onda 1 (fundamentos):** externalizar segredos; confirmar/adicionar
  autorização; publicar ADRs + um C4 mínimo. *Sobe Segurança 2→3 e Modelagem 1→3.*
- **Onda 2 (consolidação):** eliminar o polling do worker (voltar a EDA pura);
  padronizar timeout+breaker em todas as chamadas entre serviços; automatizar o
  deploy de produção. *Fecha os três conflitos.*
- **Onda 3 (excelência):** HPA + teste de carga; progressive delivery com
  métricas DORA; iniciar trilha analítica de dados (CDC → warehouse).

---

_Notas são um retrato temporal, ancorado em evidências. Reavaliar após cada onda._
_Gerado pela coleção [`csaaf`](../README.md) — operacionaliza a linha
"Measurement and Evaluation" do SMoSA (ATAM/SAAM)._
