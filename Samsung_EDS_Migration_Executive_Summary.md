# AEM Edge Delivery Services Migration Estimate
## Samsung Semiconductor & LED Division

---

**Prepared by:** Adobe Professional Services  
**Date:** May 2026  
**Version:** 1.0  
**Classification:** Confidential

---

## 1. Executive Summary

Samsung Electronics' Semiconductor Division has requested a migration from their current **AEM On-Premise** instance to **AEM Edge Delivery Services (EDS)** — Adobe's modern, high-performance content delivery platform. This estimate covers two websites currently hosted on the same AEM instance:

- **semiconductor.samsung.com** — Primary semiconductor business website
- **led.samsung.com** — LED product division website

This document provides a detailed effort estimate for three scenarios:
1. Semiconductor website only (excluding LED)
2. LED website only (standalone)
3. Combined migration (Semiconductor + LED)

---

## 2. Current State Assessment

### semiconductor.samsung.com

| Attribute | Details |
|-----------|---------|
| **Content Volume** | 350-500+ pages across 12 product categories |
| **Page Templates** | 7-9 unique templates (PLP, PDP, Blog, Corporate, Foundry, etc.) |
| **Languages** | 4 locales (English, Korean, Chinese, Japanese) |
| **Key Features** | Mega navigation, product spec tables, video embeds, multi-step forms, FAQ accordions, tech blog, event listings, search with suggestions |
| **Integrations** | Search engine, analytics, form backends, CDN, B2B portal link |
| **Complexity** | HIGH — Enterprise-grade with extensive product taxonomy, foundry services, and interactive components |

### led.samsung.com

| Attribute | Details |
|-----------|---------|
| **Content Volume** | 50-80+ pages across 5 product categories |
| **Page Templates** | 3-4 additional unique templates |
| **Regions** | 6 regional variants (Americas, EMEA, China, SE Asia, Japan, Korea) |
| **Key Features** | LED/Engine calculators, product comparison, virtual exhibition, datasheet downloads, regional sales network |
| **Integrations** | Calculator tools, regional contact systems, download management |
| **Complexity** | MEDIUM-HIGH — Specialized tools (calculators) add significant development effort |

---

## 3. Effort Summary

### Scenario A: Semiconductor Only (Excluding LED)

| Work Stream | Effort (Person-Days) |
|-------------|---------------------|
| Discovery & Architecture | 41 |
| Foundation & Setup | 61 |
| Block Development (25 blocks) | 147 |
| Content Migration | 106 |
| Integrations | 39 |
| Testing & QA | 63 |
| Launch & Handover | 28 |
| **TOTAL** | **485 person-days** |

**Duration:** 20-26 weeks | **Team:** 4-5 FTEs | **Est. Cost:** $850K - $1.1M

---

### Scenario B: LED Incremental (When Combined with Semiconductor)

| Work Stream | Effort (Person-Days) |
|-------------|---------------------|
| Discovery (incremental) | 12 |
| LED-specific Blocks (10 blocks) | 72 |
| Content Migration | 39 |
| Integrations & Testing | 29 |
| **TOTAL** | **152 person-days** |

**Additional Duration:** 6-8 weeks | **Additional Resources:** +1 FTE

---

### Scenario C: Combined (Semiconductor + LED)

| Work Stream | Effort (Person-Days) |
|-------------|---------------------|
| Discovery & Architecture | 53 |
| Foundation & Setup | 61 |
| Block Development (35 blocks) | 219 |
| Content Migration | 145 |
| Integrations | 55 |
| Testing & QA | 76 |
| Launch & Handover | 28 |
| **TOTAL** | **637 person-days** |

**Duration:** 26-32 weeks | **Team:** 5-6 FTEs | **Est. Cost:** $1.1M - $1.4M

---

## 4. Cost Comparison

