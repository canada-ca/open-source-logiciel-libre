export default class SecurityModule {
    static _config = {
        checkInterval: 60000,
        maxLogs: 100,
        allowedDomains: ['canada.ca', 'www.canada.ca', 'open.canada.ca'],
        sessionKey: 'gcweb-session',
        pathPrefix: '/open-source-logiciel-libre'
    };

    static _metrics = {
        startTime: Date.now(),
        checks: 0,
        anomalies: 0,
        lastCheck: null
    };

    static _state = {
        domObserver: null,
        navigationObserver: null,
        initialized: false,
        validatedPaths: new Set(),
        pendingChecks: new Map()
    };

    static async verifyIntegrity(url) {
        if (!url) return false;

        try {
            const urlObj = new URL(url);

            if (!SecurityModule._config.allowedDomains.some(domain =>
                urlObj.hostname.endsWith(domain))) {
                SecurityModule._handleAnomaly('domain_mismatch', urlObj.hostname);
                return false;
            }

            const nonce = Date.now().toString(36) + Math.random().toString(36).substr(2);
            const checkUrl = `${url}${url.includes('?') ? '&' : '?'}_=${nonce}`;

            const response = await fetch(checkUrl, {
                method: 'HEAD',
                cache: 'no-store',
                credentials: 'same-origin',
                headers: {
                    'Cache-Control': 'no-cache',
                    'Pragma': 'no-cache'
                }
            });

            SecurityModule._state.validatedPaths.add(urlObj.pathname);
            SecurityModule._metrics.checks++;

            return response.ok;
        } catch (error) {
            SecurityModule._handleAnomaly('integrity_check_failed', {
                url,
                error: error.message
            });
            return false;
        }
    }

    static validateSession() {
        try {
            const time = Date.now() - SecurityModule._metrics.startTime;
            const session = document.cookie
                .split(';')
                .map(c => c.trim())
                .find(c => c.startsWith(`${SecurityModule._config.sessionKey}=`));

            if (!session) {
                SecurityModule._handleAnomaly('session_missing', time);
                return false;
            }

            const [, token] = session.split('=');
            if (!token || token.length < 32) {
                SecurityModule._handleAnomaly('session_malformed', token);
                return false;
            }

            return true;
        } catch (error) {
            SecurityModule._handleAnomaly('session_validation_error', error.message);
            return false;
        }
    }

    static _handleAnomaly(type, data) {
        SecurityModule._metrics.anomalies++;

        const anomaly = {
            timestamp: Date.now(),
            type,
            data,
            url: window.location.href,
            metrics: { ...SecurityModule._metrics }
        };

        const key = `_sec_${Date.now().toString(36)}`;

        try {
            sessionStorage.setItem(key, JSON.stringify(anomaly));

            const keys = Object.keys(sessionStorage)
                .filter(k => k.startsWith('_sec_'))
                .sort();

            while (keys.length > SecurityModule._config.maxLogs) {
                sessionStorage.removeItem(keys.shift());
            }
        } catch (e) {
            // Fail silently
        }

        if (window.location.hostname === 'localhost') {
            console.debug('Security anomaly detected:', type, data);
        }
    }

    static _initObservers() {
        SecurityModule._state.domObserver = new MutationObserver((mutations) => {
            mutations.forEach(mutation => {
                if (mutation.type === 'childList') {
                    mutation.addedNodes.forEach(node => {
                        if (node.tagName === 'A') {
                            SecurityModule.verifyIntegrity(node.href);
                        }
                    });
                }
            });
        });

        SecurityModule._state.domObserver.observe(document.body, {
            childList: true,
            subtree: true
        });

        if (window.PerformanceObserver) {
            SecurityModule._state.navigationObserver = new PerformanceObserver((list) => {
                list.getEntries().forEach(entry => {
                    if (entry.entryType === 'resource') {
                        SecurityModule._validateResource(entry);
                    }
                });
            });

            SecurityModule._state.navigationObserver.observe({
                entryTypes: ['resource', 'navigation']
            });
        }
    }

    static _validateResource(entry) {
        const url = new URL(entry.name);
        if (!SecurityModule._state.validatedPaths.has(url.pathname)) {
            SecurityModule._handleAnomaly('unvalidated_resource', entry.name);
        }
    }

    static async securityCheck() {
        SecurityModule._metrics.lastCheck = Date.now();

        const results = {
            https: window.location.protocol === 'https:',
            session: SecurityModule.validateSession(),
            integrity: await SecurityModule.verifyIntegrity(window.location.href)
        };

        if (!results.https || !results.session || !results.integrity) {
            SecurityModule._handleAnomaly('security_check_failed', results);
        }

        return results;
    }

    static init() {
        if (SecurityModule._state.initialized) return;

        SecurityModule._initObservers();
        SecurityModule._state.initialized = true;

        SecurityModule.securityCheck();

        setInterval(() => {
            SecurityModule.securityCheck();
        }, SecurityModule._config.checkInterval);
    }
}