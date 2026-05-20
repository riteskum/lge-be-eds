# AEM Edge Delivery Services Migration Estimate
## Samsung Semiconductor & LED Division

---

**Prepared by:** Adobe Professional Services  
**Date:** May 2026  
**Version:** 2.0 (Revised — Block Library Reuse Optimization)  
**Classification:** Confidential

---

## 1. Executive Summary

Samsung Electronics' Semiconductor Division has requested a migration from their current **AEM On-Premise** instance to **AEM Edge Delivery Services (EDS)** — Adobe's modern, high-performance content delivery platform. This estimate covers two websites currently hosted on the same AEM instance:

- **semiconductor.samsung.com** — Primary semiconductor business website
- **led.samsung.com** — LED product division website

### Revision Notes (v2.0)

This revised estimate incorporates two key adjustments from v1.0:

1. **Block Library Reuse Optimization** — Leverages AEM Block Collection, Block Party, and EDS Boilerplate to reduce custom development by 35%. Blocks are tiered into Reuse (style-only), Extend (customize), and Custom (new build).

2. **DAM-Informed Asset Migration** — Based on actual AEM disk usage report showing **229.17 GB** across **1,692,306 nodes**, asset migration effort has been recalculated with phased approach.

---

## 2. DAM Repository Analysis

The AEM On-Premise instance contains a significant Digital Asset Management repository:

| DAM Path | Size | Nodes | Properties |
|----------|------|-------|------------|
| /content/dam/samsung | 224.62 GB | 1,626,711 | 8,469,557 |
| /content/dam/test | 4.55 GB | 65,295 | 345,206 |
| /content/dam/_CSS | 458 KB | 109 | 333 |
| /content/dam/formsanddocuments | 1,266 bytes | 26 | 88 |
| /content/dam/collections | 3,427 bytes | 62 | 183 |
| **TOTAL** | **229.17 GB** | **1,692,306** | **8,815,757** |

### Key Observations:
- **98% of DAM** is in the `/samsung` folder (224.62 GB) — primary migration target
- The `/test` folder (4.55 GB) likely contains staging/QA assets — may not require migration
- Node count (1.69M) suggests extensive rendition/metadata overhead — actual unique assets likely 200K-400K
- **DAM audit in Phase 1 is critical** to identify active vs. archival content and avoid migrating unused assets

---

## 3. Current State Assessment

### semiconductor.samsung.com

| Attribute | Details |
|-----------|---------|
| **Content Volume** | 350-500+ pages across 12 product categories |
| **DAM Assets** | 224.62 GB / 1,626,711 nodes |
| **Page Templates** | 7-9 unique templates (PLP, PDP, Blog, Corporate, Foundry, etc.) |
| **Languages** | 4 locales (English, Korean, Chinese, Japanese) |
| **Key Features** | Mega navigation, product spec tables, video embeds, multi-step forms, FAQ accordions, tech blog, event listings, search with suggestions |
| **Integrations** | Search engine, analytics, form backends, CDN, B2B portal link |
| **Complexity** | HIGH — Enterprise-grade with extensive product taxonomy and interactive components |

### led.samsung.com

| Attribute | Details |
|-----------|---------|
| **Content Volume** | 50-80+ pages across 5 product categories |
| **DAM Assets** | Subset of samsung folder (shared DAM) |
| **Page Templates** | 3-4 additional unique templates |
| **Regions** | 6 regional variants (Americas, EMEA, China, SE Asia, Japan, Korea) |
| **Key Features** | LED/Engine calculators, product comparison, virtual exhibition, datasheet downloads, regional sales network |
| **Integrations** | Calculator tools, regional contact systems, download management |
| **Complexity** | MEDIUM-HIGH — Specialized calculator tools add significant custom development |

---

## 4. Block Reuse Strategy

The key optimization in this revised estimate leverages Adobe's existing EDS ecosystem:

### Block Development Tiers

| Tier | Description | Effort/Block | Blocks (Semi) | Blocks (LED) |
|------|-------------|-------------|---------------|--------------|
| **REUSE** | Block exists in AEM library; only brand CSS needed | 2-3 days | 10 | 3 |
| **EXTEND** | Library foundation + JS/logic modifications | 4-6 days | 8 | 3 |
| **CUSTOM** | No library equivalent; full build required | 8-12 days | 6 | 4 |

