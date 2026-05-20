# AEM Edge Delivery Services Migration Estimate
## Samsung Semiconductor & LED Division

---

**Prepared by:** Adobe Professional Services  
**Date:** May 2026  
**Version:** 3.0 (Revised — Based on Samsung Internal Migration Analysis)  
**Classification:** Confidential  
**Source Data:** Samsung AEM 6.5 → Cloud Service Migration Analysis Document + DAM Disk Usage Report

---

## 1. Executive Summary

Samsung Electronics' Semiconductor Division has requested migration from **AEM 6.5 On-Premise** to **AEM Edge Delivery Services (EDS)**. Based on Samsung's internal migration analysis document, this is classified as a **Large** instance requiring **9-12 months** (standard estimate) to **11-14 months** (including LED website).

### Key Findings (from Samsung Internal Analysis)

| Metric | Value |
|--------|-------|
| **Total Pages** | 31,603 across 9 regions |
| **Components** | 643 component nodes / 132+ types |
| **DAM** | 229.17 GB / 1,692,306 nodes / 8.8M properties |
| **Languages** | 4 locales (EN, KR, JP, CN) |
| **Regions** | 9 (global, kr, us, emea, jp, cn, de, ssir, ds-test) |
| **OSGi Bundles** | 6 custom + 3 third-party |
| **Custom Admin UIs** | 5 (PIM, privacy, terms, site-ia, taskmanagement) |
| **WCM Templates** | 44 + 6 template-types |
| **External Dependencies** | MySQL (direct JDBC), Akamai NetStorage |
| **Samsung Classification** | Large (readme standard: 9-12 months) |

---

## 2. Current State — Regional Page Breakdown

| Region | Size | Pages | Notes |
|--------|------|-------|-------|
| global | 347 MB | 7,128 | Global master + multi-region master content |
| kr | 225 MB | 5,674 | Korea (ko_kr) |
| us | 193 MB | 5,351 | US + careers dedicated components |
| emea | 171 MB | 5,041 | Europe + searchjobs dedicated |
| jp | 171 MB | 4,007 | Japan (ja_jp) |
| cn | 155 MB | 4,298 | China (zh_cn) |
| de | 2.2 MB | 33 | Germany (small, insights/newsroom only) |
| ssir | 936 KB | 19 | SSIR dedicated small site |
| ds-test | 6.2 MB | 52 | Test/staging content |
| **TOTAL** | **1.3 GB** | **31,603** | |

---

## 3. Component Inventory (from Samsung Analysis)

### Content Component Categories

| Category | Types | Key Components |
|----------|-------|----------------|
| global/content/statics | 44 | st-semi-hero, accordion, carousel, feature-benefit, table |
| global/content/common | 26 | cm-semi-gnb, footer, breadcrumb, hashtag, contactus, cookie |
| global/content/product | 21 | pd-semi-hero, lnb, spec, product-finder, related-resources |
| global/content/event | 16 | ev-semi-login, mypage, webinar-regist, subscription |
| global/content/article | 11 | ar-semi-article-grid, event-calendar, event-grid, popular-news |
| global/content/search | 4 | sr-semi-search-grid, search-publications |
| global/content/careers | 2 | cr-semi-job-list, cr-semi-job-detail |
| global/page (templates) | 6 | product-page, content-page, empty-page, empty-xf, static-content-page, marketing-static-content-page |
| Region-specific | 2 | emea/searchjobs, us/careers |
| **TOTAL** | **132+ types / 643 nodes** | Including all variants (.content.xml based) |

### Code Inventory

| Type | Count | Notes |
|------|-------|-------|
| HTL Files | 205 | Already HTL (not JSP) — good for analysis |
| JSP Files | 9 | Must convert → HTL (admin/taskmanagement) |
| JS Files | 582 | Client-side + design plugins |
| CSS Files | 254 | Styling to extract into EDS design system |
| Apps Config | 216 KB | conf / conf.dev / conf.stg / conf.prd |
| i18n Dictionaries | 180 KB | 4 locale JSON files |

