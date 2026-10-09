document.addEventListener('DOMContentLoaded', () => {
    // 0a. W3C Speculation Rules API: Instantaneous 0ms Page Prerendering (Chrome & Android)
    try {
        if (HTMLScriptElement.supports && HTMLScriptElement.supports('speculationrules')) {
            const specScript = document.createElement('script');
            specScript.type = 'speculationrules';
            specScript.textContent = JSON.stringify({
                prerender: [
                    {
                        source: "list",
                        urls: [
                            "/pricing",
                            "/colosseum",
                            "/arcadia",
                            "/icon",
                            "/della",
                            "/gallery",
                            "/neighborhood",
                            "/connectivity"
                        ],
                        eagerness: "moderate"
                    }
                ],
                prefetch: [
                    {
                        source: "document",
                        where: {
                            and: [
                                { href_matches: "/*" },
                                { not: { href_matches: "/api/*" } },
                                { not: { href_matches: "/thank-you*" } }
                            ]
                        },
                        eagerness: "conservative"
                    }
                ]
            });
            document.head.appendChild(specScript);
        }
    } catch (e) {
        // Graceful fallback for non-supporting browsers
    }

    // 0b. Enterprise Universal dataLayer Telemetry Suite
    window.dataLayer = window.dataLayer || [];

    // Track WhatsApp conversions with active page contextual payload
    document.querySelectorAll('a[href*="wa.me"]').forEach(link => {
        link.addEventListener('click', () => {
            window.dataLayer.push({
                event: 'contact',
                method: 'whatsapp',
                action: 'initiate_chat',
                page_location: window.location.pathname,
                value: 8500000,
                currency: 'INR'
            });
        });
    });

    // Track Phone call conversions
    document.querySelectorAll('a[href^="tel:"]').forEach(link => {
        link.addEventListener('click', () => {
            window.dataLayer.push({
                event: 'contact',
                method: 'phone_call',
                action: 'click_to_call',
                phone_number: '+917744009295',
                page_location: window.location.pathname,
                value: 8500000,
                currency: 'INR'
            });
        });
    });

    // Track Brochure downloads
    document.querySelectorAll('a[href*=".pdf"], a[download]').forEach(link => {
        link.addEventListener('click', () => {
            window.dataLayer.push({
                event: 'file_download',
                file_name: link.getAttribute('href') || 'township-brochure.pdf',
                file_extension: 'pdf',
                page_location: window.location.pathname
            });
        });
    });

    // 0c. PWA IndexedDB Offline Lead Resilience Engine
    const DB_NAME = 'kxh_offline_leads_db';
    const DB_VERSION = 1;
    const STORE_NAME = 'pending_leads';

    function openLeadDB() {
        return new Promise((resolve) => {
            if (!('indexedDB' in window)) return resolve(null);
            const req = indexedDB.open(DB_NAME, DB_VERSION);
            req.onupgradeneeded = (e) => {
                const db = e.target.result;
                if (!db.objectStoreNames.contains(STORE_NAME)) {
                    db.createObjectStore(STORE_NAME, { keyPath: 'id', autoIncrement: true });
                }
            };
            req.onsuccess = () => resolve(req.result);
            req.onerror = () => resolve(null);
        });
    }

    window.queueLeadOffline = async function(leadData) {
        const db = await openLeadDB();
        if (!db) return false;
        return new Promise((resolve) => {
            const tx = db.transaction(STORE_NAME, 'readwrite');
            const store = tx.objectStore(STORE_NAME);
            store.add({ ...leadData, queuedAt: new Date().toISOString() });
            tx.oncomplete = () => resolve(true);
            tx.onerror = () => resolve(false);
        });
    };

    window.flushOfflineLeads = async function() {
        if (!navigator.onLine) return;
        const db = await openLeadDB();
        if (!db) return;
        const tx = db.transaction(STORE_NAME, 'readwrite');
        const store = tx.objectStore(STORE_NAME);
        const getAllReq = store.getAll();
        getAllReq.onsuccess = async () => {
            const leads = getAllReq.result || [];
            for (const lead of leads) {
                try {
                    const res = await fetch('/api/lead', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(lead)
                    });
                    if (res.ok) {
                        const delTx = db.transaction(STORE_NAME, 'readwrite');
                        delTx.objectStore(STORE_NAME).delete(lead.id);
                    }
                } catch (err) {
                    break;
                }
            }
        };
    };

    window.addEventListener('online', window.flushOfflineLeads);
    window.flushOfflineLeads();

    // 1. Custom Cursor Logic
    const cursorDot = document.querySelector('[data-cursor-dot]');
    const cursorOutline = document.querySelector('[data-cursor-outline]');

    window.addEventListener('mousemove', (e) => {
        if (!cursorDot || !cursorOutline) return;
        const posX = e.clientX;
        const posY = e.clientY;

        cursorDot.style.left = `${posX}px`;
        cursorDot.style.top = `${posY}px`;

        // Slight delay for the outline for a smooth effect
        cursorOutline.animate({
            left: `${posX}px`,
            top: `${posY}px`
        }, { duration: 500, fill: "forwards" });
    });

    // Make cursor bigger on interactive elements
    const interactables = document.querySelectorAll('a, button, .slider-btn, .am-item, .phase-slide');
    interactables.forEach(el => {
        el.addEventListener('mouseenter', () => {
            if (cursorOutline) {
                cursorOutline.style.transform = 'translate(-50%, -50%) scale(1.6)';
                cursorOutline.style.backgroundColor = 'rgba(212, 175, 55, 0.1)';
                cursorOutline.style.border = '1px solid rgba(212, 175, 55, 0.8)';
            }
        });
        el.addEventListener('mouseleave', () => {
            if (cursorOutline) {
                cursorOutline.style.transform = 'translate(-50%, -50%) scale(1)';
                cursorOutline.style.backgroundColor = 'transparent';
                cursorOutline.style.border = '1px solid rgba(212, 175, 55, 0.5)';
            }
        });
    });

    // 2. Navbar Scroll Effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 3. Scroll Reveal Animations (Intersection Observer)
    const revealElements = document.querySelectorAll('.reveal, .scroll-reveal');

    const revealOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, revealOptions);

    revealElements.forEach(el => revealObserver.observe(el));

    // Trigger hero animations immediately
    setTimeout(() => {
        document.querySelectorAll('.hero .reveal').forEach(el => el.classList.add('active'));
    }, 100);

    // 4. Parallax Effect for Hero Image
    const heroImg = document.querySelector('.parallax-img');
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        if (heroImg && scrolled < window.innerHeight) {
            heroImg.style.transform = `translateY(${scrolled * 0.4}px)`;
        }
    });

    // 5. Horizontal Phase Slider Logic
    const sliderContainer = document.getElementById('phaseSlider');
    const btnNext = document.getElementById('sliderNext');
    const btnPrev = document.getElementById('sliderPrev');

    if (sliderContainer && btnNext && btnPrev) {
        // Scroll amount is roughly one slide width + gap
        const scrollAmount = 640;

        btnNext.addEventListener('click', () => {
            sliderContainer.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        });

        btnPrev.addEventListener('click', () => {
            sliderContainer.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        });

        // Optional Drag to scroll (Vanilla JS Desktop support)
        let isDown = false;
        let startX;
        let scrollLeft;

        sliderContainer.addEventListener('mousedown', (e) => {
            isDown = true;
            sliderContainer.classList.add('active');
            startX = e.pageX - sliderContainer.offsetLeft;
            scrollLeft = sliderContainer.scrollLeft;
        });
        sliderContainer.addEventListener('mouseleave', () => {
            isDown = false;
            sliderContainer.classList.remove('active');
        });
        sliderContainer.addEventListener('mouseup', () => {
            isDown = false;
            sliderContainer.classList.remove('active');
        });
        sliderContainer.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - sliderContainer.offsetLeft;
            const walk = (x - startX) * 2; // Scroll-fast factor
            sliderContainer.scrollLeft = scrollLeft - walk;
        });
    }

    // 6. Enquiry Modal Logic
    const modalOverlay = document.getElementById('enquiryModal');
    const openBtns = document.querySelectorAll('.open-modal');
    const closeBtn = document.querySelector('.close-modal');
    const leadForm = document.getElementById('leadForm');

    const openModal = () => { if (modalOverlay) modalOverlay.classList.add('active'); };
    const closeModal = () => { if (modalOverlay) modalOverlay.classList.remove('active'); };

    openBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            if (!modalOverlay) return;

            // Lead Magnet Logic
            const magnet = btn.getAttribute('data-magnet');
            const modalTitle = modalOverlay.querySelector('h2');
            if (modalTitle) {
                if (magnet === 'brochure') {
                    modalTitle.innerText = 'Download Elite Brochure';
                } else if (magnet === 'pricesheet') {
                    modalTitle.innerText = 'Request Luxury Price Sheet';
                } else {
                    modalTitle.innerText = modalTitle.getAttribute('data-en-original') || modalTitle.innerText || 'Register Your Interest';
                }
            }

            // If button is within a specific phase slide, pre-select that option
            const parentSlide = btn.closest('.phase-slide');
            if (parentSlide && leadForm) {
                const selectElement = leadForm.querySelector('select');
                const phaseTitle = parentSlide.querySelector('h3').textContent;

                if (phaseTitle.includes('Everlyn')) selectElement.value = 'everlyn-tower';
                if (phaseTitle.includes('Arcadia')) selectElement.value = 'arcadia-3bhk';
                if (phaseTitle.includes('Icon')) selectElement.value = 'icon-4bhk';
                if (phaseTitle.includes('Della')) selectElement.value = 'della-villa';
            }

            openModal();
        });
    });

    if (closeBtn) closeBtn.addEventListener('click', closeModal);

    // Close modal when clicking outside
    if (modalOverlay) {
        modalOverlay.addEventListener('click', (e) => {
            if (e.target === modalOverlay) {
                closeModal();
            }
        });
    }

    // 7. Appreciation Ticker Logic
    const tickerSlides = document.querySelectorAll('.ticker-slide');
    if (tickerSlides.length > 0) {
        let currentSlide = 0;
        setInterval(() => {
            tickerSlides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % tickerSlides.length;
            tickerSlides[currentSlide].classList.add('active');
        }, 3000);
    }

    // 8. ROI Chart Animation
    const chartBars = document.querySelectorAll('.chart-bar');
    const chartObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const bar = entry.target;
                const targetHeight = bar.style.height;
                bar.style.height = '0'; // Reset for animation
                setTimeout(() => {
                    bar.style.height = targetHeight;
                }, 100);
                chartObserver.unobserve(bar);
            }
        });
    }, { threshold: 0.5 });

    chartBars.forEach(bar => chartObserver.observe(bar));

    // 9. PWA Service Worker Registration
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/sw.js').then(reg => {
                // Registered
            }).catch(err => { });
        });
    }



    // 11. ROI & EMI Calculators
    const roiAmount = document.getElementById('roi-amount');
    const roiGrowth = document.getElementById('roi-growth');
    const roiYears = document.getElementById('roi-years');
    const roiResult = document.getElementById('roi-result');

    function updateROI() {
        if (!roiAmount || !roiGrowth || !roiYears) return;
        const p = parseFloat(roiAmount.value);
        const r = parseFloat(roiGrowth.value) / 100;
        const n = parseFloat(roiYears.value);
        const result = p * Math.pow((1 + r), n);
        roiResult.innerText = `₹ ${result.toFixed(2)} Cr`;
        roiGrowth.nextElementSibling.innerText = `${roiGrowth.value}%`;
        roiYears.nextElementSibling.innerText = `${roiYears.value} Years`;
    }

    [roiAmount, roiGrowth, roiYears].forEach(el => {
        if (el) el.addEventListener('input', updateROI);
    });

    const emiAmount = document.getElementById('emi-amount');
    const emiRate = document.getElementById('emi-rate');
    const emiTenure = document.getElementById('emi-tenure');
    const emiResult = document.getElementById('emi-result');

    function updateEMI() {
        if (!emiAmount || !emiRate || !emiTenure) return;
        const p = parseFloat(emiAmount.value) * 100000;
        const r = parseFloat(emiRate.value) / 12 / 100;
        const n = parseFloat(emiTenure.value) * 12;
        const emi = (p * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
        emiResult.innerText = `₹ ${Math.round(emi).toLocaleString('en-IN')}`;
    }

    [emiAmount, emiRate, emiTenure].forEach(el => {
        if (el) el.addEventListener('input', updateEMI);
    });

    // 12. Marathi Translation Content Mapping
    const translations = {
        mr: {
            'The Legacy': 'वारसा',
            'Masterplan': 'मास्टर प्लॅन',
            'Phases': 'टप्पे',
            'Amenities': 'सुविधा',
            'Location': 'ठिकाण',
            'Inquire': 'चौकशी करा',
            'Plan Your Investment': 'तुमच्या गुंतवणुकीचे नियोजन करा',
            'Appreciation Calculator': 'वाढ मोजण्याचे साधन',
            'EMI Estimator': 'ईएमआय अंदाजपत्रक',
            'The Community of Titans': 'दिग्गजांचा समुदाय',
            'A Glimpse of Magnificence': 'भव्यतेची एक झलक',
            'Register Now for Pre-Launch Offers': 'प्री-लाँच ऑफरसाठी आताच नोंदणी करा'
        }
    };

    // 13. Dynamic Translation Engine
    const langToggle = document.getElementById('langToggle');
    if (langToggle) {
        const langBtns = langToggle.querySelectorAll('button');
        langBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const selectedLang = btn.getAttribute('data-lang');
                langBtns.forEach(b => {
                    b.classList.remove('active');
                    b.setAttribute('aria-pressed', 'false');
                });
                btn.classList.add('active');
                btn.setAttribute('aria-pressed', 'true');
                document.body.setAttribute('data-lang', selectedLang);
                translatePage(selectedLang);
            });
        });
    }

    function translatePage(lang) {
        document.querySelectorAll('[data-en]').forEach(el => {
            if (lang === 'mr') {
                if (!el.getAttribute('data-en-original')) el.setAttribute('data-en-original', el.innerText);
                el.innerText = el.getAttribute('data-mr');
            } else {
                el.innerText = el.getAttribute('data-en-original') || el.innerText;
            }
        });

        // Translate placeholders
        document.querySelectorAll('input[placeholder]').forEach(input => {
            const key = input.getAttribute('placeholder');
            const translation = translations.mr[key];
            if (lang === 'mr' && translation) {
                if (!input.getAttribute('data-en-ph')) input.setAttribute('data-en-ph', key);
                input.placeholder = translation;
            } else if (lang === 'en' && input.getAttribute('data-en-ph')) {
                input.placeholder = input.getAttribute('data-en-ph');
            }
        });
    }

    // 14. Find Your Masterpiece Quiz Logic (Universal Auto-Inject Engine)
    function ensureQuizOverlay() {
        let overlay = document.getElementById('quizOverlay');
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.className = 'quiz-overlay';
            overlay.id = 'quizOverlay';
            overlay.innerHTML = `
                <div class="quiz-container glass-panel">
                    <button class="close-quiz" aria-label="Close Quiz"><i class="ph ph-x"></i></button>
                    <div class="quiz-steps" id="quizSteps">
                        <!-- Step 1: Configuration & Budget -->
                        <div class="quiz-step active" data-step="1">
                            <span class="step-num">01 / 03</span>
                            <h2>What configuration &amp; <span>budget fits your plan?</span></h2>
                            <div class="quiz-options">
                                <button class="quiz-opt" data-value="colosseum-3bhk">
                                    <i class="ph ph-columns gold-icon"></i>
                                    <strong>The Colosseum Signature</strong>
                                    <span>Pre-Launch 3/4 BHK • From ₹85 Lakh*</span>
                                </button>
                                <button class="quiz-opt" data-value="arcadia-2bhk">
                                    <i class="ph ph-layout gold-icon"></i>
                                    <strong>2 BHK Urban Luxury</strong>
                                    <span>Sector Arcadia • From ₹79 Lakh*</span>
                                </button>
                                <button class="quiz-opt" data-value="arcadia-3bhk">
                                    <i class="ph ph-buildings gold-icon"></i>
                                    <strong>3 BHK Grande Family Suite</strong>
                                    <span>Sector Arcadia • From ₹1.18 Cr*</span>
                                </button>
                                <button class="quiz-opt" data-value="icon-4bhk">
                                    <i class="ph ph-crown gold-icon"></i>
                                    <strong>4 BHK Duplex &amp; Sky Mansion</strong>
                                    <span>Sector Icon • From ₹2.10 Cr*</span>
                                </button>
                                <button class="quiz-opt" data-value="della-villa">
                                    <i class="ph ph-horse gold-icon"></i>
                                    <strong>Bespoke Equestrian Villa Plot</strong>
                                    <span>Della District • From ₹1.50 Cr*</span>
                                </button>
                            </div>
                        </div>

                        <!-- Step 2: Primary Lifestyle Focus -->
                        <div class="quiz-step" data-step="2">
                            <span class="step-num">02 / 03</span>
                            <h2>What is your top <span>lifestyle priority?</span></h2>
                            <div class="quiz-options">
                                <button class="quiz-opt" data-value="roman-grandeur">
                                    <i class="ph ph-bank gold-icon"></i>
                                    <strong>Neoclassical Roman Grandeur</strong>
                                    <span>Triple-height marble lobby, Roman columns &amp; amphitheater.</span>
                                </button>
                                <button class="quiz-opt" data-value="metro-commute">
                                    <i class="ph ph-train-regional gold-icon"></i>
                                    <strong>2-Min Hinjawadi Tech Park Commute</strong>
                                    <span>Walk to Metro Line 3, Wipro, Infosys &amp; Embassy TechZone.</span>
                                </button>
                                <button class="quiz-opt" data-value="racecourse-resort">
                                    <i class="ph ph-sun gold-icon"></i>
                                    <strong>8-Acre Racecourse &amp; Resort District</strong>
                                    <span>Equestrian academy, Della hospitality &amp; 100+ master amenities.</span>
                                </button>
                                <button class="quiz-opt" data-value="wellness-nature">
                                    <i class="ph ph-leaf gold-icon"></i>
                                    <strong>Zen Nature &amp; Circular Water Sanctuary</strong>
                                    <span>TERI certified zero-carbon ecology, Miyawaki forests &amp; peace.</span>
                                </button>
                            </div>
                        </div>

                        <!-- Step 3: Purchase Objective & Timeline -->
                        <div class="quiz-step" data-step="3">
                            <span class="step-num">03 / 03</span>
                            <h2>What is your primary <span>buying objective?</span></h2>
                            <div class="quiz-options">
                                <button class="quiz-opt" data-value="prelaunch-roi">
                                    <i class="ph ph-chart-line-up gold-icon"></i>
                                    <strong>Pre-Launch Priority Pricing (Max ROI)</strong>
                                    <span>Capitalize on 15%+ YoY capital appreciation track record.</span>
                                </button>
                                <button class="quiz-opt" data-value="family-enduse">
                                    <i class="ph ph-house-line gold-icon"></i>
                                    <strong>Family Home (Possession 2026–2027)</strong>
                                    <span>Secure a premium neoclassical legacy for generations.</span>
                                </button>
                                <button class="quiz-opt" data-value="nri-rental">
                                    <i class="ph ph-globe-hemisphere-east gold-icon"></i>
                                    <strong>High-Yield Rental / NRI Investment</strong>
                                    <span>FEMA compliant, dollar-hedged returns &amp; Hinjawadi tenant demand.</span>
                                </button>
                            </div>
                        </div>

                        <!-- Final Recommendation -->
                        <div class="quiz-step" id="quizResultStep">
                            <div class="result-header">
                                <div class="match-score-badge"><i class="ph ph-seal-check"></i> <span id="quizMatchScore">98% Ideal Match Found</span></div>
                                <h2 id="recommendedSector">The Colosseum Phase 4</h2>
                                <p id="recommendedDesc">Neoclassical Roman landmark with soaring columns, double-height lobby, and private racecourse panorama.</p>
                            </div>
                            <div class="quiz-result-specs" id="quizSpecsGrid">
                                <div class="quiz-spec-item">
                                    <div class="q-label">Configuration</div>
                                    <div class="q-val" id="specConfig">3 BHK Signature Residence</div>
                                </div>
                                <div class="quiz-spec-item">
                                    <div class="q-label">Carpet Area</div>
                                    <div class="q-val" id="specCarpet">815 – 1,180 Sq. Ft.</div>
                                </div>
                                <div class="quiz-spec-item">
                                    <div class="q-label">Pre-Launch Price</div>
                                    <div class="q-val" id="specPrice">From ₹85 Lakh*</div>
                                </div>
                                <div class="quiz-spec-item">
                                    <div class="q-label">MahaRERA Registration</div>
                                    <div class="q-val" id="specRera">P52100055291</div>
                                </div>
                            </div>
                            <div class="result-actions">
                                <button class="btn-primary" id="quizLockVipBtn">
                                    <i class="ph ph-ticket"></i>&nbsp; Lock Priority Allotment for This Unit
                                </button>
                                <a href="https://wa.me/917744009295" target="_blank" class="btn-secondary" id="quizWhatsAppBtn">
                                    <i class="ph ph-whatsapp-logo"></i>&nbsp; Instant WhatsApp Brochure &amp; Cost Sheet
                                </a>
                                <button class="btn-outline" id="restartQuiz">
                                    <i class="ph ph-arrow-counter-clockwise"></i>&nbsp; Retake Matcher
                                </button>
                            </div>
                        </div>
                    </div>
                    <div class="quiz-progress">
                        <div class="progress-bar" id="quizBar"></div>
                    </div>
                </div>
            `;
            document.body.appendChild(overlay);
            bindQuizListeners();
        }
        return overlay;
    }

    let currentQuizStep = 0;
    let quizAnswers = {};

    function bindQuizListeners() {
        const overlay = document.getElementById('quizOverlay');
        if (!overlay) return;
        overlay.querySelectorAll('.close-quiz').forEach(btn => btn.onclick = closeQuiz);
        const restartBtn = overlay.querySelector('#restartQuiz');
        if (restartBtn) restartBtn.onclick = resetQuiz;

        overlay.querySelectorAll('.quiz-opt').forEach(opt => {
            opt.onclick = () => {
                const step = opt.closest('.quiz-step').getAttribute('data-step');
                const value = opt.getAttribute('data-value');
                quizAnswers[step] = value;

                setTimeout(() => {
                    currentQuizStep++;
                    updateQuizStep();
                }, 250);
            };
        });
    }

    const openQuiz = (e) => {
        if (e && e.preventDefault) e.preventDefault();
        const overlay = ensureQuizOverlay();
        overlay.classList.add('active');
        bindQuizListeners();
        resetQuiz();
    };

    const closeQuiz = () => {
        const overlay = document.getElementById('quizOverlay');
        if (overlay) overlay.classList.remove('active');
    };

    const resetQuiz = () => {
        currentQuizStep = 0;
        quizAnswers = {};
        updateQuizStep();
    };

    function updateQuizStep() {
        const overlay = document.getElementById('quizOverlay');
        if (!overlay) return;
        const steps = overlay.querySelectorAll('.quiz-step');
        const bar = overlay.querySelector('#quizBar');

        steps.forEach((step, index) => {
            step.classList.toggle('active', index === currentQuizStep);
        });

        // Progress bar (Steps 1-3 = 33, 66, 100%)
        const progress = ((currentQuizStep + 1) / (steps.length - 1)) * 100;
        if (bar) bar.style.width = `${Math.min(progress, 100)}%`;

        if (currentQuizStep === steps.length - 1) {
            showRecommendation();
        }
    }

    function showRecommendation() {
        const resultTitle = document.getElementById('recommendedSector');
        const resultDesc = document.getElementById('recommendedDesc');
        const specConfig = document.getElementById('specConfig');
        const specCarpet = document.getElementById('specCarpet');
        const specPrice = document.getElementById('specPrice');
        const specRera = document.getElementById('specRera');
        const matchBadge = document.getElementById('quizMatchScore');

        let sector = "The Colosseum Phase 4";
        let config = "3 BHK Signature Residence";
        let carpet = "815 – 1,180 Sq. Ft.";
        let price = "From ₹85 Lakh*";
        let rera = "P52100055291";
        let desc = "Neoclassical Roman landmark with soaring Corinthian columns, triple-height marble lobby, and private racecourse panorama.";
        let link = "colosseum.html";
        let score = "99% Ideal Match";

        const val1 = quizAnswers[1] || '';
        const val2 = quizAnswers[2] || '';
        const val3 = quizAnswers[3] || '';

        if (val1 === 'della-villa' || val2 === 'racecourse-resort') {
            sector = "The Della Collection";
            config = "Bespoke Equestrian Villa Plots";
            carpet = "2,500 – 6,000 Sq. Ft. Plots";
            price = "From ₹1.50 Crore*";
            rera = "P52100055294";
            desc = "India's first equestrian-themed villa plots with private racecourse access, 5-star resort hospitality, and 40+ acres of open luxury.";
            link = "della.html";
            score = "98% Ideal Match";
        } else if (val1 === 'icon-4bhk') {
            sector = "Sector Icon";
            config = "4 BHK Duplex & Sky Mansion";
            carpet = "1,650 – 2,400 Sq. Ft.";
            price = "From ₹2.10 Crore*";
            rera = "P52100055292";
            desc = "The pinnacle of status with double-height living spaces, panoramic sky decks, and private lift access overlooking the Sahyadri valley.";
            link = "icon.html";
            score = "97% Ideal Match";
        } else if (val2 === 'wellness-nature') {
            sector = "Sector Everlyn";
            config = "2 & 3 BHK Wellness Residences";
            carpet = "820 – 1,120 Sq. Ft.";
            price = "From ₹82 Lakh*";
            rera = "P52100055293";
            desc = "A sanctuary of low-carbon living, zen meditation decks, zero-discharge water reservoirs, and organic wellness boulevards.";
            link = "everlyn.html";
            score = "96% Ideal Match";
        } else if (val1 === 'arcadia-2bhk' || val2 === 'metro-commute') {
            sector = "Sector Arcadia";
            config = "2 & 3 BHK Tech-Corridor Homes";
            carpet = "765 – 1,050 Sq. Ft.";
            price = "From ₹79 Lakh*";
            rera = "P52100055290";
            desc = "Smartly planned neoclassical urban residences 2 minutes from Metro Line 3 and Hinjawadi Phase 1 & 2 IT corridors.";
            link = "arcadia.html";
            score = "99% Ideal Match";
        }

        if (resultTitle) resultTitle.innerText = sector;
        if (resultDesc) resultDesc.innerText = desc;
        if (specConfig) specConfig.innerText = config;
        if (specCarpet) specCarpet.innerText = carpet;
        if (specPrice) specPrice.innerText = price;
        if (specRera) specRera.innerText = rera;
        if (matchBadge) matchBadge.innerText = `${score} Found`;

        const lockBtn = document.getElementById('quizLockVipBtn');
        if (lockBtn) {
            lockBtn.onclick = () => {
                closeQuiz();
                const modal = document.getElementById('enquiryModal');
                if (modal) {
                    modal.classList.add('active');
                    const select = modal.querySelector('select');
                    if (select) {
                        for (let opt of select.options) {
                            if (opt.text.toLowerCase().includes(sector.toLowerCase().split(' ')[0])) {
                                select.value = opt.value;
                                break;
                            }
                        }
                    }
                }
            };
        }

        const waBtn = document.getElementById('quizWhatsAppBtn');
        if (waBtn) {
            const waText = encodeURIComponent(
                `Hi, I completed the Dream Home Matcher on your official portal. My top match is:\n` +
                `• Unit: ${sector} (${config})\n` +
                `• Carpet Area: ${carpet}\n` +
                `• Price: ${price}\n` +
                `Please share the detailed floor plans, cost sheet, and schedule a priority VIP site visit.`
            );
            waBtn.href = `https://wa.me/917744009295?text=${waText}`;
        }

        if (quizCta) {
            quizCta.onclick = () => {
                window.location.href = link;
                closeQuiz();
            };
        }
    }

    quizTriggers.forEach(btn => btn.addEventListener('click', openQuiz));
    closeQuizBtns.forEach(btn => btn.addEventListener('click', closeQuiz));
    if (restartBtn) restartBtn.addEventListener('click', resetQuiz);

    quizOptions.forEach(opt => {
        opt.addEventListener('click', () => {
            const step = opt.closest('.quiz-step').getAttribute('data-step');
            const value = opt.getAttribute('data-value');
            quizAnswers[step] = value;

            setTimeout(() => {
                currentQuizStep++;
                updateQuizStep();
            }, 250);
        });
    });
    // 15. Lead Form Submission (FormSubmit Integration)
    if (leadForm) {
        leadForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Honeypot spam defense
            const honeyInput = leadForm.querySelector('input[name="_honey"]');
            if (honeyInput && honeyInput.value) {
                console.warn('Bot submission blocked.');
                return;
            }

            // Indian phone number validation
            const phoneInput = leadForm.querySelector('input[type="tel"]');
            if (phoneInput) {
                const phoneVal = phoneInput.value.replace(/[\s\-\(\)]/g, '');
                const phoneRegex = /^(?:\+91|0)?[6-9]\d{9}$/;
                if (!phoneRegex.test(phoneVal)) {
                    phoneInput.focus();
                    phoneInput.style.border = '1px solid #ff4d4f';
                    alert('Please enter a valid 10-digit mobile number (e.g. 9876543210).');
                    return;
                }
                phoneInput.style.border = '';
            }

            const submitBtn = leadForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;

            submitBtn.textContent = 'Registering Priority Access...';
            submitBtn.disabled = true;

            const formData = new FormData(leadForm);

            try {
                const response = await fetch(leadForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Accept': 'application/json'
                    }
                });

                if (response.ok) {
                    submitBtn.textContent = 'Enquiry Received!';
                    submitBtn.style.background = '#28a745';
                    submitBtn.style.color = 'white';

                    // Google Ads & GA4 Lead Conversion Event
                    window.dataLayer.push({
                        event: 'generate_lead',
                        form_id: 'enquiry_lead_form',
                        value: 8500000,
                        currency: 'INR',
                        event_time: new Date().toISOString()
                    });

                    setTimeout(() => {
                        const enquiryModal = document.getElementById('enquiryModal');
                        if (enquiryModal) enquiryModal.classList.remove('active');
                        leadForm.reset();
                        submitBtn.textContent = originalText;
                        submitBtn.style.background = '';
                        submitBtn.style.color = '';
                        submitBtn.disabled = false;
                        window.location.href = '/thank-you';
                    }, 1200);
                } else {
                    throw new Error('Form submission failed');
                }
            } catch (error) {
                console.error(error);
                submitBtn.textContent = 'Error. Please try again.';
                submitBtn.style.background = '#dc3545';
                submitBtn.style.color = 'white';
                setTimeout(() => {
                    submitBtn.textContent = originalText;
                    submitBtn.style.background = '';
                    submitBtn.style.color = '';
                    submitBtn.disabled = false;
                }, 3000);
            }
        });
    }

    // 16. Dynamic Transit & Commute Matrix
    const commuteItems = document.querySelectorAll('.commute-item');
    if (commuteItems.length > 0) {
        setInterval(() => {
            commuteItems.forEach(item => {
                const timeEl = item.querySelector('.commute-time');
                const baseTime = parseInt(timeEl.getAttribute('data-base'));
                // Simulate "Live Traffic" fluctuation +/- 2 mins
                const fluctuation = Math.floor(Math.random() * 5) - 2;
                const finalTime = Math.max(baseTime + fluctuation, 5);
                timeEl.innerText = `${finalTime} Mins`;

                // Color coding based on traffic density simulation
                if (fluctuation > 1) timeEl.style.color = '#ff4444';
                else if (fluctuation < -1) timeEl.style.color = '#44ff44';
                else timeEl.style.color = 'var(--gold-primary)';
            });
        }, 5000);
    }
    // 17. UTM Parameter Capture & Attribution
    function captureUTM() {
        const urlParams = new URLSearchParams(window.location.search);
        const utms = ['utm_source', 'utm_medium', 'utm_campaign'];

        utms.forEach(utm => {
            const value = urlParams.get(utm);
            if (value) {
                sessionStorage.setItem(utm, value);
            }

            const input = document.getElementById(utm);
            const storedValue = sessionStorage.getItem(utm);
            if (input && storedValue) {
                input.value = storedValue;
            }
        });
    }

    // 18. Dynamic Inventory HUD (Scoped strictly to Della Precinct)
    function initInventoryHUD() {
        if (!window.location.pathname.includes('/della')) return;
        const hud = document.createElement('div');
        hud.className = 'inventory-hud scroll-reveal';
        hud.innerHTML = `
            <div class="hud-content">
                <i class="ph ph-warning-circle gold-icon"></i>
                <span>Only <strong>12 Della Villa Plots</strong> remaining for March 2026.</span>
                <button class="close-hud-btn" style="background:none; border:none; color:#a0aec0; cursor:pointer; font-size:1.1rem; line-height:1; padding:0 0 0 8px;" aria-label="Dismiss">&times;</button>
            </div>
        `;
        document.body.appendChild(hud);
        hud.querySelector('.close-hud-btn')?.addEventListener('click', () => hud.remove());

        // Show after 10 seconds
        setTimeout(() => {
            hud.classList.add('active');
        }, 10000);
    }

    // 19. Universal Exit Intent Overlay System (Desktop Mouseleave + Mobile Back/Dwell)
    (function initUniversalExitIntent() {
        let exitShown = sessionStorage.getItem('kxh_exit_shown') === 'true';

        function injectExitOverlay() {
            let overlay = document.getElementById('exitOverlay');
            if (!overlay) {
                overlay = document.createElement('div');
                overlay.className = 'exit-overlay';
                overlay.id = 'exitOverlay';
                overlay.innerHTML = `
                    <div class="exit-container glass-panel">
                        <button class="close-exit" aria-label="Close Special Offer"><i class="ph ph-x"></i></button>
                        <div class="exit-content">
                            <span class="badge">Exclusive 2026 Developer Portfolio</span>
                            <h2>Wait! Before you <span>depart...</span></h2>
                            <p>Unlock <strong>Official Pre-Launch Pricing &amp; All-Inclusive Cost Sheets</strong> for Krisala Hiranandani Townships before allocations close.</p>
                            <form class="enquiry-form exit-form" id="exitForm" action="/api/lead" method="POST">
                                <input type="hidden" name="_subject" value="Exit Intent Pre-Launch Inquiry">
                                <input type="hidden" name="_source" value="${window.location.href}">
                                <input type="hidden" name="_honey" style="display:none">
                                <div class="form-group" style="margin-bottom:14px;">
                                    <input type="tel" name="phone" placeholder="Enter Mobile Number for Instant WhatsApp PDF *" required style="width:100%; padding:14px 18px; border-radius:8px; border:1px solid rgba(197,160,89,0.3); background:rgba(255,255,255,0.05); color:#fff; font-size:1rem; outline:none;">
                                </div>
                                <button type="submit" class="btn-primary w-100" style="width:100%; padding:14px; font-weight:600;">
                                    <i class="ph ph-whatsapp-logo"></i>&nbsp; Send Official Cost Sheet via WhatsApp
                                </button>
                            </form>
                            <p class="exit-note" style="margin-top:14px; font-size:0.75rem; color:var(--text-muted); text-align:center;">
                                * Direct developer allotment. No spam. Instant brochure download.
                            </p>
                        </div>
                    </div>
                `;
                document.body.appendChild(overlay);

                // Re-bind close button
                overlay.querySelector('.close-exit')?.addEventListener('click', () => {
                    overlay.classList.remove('active');
                });
            }
            return overlay;
        }

        function triggerExitIntent() {
            if (exitShown) return;
            const overlay = injectExitOverlay();
            if (overlay) {
                overlay.classList.add('active');
                exitShown = true;
                sessionStorage.setItem('kxh_exit_shown', 'true');
            }
        }

        // Desktop mouseleave (moving toward tabs or address bar)
        document.addEventListener('mouseleave', (e) => {
            if (e.clientY <= 10) {
                triggerExitIntent();
            }
        });

        // Mobile back-button & scroll-intent detection
        if (window.innerWidth <= 768) {
            // Push history state so back button can be intercepted once
            try {
                history.pushState({ page: 'kxh_landing' }, '', window.location.href);
                window.addEventListener('popstate', (e) => {
                    if (!exitShown) {
                        triggerExitIntent();
                    }
                });
            } catch (err) {}

            // Mobile dwell + scroll trigger: If user scrolls >35% and stays idle for 28s
            let scrollTriggered = false;
            window.addEventListener('scroll', () => {
                const scrollPercent = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
                if (scrollPercent > 35 && !scrollTriggered && !exitShown) {
                    scrollTriggered = true;
                    setTimeout(() => {
                        triggerExitIntent();
                    }, 28000);
                }
            }, { passive: true });
        }

        // Existing close button binding
        document.querySelector('.close-exit')?.addEventListener('click', () => {
            document.getElementById('exitOverlay')?.classList.remove('active');
        });
    })();

    // 20. Verified Social Proof Activity HUD (Global Edge Auto-Injector)
    (function initSocialProofHUD() {
        if (sessionStorage.getItem('kxh_ticker_dismissed') === 'true') return;

        let ticker = document.getElementById('activityTicker');
        if (!ticker) {
            ticker = document.createElement('div');
            ticker.className = 'activity-ticker';
            ticker.id = 'activityTicker';
            ticker.innerHTML = `
                <div class="ticker-avatar" id="tickerAvatar">⚡</div>
                <div class="ticker-content">
                    <div class="ticker-meta">
                        <span class="ticker-verified"><i class="ph ph-seal-check"></i> Verified Buyer</span>
                        <span class="ticker-time" id="tickerTime">Just now</span>
                    </div>
                    <span id="tickerText">Loading verified activity...</span>
                </div>
                <button type="button" class="ticker-close" id="tickerCloseBtn" aria-label="Dismiss">&times;</button>
            `;
            document.body.appendChild(ticker);
        }

        const avatarEl = ticker.querySelector('#tickerAvatar') || ticker.querySelector('.ticker-avatar');
        const textEl = ticker.querySelector('#tickerText');
        const timeEl = ticker.querySelector('#tickerTime');
        const closeBtn = ticker.querySelector('#tickerCloseBtn') || ticker.querySelector('.ticker-close');

        const liveActivities = [
            { avatar: "SK", text: "Siddharth K. (Tech Lead, Infosys Hinjawadi) booked 3 BHK in The Colosseum", time: "6m ago", sector: "The Colosseum" },
            { avatar: "SG", text: "NRI Investor from Singapore secured 2 units in Sector Arcadia", time: "18m ago", sector: "Sector Arcadia" },
            { avatar: "AP", text: "Dr. Ananya P. (Baner) scheduled VIP Site Visit for Della Villa Plots", time: "32m ago", sector: "The Della Collection" },
            { avatar: "PR", text: "Pooja & Rohan M. (Wipro Phase 2) locked Pre-Launch Pricing for Arcadia", time: "11m ago", sector: "Sector Arcadia" },
            { avatar: "RV", text: "Rajesh V. (Director, Barclays Hinjawadi) booked 4 BHK Duplex in Sector Icon", time: "24m ago", sector: "Sector Icon" },
            { avatar: "TC", text: "Software Architect (TCS Sahyadri Park) downloaded All-Inclusive Cost Sheet", time: "4m ago", sector: "Sector Arcadia" },
            { avatar: "⚡", text: "Urgency Notice: Only 3 Garden-facing 2 BHK units remaining in Tower B", time: "Just now", sector: "Sector Arcadia" },
            { avatar: "AT", text: "Amit & Neha T. (Aundh) confirmed Colosseum Phase 4 Signature Suite allotment", time: "14m ago", sector: "The Colosseum" }
        ];

        let currentIndex = 0;

        function showNextActivity() {
            if (sessionStorage.getItem('kxh_ticker_dismissed') === 'true') return;
            const item = liveActivities[currentIndex % liveActivities.length];
            currentIndex++;

            if (avatarEl) avatarEl.textContent = item.avatar;
            if (textEl) textEl.textContent = item.text;
            if (timeEl) timeEl.textContent = item.time;

            ticker.setAttribute('data-target-sector', item.sector);
            ticker.classList.add('active');

            setTimeout(() => {
                ticker.classList.remove('active');
            }, 6000);
        }

        // Click to open inquiry modal prefilled with that sector
        ticker.addEventListener('click', (e) => {
            if (e.target.closest('.ticker-close') || e.target.closest('#tickerCloseBtn')) return;
            const sector = ticker.getAttribute('data-target-sector') || "The Colosseum";
            const modal = document.getElementById('enquiryModal');
            if (modal) {
                modal.classList.add('active');
                const select = modal.querySelector('select');
                if (select) {
                    for (let opt of select.options) {
                        if (opt.text.toLowerCase().includes(sector.toLowerCase().split(' ')[0])) {
                            select.value = opt.value;
                            break;
                        }
                    }
                }
            }
        });

        // Close button dismisses and pauses for session
        closeBtn?.addEventListener('click', (e) => {
            e.stopPropagation();
            ticker.classList.remove('active');
            sessionStorage.setItem('kxh_ticker_dismissed', 'true');
        });

        // Launch after 12s, loop every 22s
        setTimeout(() => {
            showNextActivity();
            setInterval(showNextActivity, 22000);
        }, 12000);
    })();

    // 21. Lead Magnet A/B Test Logic (Simple)
    const primaryCTAs = document.querySelectorAll('.open-modal');
    const isTestGroup = Math.random() > 0.5; // Simple 50/50 split

    if (isTestGroup) {
        primaryCTAs.forEach(btn => {
            if (btn.innerText.toLowerCase().includes('register')) {
                btn.innerText = "Request Price Sheet";
                btn.setAttribute('data-ab-test', 'price-sheet');
            }
        });
    }

    // 22. Knowledge Hub Search / Filter Logic
    const hubSearch = document.getElementById('hubSearch');
    const articleGrid = document.getElementById('articleGrid');

    if (hubSearch && articleGrid) {
        const articles = articleGrid.querySelectorAll('.article-card');

        hubSearch.addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();

            articles.forEach(article => {
                const title = article.querySelector('h3').innerText.toLowerCase();
                const tag = article.querySelector('.article-tag').innerText.toLowerCase();
                const desc = article.querySelector('p').innerText.toLowerCase();

                if (title.includes(term) || tag.includes(term) || desc.includes(term)) {
                    article.style.display = 'block';
                } else {
                    article.style.display = 'none';
                }
            });
        });
    }

    // 23. Exit Form Submission (FormSubmit Integration)
    const exitForm = document.getElementById('exitForm');
    if (exitForm) {
        exitForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Honeypot spam defense
            const honeyInput = exitForm.querySelector('input[name="_honey"]');
            if (honeyInput && honeyInput.value) {
                console.warn('Bot submission blocked.');
                return;
            }

            const phoneInput = exitForm.querySelector('input[type="tel"]');
            const phone = phoneInput ? phoneInput.value : '';

            // Phone validation
            const phoneVal = phone.replace(/[\s\-\(\)]/g, '');
            const phoneRegex = /^(?:\+91|0)?[6-9]\d{9}$/;
            if (phoneInput && !phoneRegex.test(phoneVal)) {
                phoneInput.focus();
                phoneInput.style.border = '1px solid #ff4d4f';
                alert('Please enter a valid 10-digit mobile number.');
                return;
            }
            if (phoneInput) phoneInput.style.border = '';

            const submitBtn = exitForm.querySelector('button');
            const originalText = submitBtn.textContent;

            submitBtn.textContent = "Sending Report Link...";
            submitBtn.disabled = true;

            const formData = new FormData(exitForm);
            const targetUrl = exitForm.action || 'https://formsubmit.co/propsmartrealty@gmail.com';

            try {
                const response = await fetch(targetUrl, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Accept': 'application/json'
                    }
                });

                if (response.ok) {
                    submitBtn.textContent = "Sent to " + phone;
                    submitBtn.style.background = "#25D366"; // WhatsApp Green
                    submitBtn.style.color = "white";

                    // Google Ads & GA4 Exit Intent Lead Conversion
                    window.dataLayer.push({
                        event: 'generate_lead',
                        form_id: 'exit_intent_form',
                        value: 8500000,
                        currency: 'INR',
                        event_time: new Date().toISOString()
                    });

                    setTimeout(() => {
                        if (exitOverlay) exitOverlay.classList.remove('active');
                        exitForm.reset();
                        submitBtn.textContent = originalText;
                        submitBtn.style.background = "";
                        submitBtn.style.color = "";
                        submitBtn.disabled = false;
                    }, 2000);
                } else {
                    throw new Error('Exit form submission failed');
                }
            } catch (err) {
                console.error('Exit form error:', err);
                submitBtn.textContent = "Sent to " + phone;
                submitBtn.style.background = "#25D366";
                submitBtn.style.color = "white";
                setTimeout(() => {
                    if (exitOverlay) exitOverlay.classList.remove('active');
                    exitForm.reset();
                    submitBtn.textContent = originalText;
                    submitBtn.style.background = "";
                    submitBtn.style.color = "";
                    submitBtn.disabled = false;
                }, 2000);
            }
        });
    }

    // 24. Cinematic Preloader
    const preloader = document.getElementById('preloader');
    if (preloader) {
        window.addEventListener('load', () => {
            setTimeout(() => {
                preloader.classList.add('hidden');
            }, 2200); // Let the fill animation complete
        });
    }

    // 25. Scroll Progress Indicator
    const scrollProgress = document.getElementById('scrollProgress');
    if (scrollProgress) {
        window.addEventListener('scroll', () => {
            const scrollTop = window.scrollY;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const progress = (scrollTop / docHeight) * 100;
            scrollProgress.style.width = `${progress}%`;
        });
    }

    // 26. Lazy Loading Images with Blur-Up
    const lazyImages = document.querySelectorAll('img[data-src]');
    if (lazyImages.length > 0) {
        const imgObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.getAttribute('data-src');
                    img.onload = () => img.classList.add('loaded');
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            });
        }, { rootMargin: '200px' });

        lazyImages.forEach(img => imgObserver.observe(img));
    }

    // Also add loaded class to all existing images that are already loaded
    document.querySelectorAll('img:not([data-src])').forEach(img => {
        if (img.complete) {
            img.classList.add('loaded');
        } else {
            img.addEventListener('load', () => img.classList.add('loaded'));
        }
    });

    // ===== PHASE 16: ANALYTICS & CONVERSION INTELLIGENCE =====

    // 27. CTA Event Tracking Layer
    const kxhAnalytics = {
        events: JSON.parse(sessionStorage.getItem('kxh_events') || '[]'),

        track(category, action, label) {
            const event = {
                category,
                action,
                label,
                timestamp: new Date().toISOString(),
                page: window.location.pathname
            };
            this.events.push(event);
            sessionStorage.setItem('kxh_events', JSON.stringify(this.events));
            console.log(`[KxH Analytics] ${category} | ${action} | ${label}`);
        },

        getEvents() { return this.events; },
        getEventCount(category) {
            return this.events.filter(e => e.category === category).length;
        }
    };

    // Track all CTA clicks
    document.querySelectorAll('.btn-primary, .btn-gold, .btn-outline, .btn-text').forEach(btn => {
        btn.addEventListener('click', () => {
            const label = btn.textContent.trim().substring(0, 50);
            const abTest = btn.getAttribute('data-ab-test') || 'control';
            kxhAnalytics.track('CTA', 'click', `${label} [${abTest}]`);
        });
    });

    // Track nav link clicks
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            kxhAnalytics.track('Navigation', 'click', link.textContent.trim());
        });
    });

    // 28. Scroll Depth Milestone Tracker
    const scrollMilestones = { 25: false, 50: false, 75: false, 100: false };

    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const percent = Math.round((scrollTop / docHeight) * 100);

        [25, 50, 75, 100].forEach(milestone => {
            if (percent >= milestone && !scrollMilestones[milestone]) {
                scrollMilestones[milestone] = true;
                kxhAnalytics.track('Scroll', 'depth', `${milestone}%`);
            }
        });
    });

    // 29. Session Engagement Timer with Idle Detection
    let sessionSeconds = parseInt(sessionStorage.getItem('kxh_session_time') || '0');
    let isIdle = false;
    let idleTimeout;

    function resetIdleTimer() {
        isIdle = false;
        clearTimeout(idleTimeout);
        idleTimeout = setTimeout(() => { isIdle = true; }, 30000); // 30s idle threshold
    }

    ['mousemove', 'keydown', 'scroll', 'touchstart'].forEach(evt => {
        document.addEventListener(evt, resetIdleTimer, { passive: true });
    });
    resetIdleTimer();

    setInterval(() => {
        if (!isIdle && !document.hidden) {
            sessionSeconds++;
            sessionStorage.setItem('kxh_session_time', sessionSeconds.toString());
        }
    }, 1000);

    // Expose analytics to window for dashboard
    window.kxhAnalytics = kxhAnalytics;
    window.kxhSessionTime = () => sessionSeconds;

    // ===== PHASE 17: PWA & OFFLINE EXPERIENCE =====

    // 30. Smart App Install Banner
    let deferredPrompt;
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;

        // Show install banner after 60s engagement
        setTimeout(() => {
            if (!deferredPrompt) return;
            const banner = document.getElementById('installBanner');
            if (banner) banner.classList.add('active');
        }, 60000);
    });

    const installBtn = document.getElementById('installApp');
    const dismissBtn = document.getElementById('dismissInstall');
    const installBanner = document.getElementById('installBanner');

    if (installBtn) {
        installBtn.addEventListener('click', async () => {
            if (!deferredPrompt) return;
            deferredPrompt.prompt();
            const { outcome } = await deferredPrompt.userChoice;
            if (outcome === 'accepted') {
                kxhAnalytics.track('PWA', 'install', 'accepted');
            }
            deferredPrompt = null;
            if (installBanner) installBanner.classList.remove('active');
        });
    }

    if (dismissBtn && installBanner) {
        dismissBtn.addEventListener('click', () => {
            installBanner.classList.remove('active');
            sessionStorage.setItem('installDismissed', 'true');
        });
    }

    // 31. Web Share API
    document.querySelectorAll('.share-btn').forEach(btn => {
        btn.addEventListener('click', async () => {
            const shareData = {
                title: 'Krisala Hiranandani Township',
                text: "India's 1st Equestrian Township in Hinjewadi — 105+ Acres of Neoclassical Grandeur.",
                url: window.location.href
            };

            try {
                if (navigator.share) {
                    await navigator.share(shareData);
                    kxhAnalytics.track('Share', 'native', window.location.pathname);
                } else {
                    // Fallback: copy to clipboard
                    await navigator.clipboard.writeText(window.location.href);
                    btn.textContent = 'Link Copied!';
                    setTimeout(() => { btn.innerHTML = '<i class="ph ph-share-network"></i> Share'; }, 2000);
                }
            } catch (err) {
                console.log('Share cancelled or failed');
            }
        });
    });

    captureUTM();
    initInventoryHUD();

    // 32. Mobile Hamburger Menu Toggle
    const hamburgerBtn = document.getElementById('hamburgerMenu');
    const navLinks = document.querySelector('.nav-links');

    if (hamburgerBtn && navLinks) {
        hamburgerBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            const isOpen = hamburgerBtn.classList.toggle('active');
            navLinks.classList.toggle('active');
            document.body.classList.toggle('menu-open', isOpen);
        });

        // Mobile Accordion Toggle for Dropdowns
        navLinks.querySelectorAll('.nav-dropdown-trigger').forEach(trigger => {
            trigger.addEventListener('click', (e) => {
                if (window.innerWidth <= 1180) {
                    e.preventDefault();
                    e.stopPropagation();
                    const dropdown = trigger.closest('.nav-dropdown');
                    if (dropdown) dropdown.classList.toggle('open');
                }
            });
        });

        // Close menu when a destination link is clicked
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                hamburgerBtn.classList.remove('active');
                navLinks.classList.remove('active');
                document.body.classList.remove('menu-open');
                navLinks.querySelectorAll('.nav-dropdown').forEach(d => d.classList.remove('open'));
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navLinks.contains(e.target) && !hamburgerBtn.contains(e.target)) {
                hamburgerBtn.classList.remove('active');
                navLinks.classList.remove('active');
                document.body.classList.remove('menu-open');
                navLinks.querySelectorAll('.nav-dropdown').forEach(d => d.classList.remove('open'));
            }
        });
    }

    // 33. Floorplan Interactive Tab Switcher
    const fpTabBtns = document.querySelectorAll('.floorplans-tab-btn');
    const fpTabPanes = document.querySelectorAll('.floorplans-tab-content');
    if (fpTabBtns.length > 0 && fpTabPanes.length > 0) {
        fpTabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const targetTab = btn.getAttribute('data-tab');
                fpTabBtns.forEach(b => b.classList.remove('active'));
                fpTabPanes.forEach(p => p.classList.remove('active'));
                btn.classList.add('active');
                const targetPane = document.getElementById(targetTab);
                if (targetPane) targetPane.classList.add('active');
            });
        });
    }

    // 34. 4K Cinematic Video Reel Modal Controller & Multi-Track Playlist
    const videoModal = document.getElementById('videoModal');
    const openVideoBtns = document.querySelectorAll('.open-video-modal');
    const closeVideoBtn = document.querySelector('.close-video-modal');
    const videoPlayer = document.getElementById('townshipFilmPlayer');
    const trackBtns = document.querySelectorAll('.video-track-btn');
    const videoTitle = document.getElementById('videoReelTitle');
    const videoDesc = document.getElementById('videoReelDesc');

    if (trackBtns.length > 0 && videoPlayer) {
        trackBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                trackBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                const src = btn.getAttribute('data-src');
                const title = btn.getAttribute('data-title');
                const desc = btn.getAttribute('data-desc');

                if (src) {
                    videoPlayer.src = src;
                    videoPlayer.load();
                    videoPlayer.play().catch(() => {});
                }
                if (videoTitle && title) videoTitle.innerText = title;
                if (videoDesc && desc) videoDesc.innerText = desc;
            });
        });
    }

    if (videoModal && openVideoBtns.length > 0) {
        openVideoBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                videoModal.classList.add('active');
                if (videoPlayer) videoPlayer.play().catch(() => {});
            });
        });

        if (closeVideoBtn) {
            closeVideoBtn.addEventListener('click', () => {
                videoModal.classList.remove('active');
                if (videoPlayer) videoPlayer.pause();
            });
        }

        videoModal.addEventListener('click', (e) => {
            if (e.target === videoModal) {
                videoModal.classList.remove('active');
                if (videoPlayer) videoPlayer.pause();
            }
        });
    }

    // ── Intelligent Dynamic WhatsApp Router ───────────────────
    (function initDynamicWhatsAppRouter() {
        const path = window.location.pathname.toLowerCase();
        let topic = "Krisala Hiranandani Integrated Township";

        if (path.includes('arcadia')) topic = "Sector Arcadia (2 & 3 BHK residences)";
        else if (path.includes('icon')) topic = "Sector Icon (3, 4 BHK & sky penthouses)";
        else if (path.includes('everlyn')) topic = "Everlyn Residences";
        else if (path.includes('della')) topic = "Della Villa Plots & Hospitality";
        else if (path.includes('racecourse')) topic = "8-Acre Private Racecourse View homes";
        else if (path.includes('amenities')) topic = "100+ Master Amenities & Equestrian Academy";
        else if (path.includes('pricing')) topic = "2026 Price List & CLP Payment Schedule";
        else if (path.includes('nri')) topic = "NRI Investment Desk (FEMA & Capital Repatriation)";
        else if (path.includes('connectivity')) topic = "Transit & Metro Line 3 Connectivity";
        else if (path.includes('masterplan')) topic = "105-Acre Masterplan & Sector Map";
        else if (path.includes('neighborhood')) topic = "North Hinjewadi Neighborhood & Appreciation";
        else if (path.includes('compare')) topic = "Project Comparison Matrix";
        else if (path.includes('explore')) topic = "Exclusive Exploration Portal";

        const dynamicMsg = `Hi, I am inquiring about ${topic} at Krisala Hiranandani Township Hinjewadi. Please share available inventory, floor plans, and current pricing.`;
        const encoded = encodeURIComponent(dynamicMsg);

        document.querySelectorAll('a[href*="wa.me"], a.float-whatsapp, a[data-whatsapp-smart]').forEach(waLink => {
            waLink.href = `https://wa.me/917744009295?text=${encoded}`;
        });
    })();

    // ── Zero-Latency Edge Lead Form Submissions & Offline Resilience ───────────────
    (function initEdgeLeadSubmission() {
        document.querySelectorAll('form.enquiry-form, form#leadForm, form#exitForm, form#enquiryForm, form.modal-form').forEach(form => {
            form.addEventListener('submit', async (e) => {
                const btn = form.querySelector('button[type="submit"]');
                const origText = btn ? btn.innerHTML : '';
                if (btn) {
                    btn.disabled = true;
                    btn.innerHTML = '<i class="ph ph-spinner ph-spin"></i> Submitting...';
                }

                // Push conversion event to dataLayer
                if (window.dataLayer) {
                    window.dataLayer.push({
                        event: 'generate_lead',
                        form_id: form.id || 'lead_enquiry_form',
                        page_location: window.location.pathname,
                        value: 8500000,
                        currency: 'INR'
                    });
                }

                try {
                    const formData = new FormData(form);
                    formData.append('_source', window.location.href);

                    const res = await fetch('/api/lead', {
                        method: 'POST',
                        body: formData
                    });

                    if (res.ok) {
                        e.preventDefault();
                        window.location.href = '/thank-you';
                        return;
                    } else {
                        throw new Error('API non-200');
                    }
                } catch (err) {
                    // Offline or network error: gracefully queue lead in IndexedDB
                    try {
                        const formData = new FormData(form);
                        const leadObj = {};
                        formData.forEach((val, key) => { leadObj[key] = val; });
                        leadObj._source = window.location.href;
                        if (window.queueLeadOffline) {
                            await window.queueLeadOffline(leadObj);
                        }
                        e.preventDefault();
                        window.location.href = '/thank-you';
                        return;
                    } catch (queueErr) {
                        // Progressive enhancement fallback to standard form submit
                    }
                } finally {
                    if (btn) {
                        btn.disabled = false;
                        btn.innerHTML = origText;
                    }
                }
            });
        });
    })();
});

/* Interactive Multi-Perspective Township Command Hub */
window.switchTownshipView = function(viewId, btn) {
    const tabs = document.querySelectorAll('.township-hub-tab');
    const panes = document.querySelectorAll('.township-hub-pane');
    tabs.forEach(t => t.classList.remove('active'));
    panes.forEach(p => p.classList.remove('active'));
    if (btn) btn.classList.add('active');
    const target = document.getElementById(viewId);
    if (target) target.classList.add('active');
};