### Reuse Tier (Style Only — from AEM Block Collection/Boilerplate)
Hero, Cards, Carousel, Tabs, Accordion, Video Embed, Breadcrumb, CTA, Columns, Image Gallery

### Extend Tier (Library + Customization)
FAQ (+ schema), Contact Form (+ multi-step), News Listing (+ filters), Event Listing, Downloads, Related Content, Statistics, Cookie Consent

### Custom Tier (Full Development — No Library Equivalent)
Product Specs Table, Regional Contact Tabs, Application Showcase, Foundry Services, Partner Ecosystem, Sustainability Highlights, LED Calculators (x2), LED Configurator, Virtual Exhibition

### Impact on Estimates
- **Block Development reduced 35%**: 147 → 95 days (Semiconductor)
- **Block Development reduced 17%**: 72 → 60 days (LED)
- Asset migration effort increased to account for 229GB DAM

---

## 5. Effort Summary (Revised)

### Scenario A: Semiconductor Only (Excluding LED)

| Work Stream | Effort (Person-Days) |
|-------------|---------------------|
| Discovery & Architecture (incl. DAM audit) | 45 |
| Foundation & Setup | 55 |
| Block Development — Reuse (10 blocks) | 22 |
| Block Development — Extend (8 blocks) | 40 |
| Block Development — Custom (6 blocks) | 33 |
| Content & Asset Migration (224 GB DAM) | 130 |
| Integrations | 32 |
| Testing & QA | 55 |
| Launch & Handover | 25 |
| **TOTAL** | **437 person-days** |

**Duration:** 18-22 weeks | **Team:** 4-5 FTEs | **Est. Cost:** $760K - $960K

---

### Scenario B: LED Incremental (When Combined with Semiconductor)

| Work Stream | Effort (Person-Days) |
|-------------|---------------------|
| Discovery (incremental) | 11 |
| LED Blocks — Reuse (3 blocks) | 7 |
| LED Blocks — Extend (3 blocks) | 13 |
| LED Blocks — Custom (4 blocks) | 40 |
| Content Migration | 32 |
| Integrations & Testing | 23 |
| **TOTAL** | **126 person-days** |

**Additional Duration:** 5-6 weeks | **Additional Resources:** +1 FTE

---

### Scenario C: Combined (Semiconductor + LED)

| Work Stream | Effort (Person-Days) |
|-------------|---------------------|
| Discovery & Architecture | 56 |
| Foundation & Setup | 55 |
| Block Development — Reuse (13 blocks) | 29 |
| Block Development — Extend (11 blocks) | 53 |
| Block Development — Custom (10 blocks) | 73 |
| Content & Asset Migration | 162 |
| Integrations | 45 |
| Testing & QA | 65 |
| Launch & Handover | 25 |
| **TOTAL** | **563 person-days** |

**Duration:** 24-28 weeks | **Team:** 5-6 FTEs | **Est. Cost:** $985K - $1.24M

---

## 6. Cost Comparison (Revised)

| Scenario | Person-Days | Duration | Est. Cost (USD) |
|----------|-------------|----------|-----------------|
| Semiconductor Only | 437 | 18-22 weeks | $760K - $960K |
| LED Only (standalone*) | 255 | 12-16 weeks | $445K - $560K |
| **Combined (Semi + LED)** | **563** | **24-28 weeks** | **$985K - $1.24M** |

### Savings vs. Original Estimate (Full Custom)

| Scenario | Original | Revised | Savings |
|----------|----------|---------|---------|
| Semiconductor Only | 485 days / $850K-$1.1M | 437 days / $760K-$960K | **~10% / $90K-$140K** |
| LED Incremental | 152 days | 126 days | **~17%** |
| Combined | 637 days / $1.1M-$1.4M | 563 days / $985K-$1.24M | **~12% / $115K-$160K** |

*LED standalone includes foundation setup costs shared in the combined scenario.

**Combined approach savings:** Bundling both sites saves approximately **$160K-$250K** vs. separate projects.

---

## 7. Key Benefits of Migration to EDS

| Benefit | Impact |
|---------|--------|
| **Performance** | Sub-second page loads, Lighthouse 95+ (vs. current ~60-70) |
| **Authoring Speed** | Document-based authoring — 5x faster content updates |
| **Cost Reduction** | Eliminates AEM On-Prem infrastructure (servers, patches, upgrades) |
| **DAM Optimization** | From 229GB to optimized CDN-delivered assets (~60-80% size reduction) |
| **Security** | CDN-edge delivery eliminates server-side vulnerabilities |
| **SEO** | Core Web Vitals compliance improves search rankings |
| **Developer Velocity** | No build step, instant preview, simplified codebase |
| **Block Reuse** | AEM Block Library accelerates future feature development |