### OSGi Bundles (install/)

| Bundle | Size | Last Build | Impact |
|--------|------|-----------|--------|
| **semi-common-1.0.0-SNAPSHOT.jar** | 1.7 MB | 2025-10 | ★ Largest core bundle, high impact |
| semi-apiservice-1.0.0-SNAPSHOT.jar | 157 KB | 2026-01 | REST/API services |
| semi-admin-1.0.0-SNAPSHOT.jar | 102 KB | 2022-10 | Admin backoffice |
| semi-article-1.0.0-SNAPSHOT.jar | 48 KB | 2026-02 | Article domain |
| semi-product-1.0.0-SNAPSHOT.jar | 39 KB | 2025-06 | Product domain |
| semi-gnb-1.0.0-SNAPSHOT.jar | 30 KB | 2024-07 | GNB menu |
| **mysql-connector-java-8.0.26.jar** | 2.4 MB | 3rd party | ★ External MySQL direct JDBC (NOT possible in Cloud) |
| jsoup-1.8.3.jar | 308 KB | 3rd party | HTML parser |
| **NetStorageKit-3.6.7.jar** | 59 KB | 3rd party | ★ Akamai NetStorage integration |

---

## 4. Critical Architecture Challenges

EDS migration is **NOT a standard AEM upgrade** — it requires architectural re-implementation:

| Challenge | Current State | EDS Target | Migration Approach |
|-----------|--------------|------------|-------------------|
| Rendering | Server-side HTL/Sling | Client-side vanilla JS | Re-implement all 643 components as 33 EDS blocks |
| Data Storage | JCR + MySQL (JDBC) | Document-based + API | Externalize MySQL as REST microservice |
| Asset Delivery | Akamai NetStorage | EDS CDN (edge delivery) | Migrate 229GB to EDS-compatible format |
| Admin Tools | 5 custom Granite/JSP UIs | No server-side UI in EDS | Build separate headless admin application |
| Templates | 44 WCM + 6 types | 8-10 document templates | Template consolidation & simplification |
| Bundles | 6 custom OSGi bundles | No OSGi in EDS | Externalize as serverless/microservices |
| Auth/Login | ev-semi-login (Sling auth) | Client-side or external | External auth service (OAuth/OIDC) |

**NOTE:** AEM Modernization Tools/Agent are designed for AEM 6.x → AEMaaCS (same architecture). They do NOT apply to EDS migration since EDS has no JCR, no OSGi, no HTL, and no server-side rendering.

---

## 5. Block Reuse Strategy

Despite the scale, we optimize by leveraging the AEM Block Library:

| Tier | Description | Blocks | Effort/Block | Total |
|------|-------------|--------|-------------|-------|
| **REUSE** | Library block + brand CSS only | 12 (Semi) + 3 (LED) | 2-3 days | 34 days |
| **EXTEND** | Library + significant customization | 10 (Semi) + 4 (LED) | 4-8 days | 76 days |
| **CUSTOM** | Full build, no equivalent | 11 (Semi) + 4 (LED) | 6-15 days | 128 days |
| **TOTAL** | | **44 blocks** | | **238 days** |

### How 643 AEM Components → 33-44 EDS Blocks

The 643 component node count includes variants. After consolidation:
- 44 statics components → ~8-10 EDS blocks (hero, carousel, accordion, table, cards, etc.)
- 26 common components → ~5-6 EDS blocks (gnb, footer, breadcrumb, cookie, hashtag)
- 21 product components → ~4-5 EDS blocks (spec, product-finder, hero, resources)
- 16 event components → ~3-4 EDS blocks (login/mypage, webinar, subscription)
- 11 article components → ~3 EDS blocks (article-grid, event-calendar, news)
- Remaining → search, careers, regional = ~5-6 EDS blocks

---

## 6. Effort Summary (Revised v3.0)

### Scenario A: Semiconductor Only (Excluding LED)