| Scenario | Person-Days | Duration | Est. Cost (USD) |
|----------|-------------|----------|-----------------|
| Semiconductor Only | 485 | 20-26 weeks | $850K - $1.1M |
| LED Only (standalone*) | 290 | 14-18 weeks | $500K - $650K |
| **Combined (Semi + LED)** | **637** | **26-32 weeks** | **$1.1M - $1.4M** |

*LED standalone includes foundation setup costs that are shared in the combined scenario, saving ~$150K-$200K.

**Savings from combined approach:** Bundling both sites saves approximately **$200K-$350K** compared to executing them as separate projects, due to shared foundation, design system, and infrastructure work.

---

## 5. Key Benefits of Migration to EDS

| Benefit | Impact |
|---------|--------|
| **Performance** | Sub-second page loads, Lighthouse 95+ (vs. current ~60-70) |
| **Authoring Speed** | Document-based authoring — 5x faster content updates |
| **Cost Reduction** | No AEM On-Prem infrastructure costs (servers, patches, upgrades) |
| **Security** | CDN-edge delivery eliminates server-side vulnerabilities |
| **SEO** | Core Web Vitals compliance improves search rankings |
| **Developer Velocity** | No build step, instant preview, simplified codebase |

---

## 6. Scope Exclusions

The following are **out of scope** for this estimate:

- Samsung Foundry B2B Portal (samsungfoundry.com) — separate platform
- Consumer Storage section (redirects to samsung.com) — separate domain
- Content creation/writing — client responsibility
- Content translation — client responsibility (framework provided)
- Third-party license costs (search, analytics, consent tools)
- AEM Cloud Service licensing fees
- Ongoing maintenance beyond 2-week hypercare period

---

## 7. Recommended Approach

### Phased Delivery Strategy

```
Phase 1 (Weeks 1-4):   Discovery & Architecture
Phase 2 (Weeks 3-7):   Foundation & Setup
Phase 3 (Weeks 6-20):  Block Development
Phase 4 (Weeks 12-24): Content Migration
Phase 5 (Weeks 14-20): Integrations
Phase 6 (Weeks 18-26): Testing & QA
Phase 7 (Weeks 24-28): UAT & Launch Prep
Phase 8 (Weeks 28-32): Go-Live & Hypercare
```

### Recommended Team Structure

| Role | Count | Duration |
|------|-------|----------|
| Solution Architect | 1 | Full |
| Senior EDS Developer | 2 | Full |
| Frontend Developer | 1-2 | Weeks 4-24 |
| Content Engineer | 1 | Weeks 8-22 |
| QA Engineer | 1 | Weeks 12-26 |
| Project Manager | 1 | Full |
| UX Designer | 0.5 | Weeks 1-8 |
| DevOps Engineer | 0.5 | As needed |

---

## 8. Key Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Calculator tools exceed complexity estimates | Medium | High | POC spike in Phase 1 |
| Content volume larger than estimated | High | Medium | Automated crawl; 20% buffer |
| Multi-language content sync issues | Medium | High | Early i18n framework testing |
| SEO ranking impact during migration | Medium | High | Comprehensive redirect strategy |
| Third-party integration delays | Medium | Medium | Early vendor engagement |

---

## 9. Success Criteria

- All pages achieving Lighthouse Performance score ≥ 95
- WCAG 2.1 AA accessibility compliance
- Zero SEO ranking regression (monitored for 90 days post-launch)
- Content author self-sufficiency within 2 weeks of training
- 99.9% uptime during and after migration

---

## 10. Next Steps

1. **Approve estimate scope** — Confirm inclusion/exclusion of LED website
2. **Kick-off Discovery Phase** — 2-week deep-dive site audit
3. **Stakeholder alignment** — Content freeze windows, UAT schedules
4. **Contract & SOW** — Based on selected scenario
5. **Team mobilization** — 2-week ramp-up after contract signing

---

*This estimate is valid for 60 days from the date of issue. Actual effort may vary based on discovery findings.*

---

**Adobe Professional Services**  
*Empowering digital experiences at the speed of business*
