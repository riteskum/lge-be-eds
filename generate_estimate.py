#!/usr/bin/env python3
"""
Generate AEM On-Premise to EDS Migration Estimate (REVISED v2.0)
Samsung Semiconductor + LED Website
Adobe Professional Format

REVISION NOTES:
- Block development effort reduced by leveraging AEM Block Collection/Block Party
- Blocks categorized as: Reuse (style-only), Extend (customize), Custom (new build)
- Asset migration effort increased based on actual DAM report (229GB, 1.69M nodes)
"""

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, numbers
from openpyxl.utils import get_column_letter
from copy import copy

# Adobe brand colors
ADOBE_RED = "FA0F00"
ADOBE_DARK = "2C2C2C"
ADOBE_GRAY = "747474"
ADOBE_LIGHT_GRAY = "F5F5F5"
ADOBE_WHITE = "FFFFFF"
ADOBE_BLUE = "1473E6"
ADOBE_GREEN = "2D9D78"
HEADER_BG = "323232"

# Styles
title_font = Font(name="Adobe Clean", size=18, bold=True, color=ADOBE_DARK)
subtitle_font = Font(name="Adobe Clean", size=14, bold=True, color=ADOBE_GRAY)
header_font = Font(name="Adobe Clean", size=11, bold=True, color=ADOBE_WHITE)
body_font = Font(name="Adobe Clean", size=10, color=ADOBE_DARK)
body_bold_font = Font(name="Adobe Clean", size=10, bold=True, color=ADOBE_DARK)
total_font = Font(name="Adobe Clean", size=11, bold=True, color=ADOBE_RED)
section_font = Font(name="Adobe Clean", size=11, bold=True, color=ADOBE_BLUE)
reuse_font = Font(name="Adobe Clean", size=10, color=ADOBE_GREEN, bold=True)

header_fill = PatternFill(start_color=HEADER_BG, end_color=HEADER_BG, fill_type="solid")
alt_fill = PatternFill(start_color=ADOBE_LIGHT_GRAY, end_color=ADOBE_LIGHT_GRAY, fill_type="solid")
total_fill = PatternFill(start_color="FFF0F0", end_color="FFF0F0", fill_type="solid")
section_fill = PatternFill(start_color="E8F4FD", end_color="E8F4FD", fill_type="solid")
reuse_fill = PatternFill(start_color="E8F8F0", end_color="E8F8F0", fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color='DDDDDD'),
    right=Side(style='thin', color='DDDDDD'),
    top=Side(style='thin', color='DDDDDD'),
    bottom=Side(style='thin', color='DDDDDD')
)

center_align = Alignment(horizontal='center', vertical='center', wrap_text=True)
left_align = Alignment(horizontal='left', vertical='center', wrap_text=True)
right_align = Alignment(horizontal='right', vertical='center')


def style_header_row(ws, row, cols):
    for col in range(1, cols + 1):
        cell = ws.cell(row=row, column=col)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border


def style_data_row(ws, row, cols, is_alt=False, is_total=False, is_section=False, is_reuse=False):
    for col in range(1, cols + 1):
        cell = ws.cell(row=row, column=col)
        cell.border = thin_border
        if is_total:
            cell.font = total_font
            cell.fill = total_fill
        elif is_section:
            cell.font = section_font
            cell.fill = section_fill
        elif is_reuse:
            cell.font = body_font
            cell.fill = reuse_fill
        else:
            cell.font = body_font
            if is_alt:
                cell.fill = alt_fill
        if col >= 3:
            cell.alignment = center_align
        else:
            cell.alignment = left_align


