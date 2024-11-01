import { expect } from 'chai';
import sinon from 'sinon';
import { JSDOM } from 'jsdom';
import SecurityModule from '../../assets/js/security.js';
import SecurityBanner from '../../assets/js/security-banner.js';

// Setup test environment
const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>', {
    url: 'http://localhost',
    referrer: 'http://localhost',
    contentType: 'text/html'
});

global.window = dom.window;
global.document = dom.window.document;
global.navigator = dom.window.navigator;
global.MutationObserver = dom.window.MutationObserver;
global.fetch = dom.window.fetch;
global.sessionStorage = {
    getItem: () => null,
    setItem: () => {},
    removeItem: () => {}
};

global.PerformanceObserver = class PerformanceObserver {
    observe() {}
    disconnect() {}
};

describe('Security Implementation Tests', () => {
    let sandbox;

    beforeEach(() => {
        sandbox = sinon.createSandbox();
        document.body.innerHTML = `
            <div id="wb-bnr">
                <a href="https://www.canada.ca/index.html">Home</a>
                <div id="wb-lng">
                    <a href="/fr" lang="fr">Français</a>
                </div>
            </div>
            <nav class="gcweb-menu"></nav>
        `;
    });

    afterEach(() => {
        sandbox.restore();
    });

    describe('SecurityModule Core Tests', () => {
        it('should initialize with correct configuration', () => {
            SecurityModule.init();
            expect(SecurityModule._state.initialized).to.be.true;
            expect(SecurityModule._metrics.startTime).to.be.a('number');
        });

        it('should detect invalid domains', async () => {
            const result = await SecurityModule.verifyIntegrity(
                'https://malicious-site.com/fake.html'
            );
            expect(result).to.be.false;
        });
    });

    describe('SecurityBanner Implementation Tests', () => {
        it('should fix banner links on initialization', () => {
            SecurityBanner.init();
            const links = document.querySelectorAll('a[href*="canada.ca"]');
            links.forEach(link => {
                expect(link.getAttribute('data-processed')).to.equal('true');
            });
        });
    });
});