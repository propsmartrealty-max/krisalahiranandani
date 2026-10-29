/**
 * Krisala Hiranandani Verified Partner & Authority Badge
 * Programmatic Off-Page SEO & Verification Embed
 * (C) 2026 Krisala Developers & Hiranandani Communities
 */
(function() {
 function initBadge() {
 var containers = document.querySelectorAll('[data-hiranandani-badge], #hiranandani-pune-badge');
 if (!containers || containers.length === 0) return;

 var css = `
 .kxh-badge-wrap {
 font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
 display: inline-flex;
 flex-direction: column;
 border: 1px solid rgba(197, 160, 89, 0.4);
 border-radius: 8px;
 background: #090a0f;
 color: #fcfbf7;
 padding: 14px 18px;
 box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
 max-width: 380px;
 text-align: left;
 line-height: 1.4;
 }
 .kxh-badge-head {
 display: flex;
 align-items: center;
 justify-content: space-between;
 border-bottom: 1px solid rgba(197, 160, 89, 0.2);
 padding-bottom: 8px;
 margin-bottom: 8px;
 }
 .kxh-badge-title {
 font-size: 14px;
 font-weight: 700;
 color: #dfc07b;
 text-decoration: none;
 }
 .kxh-badge-title:hover {
 text-decoration: underline;
 }
 .kxh-badge-rera {
 font-size: 10px;
 background: rgba(197, 160, 89, 0.15);
 color: #dfc07b;
 padding: 2px 6px;
 border-radius: 4px;
 border: 1px solid rgba(197, 160, 89, 0.3);
 }
 .kxh-badge-body {
 font-size: 12px;
 color: #b8b8cc;
 margin-bottom: 10px;
 }
 .kxh-badge-links {
 display: flex;
 flex-wrap: wrap;
 gap: 8px;
 font-size: 11px;
 }
 .kxh-badge-link {
 color: #dfc07b;
 text-decoration: none;
 background: rgba(255, 255, 255, 0.05);
 padding: 4px 8px;
 border-radius: 4px;
 transition: all 0.2s;
 }
 .kxh-badge-link:hover {
 background: #dfc07b;
 color: #000;
 }
 `;

 var style = document.createElement('style');
 style.textContent = css;
 document.head.appendChild(style);

 containers.forEach(function(el) {
 el.innerHTML = `
 <div class="kxh-badge-wrap">
 <div class="kxh-badge-head">
 <a href="https://krisalahiranandanitownships.com/hiranandani-pune" class="kxh-badge-title" target="_blank" rel="noopener">
 Krisala Hiranandani Pune
 </a>
 <span class="kxh-badge-rera">MahaRERA Verified</span>
 </div>
 <div class="kxh-badge-body">
 105-Acre Integrated Equestrian Township in North Hinjewadi with India's 1st 8-Acre Private Racecourse & 40-Acre Della Resort.
 </div>
 <div class="kxh-badge-links">
 <a href="https://krisalahiranandanitownships.com/" class="kxh-badge-link" target="_blank" rel="noopener">Township Portal</a>
 <a href="https://krisalahiranandanitownships.com/hiranandani-price-list-2026" class="kxh-badge-link" target="_blank" rel="noopener">2026 Price List</a>
 <a href="https://krisalahiranandanitownships.com/colosseum" class="kxh-badge-link" target="_blank" rel="noopener">The Colosseum</a>
 </div>
 </div>
 `;
 });
 }

 if (document.readyState === 'loading') {
 document.addEventListener('DOMContentLoaded', initBadge);
 } else {
 initBadge();
 }
})();