| Work Stream | Effort (Person-Days) |
|-------------|---------------------|
| Discovery & Architecture (31K pages, 643 components, DAM) | 66 |
| Foundation & Setup (templates, i18n, search, auth) | 77 |
| Block Development — Reuse (12 blocks, style only) | 27 |
| Block Development — Extend (10 blocks) | 59 |
| Block Development — Custom (11 blocks) | 88 |
| External Services & API Layer (6 OSGi + 5 Admin UIs) | 95 |
| Content & Asset Migration (31,603 pages + 229GB DAM) | 173 |
| Integrations (search, analytics, forms, CDN) | 36 |
| Testing & QA (9 regions × 4 locales) | 95 |
| Launch & Handover (staged regional cutover) | 41 |
| **TOTAL** | **757 person-days** |

**Duration:** 9-11 months | **Team:** 5-7 FTEs | **Est. Cost:** $1.32M - $1.67M

---

### Scenario B: LED Incremental (Combined with Semiconductor)

| Work Stream | Effort (Person-Days) |
|-------------|---------------------|
| Discovery (incremental) | 11 |
| LED Blocks — Reuse (3 blocks) | 7 |
| LED Blocks — Extend (4 blocks) | 17 |
| LED Blocks — Custom (4 blocks, inc. calculators) | 40 |
| Content Migration (~80 pages × 6 regions) | 35 |
| Integrations & Testing | 26 |
| **TOTAL** | **136 person-days** |

**Additional Duration:** 5-6 weeks | **Additional Resources:** +1 FTE

---

### Scenario C: Combined (Semiconductor + LED)

| Work Stream | Effort (Person-Days) |
|-------------|---------------------|
| Discovery & Architecture | 77 |
| Foundation & Setup | 77 |
| Block Development (44 total blocks) | 238 |
| External Services & API Layer | 95 |
| Content & Asset Migration | 208 |
| Integrations | 36 |
| Testing & QA | 121 |
| Launch & Handover | 41 |
| **TOTAL** | **893 person-days** |

**Duration:** 11-14 months | **Team:** 6-8 FTEs | **Est. Cost:** $1.56M - $1.96M

---

## 7. Cost Comparison

| Scenario | Person-Days | Duration | Est. Cost (USD) |
|----------|-------------|----------|-----------------|
| Semiconductor Only | 757 | 9-11 months | $1.32M - $1.67M |
| LED Only (standalone*) | 420 | 6-8 months | $735K - $925K |
| **Combined (Semi + LED)** | **893** | **11-14 months** | **$1.56M - $1.96M** |

*LED standalone includes shared foundation/API effort absorbed in combined scenario.

**Combined approach savings:** ~$500K-$650K vs. separate projects.

---

## 8. Key Risks (from Samsung Analysis + Our Assessment)

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| R1 | MySQL JDBC → Cloud has no direct JDBC | Confirmed | High | Externalize as REST microservice; API-only calls |
| R2 | DAM 224GB single tree (98% in /samsung) | Confirmed | High | CTT chunk split + top-up rounds; pre-cleanup |
| R3 | Akamai NetStorageKit dependency | Confirmed | High | Migrate to Cloud Manager CDN or EDS native |
| R4 | 5 Custom Admin UIs (no equivalent in EDS) | Confirmed | High | Externalize as SPA or headless admin apps |
| R5 | 9 regions × 4 locales simultaneous ops | Confirmed | High | Region-by-region cutover with validation |
| R6 | 31,603 pages migration volume | Confirmed | High | Automated import per region; parallel processing |
| R7 | semi-common 1.7MB core bundle | High | High | Priority #1 refactoring; SDK compatibility |
| R8 | 643 components → 33 EDS blocks mapping | Medium | High | POC key blocks in Phase 1; validate assumptions |
| R9 | SEO impact — 31,603 URL redirects | High | High | Comprehensive redirect map; staged rollout |
| R10 | LED calculator complexity | Medium | High | Dedicated spike; third-party fallback |

---

## 9. Recommended Approach — Staged Regional Cutover

### Phase Timeline (11-14 months combined)