---

## 8. Scope Exclusions

The following are **out of scope** for this estimate:

- Samsung Foundry B2B Portal (samsungfoundry.com) — separate platform
- Consumer Storage section (redirects to samsung.com) — separate domain
- Content creation/writing — client responsibility
- Content translation — client responsibility (framework provided)
- Archival DAM assets (identified during Phase 1 audit as inactive)
- Third-party license costs (search, analytics, consent tools)
- AEM Cloud Service licensing fees
- Ongoing maintenance beyond 2-week hypercare period

---

## 9. Recommended Approach (Revised)

### Phased Delivery Strategy

```
Phase 1 (Weeks 1-4):   Discovery, DAM Audit & Architecture
Phase 2 (Weeks 3-6):   Foundation & Setup
Phase 3a (Weeks 5-7):  Block Reuse — Style Only (accelerated)
Phase 3b (Weeks 6-10): Block Extend — Customize Library Blocks
Phase 3c (Weeks 8-18): Block Custom — Full Development (Semi + LED)
Phase 4a (Weeks 8-16): DAM/Asset Migration (phased, 229GB)
Phase 4b (Weeks 10-18):Content Migration
Phase 5 (Weeks 12-16): Integrations
Phase 6 (Weeks 16-22): Testing & QA
Phase 7 (Weeks 20-24): UAT & Launch Prep
Phase 8 (Weeks 24-28): Go-Live & Hypercare
```

### Recommended Team Structure

| Role | Count | Key Focus | Duration |
|------|-------|-----------|----------|
| Solution Architect | 1 | Block library mapping, DAM strategy | Full |
| Senior EDS Developer | 2 | Extend/custom blocks, integrations | Full |
| Frontend Developer | 1 | Reuse block styling, responsive design | Weeks 3-20 |
| Content/DAM Engineer | 1 | DAM audit (229GB), asset migration, import scripts | Weeks 6-22 |
| QA Engineer | 1 | Testing, accessibility, asset verification | Weeks 12-24 |
| Project Manager | 1 | Planning, coordination, training | Full |
| UX Designer | 0.5 | Design system extraction | Weeks 1-6 |
| DevOps Engineer | 0.5 | CDN, CI/CD, DAM migration tooling | As needed |

---

## 10. Key Risks (Revised)

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| DAM contains significant archival/unused assets (229GB) | High | Medium | Phase 1 audit to classify active vs. archive |
| Asset migration throughput (224GB transfer time) | Medium | High | Phased migration, parallel transfer, CDN pre-warm |
| Block Library doesn't match Samsung's exact UX | Medium | Medium | POC 2-3 key blocks in Phase 1 |
| LED Calculator tool complexity | Medium | High | Dedicated spike/POC; third-party fallback |
| Content volume larger than estimated | High | Medium | JCR query in discovery; 20% buffer |
| SEO ranking impact during migration | Medium | High | Comprehensive redirect map; staged rollout |
| DAM node count (1.69M) causes import performance issues | Medium | Medium | Batch processing; parallel workers |

---

## 11. Success Criteria

- All pages achieving Lighthouse Performance score ≥ 95
- WCAG 2.1 AA accessibility compliance
- Zero SEO ranking regression (monitored for 90 days post-launch)
- DAM reduced to actively-used assets only (target: 60-70% size reduction)
- Content author self-sufficiency within 2 weeks of training
- 99.9% uptime during and after migration

---

## 12. Next Steps

1. **Approve estimate scope** — Confirm inclusion/exclusion of LED website
2. **DAM audit authorization** — Provide access to AEM On-Prem for asset classification
3. **Block Library POC** — Validate 2-3 reuse-tier blocks against Samsung's UX requirements
4. **Kick-off Discovery Phase** — 3-4 week deep-dive site + DAM audit
5. **Stakeholder alignment** — Content freeze windows, UAT schedules
6. **Contract & SOW** — Based on selected scenario
7. **Team mobilization** — 2-week ramp-up after contract signing

---

*This estimate is valid for 60 days from the date of issue. Actual effort may vary based on discovery findings, particularly the DAM audit results.*

---

**Adobe Professional Services**  
*Empowering digital experiences at the speed of business*
