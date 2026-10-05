<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" 
    xmlns:html="http://www.w3.org/TR/REC-html40"
    xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
    xmlns:video="http://www.google.com/schemas/sitemap-video/1.1"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>

    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml" lang="en">
            <head>
                <title>XML Sitemap | Krisala Hiranandani Township Hinjewadi</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
                <link rel="icon" type="image/png" href="/favicon.png"/>
                <link rel="preconnect" href="https://fonts.googleapis.com"/>
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
                <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&amp;family=Montserrat:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
                <style type="text/css">
                    :root {
                        --bg-base: #0b0b0e;
                        --bg-card: rgba(22, 22, 28, 0.85);
                        --border: rgba(212, 175, 55, 0.25);
                        --gold-primary: #d4af37;
                        --gold-light: #f3e5ab;
                        --text-main: #f5f5f7;
                        --text-muted: #a0a0ab;
                    }
                    * {
                        box-sizing: border-box;
                        margin: 0;
                        padding: 0;
                    }
                    body {
                        background-color: var(--bg-base);
                        color: var(--text-main);
                        font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                        line-height: 1.6;
                        padding: 30px 20px;
                        min-height: 100vh;
                    }
                    .container {
                        max-width: 1200px;
                        margin: 0 auto;
                    }
                    header {
                        background: var(--bg-card);
                        border: 1px solid var(--border);
                        border-radius: 12px;
                        padding: 30px 35px;
                        margin-bottom: 25px;
                        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                    }
                    .header-top {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        flex-wrap: wrap;
                        gap: 20px;
                        margin-bottom: 20px;
                        border-bottom: 1px solid rgba(255,255,255,0.08);
                        padding-bottom: 20px;
                    }
                    .logo-title {
                        font-family: 'Cinzel', serif;
                        font-size: 1.6rem;
                        color: var(--gold-light);
                        letter-spacing: 1px;
                        display: flex;
                        align-items: center;
                        gap: 12px;
                    }
                    .badge {
                        background: rgba(212, 175, 55, 0.15);
                        color: var(--gold-primary);
                        border: 1px solid var(--border);
                        padding: 6px 14px;
                        border-radius: 20px;
                        font-size: 0.8rem;
                        font-weight: 600;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                    }
                    h1 {
                        font-family: 'Cinzel', serif;
                        font-size: 1.8rem;
                        color: #ffffff;
                        margin-bottom: 10px;
                    }
                    p.desc {
                        color: var(--text-muted);
                        font-size: 0.95rem;
                        max-width: 900px;
                    }
                    .stats-bar {
                        display: flex;
                        gap: 25px;
                        margin-top: 15px;
                        flex-wrap: wrap;
                    }
                    .stat-item {
                        font-size: 0.9rem;
                        color: var(--text-muted);
                    }
                    .stat-item strong {
                        color: var(--gold-light);
                        font-size: 1.05rem;
                    }
                    .table-wrapper {
                        background: var(--bg-card);
                        border: 1px solid var(--border);
                        border-radius: 12px;
                        overflow: hidden;
                        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        text-align: left;
                    }
                    thead th {
                        background: rgba(10, 10, 14, 0.9);
                        color: var(--gold-light);
                        font-family: 'Cinzel', serif;
                        font-size: 0.85rem;
                        letter-spacing: 1px;
                        text-transform: uppercase;
                        padding: 16px 20px;
                        border-bottom: 1px solid var(--border);
                    }
                    tbody tr {
                        border-bottom: 1px solid rgba(255,255,255,0.05);
                        transition: background-color 0.2s ease;
                    }
                    tbody tr:hover {
                        background: rgba(212, 175, 55, 0.04);
                    }
                    tbody td {
                        padding: 16px 20px;
                        font-size: 0.9rem;
                        word-break: break-all;
                    }
                    tbody td a {
                        color: #70b8ff;
                        text-decoration: none;
                        font-weight: 500;
                        transition: color 0.2s ease;
                    }
                    tbody td a:hover {
                        color: var(--gold-light);
                        text-decoration: underline;
                    }
                    .date-badge {
                        color: var(--text-muted);
                        font-family: monospace;
                        font-size: 0.85rem;
                    }
                    footer {
                        text-align: center;
                        margin-top: 30px;
                        color: var(--text-muted);
                        font-size: 0.85rem;
                    }
                    footer a {
                        color: var(--gold-primary);
                        text-decoration: none;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <header>
                        <div class="header-top">
                            <div class="logo-title">
                                Krisala × Hiranandani
                            </div>
                            <span class="badge">Google XML Sitemap</span>
                        </div>
                        <xsl:choose>
                            <xsl:when test="sitemap:sitemapindex">
                                <h1>Master Sitemap Index</h1>
                                <p class="desc">
                                    This sitemap index coordinates all primary residential corridors, floor plan typologies, infrastructure links, and 10,000 programmatic real estate exploration pages for <strong>Krisala Hiranandani Township Hinjewadi, Pune</strong>.
                                </p>
                                <div class="stats-bar">
                                    <div class="stat-item">Total Sub-Sitemaps: <strong><xsl:value-of select="count(sitemap:sitemapindex/sitemap:sitemap)"/></strong></div>
                                    <div class="stat-item">Status: <strong>Indexed &amp; Active</strong></div>
                                    <div class="stat-item">Format: <strong>sitemaps.org 0.9</strong></div>
                                </div>
                            </xsl:when>
                            <xsl:otherwise>
                                <h1>XML URL Directory</h1>
                                <p class="desc">
                                    Direct canonical index of published residential inventory, floor plans, and real estate market intelligence reports.
                                </p>
                                <div class="stats-bar">
                                    <div class="stat-item">Total URLs: <strong><xsl:value-of select="count(sitemap:urlset/sitemap:url)"/></strong></div>
                                    <div class="stat-item">Status: <strong>Live</strong></div>
                                </div>
                            </xsl:otherwise>
                        </xsl:choose>
                    </header>

                    <div class="table-wrapper">
                        <table>
                            <xsl:choose>
                                <xsl:when test="sitemap:sitemapindex">
                                    <thead>
                                        <tr>
                                            <th style="width: 5%;">#</th>
                                            <th style="width: 70%;">Sitemap Location</th>
                                            <th style="width: 25%;">Last Modified</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <xsl:for-each select="sitemap:sitemapindex/sitemap:sitemap">
                                            <tr>
                                                <td style="color: var(--gold-primary); font-weight: 600;"><xsl:value-of select="position()"/></td>
                                                <td>
                                                    <a href="{sitemap:loc}">
                                                        <xsl:value-of select="sitemap:loc"/>
                                                    </a>
                                                </td>
                                                <td>
                                                    <span class="date-badge"><xsl:value-of select="sitemap:lastmod"/></span>
                                                </td>
                                            </tr>
                                        </xsl:for-each>
                                    </tbody>
                                </xsl:when>
                                <xsl:otherwise>
                                    <thead>
                                        <tr>
                                            <th style="width: 5%;">#</th>
                                            <th style="width: 60%;">URL Location</th>
                                            <th style="width: 15%;">Change Frequency</th>
                                            <th style="width: 10%;">Priority</th>
                                            <th style="width: 10%;">Last Modified</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <xsl:for-each select="sitemap:urlset/sitemap:url">
                                            <tr>
                                                <td style="color: var(--gold-primary); font-weight: 600;"><xsl:value-of select="position()"/></td>
                                                <td>
                                                    <a href="{sitemap:loc}">
                                                        <xsl:value-of select="sitemap:loc"/>
                                                    </a>
                                                </td>
                                                <td style="color: var(--text-muted); text-transform: capitalize;">
                                                    <xsl:value-of select="sitemap:changefreq"/>
                                                </td>
                                                <td>
                                                    <span style="color: var(--gold-light); font-weight: 600;">
                                                        <xsl:value-of select="sitemap:priority"/>
                                                    </span>
                                                </td>
                                                <td>
                                                    <span class="date-badge"><xsl:value-of select="substring(sitemap:lastmod, 1, 10)"/></span>
                                                </td>
                                            </tr>
                                        </xsl:for-each>
                                    </tbody>
                                </xsl:otherwise>
                            </xsl:choose>
                        </table>
                    </div>

                    <footer>
                        <p>© 2026 Krisala × Hiranandani Communities. All rights reserved. | <a href="/">Return to Official Township Portal</a></p>
                    </footer>
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
