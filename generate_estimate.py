#!/usr/bin/env python3
"""
Generate AEM On-Premise to EDS Migration Estimate
Samsung Semiconductor + LED Website
Adobe Professional Format
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
HEADER_BG = "323232"

# Styles
title_font = Font(name="Adobe Clean", size=18, bold=True, color=ADOBE_DARK)
subtitle_font = Font(name="Adobe Clean", size=14, bold=True, color=ADOBE_GRAY)
header_font = Font(name="Adobe Clean", size=11, bold=True, color=ADOBE_WHITE)
body_font = Font(name="Adobe Clean", size=10, color=ADOBE_DARK)
body_bold_font = Font(name="Adobe Clean", size=10, bold=True, color=ADOBE_DARK)
total_font = Font(name="Adobe Clean", size=11, bold=True, color=ADOBE_RED)
section_font = Font(name="Adobe Clean", size=11, bold=True, color=ADOBE_BLUE)

header_fill = PatternFill(start_color=HEADER_BG, end_color=HEADER_BG, fill_type="solid")
alt_fill = PatternFill(start_color=ADOBE_LIGHT_GRAY, end_color=ADOBE_LIGHT_GRAY, fill_type="solid")
total_fill = PatternFill(start_color="FFF0F0", end_color="FFF0F0", fill_type="solid")
section_fill = PatternFill(start_color="E8F4FD", end_color="E8F4FD", fill_type="solid")

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


def style_data_row(ws, row, cols, is_alt=False, is_total=False, is_section=False):
    for col in range(1, cols + 1):
        cell = ws.cell(row=row, column=col)
        cell.border = thin_border
        if is_total:
            cell.font = total_font
            cell.fill = total_fill
        elif is_section:
            cell.font = section_font
            cell.fill = section_fill
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

    row = 2
    ws_exec.cell(row=row, column=2, value="ADOBE EXPERIENCE MANAGER").font = Font(name="Adobe Clean", size=10, color=ADOBE_RED, bold=True)
    row += 1
    ws_exec.cell(row=row, column=2, value="Edge Delivery Services Migration Estimate").font = title_font
    row += 1
    ws_exec.cell(row=row, column=2, value="Samsung Semiconductor & LED Division").font = subtitle_font
    row += 2

    # Project Overview
    ws_exec.cell(row=row, column=2, value="PROJECT OVERVIEW").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_RED)
    row += 2

    overview_items = [
        ("Client:", "Samsung Electronics - Semiconductor Division"),
        ("Source Platform:", "AEM On-Premise (6.x)"),
        ("Target Platform:", "AEM Edge Delivery Services (Cloud)"),
        ("Websites in Scope:", "semiconductor.samsung.com + led.samsung.com"),
        ("Date:", "May 2026"),
        ("Prepared by:", "Adobe Professional Services"),
    ]

    for label, value in overview_items:
        ws_exec.cell(row=row, column=2, value=label).font = body_bold_font
        ws_exec.cell(row=row, column=3, value=value).font = body_font
        row += 1

    row += 2
    ws_exec.cell(row=row, column=2, value="SCOPE SUMMARY").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_RED)
    row += 2

    # Scope table
    scope_headers = ["Metric", "Semiconductor Only", "Semiconductor + LED"]
    ws_exec.cell(row=row, column=2, value=scope_headers[0])
    ws_exec.cell(row=row, column=3, value=scope_headers[1])
    ws_exec.cell(row=row, column=4, value=scope_headers[2])
    ws_exec.column_dimensions['D'].width = 25
    for col in range(2, 5):
        cell = ws_exec.cell(row=row, column=col)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border
    row += 1

    scope_data = [
        ("Estimated Page Count", "350-500+", "400-580+"),
        ("Unique Page Templates", "7-9", "10-12"),
        ("Custom Blocks Required", "25-35", "32-42"),
        ("Languages/Locales", "4 (EN, KR, CN, JP)", "4 + 6 Regions"),
        ("Interactive Features", "8-10", "12-15"),
        ("Integrations", "5-7", "7-9"),
        ("Total Effort (Person-Days)", "480-600", "620-780"),
        ("Duration (Weeks)", "20-26", "26-32"),
    ]

    for i, (metric, semi, both) in enumerate(scope_data):
        ws_exec.cell(row=row, column=2, value=metric)
        ws_exec.cell(row=row, column=3, value=semi)
        ws_exec.cell(row=row, column=4, value=both)
        for col in range(2, 5):
            cell = ws_exec.cell(row=row, column=col)
            cell.border = thin_border
            cell.alignment = center_align if col > 2 else left_align
            if i == len(scope_data) - 2 or i == len(scope_data) - 1:
                cell.font = total_font
                cell.fill = total_fill
            elif i % 2 == 0:
                cell.fill = alt_fill
                cell.font = body_font
            else:
                cell.font = body_font
        row += 1

    row += 2
    ws_exec.cell(row=row, column=2, value="KEY ASSUMPTIONS & RISKS").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_RED)
    row += 2

    assumptions = [
        "• Content migration assumes automated tooling (AEM Importer) with manual QA for critical pages",
        "• Foundry section (samsungfoundry.com) B2B portal is OUT OF SCOPE (separate platform)",
        "• Consumer Storage section redirects to samsung.com — OUT OF SCOPE",
        "• Multi-language support requires i18n framework setup; content translation is client responsibility",
        "• Existing AEM DAM assets will be migrated to EDS-compatible format (optimized images)",
        "• Search functionality will leverage AEM EDS indexing or third-party search (Algolia/Coveo)",
        "• LED Calculator tools require custom JavaScript development and validation",
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
        "Phase 1: Discovery & Architecture (3-4 weeks) — Site audit, block inventory, template mapping",
        "Phase 2: Foundation Setup (3-4 weeks) — EDS project setup, design system, core blocks",
        "Phase 3: Block Development (6-8 weeks) — Custom blocks, interactive features, integrations",
        "Phase 4: Content Migration (4-6 weeks) — Automated import, manual QA, asset optimization",
        "Phase 5: Testing & Launch (4-6 weeks) — Performance, accessibility, UAT, go-live",
    ]

    for item in approach:
        ws_exec.cell(row=row, column=2, value=item).font = body_font
        row += 1

    # ============================================================
    # SHEET 2: Detailed Estimate - Semiconductor Only
    # ============================================================
    ws_semi = wb.create_sheet("Semiconductor - Detailed")
    ws_semi.sheet_properties.tabColor = ADOBE_BLUE

    # Column widths
    col_widths = [5, 8, 45, 15, 15, 15, 15, 40]
    for i, w in enumerate(col_widths, 1):
        ws_semi.column_dimensions[get_column_letter(i)].width = w

    row = 2
    ws_semi.cell(row=row, column=2, value="Samsung Semiconductor - EDS Migration Estimate (Excluding LED)").font = title_font
    row += 2

    # Headers
    headers = ["#", "Work Stream", "Task", "Complexity", "Effort (Days)", "Resources", "Notes"]
    for col, h in enumerate(headers, 2):
        ws_semi.cell(row=row, column=col, value=h)
    style_header_row(ws_semi, row, 8)
    row += 1

    # Data
    semi_tasks = [
        # Section: Discovery & Architecture
        ("", "DISCOVERY & ARCHITECTURE", "", "", "", "", ""),
        ("1.1", "", "Site Audit & Content Inventory", "Medium", "10", "1 Architect", "Crawl all pages, map content types"),
        ("1.2", "", "Template & Block Mapping", "High", "8", "1 Architect", "Map AEM components to EDS blocks"),
        ("1.3", "", "Information Architecture Review", "Medium", "5", "1 Architect", "Navigation, URL strategy, redirects"),
        ("1.4", "", "Technical Architecture Design", "High", "8", "1 Architect + 1 Dev", "Integration points, search, i18n"),
        ("1.5", "", "Design System Extraction", "Medium", "6", "1 Designer", "Tokens, typography, spacing, colors"),
        ("1.6", "", "Migration Strategy Document", "Low", "4", "1 PM", "Phasing, risk mitigation, timelines"),
        ("", "", "Subtotal - Discovery", "", "41", "", ""),

        # Section: Foundation & Setup
        ("", "FOUNDATION & SETUP", "", "", "", "", ""),
        ("2.1", "", "EDS Project Scaffolding", "Low", "3", "1 Dev", "Repo setup, CI/CD, environments"),
        ("2.2", "", "Global Styles & Design Tokens", "Medium", "8", "1 Dev", "CSS variables, fonts, base styles"),
        ("2.3", "", "Header/Navigation Block", "High", "12", "1 Dev", "Mega menu, multi-level, responsive"),
        ("2.4", "", "Footer Block", "Medium", "5", "1 Dev", "Multi-column, social links, legal"),
        ("2.5", "", "Core Page Templates (7-9)", "High", "15", "1 Dev", "PLP, PDP, Blog, Landing, Corporate, etc."),
        ("2.6", "", "i18n Framework Setup", "High", "10", "1 Dev", "4 locales: EN, KR, CN, JP"),
        ("2.7", "", "Search Infrastructure", "High", "8", "1 Dev", "Indexing, search UI, suggestions"),
        ("", "", "Subtotal - Foundation", "", "61", "", ""),

        # Section: Block Development
        ("", "BLOCK DEVELOPMENT", "", "", "", "", ""),
        ("3.1", "", "Hero/Banner Block (variants)", "Medium", "8", "1 Dev", "Carousel, video, static variants"),
        ("3.2", "", "Product Card Grid Block", "Medium", "6", "1 Dev", "Responsive grid, hover states"),
        ("3.3", "", "Product Specs Table Block", "High", "10", "1 Dev", "Dynamic tables, responsive"),
        ("3.4", "", "FAQ Accordion Block", "Low", "4", "1 Dev", "Expandable, accessible"),
        ("3.5", "", "Tabs Block", "Medium", "5", "1 Dev", "Content tabs, accessible"),
        ("3.6", "", "Video Embed Block", "Medium", "5", "1 Dev", "YouTube/custom player"),
        ("3.7", "", "Contact Form Block", "High", "12", "1 Dev", "Multi-step, validation, conditional"),
        ("3.8", "", "Cards Block (variants)", "Medium", "6", "1 Dev", "Multiple card layouts"),
        ("3.9", "", "Carousel/Slider Block", "Medium", "6", "1 Dev", "Touch, responsive, accessible"),
        ("3.10", "", "Download/Resources Block", "Medium", "5", "1 Dev", "File downloads, filters"),
        ("3.11", "", "Timeline/Process Block", "Medium", "4", "1 Dev", "Visual timeline component"),
        ("3.12", "", "Statistics/Counter Block", "Low", "3", "1 Dev", "Animated counters"),
        ("3.13", "", "Call-to-Action Block", "Low", "3", "1 Dev", "Banner CTA variants"),
        ("3.14", "", "Image Gallery Block", "Medium", "5", "1 Dev", "Lightbox, grid layout"),
        ("3.15", "", "Breadcrumb Block", "Low", "2", "1 Dev", "Auto-generated from nav"),
        ("3.16", "", "Related Content Block", "Medium", "5", "1 Dev", "Dynamic content recommendations"),
        ("3.17", "", "News/Blog Listing Block", "High", "10", "1 Dev", "Filters, pagination, sorting"),
        ("3.18", "", "Event Listing Block", "Medium", "6", "1 Dev", "Date filters, cards"),
        ("3.19", "", "Partner/Logo Grid Block", "Low", "3", "1 Dev", "SAFE™ ecosystem logos"),
        ("3.20", "", "Sustainability Highlights Block", "Medium", "5", "1 Dev", "Story cards, metrics"),
        ("3.21", "", "Cookie Consent Integration", "High", "8", "1 Dev", "OneTrust/custom, GDPR compliant"),
        ("3.22", "", "Regional Contact Tabs Block", "Medium", "5", "1 Dev", "Region-based content switching"),
        ("3.23", "", "Application Showcase Block", "Medium", "5", "1 Dev", "AI, Server, Auto, Network cards"),
        ("3.24", "", "Tech Blog Article Template", "Medium", "6", "1 Dev", "Rich content, code blocks"),
        ("3.25", "", "Foundry Services Block", "Medium", "6", "1 Dev", "Process tech showcase"),
        ("", "", "Subtotal - Block Development", "", "147", "", ""),

        # Section: Content Migration
        ("", "CONTENT MIGRATION", "", "", "", "", ""),
        ("4.1", "", "Import Script Development", "High", "12", "1 Dev", "AEM Importer customization"),
        ("4.2", "", "Content Migration - Products (50+ pages)", "High", "20", "1 Dev + 1 Content", "Automated + manual QA"),
        ("4.3", "", "Content Migration - Corporate (30+ pages)", "Medium", "10", "1 Content", "About, Sustainability, Careers"),
        ("4.4", "", "Content Migration - News/Blog (100+ pages)", "Medium", "15", "1 Dev + 1 Content", "Bulk import, metadata"),
        ("4.5", "", "Content Migration - Foundry (40+ pages)", "High", "15", "1 Dev + 1 Content", "Complex layouts"),
        ("4.6", "", "Content Migration - Support (20+ pages)", "Medium", "8", "1 Content", "Resources, tools"),
        ("4.7", "", "Asset Migration (Images/Videos)", "Medium", "10", "1 Dev", "Optimization, CDN setup"),
        ("4.8", "", "URL Redirect Mapping", "Medium", "8", "1 Dev", "301 redirects, SEO preservation"),
        ("4.9", "", "Metadata & SEO Migration", "Medium", "8", "1 Dev", "Schema, OG tags, sitemap"),
        ("", "", "Subtotal - Content Migration", "", "106", "", ""),

        # Section: Integrations
        ("", "INTEGRATIONS", "", "", "", "", ""),
        ("5.1", "", "Search Integration (Algolia/Coveo)", "High", "12", "1 Dev", "Index, UI, suggestions"),
        ("5.2", "", "Analytics Setup (Adobe Analytics)", "Medium", "8", "1 Dev", "Event tracking, data layer"),
        ("5.3", "", "Form Submission Backend", "Medium", "6", "1 Dev", "API endpoints, notifications"),
        ("5.4", "", "CDN & Edge Configuration", "Medium", "5", "1 DevOps", "Caching, headers, security"),
        ("5.5", "", "SSO/Authentication (if needed)", "High", "8", "1 Dev", "B2B portal access"),
        ("", "", "Subtotal - Integrations", "", "39", "", ""),

        # Section: Testing & QA
        ("", "TESTING & QUALITY ASSURANCE", "", "", "", "", ""),
        ("6.1", "", "Performance Testing & Optimization", "High", "10", "1 Dev", "Lighthouse 95+, Core Web Vitals"),
        ("6.2", "", "Accessibility Testing (WCAG 2.1 AA)", "High", "10", "1 QA", "Screen readers, keyboard nav"),
        ("6.3", "", "Cross-browser/Device Testing", "Medium", "8", "1 QA", "Chrome, Safari, Firefox, Edge, mobile"),
        ("6.4", "", "Content QA (all locales)", "High", "15", "2 QA", "Visual regression, links, media"),
        ("6.5", "", "SEO Validation", "Medium", "5", "1 Dev", "Rankings preservation, crawl test"),
        ("6.6", "", "Security Testing", "Medium", "5", "1 DevOps", "Headers, CSP, vulnerability scan"),
        ("6.7", "", "UAT Support", "Medium", "10", "1 Dev + 1 QA", "Bug fixes, stakeholder feedback"),
        ("", "", "Subtotal - Testing & QA", "", "63", "", ""),

        # Section: Launch & Handover
        ("", "LAUNCH & HANDOVER", "", "", "", "", ""),
        ("7.1", "", "Go-Live Planning & Cutover", "High", "5", "1 PM + 1 Dev", "DNS, CDN switch, monitoring"),
        ("7.2", "", "Author Training & Documentation", "Medium", "8", "1 PM", "Content author guides"),
        ("7.3", "", "Developer Handover", "Medium", "5", "1 Dev", "Code docs, architecture guide"),
        ("7.4", "", "Post-Launch Hypercare (2 weeks)", "Medium", "10", "1 Dev", "Monitoring, hotfixes"),
        ("", "", "Subtotal - Launch & Handover", "", "28", "", ""),

        # Grand Total
        ("", "GRAND TOTAL - SEMICONDUCTOR ONLY", "", "", "485", "", "~24 weeks with 4-5 FTEs"),
    ]

    for i, task in enumerate(semi_tasks):
        for col, val in enumerate(task, 2):
            ws_semi.cell(row=row, column=col, value=val)

        is_section = task[0] == "" and task[1] != "" and task[2] == ""
        is_subtotal = "Subtotal" in str(task[2]) or "GRAND TOTAL" in str(task[1])
        style_data_row(ws_semi, row, 8, is_alt=(i % 2 == 0), is_total=is_subtotal, is_section=is_section)
        row += 1

    # ============================================================
    # SHEET 3: Detailed Estimate - LED Website
    # ============================================================
    ws_led = wb.create_sheet("LED Website - Detailed")
    ws_led.sheet_properties.tabColor = "00A86B"

    for i, w in enumerate(col_widths, 1):
        ws_led.column_dimensions[get_column_letter(i)].width = w

    row = 2
    ws_led.cell(row=row, column=2, value="Samsung LED Website - Additional EDS Migration Effort").font = title_font
    row += 1
    ws_led.cell(row=row, column=2, value="(Incremental effort when combined with Semiconductor migration)").font = subtitle_font
    row += 2

    headers_led = ["#", "Work Stream", "Task", "Complexity", "Effort (Days)", "Resources", "Notes"]
    for col, h in enumerate(headers_led, 2):
        ws_led.cell(row=row, column=col, value=h)
    style_header_row(ws_led, row, 8)
    row += 1

    led_tasks = [
        ("", "DISCOVERY (INCREMENTAL)", "", "", "", "", ""),
        ("L1.1", "", "LED Site Audit & Inventory", "Medium", "5", "1 Architect", "Product catalog, templates"),
        ("L1.2", "", "LED-specific Template Mapping", "Medium", "4", "1 Architect", "3 additional templates"),
        ("L1.3", "", "LED Navigation & IA Design", "Medium", "3", "1 Architect", "Separate nav structure"),
        ("", "", "Subtotal - Discovery", "", "12", "", ""),

        ("", "LED-SPECIFIC BLOCKS", "", "", "", "", ""),
        ("L2.1", "", "LED Product Category Block", "Medium", "6", "1 Dev", "Mid/High/CSP/COB/Module cards"),
        ("L2.2", "", "LED Spec Comparison Block", "High", "8", "1 Dev", "Multi-product comparison table"),
        ("L2.3", "", "LED Component Calculator", "High", "12", "1 Dev", "Interactive calculator tool"),
        ("L2.4", "", "LED Engine Calculator", "High", "10", "1 Dev", "Performance modeling tool"),
        ("L2.5", "", "Automotive LED Showcase Block", "Medium", "5", "1 Dev", "Application-specific display"),
        ("L2.6", "", "LED Module Configurator", "High", "8", "1 Dev", "Product selection wizard"),
        ("L2.7", "", "In-branding Program Block", "Medium", "4", "1 Dev", "Partner program info"),
        ("L2.8", "", "Virtual Exhibition Block", "High", "10", "1 Dev", "Interactive virtual tour"),
        ("L2.9", "", "LED Application Gallery Block", "Medium", "5", "1 Dev", "Horticulture, automotive, etc."),
        ("L2.10", "", "Quick Downloads Block (LED-specific)", "Medium", "4", "1 Dev", "Datasheet repository"),
        ("", "", "Subtotal - LED Blocks", "", "72", "", ""),

        ("", "LED CONTENT MIGRATION", "", "", "", "", ""),
        ("L3.1", "", "LED Import Script Customization", "Medium", "6", "1 Dev", "LED-specific parsers"),
        ("L3.2", "", "LED Product Pages (20+ pages)", "Medium", "10", "1 Dev + 1 Content", "All product lines"),
        ("L3.3", "", "LED Application Pages (10+ pages)", "Medium", "6", "1 Content", "Lighting, Auto, Display"),
        ("L3.4", "", "LED Support & Tools Pages", "Medium", "5", "1 Content", "Calculators, downloads"),
        ("L3.5", "", "LED News & Events Pages", "Low", "4", "1 Content", "Articles, event listings"),
        ("L3.6", "", "LED Asset Migration", "Medium", "5", "1 Dev", "Product images, datasheets"),
        ("L3.7", "", "LED URL Redirects", "Low", "3", "1 Dev", "led.samsung.com mapping"),
        ("", "", "Subtotal - Content Migration", "", "39", "", ""),

        ("", "LED INTEGRATIONS & TESTING", "", "", "", "", ""),
        ("L4.1", "", "LED Regional Support (6 regions)", "High", "10", "1 Dev", "America, EMEA, CN, SEA, JP, KR"),
        ("L4.2", "", "LED Sales Network Integration", "Medium", "6", "1 Dev", "Regional sales contacts"),
        ("L4.3", "", "LED-specific Testing & QA", "Medium", "8", "1 QA", "Calculator validation, cross-browser"),
        ("L4.4", "", "LED Performance Optimization", "Medium", "5", "1 Dev", "Calculator load performance"),
        ("", "", "Subtotal - Integrations & Testing", "", "29", "", ""),

        ("", "GRAND TOTAL - LED INCREMENTAL", "", "", "152", "", "~6-8 additional weeks"),
    ]

    for i, task in enumerate(led_tasks):
        for col, val in enumerate(task, 2):
            ws_led.cell(row=row, column=col, value=val)

        is_section = task[0] == "" and task[1] != "" and task[2] == ""
        is_subtotal = "Subtotal" in str(task[2]) or "GRAND TOTAL" in str(task[1])
        style_data_row(ws_led, row, 8, is_alt=(i % 2 == 0), is_total=is_subtotal, is_section=is_section)
        row += 1

    # ============================================================
    # SHEET 4: Combined Summary
    # ============================================================
    ws_combined = wb.create_sheet("Combined Summary")
    ws_combined.sheet_properties.tabColor = ADOBE_RED

    ws_combined.column_dimensions['A'].width = 5
    ws_combined.column_dimensions['B'].width = 40
    ws_combined.column_dimensions['C'].width = 20
    ws_combined.column_dimensions['D'].width = 20
    ws_combined.column_dimensions['E'].width = 20
    ws_combined.column_dimensions['F'].width = 20

    row = 2
    ws_combined.cell(row=row, column=2, value="Migration Effort Summary - All Scenarios").font = title_font
    row += 3

    # Summary headers
    sum_headers = ["Work Stream", "Semi Only (Days)", "LED Only (Days)", "Combined (Days)", "Combined (Weeks)"]
    for col, h in enumerate(sum_headers, 2):
        ws_combined.cell(row=row, column=col, value=h)
    style_header_row(ws_combined, row, 6)
    row += 1

    summary_data = [
        ("Discovery & Architecture", "41", "12", "53", "2.5"),
        ("Foundation & Setup", "61", "—", "61", "3"),
        ("Block Development", "147", "72", "219", "10"),
        ("Content Migration", "106", "39", "145", "7"),
        ("Integrations", "39", "16", "55", "2.5"),
        ("Testing & QA", "63", "13", "76", "3.5"),
        ("Launch & Handover", "28", "—", "28", "1.5"),
    ]

    for i, (stream, semi, led, combined, weeks) in enumerate(summary_data):
        ws_combined.cell(row=row, column=2, value=stream)
        ws_combined.cell(row=row, column=3, value=semi)
        ws_combined.cell(row=row, column=4, value=led)
        ws_combined.cell(row=row, column=5, value=combined)
        ws_combined.cell(row=row, column=6, value=weeks)
        style_data_row(ws_combined, row, 6, is_alt=(i % 2 == 0))
        row += 1

    # Totals
    totals = [
        ("TOTAL - Semiconductor Only", "485", "—", "485", "~24"),
        ("TOTAL - LED Incremental", "—", "152", "152", "~6-8"),
        ("TOTAL - Combined (Semi + LED)", "485", "152", "637", "~28-32"),
    ]

    for label, semi, led, combined, weeks in totals:
        ws_combined.cell(row=row, column=2, value=label)
        ws_combined.cell(row=row, column=3, value=semi)
        ws_combined.cell(row=row, column=4, value=led)
        ws_combined.cell(row=row, column=5, value=combined)
        ws_combined.cell(row=row, column=6, value=weeks)
        style_data_row(ws_combined, row, 6, is_total=True)
        row += 1

    row += 3
    ws_combined.cell(row=row, column=2, value="COST ESTIMATION (Based on Adobe Professional Services Rates)").font = Font(name="Adobe Clean", size=12, bold=True, color=ADOBE_RED)
    row += 2

    cost_headers = ["Scenario", "Person-Days", "Team Size", "Duration", "Est. Cost Range (USD)"]
    for col, h in enumerate(cost_headers, 2):
        ws_combined.cell(row=row, column=col, value=h)
    style_header_row(ws_combined, row, 6)
    row += 1

    cost_data = [
        ("Semiconductor Only", "485", "4-5 FTEs", "20-26 weeks", "$850K - $1.1M"),
        ("LED Only (standalone)", "290*", "3-4 FTEs", "14-18 weeks", "$500K - $650K"),
        ("Combined (Semi + LED)", "637", "5-6 FTEs", "26-32 weeks", "$1.1M - $1.4M"),
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
    ws_combined.cell(row=row, column=2, value="* LED standalone includes shared foundation effort that is absorbed in combined scenario").font = Font(name="Adobe Clean", size=9, italic=True, color=ADOBE_GRAY)
    row += 1
    ws_combined.cell(row=row, column=2, value="Note: Cost estimates based on blended rate of $1,750-$2,200/day for Adobe PS resources").font = Font(name="Adobe Clean", size=9, italic=True, color=ADOBE_GRAY)

    # ============================================================
    # SHEET 5: Resource Plan
    # ============================================================
    ws_resource = wb.create_sheet("Resource Plan")
    ws_resource.sheet_properties.tabColor = ADOBE_GRAY

    ws_resource.column_dimensions['A'].width = 5
    ws_resource.column_dimensions['B'].width = 25
    ws_resource.column_dimensions['C'].width = 15
    ws_resource.column_dimensions['D'].width = 50
    ws_resource.column_dimensions['E'].width = 20

    row = 2
    ws_resource.cell(row=row, column=2, value="Recommended Team Structure").font = title_font
    row += 3

    res_headers = ["Role", "Count", "Responsibilities", "Duration"]
    for col, h in enumerate(res_headers, 2):
        ws_resource.cell(row=row, column=col, value=h)
    style_header_row(ws_resource, row, 5)
    row += 1

    resources = [
        ("Solution Architect", "1", "Architecture design, template mapping, technical oversight", "Full duration"),
        ("Senior EDS Developer", "2", "Block development, integrations, performance optimization", "Full duration"),
        ("Frontend Developer", "1-2", "CSS/JS implementation, responsive design, accessibility", "Weeks 4-24"),
        ("Content Engineer", "1", "Import scripts, content migration, asset optimization", "Weeks 8-22"),
        ("QA Engineer", "1", "Testing, accessibility audit, cross-browser validation", "Weeks 12-26"),
        ("Project Manager", "1", "Planning, coordination, stakeholder management, training", "Full duration"),
        ("UX Designer", "0.5", "Design system extraction, component design review", "Weeks 1-8"),
        ("DevOps Engineer", "0.5", "CDN config, CI/CD, security, monitoring", "Weeks 2-6, 20-26"),
    ]

    for i, (role, count, resp, duration) in enumerate(resources):
        ws_resource.cell(row=row, column=2, value=role)
        ws_resource.cell(row=row, column=3, value=count)
        ws_resource.cell(row=row, column=4, value=resp)
        ws_resource.cell(row=row, column=5, value=duration)
        style_data_row(ws_resource, row, 5, is_alt=(i % 2 == 0))
        row += 1

    # ============================================================
    # SHEET 6: Risk Register
    # ============================================================
    ws_risk = wb.create_sheet("Risk Register")
    ws_risk.sheet_properties.tabColor = "FF6600"

    ws_risk.column_dimensions['A'].width = 5
    ws_risk.column_dimensions['B'].width = 8
    ws_risk.column_dimensions['C'].width = 35
    ws_risk.column_dimensions['D'].width = 12
    ws_risk.column_dimensions['E'].width = 12
    ws_risk.column_dimensions['F'].width = 45
    ws_risk.column_dimensions['G'].width = 30

    row = 2
    ws_risk.cell(row=row, column=2, value="Risk Register").font = title_font
    row += 3

    risk_headers = ["ID", "Risk Description", "Likelihood", "Impact", "Mitigation Strategy", "Owner"]
    for col, h in enumerate(risk_headers, 2):
        ws_risk.cell(row=row, column=col, value=h)
    style_header_row(ws_risk, row, 7)
    row += 1

    risks = [
        ("R1", "Complex interactive features (calculators) exceed estimates", "Medium", "High", "Spike/POC in Phase 1; consider phased delivery", "Tech Lead"),
        ("R2", "Content volume larger than estimated (hidden pages)", "High", "Medium", "Automated crawl in discovery; buffer 20% for content", "Content Engineer"),
        ("R3", "Multi-language content sync issues", "Medium", "High", "Establish translation workflow early; test with 2 locales first", "Architect"),
        ("R4", "Performance regression on complex pages", "Medium", "High", "Continuous Lighthouse monitoring; performance budget per block", "Dev Lead"),
        ("R5", "Third-party integration delays (search, analytics)", "Medium", "Medium", "Early vendor engagement; fallback to native EDS search", "PM"),
        ("R6", "Foundry B2B portal dependencies", "Low", "High", "Clearly define scope boundary; API-only integration if needed", "Architect"),
        ("R7", "SEO ranking impact during migration", "Medium", "High", "Comprehensive redirect map; staged rollout; monitoring", "SEO Specialist"),
        ("R8", "Stakeholder availability for UAT", "High", "Medium", "Schedule UAT windows early; provide async review tools", "PM"),
        ("R9", "AEM On-Prem content access/export challenges", "Medium", "Medium", "Early access to AEM instance; backup export strategy", "Dev Lead"),
        ("R10", "LED calculator tool complexity underestimated", "Medium", "High", "Dedicated spike for calculator; consider third-party widget", "Tech Lead"),
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
    # SHEET 7: Timeline
    # ============================================================
    ws_timeline = wb.create_sheet("Timeline")
    ws_timeline.sheet_properties.tabColor = "9B59B6"

    ws_timeline.column_dimensions['A'].width = 5
    ws_timeline.column_dimensions['B'].width = 30
    for i in range(3, 35):
        ws_timeline.column_dimensions[get_column_letter(i)].width = 4

    row = 2
    ws_timeline.cell(row=row, column=2, value="Project Timeline (Combined Semi + LED)").font = title_font
    row += 2

    # Week headers
    ws_timeline.cell(row=row, column=2, value="Phase / Activity")
    for w in range(1, 33):
        ws_timeline.cell(row=row, column=w + 2, value=f"W{w}")
    style_header_row(ws_timeline, row, 34)
    row += 1

    # Timeline data (phase, start_week, end_week)
    phases = [
        ("Phase 1: Discovery & Architecture", 1, 4),
        ("Phase 2: Foundation & Setup", 3, 7),
        ("Phase 3: Block Development (Semi)", 6, 16),
        ("Phase 3b: Block Development (LED)", 14, 20),
        ("Phase 4: Content Migration (Semi)", 12, 20),
        ("Phase 4b: Content Migration (LED)", 18, 24),
        ("Phase 5: Integrations", 14, 20),
        ("Phase 6: Testing & QA", 18, 26),
        ("Phase 7: UAT & Launch Prep", 24, 28),
        ("Phase 8: Go-Live & Hypercare", 28, 32),
    ]

    colors = ["4A90D9", "2ECC71", "E74C3C", "E67E22", "9B59B6", "F39C12", "1ABC9C", "3498DB", "E91E63", ADOBE_RED]

    for i, (phase, start, end) in enumerate(phases):
        ws_timeline.cell(row=row, column=2, value=phase).font = body_bold_font
        ws_timeline.cell(row=row, column=2).border = thin_border
        for w in range(1, 33):
            cell = ws_timeline.cell(row=row, column=w + 2)
            cell.border = thin_border
            if start <= w <= end:
                cell.fill = PatternFill(start_color=colors[i], end_color=colors[i], fill_type="solid")
        row += 1

    row += 2
    ws_timeline.cell(row=row, column=2, value="Legend:").font = body_bold_font
    row += 1
    ws_timeline.cell(row=row, column=2, value="Colored bars indicate active work periods. Phases overlap for efficiency.").font = body_font
    row += 1
    ws_timeline.cell(row=row, column=2, value="Semi-only timeline: ~24 weeks (Phases 3b, 4b removed)").font = body_font
    row += 1
    ws_timeline.cell(row=row, column=2, value="Combined timeline: ~28-32 weeks").font = body_font

    # Save
    output_path = "/backups/riteskum/lge-be-eds/repo/Samsung_EDS_Migration_Estimate.xlsx"
    wb.save(output_path)
    print(f"Estimate saved to: {output_path}")
    return output_path


if __name__ == "__main__":
    create_workbook()
