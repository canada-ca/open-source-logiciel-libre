export default class SecurityBanner {
    static _config = {
        headerSelector: '#wb-bnr',
        navSelector: '.gcweb-menu',
        langSelector: '#wb-lng',
        domains: {
            en: 'https://www.canada.ca/en.html',
            fr: 'https://www.canada.ca/fr.html'
        }
    };

    static _state = {
        currentLang: 'en',
        initialized: false
    };

    static _fixBannerLinks() {
        const header = document.querySelector(SecurityBanner._config.headerSelector);
        if (!header) return;

        header.querySelectorAll('a[href*="canada.ca"]').forEach(link => {
            const url = new URL(link.href);
            const lang = link.closest('[lang]')?.getAttribute('lang') ||
                document.documentElement.lang ||
                SecurityBanner._state.currentLang;

            if (lang === 'fr' && !url.pathname.startsWith('/fr')) {
                url.pathname = `/fr${url.pathname}`;
                link.href = url.toString();
            } else if (lang === 'en' && !url.pathname.startsWith('/en')) {
                url.pathname = `/en${url.pathname}`;
                link.href = url.toString();
            }

            link.setAttribute('data-processed', 'true');
        });
    }

    static _handleLanguageSwitch() {
        const langSwitch = document.querySelector(SecurityBanner._config.langSelector);
        if (!langSwitch) return;

        langSwitch.addEventListener('click', (event) => {
            if (event.target.matches('a[lang]')) {
                event.preventDefault();

                const newLang = event.target.getAttribute('lang');
                SecurityBanner._state.currentLang = newLang;

                SecurityBanner._fixBannerLinks();

                window.location.href = event.target.href;
            }
        });
    }

    static _setupNavigationMenu() {
        const nav = document.querySelector(SecurityBanner._config.navSelector);
        if (!nav) return;

        nav.querySelectorAll('a[href]').forEach(link => {
            const url = new URL(link.href, window.location.origin);

            if (!url.pathname.startsWith('/')) {
                url.pathname = `/${url.pathname}`;
                link.href = url.toString();
            }

            link.setAttribute('rel', 'noopener noreferrer');
            if (url.origin !== window.location.origin) {
                link.setAttribute('target', '_blank');
            }
        });
    }

    static _monitorHeaderChanges() {
        const observer = new MutationObserver((mutations) => {
            mutations.forEach(mutation => {
                if (mutation.type === 'childList' || mutation.type === 'attributes') {
                    SecurityBanner._fixBannerLinks();
                }
            });
        });

        const header = document.querySelector(SecurityBanner._config.headerSelector);
        if (header) {
            observer.observe(header, {
                childList: true,
                subtree: true,
                attributes: true,
                attributeFilter: ['href', 'lang']
            });
        }
    }

    static init() {
        if (SecurityBanner._state.initialized) return;

        SecurityBanner._state.currentLang =
            document.documentElement.lang ||
            document.querySelector('html').getAttribute('lang') ||
            'en';

        SecurityBanner._fixBannerLinks();
        SecurityBanner._handleLanguageSwitch();
        SecurityBanner._setupNavigationMenu();
        SecurityBanner._monitorHeaderChanges();

        SecurityBanner._state.initialized = true;
    }
}