```
Month 1-2:   Discovery & Architecture (DAM audit, component mapping)
Month 2-4:   Foundation & Setup (templates, i18n, design system)
Month 3-4:   Block Reuse — Style Only (accelerated, 12 blocks)
Month 3-6:   Block Extend — Customize (10 blocks)
Month 4-9:   Block Custom + LED blocks (15 blocks)
Month 3-8:   External Services / API Layer (OSGi replacement)
Month 4-8:   DAM Audit & Asset Migration (229GB)
Month 5-11:  Content Migration (31,603 pages, region by region)
Month 6-8:   Integrations
Month 7-12:  Testing & QA (per region matrix)
Month 9-10:  Regional Cutover — ssir/de (low risk, smallest)
Month 10-11: Regional Cutover — kr/jp
Month 11-12: Regional Cutover — cn/us/emea
Month 12-14: Regional Cutover — global (master) + Hypercare
```

### Cutover Strategy (from Samsung recommendation)
Small/low-risk regions first → progressively larger → global master last:
```
ssir/de → kr/jp → cn → us/emea → global
```

---

## 10. Team Structure

| Role | Count | Key Focus | Duration |
|------|-------|-----------|----------|
| Solution Architect | 1 | Component mapping (643→33), integration design | Full |
| Senior EDS Developer | 2 | Extend/custom blocks, EDS patterns | Full |
| Backend Developer | 1 | MySQL API, OSGi externalization, serverless | Months 2-8 |
| Frontend Developer | 1-2 | Reuse blocks, 254 CSS migration, responsive | Months 2-10 |
| Content/DAM Engineer | 1-2 | 229GB audit, 31K page migration, import scripts | Months 4-12 |
| QA Engineer | 1-2 | 9-region testing, a11y, cross-browser | Months 6-14 |
| Project Manager | 1 | Region cutover planning, stakeholder coordination | Full |
| UX Designer | 0.5 | Design system from 582 JS / 254 CSS | Months 1-3 |
| DevOps Engineer | 1 | CDN migration, Akamai replacement, CI/CD | Months 2-6, 10-14 |

**Peak team: 6-8 FTEs (months 4-10)**

---

## 11. Scope Exclusions

- Samsung Foundry B2B Portal (samsungfoundry.com) — separate platform
- Consumer Storage section (redirects to samsung.com)
- Content creation/writing — client responsibility
- Content translation — client responsibility
- ds-test region (test/staging) — excluded from production migration
- Third-party license costs (search, analytics, consent tools)
- AEM Cloud Service / EDS licensing fees
- Ongoing maintenance beyond 4-week hypercare period
- Experience Fragments (confirmed 0 in use per Samsung analysis)

---

## 12. Next Steps

1. **Approve estimate scope** — Confirm inclusion/exclusion of LED website
2. **BPA Report** — Run Adobe Best Practices Analyzer for formal Cloud readiness assessment
3. **Adobe CAM Readiness** — Validate findings against Cloud Acceleration Manager
4. **OSGi Bundle POC** — Priority spike on semi-common externalization
5. **Block Library Validation** — POC 3 key blocks against Samsung UX
6. **DAM Cleanup Authorization** — Begin CTT pre-cleanup of /samsung tree
7. **Contract & SOW** — Based on selected scenario
8. **Team Mobilization** — 2-week ramp-up after signing

---

## 13. Alignment with Samsung's Own Assessment

Samsung's internal document classified this as **Large (9-12 months)** based on:
- DAM 229GB + 31,603 pages → Large threshold exceeded
- 6 custom OSGi bundles + custom Admin UI → code modernization is significant
- 9 regions × 4 locales → regression test/validation matrix is 9x normal

Our estimate of **9-11 months (Semi only)** and **11-14 months (Combined)** aligns with and slightly extends their assessment, accounting for the EDS-specific re-implementation work that goes beyond a standard AEMaaCS migration.

---

*This estimate is valid for 60 days from the date of issue. Actual effort may vary based on BPA results and discovery findings.*

---

**Adobe Professional Services**  
*Empowering digital experiences at the speed of business*