def create_workbook():
    wb = Workbook()

    # ============================================================
    # SHEET 1: Executive Summary
    # ============================================================
    ws_exec = wb.active
    ws_exec.title = "Executive Summary"
    ws_exec.sheet_properties.tabColor = ADOBE_RED

    # Set column widths
    ws_exec.column_dimensions['A'].width = 5
    ws_exec.column_dimensions['B'].width = 80
    ws_exec.column_dimensions['C'].width = 25
    ws_exec.column_dimensions['D'].width = 25

    row = 2
    ws_exec.cell(row=row, column=2, value="ADOBE EXPERIENCE MANAGER").font = Font(name="Adobe Clean", size=10, color=ADOBE_RED, bold=True)
    row += 1
    ws_exec.cell(row=row, column=2, value="Edge Delivery Services Migration Estimate").font = title_font
    row += 1
    ws_exec.cell(row=row, column=2, value="Samsung Semiconductor & LED Division").font = subtitle_font
    row += 1
    ws_exec.cell(row=row, column=2, value="REVISED v2.0 — Optimized with AEM Block Library Reuse").font = Font(name="Adobe Clean", size=10, italic=True, color=ADOBE_GREEN)
    row += 2

    # Project Overview
    ws_exec.cell(row=row, column=2, value="PROJECT OVERVIEW").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_RED)
    row += 2

    overview_items = [
        ("Client:", "Samsung Electronics - Semiconductor Division"),
        ("Source Platform:", "AEM On-Premise (6.x)"),
        ("Target Platform:", "AEM Edge Delivery Services (Cloud)"),
        ("Websites in Scope:", "semiconductor.samsung.com + led.samsung.com"),
        ("DAM Size:", "229.17 GB | 1,692,306 nodes | 8,815,757 properties"),
        ("Date:", "May 2026"),
        ("Prepared by:", "Adobe Professional Services"),
        ("Version:", "2.0 (Revised — Block Library reuse optimization)"),
    ]

    for label, value in overview_items:
        ws_exec.cell(row=row, column=2, value=label).font = body_bold_font
        ws_exec.cell(row=row, column=3, value=value).font = body_font
        row += 1

    row += 2
    ws_exec.cell(row=row, column=2, value="DAM REPOSITORY ANALYSIS").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_RED)
    row += 2

    # DAM table
    dam_headers = ["DAM Folder", "Size", "Nodes"]
    ws_exec.cell(row=row, column=2, value=dam_headers[0])
    ws_exec.cell(row=row, column=3, value=dam_headers[1])
    ws_exec.cell(row=row, column=4, value=dam_headers[2])
    for col in range(2, 5):
        cell = ws_exec.cell(row=row, column=col)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border
    row += 1

    dam_data = [
        ("/content/dam/samsung", "224.62 GB", "1,626,711"),
        ("/content/dam/test", "4.55 GB", "65,295"),
        ("/content/dam/_CSS", "458 KB", "109"),
        ("/content/dam/formsanddocuments", "1,266 bytes", "26"),
        ("/content/dam/collections", "3,427 bytes", "62"),
        ("TOTAL", "229.17 GB", "1,692,306"),
    ]

    for i, (folder, size, nodes) in enumerate(dam_data):
        ws_exec.cell(row=row, column=2, value=folder)
        ws_exec.cell(row=row, column=3, value=size)
        ws_exec.cell(row=row, column=4, value=nodes)
        is_t = (i == len(dam_data) - 1)
        for col in range(2, 5):
            cell = ws_exec.cell(row=row, column=col)
            cell.border = thin_border
            cell.alignment = center_align if col > 2 else left_align
            if is_t:
                cell.font = total_font
                cell.fill = total_fill
            elif i % 2 == 0:
                cell.fill = alt_fill
                cell.font = body_font
            else:
                cell.font = body_font
        row += 1

    row += 2
    ws_exec.cell(row=row, column=2, value="SCOPE SUMMARY (REVISED)").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_RED)
    row += 2

    # Scope table
    scope_headers = ["Metric", "Semiconductor Only", "Semiconductor + LED"]
    ws_exec.cell(row=row, column=2, value=scope_headers[0])
    ws_exec.cell(row=row, column=3, value=scope_headers[1])
    ws_exec.cell(row=row, column=4, value=scope_headers[2])
    for col in range(2, 5):
        cell = ws_exec.cell(row=row, column=col)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border
    row += 1

    scope_data = [
        ("Estimated Page Count", "350-500+", "400-580+"),
        ("DAM Assets to Migrate", "224 GB (~1.6M nodes)", "229 GB (~1.7M nodes)"),
        ("Unique Page Templates", "7-9", "10-12"),
        ("Total Blocks Required", "25-30", "35-40"),
        ("  → Reuse from Block Library (style only)", "10-12", "12-15"),
        ("  → Extend/Customize existing blocks", "8-10", "10-13"),
        ("  → Custom Development (new blocks)", "7-8", "10-12"),
        ("Languages/Locales", "4 (EN, KR, CN, JP)", "4 + 6 Regions"),
        ("Integrations", "5-7", "7-9"),
        ("Total Effort (Person-Days)", "390-420", "520-560"),
        ("Duration (Weeks)", "18-22", "24-28"),
    ]

    for i, (metric, semi, both) in enumerate(scope_data):
        ws_exec.cell(row=row, column=2, value=metric)
        ws_exec.cell(row=row, column=3, value=semi)
        ws_exec.cell(row=row, column=4, value=both)
        for col in range(2, 5):
            cell = ws_exec.cell(row=row, column=col)
            cell.border = thin_border
            cell.alignment = center_align if col > 2 else left_align
            if i >= len(scope_data) - 2:
                cell.font = total_font
                cell.fill = total_fill
            elif "Reuse" in metric or "Extend" in metric:
                cell.font = body_font
                cell.fill = reuse_fill
            elif i % 2 == 0:
                cell.fill = alt_fill
                cell.font = body_font
            else:
                cell.font = body_font
        row += 1

    row += 2
    ws_exec.cell(row=row, column=2, value="BLOCK REUSE STRATEGY — KEY OPTIMIZATION").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_GREEN)
    row += 2

    reuse_note = [
        "The revised estimate leverages the AEM Block Collection, Block Party, and EDS Boilerplate to significantly",
        "reduce custom development effort. Blocks are categorized into three tiers:",
        "",
        "• REUSE (Style Only) — Block exists in AEM library; only brand CSS customization needed (~2-3 days each)",
        "    Examples: Hero, Cards, Carousel, Tabs, Accordion, Video, Breadcrumb, Columns, CTA",
        "",
        "• EXTEND (Customize) — Block library provides foundation; requires JS/logic modifications (~4-6 days each)",
        "    Examples: Header/Nav (mega menu), Footer, FAQ, News Listing, Contact Form",
        "",
        "• CUSTOM (New Development) — No library equivalent; full custom build required (~8-12 days each)",
        "    Examples: Product Specs Table, LED Calculators, Virtual Exhibition, Multi-step Wizard",
        "",
        "This approach reduces Block Development from 147 days → 95 days (35% savings) for Semiconductor.",
    ]

    for item in reuse_note:
        ws_exec.cell(row=row, column=2, value=item).font = body_font
        row += 1

    row += 2
    ws_exec.cell(row=row, column=2, value="KEY ASSUMPTIONS & RISKS").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_RED)
    row += 2

    assumptions = [
        "• DAM contains 229GB / 1.69M nodes — asset migration requires phased approach with selective optimization",
        "• Not all DAM assets will be migrated — audit needed to identify active vs. archival content",
        "• Content migration assumes automated tooling (AEM Importer) with manual QA for critical pages",
        "• Foundry section (samsungfoundry.com) B2B portal is OUT OF SCOPE (separate platform)",
        "• Consumer Storage section redirects to samsung.com — OUT OF SCOPE",
        "• AEM Block Collection/Block Party provides reusable foundation for 60-70% of blocks",
        "• Multi-language support requires i18n framework setup; content translation is client responsibility",
        "• Search functionality will leverage AEM EDS indexing or third-party search (Algolia/Coveo)",
        "• LED Calculator tools require custom JavaScript development (no library equivalent)",
        "• Cookie consent and GDPR compliance requires OneTrust or similar integration",
        "• Performance target: Lighthouse score ≥ 95 on all page templates",
        "• UAT and content freeze periods to be agreed upon during project planning",
    ]

    for item in assumptions:
        ws_exec.cell(row=row, column=2, value=item).font = body_font
        row += 1

    row += 2
    ws_exec.cell(row=row, column=2, value="RECOMMENDED APPROACH").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_RED)
    row += 2

    approach = [
        "Phase 1: Discovery & Architecture (3-4 weeks) — Site audit, DAM analysis, block inventory, template mapping",
        "Phase 2: Foundation Setup (2-3 weeks) — EDS project, design system, boilerplate blocks",
        "Phase 3: Block Development (5-7 weeks) — Reuse/extend library blocks + custom builds",
        "Phase 4: Content & Asset Migration (5-7 weeks) — Automated import, DAM selective migration, QA",
        "Phase 5: Testing & Launch (4-5 weeks) — Performance, accessibility, UAT, go-live",
    ]

    for item in approach:
        ws_exec.cell(row=row, column=2, value=item).font = body_font
        row += 1

    # ============================================================
    # SHEET 2: Detailed Estimate - Semiconductor Only (REVISED)
    # ============================================================
    ws_semi = wb.create_sheet("Semiconductor - Detailed")
    ws_semi.sheet_properties.tabColor = ADOBE_BLUE

    # Column widths
    col_widths = [5, 8, 48, 15, 15, 15, 15, 45]
    for i, w in enumerate(col_widths, 1):
        ws_semi.column_dimensions[get_column_letter(i)].width = w

    row = 2
    ws_semi.cell(row=row, column=2, value="Samsung Semiconductor - EDS Migration (REVISED — Block Reuse Optimized)").font = title_font
    row += 1
    ws_semi.cell(row=row, column=2, value="Excluding LED | DAM: 224.62 GB / 1,626,711 nodes").font = subtitle_font
    row += 2

    # Headers
    headers = ["#", "Work Stream", "Task", "Complexity", "Effort (Days)", "Resources", "Notes"]
    for col, h in enumerate(headers, 2):
        ws_semi.cell(row=row, column=col, value=h)
    style_header_row(ws_semi, row, 8)
    row += 1

    # Data - REVISED with block reuse and increased DAM migration
    semi_tasks = [
        # Section: Discovery & Architecture
        ("", "DISCOVERY & ARCHITECTURE", "", "", "", "", "", False),
        ("1.1", "", "Site Audit & Content Inventory", "Medium", "10", "1 Architect", "Crawl all pages, map content types", False),
        ("1.2", "", "DAM Audit & Asset Classification", "High", "8", "1 Architect + 1 Dev", "224GB DAM — classify active vs archive assets", False),
        ("1.3", "", "Template & Block Mapping", "High", "6", "1 Architect", "Map AEM components → EDS blocks + library matches", False),
        ("1.4", "", "Information Architecture Review", "Medium", "5", "1 Architect", "Navigation, URL strategy, redirects", False),
        ("1.5", "", "Technical Architecture Design", "High", "8", "1 Architect + 1 Dev", "Integration points, search, i18n", False),
        ("1.6", "", "Design System Extraction", "Medium", "5", "1 Designer", "Tokens, typography, spacing, colors", False),
        ("1.7", "", "Migration Strategy Document", "Low", "3", "1 PM", "Phasing, risk mitigation, timelines", False),
        ("", "", "Subtotal - Discovery", "", "45", "", "", False),

        # Section: Foundation & Setup
        ("", "FOUNDATION & SETUP", "", "", "", "", "", False),
        ("2.1", "", "EDS Project Scaffolding", "Low", "3", "1 Dev", "Repo setup, CI/CD, environments", False),
        ("2.2", "", "Global Styles & Design Tokens", "Medium", "8", "1 Dev", "CSS variables, fonts, base styles from source", False),
        ("2.3", "", "Header/Navigation Block (EXTEND)", "High", "10", "1 Dev", "Extend nav block — mega menu, multi-level", False),
        ("2.4", "", "Footer Block (EXTEND)", "Medium", "4", "1 Dev", "Extend footer — multi-column, social, legal", False),
        ("2.5", "", "Core Page Templates (7-9)", "High", "12", "1 Dev", "PLP, PDP, Blog, Landing, Corporate, etc.", False),
        ("2.6", "", "i18n Framework Setup", "High", "10", "1 Dev", "4 locales: EN, KR, CN, JP", False),
        ("2.7", "", "Search Infrastructure", "High", "8", "1 Dev", "Indexing, search UI, suggestions", False),
        ("", "", "Subtotal - Foundation", "", "55", "", "", False),

        # Section: Block Development — REUSE (Style Only)
        ("", "BLOCK DEVELOPMENT — REUSE (Style Only, from AEM Block Library)", "", "", "", "", "", False),
        ("3.1", "", "Hero/Banner Block (library + brand CSS)", "Low", "3", "1 Dev", "REUSE: Carousel, video, static variants", True),
        ("3.2", "", "Cards Block (library + brand CSS)", "Low", "3", "1 Dev", "REUSE: Multiple card layout variants", True),
        ("3.3", "", "Carousel/Slider Block (library + brand CSS)", "Low", "3", "1 Dev", "REUSE: Touch, responsive, accessible", True),
        ("3.4", "", "Tabs Block (library + brand CSS)", "Low", "2", "1 Dev", "REUSE: Content tabs, accessible", True),
        ("3.5", "", "Accordion Block (library + brand CSS)", "Low", "2", "1 Dev", "REUSE: FAQ expandable, accessible", True),
        ("3.6", "", "Video Embed Block (library + brand CSS)", "Low", "2", "1 Dev", "REUSE: YouTube/custom player", True),
        ("3.7", "", "Breadcrumb Block (library + brand CSS)", "Low", "1", "1 Dev", "REUSE: Auto-generated from nav", True),
        ("3.8", "", "Call-to-Action Block (library + brand CSS)", "Low", "2", "1 Dev", "REUSE: Banner CTA variants", True),
        ("3.9", "", "Columns/Grid Block (library + brand CSS)", "Low", "2", "1 Dev", "REUSE: Responsive grid layouts", True),
        ("3.10", "", "Image Gallery Block (library + brand CSS)", "Low", "2", "1 Dev", "REUSE: Lightbox, grid layout", True),
        ("", "", "Subtotal - Reuse Blocks (10 blocks)", "", "22", "", "Avg 2.2 days/block", False),

        # Section: Block Development — EXTEND (Customize)
        ("", "BLOCK DEVELOPMENT — EXTEND (Library foundation + customization)", "", "", "", "", "", False),
        ("3.11", "", "FAQ Accordion Block (extend w/ schema)", "Medium", "4", "1 Dev", "EXTEND: Add structured data, search", False),
        ("3.12", "", "Contact Form Block (extend w/ multi-step)", "High", "8", "1 Dev", "EXTEND: Multi-step, validation, conditional", False),
        ("3.13", "", "News/Blog Listing Block (extend w/ filters)", "Medium", "6", "1 Dev", "EXTEND: Add pagination, sorting, filters", False),
        ("3.14", "", "Event Listing Block (extend w/ dates)", "Medium", "5", "1 Dev", "EXTEND: Date filters, card layout", False),
        ("3.15", "", "Download/Resources Block (extend)", "Medium", "4", "1 Dev", "EXTEND: File downloads with filters", False),
        ("3.16", "", "Related Content Block (extend)", "Medium", "4", "1 Dev", "EXTEND: Dynamic recommendations", False),
        ("3.17", "", "Statistics/Counter Block (extend)", "Low", "3", "1 Dev", "EXTEND: Add animation, custom styling", False),
        ("3.18", "", "Cookie Consent Integration (extend)", "Medium", "6", "1 Dev", "EXTEND: OneTrust integration + GDPR", False),
        ("", "", "Subtotal - Extend Blocks (8 blocks)", "", "40", "", "Avg 5 days/block", False),

        # Section: Block Development — CUSTOM (New Build)
        ("", "BLOCK DEVELOPMENT — CUSTOM (No library equivalent)", "", "", "", "", "", False),
        ("3.19", "", "Product Specs Table Block", "High", "10", "1 Dev", "CUSTOM: Dynamic tables, responsive, filterable", False),
        ("3.20", "", "Regional Contact Tabs Block", "Medium", "6", "1 Dev", "CUSTOM: Region-based content switching", False),
        ("3.21", "", "Application Showcase Block", "Medium", "5", "1 Dev", "CUSTOM: AI, Server, Auto, Network cards", False),
        ("3.22", "", "Foundry Services Block", "Medium", "5", "1 Dev", "CUSTOM: Process tech showcase", False),
        ("3.23", "", "Partner/Logo Ecosystem Block (SAFE™)", "Low", "3", "1 Dev", "CUSTOM: Interactive partner grid", False),
        ("3.24", "", "Sustainability Highlights Block", "Medium", "4", "1 Dev", "CUSTOM: Story cards, metrics display", False),
        ("", "", "Subtotal - Custom Blocks (6 blocks)", "", "33", "", "Avg 5.5 days/block", False),

        ("", "", "TOTAL BLOCK DEVELOPMENT (24 blocks)", "", "95", "", "35% savings vs. full custom (was 147)", False),

        # Section: Content & Asset Migration — INCREASED due to DAM size
        ("", "CONTENT & ASSET MIGRATION (DAM: 224.62 GB / 1.6M nodes)", "", "", "", "", "", False),
        ("4.1", "", "Import Script Development", "High", "12", "1 Dev", "AEM Importer customization for Samsung", False),
        ("4.2", "", "DAM Asset Audit & Cleanup", "High", "10", "1 Dev + 1 Content", "Identify active assets from 224GB, remove duplicates", False),
        ("4.3", "", "Asset Migration — Phase 1 (Critical)", "High", "15", "1 Dev", "Product images, hero assets, logos (~50GB est.)", False),
        ("4.4", "", "Asset Migration — Phase 2 (Supporting)", "Medium", "12", "1 Dev", "Blog images, event media, documents (~80GB est.)", False),
        ("4.5", "", "Asset Optimization & CDN Setup", "High", "10", "1 Dev", "Format conversion, compression, CDN config", False),
        ("4.6", "", "Content Migration - Products (50+ pages)", "High", "18", "1 Dev + 1 Content", "Automated + manual QA", False),
        ("4.7", "", "Content Migration - Corporate (30+ pages)", "Medium", "8", "1 Content", "About, Sustainability, Careers", False),
        ("4.8", "", "Content Migration - News/Blog (100+ pages)", "Medium", "12", "1 Dev + 1 Content", "Bulk import, metadata", False),
        ("4.9", "", "Content Migration - Foundry (40+ pages)", "High", "12", "1 Dev + 1 Content", "Complex layouts", False),
        ("4.10", "", "Content Migration - Support (20+ pages)", "Medium", "6", "1 Content", "Resources, tools", False),
        ("4.11", "", "URL Redirect Mapping", "Medium", "8", "1 Dev", "301 redirects, SEO preservation", False),
        ("4.12", "", "Metadata & SEO Migration", "Medium", "7", "1 Dev", "Schema, OG tags, sitemap", False),
        ("", "", "Subtotal - Content & Asset Migration", "", "130", "", "Increased from 106 due to DAM size", False),

        # Section: Integrations
        ("", "INTEGRATIONS", "", "", "", "", "", False),
        ("5.1", "", "Search Integration (Algolia/Coveo)", "High", "10", "1 Dev", "Index, UI, suggestions", False),
        ("5.2", "", "Analytics Setup (Adobe Analytics)", "Medium", "6", "1 Dev", "Event tracking, data layer", False),
        ("5.3", "", "Form Submission Backend", "Medium", "5", "1 Dev", "API endpoints, notifications", False),
        ("5.4", "", "CDN & Edge Configuration", "Medium", "4", "1 DevOps", "Caching, headers, security", False),
        ("5.5", "", "SSO/Authentication (if needed)", "High", "7", "1 Dev", "B2B portal access", False),
        ("", "", "Subtotal - Integrations", "", "32", "", "", False),

        # Section: Testing & QA
        ("", "TESTING & QUALITY ASSURANCE", "", "", "", "", "", False),
        ("6.1", "", "Performance Testing & Optimization", "High", "8", "1 Dev", "Lighthouse 95+, Core Web Vitals", False),
        ("6.2", "", "Accessibility Testing (WCAG 2.1 AA)", "High", "8", "1 QA", "Screen readers, keyboard nav", False),
        ("6.3", "", "Cross-browser/Device Testing", "Medium", "6", "1 QA", "Chrome, Safari, Firefox, Edge, mobile", False),
        ("6.4", "", "Content QA (all locales)", "High", "12", "2 QA", "Visual regression, links, media", False),
        ("6.5", "", "Asset Integrity Verification", "Medium", "5", "1 QA", "Verify migrated DAM assets render correctly", False),
        ("6.6", "", "SEO Validation", "Medium", "4", "1 Dev", "Rankings preservation, crawl test", False),
        ("6.7", "", "Security Testing", "Medium", "4", "1 DevOps", "Headers, CSP, vulnerability scan", False),
        ("6.8", "", "UAT Support", "Medium", "8", "1 Dev + 1 QA", "Bug fixes, stakeholder feedback", False),
        ("", "", "Subtotal - Testing & QA", "", "55", "", "", False),

        # Section: Launch & Handover
        ("", "LAUNCH & HANDOVER", "", "", "", "", "", False),
        ("7.1", "", "Go-Live Planning & Cutover", "High", "5", "1 PM + 1 Dev", "DNS, CDN switch, monitoring", False),
        ("7.2", "", "Author Training & Documentation", "Medium", "6", "1 PM", "Content author guides", False),
        ("7.3", "", "Developer Handover", "Medium", "4", "1 Dev", "Code docs, architecture guide", False),
        ("7.4", "", "Post-Launch Hypercare (2 weeks)", "Medium", "10", "1 Dev", "Monitoring, hotfixes", False),
        ("", "", "Subtotal - Launch & Handover", "", "25", "", "", False),

        # Grand Total
        ("", "GRAND TOTAL - SEMICONDUCTOR ONLY (REVISED)", "", "", "437", "", "~20-22 weeks with 4-5 FTEs", False),
    ]

    for i, task in enumerate(semi_tasks):
        for col, val in enumerate(task[:7], 2):
            ws_semi.cell(row=row, column=col, value=val)

        is_section = task[0] == "" and task[1] != "" and task[2] == ""
        is_subtotal = "Subtotal" in str(task[2]) or "GRAND TOTAL" in str(task[1]) or "TOTAL BLOCK" in str(task[2])
        is_reuse = task[7] if len(task) > 7 else False
        style_data_row(ws_semi, row, 8, is_alt=(i % 2 == 0), is_total=is_subtotal, is_section=is_section, is_reuse=is_reuse)
        row += 1

    # ============================================================
    # SHEET 3: Detailed Estimate - LED Website (REVISED)
    # ============================================================
    ws_led = wb.create_sheet("LED Website - Detailed")
    ws_led.sheet_properties.tabColor = "00A86B"

    for i, w in enumerate(col_widths, 1):
        ws_led.column_dimensions[get_column_letter(i)].width = w

    row = 2
    ws_led.cell(row=row, column=2, value="Samsung LED Website - Additional EDS Migration Effort (REVISED)").font = title_font
    row += 1
    ws_led.cell(row=row, column=2, value="Incremental effort when combined with Semiconductor migration").font = subtitle_font
    row += 1
    ws_led.cell(row=row, column=2, value="Additional DAM: ~4.55 GB (test folder — LED assets subset of samsung folder)").font = Font(name="Adobe Clean", size=10, italic=True, color=ADOBE_GRAY)
    row += 2

    headers_led = ["#", "Work Stream", "Task", "Complexity", "Effort (Days)", "Resources", "Notes"]
    for col, h in enumerate(headers_led, 2):
        ws_led.cell(row=row, column=col, value=h)
    style_header_row(ws_led, row, 8)
    row += 1

    led_tasks = [
        ("", "DISCOVERY (INCREMENTAL)", "", "", "", "", "", False),
        ("L1.1", "", "LED Site Audit & Inventory", "Medium", "5", "1 Architect", "Product catalog, templates", False),
        ("L1.2", "", "LED-specific Template Mapping", "Medium", "3", "1 Architect", "3 additional templates", False),
        ("L1.3", "", "LED Navigation & IA Design", "Medium", "3", "1 Architect", "Separate nav structure", False),
        ("", "", "Subtotal - Discovery", "", "11", "", "", False),

        ("", "LED BLOCKS — REUSE (Style Only)", "", "", "", "", "", False),
        ("L2.1", "", "LED Product Category Block (reuse Cards)", "Low", "3", "1 Dev", "REUSE: Brand styling for Mid/High/CSP/COB", True),
        ("L2.2", "", "LED Application Gallery Block (reuse Gallery)", "Low", "2", "1 Dev", "REUSE: Horticulture, automotive galleries", True),
        ("L2.3", "", "Quick Downloads Block (reuse Resources)", "Low", "2", "1 Dev", "REUSE: Datasheet repository styling", True),
        ("", "", "Subtotal - LED Reuse Blocks", "", "7", "", "Avg 2.3 days/block", False),

        ("", "LED BLOCKS — EXTEND", "", "", "", "", "", False),
        ("L2.4", "", "LED Spec Comparison Block (extend Table)", "Medium", "6", "1 Dev", "EXTEND: Multi-product comparison", False),
        ("L2.5", "", "Automotive LED Showcase (extend Cards)", "Medium", "4", "1 Dev", "EXTEND: Application-specific display", False),
        ("L2.6", "", "In-branding Program Block (extend)", "Low", "3", "1 Dev", "EXTEND: Partner program info", False),
        ("", "", "Subtotal - LED Extend Blocks", "", "13", "", "Avg 4.3 days/block", False),

        ("", "LED BLOCKS — CUSTOM (No library equivalent)", "", "", "", "", "", False),
        ("L2.7", "", "LED Component Calculator", "High", "12", "1 Dev", "CUSTOM: Interactive design calculator", False),
        ("L2.8", "", "LED Engine Calculator", "High", "10", "1 Dev", "CUSTOM: Performance modeling tool", False),
        ("L2.9", "", "LED Module Configurator", "High", "8", "1 Dev", "CUSTOM: Product selection wizard", False),
        ("L2.10", "", "Virtual Exhibition Block", "High", "10", "1 Dev", "CUSTOM: Interactive virtual tour/3D", False),
        ("", "", "Subtotal - LED Custom Blocks", "", "40", "", "Avg 10 days/block", False),

        ("", "", "TOTAL LED BLOCK DEVELOPMENT (10 blocks)", "", "60", "", "Reduced from 72 with reuse strategy", False),

        ("", "LED CONTENT MIGRATION", "", "", "", "", "", False),
        ("L3.1", "", "LED Import Script Customization", "Medium", "5", "1 Dev", "LED-specific parsers", False),
        ("L3.2", "", "LED Product Pages (20+ pages)", "Medium", "8", "1 Dev + 1 Content", "All product lines", False),
        ("L3.3", "", "LED Application Pages (10+ pages)", "Medium", "5", "1 Content", "Lighting, Auto, Display", False),
        ("L3.4", "", "LED Support & Tools Pages", "Medium", "4", "1 Content", "Calculators, downloads", False),
        ("L3.5", "", "LED News & Events Pages", "Low", "3", "1 Content", "Articles, event listings", False),
        ("L3.6", "", "LED Asset Migration", "Medium", "4", "1 Dev", "Product images, datasheets", False),
        ("L3.7", "", "LED URL Redirects", "Low", "3", "1 Dev", "led.samsung.com mapping", False),
        ("", "", "Subtotal - Content Migration", "", "32", "", "", False),

        ("", "LED INTEGRATIONS & TESTING", "", "", "", "", "", False),
        ("L4.1", "", "LED Regional Support (6 regions)", "High", "8", "1 Dev", "America, EMEA, CN, SEA, JP, KR", False),
        ("L4.2", "", "LED Sales Network Integration", "Medium", "5", "1 Dev", "Regional sales contacts", False),
        ("L4.3", "", "LED-specific Testing & QA", "Medium", "6", "1 QA", "Calculator validation, cross-browser", False),
        ("L4.4", "", "LED Performance Optimization", "Medium", "4", "1 Dev", "Calculator load performance", False),
        ("", "", "Subtotal - Integrations & Testing", "", "23", "", "", False),

        ("", "GRAND TOTAL - LED INCREMENTAL (REVISED)", "", "", "126", "", "~5-6 additional weeks", False),
    ]

    for i, task in enumerate(led_tasks):
        for col, val in enumerate(task[:7], 2):
            ws_led.cell(row=row, column=col, value=val)

        is_section = task[0] == "" and task[1] != "" and task[2] == ""
        is_subtotal = "Subtotal" in str(task[2]) or "GRAND TOTAL" in str(task[1]) or "TOTAL LED" in str(task[2])
        is_reuse = task[7] if len(task) > 7 else False
        style_data_row(ws_led, row, 8, is_alt=(i % 2 == 0), is_total=is_subtotal, is_section=is_section, is_reuse=is_reuse)
        row += 1

    # ============================================================
    # SHEET 4: Combined Summary (REVISED)
    # ============================================================
    ws_combined = wb.create_sheet("Combined Summary")
    ws_combined.sheet_properties.tabColor = ADOBE_RED

    ws_combined.column_dimensions['A'].width = 5
    ws_combined.column_dimensions['B'].width = 45
    ws_combined.column_dimensions['C'].width = 20
    ws_combined.column_dimensions['D'].width = 20
    ws_combined.column_dimensions['E'].width = 20
    ws_combined.column_dimensions['F'].width = 20

    row = 2
    ws_combined.cell(row=row, column=2, value="Migration Effort Summary — All Scenarios (REVISED v2.0)").font = title_font
    row += 1
    ws_combined.cell(row=row, column=2, value="Optimized with AEM Block Library reuse | DAM: 229 GB").font = subtitle_font
    row += 3

    # Summary headers
    sum_headers = ["Work Stream", "Semi Only (Days)", "LED Incr. (Days)", "Combined (Days)", "Combined (Weeks)"]
    for col, h in enumerate(sum_headers, 2):
        ws_combined.cell(row=row, column=col, value=h)
    style_header_row(ws_combined, row, 6)
    row += 1

    summary_data = [
        ("Discovery & Architecture", "45", "11", "56", "2.5"),
        ("Foundation & Setup", "55", "—", "55", "2.5"),
        ("Block Development — Reuse (style only)", "22", "7", "29", "1.5"),
        ("Block Development — Extend (customize)", "40", "13", "53", "2.5"),
        ("Block Development — Custom (new build)", "33", "40", "73", "3.5"),
        ("Content & Asset Migration", "130", "32", "162", "7.5"),
        ("Integrations", "32", "13", "45", "2"),
        ("Testing & QA", "55", "10", "65", "3"),
        ("Launch & Handover", "25", "—", "25", "1"),
    ]

    for i, (stream, semi, led, combined, weeks) in enumerate(summary_data):
        ws_combined.cell(row=row, column=2, value=stream)
        ws_combined.cell(row=row, column=3, value=semi)
        ws_combined.cell(row=row, column=4, value=led)
        ws_combined.cell(row=row, column=5, value=combined)
        ws_combined.cell(row=row, column=6, value=weeks)
        is_reuse = "Reuse" in stream
        style_data_row(ws_combined, row, 6, is_alt=(i % 2 == 0), is_reuse=is_reuse)
        row += 1

    # Totals
    totals = [
        ("TOTAL - Semiconductor Only (Revised)", "437", "—", "437", "~20-22"),
        ("TOTAL - LED Incremental (Revised)", "—", "126", "126", "~5-6"),
        ("TOTAL - Combined Semi + LED (Revised)", "437", "126", "563", "~24-28"),
    ]

    for label, semi, led, combined, weeks in totals:
        ws_combined.cell(row=row, column=2, value=label)
        ws_combined.cell(row=row, column=3, value=semi)
        ws_combined.cell(row=row, column=4, value=led)
        ws_combined.cell(row=row, column=5, value=combined)
        ws_combined.cell(row=row, column=6, value=weeks)
        style_data_row(ws_combined, row, 6, is_total=True)
        row += 1

    # Comparison with original
    row += 2
    ws_combined.cell(row=row, column=2, value="SAVINGS vs. ORIGINAL ESTIMATE (Full Custom Development)").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_GREEN)
    row += 2

    savings_headers = ["Scenario", "Original (Days)", "Revised (Days)", "Savings (Days)", "Savings (%)"]
    for col, h in enumerate(savings_headers, 2):
        ws_combined.cell(row=row, column=col, value=h)
    style_header_row(ws_combined, row, 6)
    row += 1

    savings_data = [
        ("Semiconductor Only", "485", "437", "48", "~10%"),
        ("LED Incremental", "152", "126", "26", "~17%"),
        ("Combined", "637", "563", "74", "~12%"),
    ]

    for i, (scenario, orig, revised, saved, pct) in enumerate(savings_data):
        ws_combined.cell(row=row, column=2, value=scenario)
        ws_combined.cell(row=row, column=3, value=orig)
        ws_combined.cell(row=row, column=4, value=revised)
        ws_combined.cell(row=row, column=5, value=saved)
        ws_combined.cell(row=row, column=6, value=pct)
        style_data_row(ws_combined, row, 6, is_alt=(i % 2 == 0))
        row += 1

    row += 1
    ws_combined.cell(row=row, column=2, value="Note: Block development reduced 35% (147→95 for Semi, 72→60 for LED). Asset migration increased due to 229GB DAM.").font = Font(name="Adobe Clean", size=9, italic=True, color=ADOBE_GRAY)

    row += 3
    ws_combined.cell(row=row, column=2, value="COST ESTIMATION (Based on Adobe Professional Services Rates) — REVISED").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_RED)
    row += 2

    cost_headers = ["Scenario", "Person-Days", "Team Size", "Duration", "Est. Cost Range (USD)"]
    for col, h in enumerate(cost_headers, 2):
        ws_combined.cell(row=row, column=col, value=h)
    style_header_row(ws_combined, row, 6)
    row += 1

    cost_data = [
        ("Semiconductor Only", "437", "4-5 FTEs", "18-22 weeks", "$760K - $960K"),
        ("LED Only (standalone*)", "255", "3-4 FTEs", "12-16 weeks", "$445K - $560K"),
        ("Combined (Semi + LED)", "563", "5-6 FTEs", "24-28 weeks", "$985K - $1.24M"),
    ]

    for i, (scenario, days, team, duration, cost) in enumerate(cost_data):
        ws_combined.cell(row=row, column=2, value=scenario)
        ws_combined.cell(row=row, column=3, value=days)
        ws_combined.cell(row=row, column=4, value=team)
        ws_combined.cell(row=row, column=5, value=duration)
        ws_combined.cell(row=row, column=6, value=cost)
        style_data_row(ws_combined, row, 6, is_alt=(i % 2 == 0))
        row += 1

    row += 2
    ws_combined.cell(row=row, column=2, value="* LED standalone includes shared foundation effort absorbed in combined scenario").font = Font(name="Adobe Clean", size=9, italic=True, color=ADOBE_GRAY)
    row += 1
    ws_combined.cell(row=row, column=2, value="Cost estimates based on blended rate of $1,750-$2,200/day for Adobe Professional Services").font = Font(name="Adobe Clean", size=9, italic=True, color=ADOBE_GRAY)
    row += 1
    ws_combined.cell(row=row, column=2, value="Combined approach saves ~$160K-$250K vs. separate projects due to shared foundation & design system").font = Font(name="Adobe Clean", size=9, italic=True, color=ADOBE_GREEN)

    # ============================================================
    # SHEET 5: Block Reuse Analysis (NEW SHEET)
    # ============================================================
    ws_reuse = wb.create_sheet("Block Reuse Analysis")
    ws_reuse.sheet_properties.tabColor = ADOBE_GREEN

    ws_reuse.column_dimensions['A'].width = 5
    ws_reuse.column_dimensions['B'].width = 35
    ws_reuse.column_dimensions['C'].width = 15
    ws_reuse.column_dimensions['D'].width = 15
    ws_reuse.column_dimensions['E'].width = 15
    ws_reuse.column_dimensions['F'].width = 40
    ws_reuse.column_dimensions['G'].width = 35

    row = 2
    ws_reuse.cell(row=row, column=2, value="Block Reuse Analysis — AEM Block Library / Block Party / Boilerplate").font = title_font
    row += 2
    ws_reuse.cell(row=row, column=2, value="Blocks categorized by reuse tier to optimize development effort").font = subtitle_font
    row += 3

    reuse_headers = ["Block Name", "Tier", "Original (Days)", "Revised (Days)", "Library Source", "Customization Required"]
    for col, h in enumerate(reuse_headers, 2):
        ws_reuse.cell(row=row, column=col, value=h)
    style_header_row(ws_reuse, row, 7)
    row += 1

    reuse_blocks = [
        # REUSE blocks
        ("Hero/Banner", "REUSE", "8", "3", "Block Collection", "Brand CSS, Samsung typography"),
        ("Cards", "REUSE", "6", "3", "Block Collection", "Brand CSS, card variants"),
        ("Carousel/Slider", "REUSE", "6", "3", "Block Collection", "Brand CSS, touch behavior"),
        ("Tabs", "REUSE", "5", "2", "Block Collection", "Brand CSS only"),
        ("Accordion", "REUSE", "4", "2", "EDS Boilerplate", "Brand CSS, Samsung styling"),
        ("Video Embed", "REUSE", "5", "2", "Block Collection", "Brand CSS, player skin"),
        ("Breadcrumb", "REUSE", "2", "1", "Block Collection", "Minimal styling"),
        ("Call-to-Action", "REUSE", "3", "2", "Block Collection", "Brand colors, hover states"),
        ("Columns/Grid", "REUSE", "—", "2", "EDS Boilerplate", "Responsive breakpoints"),
        ("Image Gallery", "REUSE", "5", "2", "Block Collection", "Lightbox, Samsung styling"),
        # EXTEND blocks
        ("FAQ (with schema)", "EXTEND", "4", "4", "Block Collection + custom", "Add structured data, search integration"),
        ("Contact Form (multi-step)", "EXTEND", "12", "8", "Block Collection + custom", "Multi-step wizard, conditional fields"),
        ("News/Blog Listing", "EXTEND", "10", "6", "Block Collection + custom", "Add filters, pagination, sorting"),
        ("Event Listing", "EXTEND", "6", "5", "Block Collection + custom", "Date filtering, card layout"),
        ("Downloads/Resources", "EXTEND", "5", "4", "Block Collection + custom", "Category filters, file types"),
        ("Related Content", "EXTEND", "5", "4", "Block Collection + custom", "Dynamic content logic"),
        ("Statistics/Counter", "EXTEND", "3", "3", "Block Collection + custom", "Custom animations"),
        ("Cookie Consent", "EXTEND", "8", "6", "OneTrust SDK", "Samsung privacy requirements"),
        # CUSTOM blocks
        ("Product Specs Table", "CUSTOM", "10", "10", "None — full build", "Dynamic data, responsive, filterable"),
        ("Regional Contact Tabs", "CUSTOM", "5", "6", "None — full build", "Region switching, dynamic data"),
        ("Application Showcase", "CUSTOM", "5", "5", "None — full build", "Category-specific layouts"),
        ("Foundry Services", "CUSTOM", "6", "5", "None — full build", "Process technology display"),
        ("Partner/Logo Ecosystem", "CUSTOM", "3", "3", "None — full build", "SAFE™ partner interactions"),
        ("Sustainability Highlights", "CUSTOM", "5", "4", "None — full build", "Metrics + story cards"),
    ]

    for i, (block, tier, orig, revised, source, customization) in enumerate(reuse_blocks):
        ws_reuse.cell(row=row, column=2, value=block)
        ws_reuse.cell(row=row, column=3, value=tier)
        ws_reuse.cell(row=row, column=4, value=orig)
        ws_reuse.cell(row=row, column=5, value=revised)
        ws_reuse.cell(row=row, column=6, value=source)
        ws_reuse.cell(row=row, column=7, value=customization)
        is_reuse = tier == "REUSE"
        style_data_row(ws_reuse, row, 7, is_alt=(i % 2 == 0), is_reuse=is_reuse)
        # Color the tier cell
        tier_cell = ws_reuse.cell(row=row, column=3)
        if tier == "REUSE":
            tier_cell.font = Font(name="Adobe Clean", size=10, bold=True, color=ADOBE_GREEN)
        elif tier == "EXTEND":
            tier_cell.font = Font(name="Adobe Clean", size=10, bold=True, color=ADOBE_BLUE)
        elif tier == "CUSTOM":
            tier_cell.font = Font(name="Adobe Clean", size=10, bold=True, color=ADOBE_RED)
        row += 1

    # Summary at bottom
    row += 2
    summary_items = [
        ("REUSE (10 blocks)", "44 → 22 days", "50% savings", "Only brand CSS customization needed"),
        ("EXTEND (8 blocks)", "53 → 40 days", "25% savings", "Library foundation + logic modifications"),
        ("CUSTOM (6 blocks)", "34 → 33 days", "~3% savings", "Full development required — no library equivalent"),
        ("TOTAL (24 blocks)", "147 → 95 days", "35% savings", ""),
    ]

    ws_reuse.cell(row=row, column=2, value="Tier").font = header_font
    ws_reuse.cell(row=row, column=3, value="Effort Change").font = header_font
    ws_reuse.cell(row=row, column=4, value="Savings").font = header_font
    ws_reuse.cell(row=row, column=5, value="").font = header_font
    ws_reuse.cell(row=row, column=6, value="Rationale").font = header_font
    for col in range(2, 7):
        ws_reuse.cell(row=row, column=col).fill = header_fill
        ws_reuse.cell(row=row, column=col).border = thin_border
        ws_reuse.cell(row=row, column=col).alignment = center_align
    row += 1

    for i, (tier, change, savings, rationale) in enumerate(summary_items):
        ws_reuse.cell(row=row, column=2, value=tier)
        ws_reuse.cell(row=row, column=3, value=change)
        ws_reuse.cell(row=row, column=4, value=savings)
        ws_reuse.cell(row=row, column=6, value=rationale)
        is_t = (i == len(summary_items) - 1)
        style_data_row(ws_reuse, row, 7, is_total=is_t, is_alt=(i % 2 == 0))
        row += 1

    # ============================================================
    # SHEET 6: Resource Plan
    # ============================================================
    ws_resource = wb.create_sheet("Resource Plan")
    ws_resource.sheet_properties.tabColor = ADOBE_GRAY

    ws_resource.column_dimensions['A'].width = 5
    ws_resource.column_dimensions['B'].width = 25
    ws_resource.column_dimensions['C'].width = 15
    ws_resource.column_dimensions['D'].width = 50
    ws_resource.column_dimensions['E'].width = 20

    row = 2
    ws_resource.cell(row=row, column=2, value="Recommended Team Structure (Revised)").font = title_font
    row += 3

    res_headers = ["Role", "Count", "Responsibilities", "Duration"]
    for col, h in enumerate(res_headers, 2):
        ws_resource.cell(row=row, column=col, value=h)
    style_header_row(ws_resource, row, 5)
    row += 1

    resources = [
        ("Solution Architect", "1", "Architecture design, block library mapping, DAM strategy, oversight", "Full duration"),
        ("Senior EDS Developer", "2", "Block development (extend/custom), integrations, performance", "Full duration"),
        ("Frontend Developer", "1", "Block styling (reuse tier), responsive design, accessibility", "Weeks 3-20"),
        ("Content/DAM Engineer", "1", "DAM audit, asset migration (229GB), import scripts, content QA", "Weeks 6-22"),
        ("QA Engineer", "1", "Testing, accessibility audit, cross-browser, asset verification", "Weeks 12-24"),
        ("Project Manager", "1", "Planning, coordination, stakeholder management, training", "Full duration"),
        ("UX Designer", "0.5", "Design system extraction, component design review", "Weeks 1-6"),
        ("DevOps Engineer", "0.5", "CDN config, CI/CD, security, DAM migration tooling", "Weeks 2-6, 18-24"),
    ]

    for i, (role, count, resp, duration) in enumerate(resources):
        ws_resource.cell(row=row, column=2, value=role)
        ws_resource.cell(row=row, column=3, value=count)
        ws_resource.cell(row=row, column=4, value=resp)
        ws_resource.cell(row=row, column=5, value=duration)
        style_data_row(ws_resource, row, 5, is_alt=(i % 2 == 0))
        row += 1

    # ============================================================
    # SHEET 7: Risk Register
    # ============================================================
    ws_risk = wb.create_sheet("Risk Register")
    ws_risk.sheet_properties.tabColor = "FF6600"

    ws_risk.column_dimensions['A'].width = 5
    ws_risk.column_dimensions['B'].width = 8
    ws_risk.column_dimensions['C'].width = 40
    ws_risk.column_dimensions['D'].width = 12
    ws_risk.column_dimensions['E'].width = 12
    ws_risk.column_dimensions['F'].width = 50
    ws_risk.column_dimensions['G'].width = 20

    row = 2
    ws_risk.cell(row=row, column=2, value="Risk Register (Revised)").font = title_font
    row += 3

    risk_headers = ["ID", "Risk Description", "Likelihood", "Impact", "Mitigation Strategy", "Owner"]
    for col, h in enumerate(risk_headers, 2):
        ws_risk.cell(row=row, column=col, value=h)
    style_header_row(ws_risk, row, 7)
    row += 1

    risks = [
        ("R1", "DAM size (229GB) contains significant archival/unused assets", "High", "Medium", "DAM audit in Phase 1; classify active vs archive; migrate only active assets", "Content Engineer"),
        ("R2", "Asset migration throughput — 224GB transfer time exceeds estimate", "Medium", "High", "Phased migration; parallel transfer; compress before migrating; CDN pre-warm", "DevOps"),
        ("R3", "Block Library blocks don't match Samsung's exact UX patterns", "Medium", "Medium", "POC in Phase 1 for 2-3 key blocks; budget buffer for Extend tier blocks", "Tech Lead"),
        ("R4", "LED Calculator tools exceed complexity estimates", "Medium", "High", "Dedicated spike/POC in Phase 1; consider third-party widget as fallback", "Tech Lead"),
        ("R5", "Content volume larger than estimated (hidden/unpublished pages)", "High", "Medium", "Automated crawl + JCR query in discovery; 20% buffer for content migration", "Architect"),
        ("R6", "Multi-language content sync issues", "Medium", "High", "Establish i18n workflow early; test with 2 locales first before full rollout", "Architect"),
        ("R7", "Performance regression on asset-heavy pages", "Medium", "High", "Image optimization pipeline; lazy loading; Lighthouse monitoring per sprint", "Dev Lead"),
        ("R8", "SEO ranking impact during migration", "Medium", "High", "Comprehensive redirect map; staged rollout; 90-day monitoring period", "SEO Specialist"),
        ("R9", "AEM On-Prem content export/access challenges", "Medium", "Medium", "Early access to AEM instance; JCR export tools; backup VLT strategy", "Dev Lead"),
        ("R10", "Stakeholder availability for UAT", "High", "Medium", "Schedule UAT windows early; provide async review tools; staged sign-off", "PM"),
        ("R11", "DAM node count (1.69M) causes import script performance issues", "Medium", "Medium", "Batch processing; parallel import workers; incremental sync approach", "Content Engineer"),
    ]

    for i, (rid, desc, like, impact, mitigation, owner) in enumerate(risks):
        ws_risk.cell(row=row, column=2, value=rid)
        ws_risk.cell(row=row, column=3, value=desc)
        ws_risk.cell(row=row, column=4, value=like)
        ws_risk.cell(row=row, column=5, value=impact)
        ws_risk.cell(row=row, column=6, value=mitigation)
        ws_risk.cell(row=row, column=7, value=owner)
        style_data_row(ws_risk, row, 7, is_alt=(i % 2 == 0))
        row += 1

    # ============================================================
    # SHEET 8: Timeline (Revised)
    # ============================================================
    ws_timeline = wb.create_sheet("Timeline")
    ws_timeline.sheet_properties.tabColor = "9B59B6"

    ws_timeline.column_dimensions['A'].width = 5
    ws_timeline.column_dimensions['B'].width = 35
    for i in range(3, 32):
        ws_timeline.column_dimensions[get_column_letter(i)].width = 4

    row = 2
    ws_timeline.cell(row=row, column=2, value="Project Timeline — Combined Semi + LED (REVISED)").font = title_font
    row += 1
    ws_timeline.cell(row=row, column=2, value="24-28 weeks (reduced from 28-32 with block reuse)").font = subtitle_font
    row += 2

    # Week headers
    ws_timeline.cell(row=row, column=2, value="Phase / Activity")
    for w in range(1, 29):
        ws_timeline.cell(row=row, column=w + 2, value=f"W{w}")
    style_header_row(ws_timeline, row, 30)
    row += 1

    # Timeline data (phase, start_week, end_week)
    phases = [
        ("Phase 1: Discovery & DAM Audit", 1, 4),
        ("Phase 2: Foundation & Setup", 3, 6),
        ("Phase 3a: Block Reuse (style only)", 5, 7),
        ("Phase 3b: Block Extend (customize)", 6, 10),
        ("Phase 3c: Block Custom (Semi)", 8, 14),
        ("Phase 3d: Block Custom (LED)", 12, 18),
        ("Phase 4a: DAM/Asset Migration", 8, 16),
        ("Phase 4b: Content Migration", 10, 18),
        ("Phase 5: Integrations", 12, 16),
        ("Phase 6: Testing & QA", 16, 22),
        ("Phase 7: UAT & Launch Prep", 20, 24),
        ("Phase 8: Go-Live & Hypercare", 24, 28),
    ]

    colors = ["4A90D9", "2ECC71", ADOBE_GREEN, "27AE60", "E74C3C", "E67E22",
              "9B59B6", "F39C12", "1ABC9C", "3498DB", "E91E63", ADOBE_RED]

    for i, (phase, start, end) in enumerate(phases):
        ws_timeline.cell(row=row, column=2, value=phase).font = body_bold_font
        ws_timeline.cell(row=row, column=2).border = thin_border
        for w in range(1, 29):
            cell = ws_timeline.cell(row=row, column=w + 2)
            cell.border = thin_border
            if start <= w <= end:
                cell.fill = PatternFill(start_color=colors[i], end_color=colors[i], fill_type="solid")
        row += 1

    row += 2
    ws_timeline.cell(row=row, column=2, value="Legend:").font = body_bold_font
    row += 1
    ws_timeline.cell(row=row, column=2, value="Green bars = Block Library reuse phases (accelerated)").font = body_font
    row += 1
    ws_timeline.cell(row=row, column=2, value="Purple bar = DAM/Asset migration (extended due to 229GB volume)").font = body_font
    row += 1
    ws_timeline.cell(row=row, column=2, value="Semi-only timeline: ~20-22 weeks (remove LED phases)").font = body_font
    row += 1
    ws_timeline.cell(row=row, column=2, value="Combined timeline: ~24-28 weeks (reduced from 28-32)").font = body_font

    # Save
    output_path = "/backups/riteskum/lge-be-eds/repo/Samsung_EDS_Migration_Estimate.xlsx"
    wb.save(output_path)
    print(f"Revised estimate saved to: {output_path}")
    return output_path


if __name__ == "__main__":
    create_workbook()
