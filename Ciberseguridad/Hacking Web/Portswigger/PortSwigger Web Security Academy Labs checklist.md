#labs #web #guia

>Listado de Laboratorios

---

## Índice rápido

1. [SQL Injection](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#sql-injection)
2. [Cross‑Site Scripting (XSS)](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#cross-site-scripting-xss)
3. [Cross‑Site Request Forgery (CSRF)](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#cross-site-request-forgery-csrf)
4. [Clickjacking](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#clickjacking)
5. [DOM‑based vulnerabilities](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#dom-based-vulnerabilities)
6. [Cross‑Origin Resource Sharing (CORS)](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#cors)
7. [XML External Entity (XXE) Injection](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#xxe-injection)
8. [Server‑Side Request Forgery (SSRF)](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#server-side-request-forgery-ssrf)
9. [HTTP Request Smuggling](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#http-request-smuggling)
10. [OS Command Injection](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#os-command-injection)
11. [Server‑Side Template Injection (SSTI)](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#server-side-template-injection-ssti)
12. [Path Traversal](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#path-traversal)
13. [Access Control Vulnerabilities](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#access-control-vulnerabilities)
14. [Authentication](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#authentication)
15. [WebSockets](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#websockets)
16. [Web Cache Poisoning](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#web-cache-poisoning)
17. [Insecure Deserialization](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#insecure-deserialization)
18. [Information Disclosure](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#information-disclosure)
19. [Business Logic Vulnerabilities](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#business-logic-vulnerabilities)
20. [HTTP Host Header Attacks](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#http-host-header-attacks)
21. [OAuth Authentication](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#oauth-authentication)
22. [File Upload Vulnerabilities](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#file-upload-vulnerabilities)
23. [JSON Web Tokens (JWT)](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#json-web-tokens-jwt)
24. [Essential Skills](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#essential-skills)
25. [Prototype Pollution](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#prototype-pollution)
26. [GraphQL API Vulnerabilities](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#graphql-api-vulnerabilities)
27. [Race Conditions](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#race-conditions)
28. [NoSQL Injection](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#nosql-injection)
29. [API Testing](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#api-testing)
30. [Web LLM Attacks](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#web-llm-attacks)
31. [Web Cache Deception](https://chatgpt.com/c/68446842-460c-800d-affe-c54b51e3f170#web-cache-deception)

# PortSwigger Web Security Academy – **Tabla de progreso**

> Marca cada lab cuando lo completes para llevar un control de tu avance.

### SQL Injection (18)

- [x] SQL injection vulnerability in WHERE clause allowing retrieval of hidden data
- [x] SQL injection vulnerability allowing login bypass
- [x] SQL injection attack, querying the database type and version on Oracle
- [x] SQL injection attack, querying the database type and version on MySQL and Microsoft
- [x] SQL injection attack, listing the database contents on non-Oracle databases
- [x] SQL injection attack, listing the database contents on Oracle
- [x] SQL injection UNION attack, determining the number of columns returned by the query
- [x] SQL injection UNION attack, finding a column containing text
- [x] SQL injection UNION attack, retrieving data from other tables
- [x] SQL injection UNION attack, retrieving multiple values in a single column
- [ ] Blind SQL injection with conditional responses
- [ ] Blind SQL injection with conditional errors
- [ ] Visible error-based SQL injection
- [ ] Blind SQL injection with time delays
- [ ] Blind SQL injection with time delays and information retrieval
- [ ] Blind SQL injection with out-of-band interaction
- [ ] Blind SQL injection with out-of-band data exfiltration
- [ ] SQL injection with filter bypass via XML encoding

---
### Cross-Site Scripting (XSS) (30)

- [ ] Reflected XSS into HTML context with nothing encoded
- [ ] Stored XSS into HTML context with nothing encoded
- [ ] DOM XSS in document.write sink using source location.search
- [ ] DOM XSS in innerHTML sink using source location.search
- [ ] DOM XSS in jQuery anchor href attribute sink using location.search source
- [ ] DOM XSS in jQuery selector sink using a hashchange event
- [ ] Reflected XSS into attribute with angle brackets HTML-encoded
- [ ] Stored XSS into anchor href attribute with double quotes HTML-encoded
- [ ] Reflected XSS into a JavaScript string with angle brackets HTML-encoded
- [ ] DOM XSS in document.write sink using source location.search inside a select element
- [ ] DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded
- [ ] Reflected DOM XSS
- [ ] Stored DOM XSS
- [ ] Reflected XSS into HTML context with most tags and attributes blocked
- [ ] Reflected XSS into HTML context with all tags blocked except custom ones
- [ ] Reflected XSS with some SVG markup allowed
- [ ] Reflected XSS in canonical link tag
- [ ] Reflected XSS into a JavaScript string with single quote and backslash escaped
- [ ] Reflected XSS into a JavaScript string with angle brackets & double quotes HTML-encoded and single quotes escaped
- [ ] Stored XSS into onclick event with angle brackets & double quotes HTML-encoded and single quotes & backslash escaped
- [ ] Reflected XSS into a template literal with angle brackets, single, double quotes, backslash & backticks Unicode-escaped
- [ ] Exploiting cross-site scripting to steal cookies
- [ ] Exploiting cross-site scripting to capture passwords
- [ ] Exploiting XSS to bypass CSRF defenses
- [ ] Reflected XSS with AngularJS sandbox escape without strings
- [ ] Reflected XSS with AngularJS sandbox escape and CSP
- [ ] Reflected XSS with event handlers and href attributes blocked
- [ ] Reflected XSS in a JavaScript URL with some characters blocked
- [ ] Reflected XSS protected by very strict CSP, with dangling markup attack
- [ ] Reflected XSS protected by CSP, with CSP bypass    

---

### CSRF (12)

- [ ] CSRF vulnerability with no defenses
- [ ] CSRF where token validation depends on request method
- [ ] CSRF where token validation depends on token being present
- [ ] CSRF where token is not tied to user session
- [ ] CSRF where token is tied to non-session cookie
- [ ] CSRF where token is duplicated in cookie
- [ ] SameSite Lax bypass via method override
- [ ] SameSite Strict bypass via client-side redirect
- [ ] SameSite Strict bypass via sibling domain
- [ ] SameSite Lax bypass via cookie refresh
- [ ] CSRF where Referer validation depends on header being present
- [ ] CSRF with broken Referer validation

---

### Clickjacking (5)

- [ ] Basic clickjacking with CSRF token protection
- [ ] Clickjacking with form input data prefilled from a URL parameter
- [ ] Clickjacking with a frame buster script
- [ ] Exploiting clickjacking vulnerability to trigger DOM-based XSS
- [ ] Multistep clickjacking

---

### DOM-based Vulnerabilities (7)

- [ ] DOM XSS using web messages
- [ ] DOM XSS using web messages and a JavaScript URL
- [ ] DOM XSS using web messages and JSON.parse
- [ ] DOM-based open redirection
- [ ] DOM-based cookie manipulation
- [ ] Exploiting DOM clobbering to enable XSS
- [ ] Clobbering DOM attributes to bypass HTML filters

---

### CORS (3)

- [ ] CORS vulnerability with basic origin reflection
- [ ] CORS vulnerability with trusted null origin
- [ ] CORS vulnerability with trusted insecure protocols

---

### XXE (9)

- [ ] Exploiting XXE using external entities to retrieve files
- [ ] Exploiting XXE to perform SSRF attacks
- [ ] Blind XXE with out-of-band interaction
- [ ] Blind XXE with out-of-band interaction via XML parameter entities
- [ ] Exploiting blind XXE to exfiltrate data using a malicious external DTD
- [ ] Exploiting blind XXE to retrieve data via error messages
- [ ] Exploiting XInclude to retrieve files
- [ ] Exploiting XXE via image file upload
- [ ] Exploiting XXE to retrieve data by repurposing a local DTD

---

### SSRF (7)

- [ ] Basic SSRF against the local server
- [ ] Basic SSRF against another back-end system
- [ ] Blind SSRF with out-of-band detection
- [ ] SSRF with blacklist-based input filter
- [ ] SSRF with filter bypass via open redirection vulnerability
- [ ] Blind SSRF with Shellshock exploitation
- [ ] SSRF with whitelist-based input filter

---

### HTTP Request Smuggling (21)

- [ ] HTTP request smuggling, confirming a CL.TE vulnerability via differential responses
- [ ] HTTP request smuggling, confirming a TE.CL vulnerability via differential responses
- [ ] HTTP request smuggling, confirming a CL.TE vulnerability with large response body
- [ ] HTTP request smuggling, confirming a TE.CL vulnerability with large response body
- [ ] HTTP request smuggling, basic CL.TE vulnerability
- [ ] HTTP request smuggling, basic TE.CL vulnerability
- [ ] HTTP request smuggling, exploiting basic CL.TE to steal cookies
- [ ] HTTP request smuggling, exploiting basic TE.CL to steal cookies
- [ ] HTTP request smuggling, capturing other user's request
- [ ] HTTP request smuggling, bypassing front-end security controls (CL.TE)
- [ ] HTTP request smuggling, bypassing front-end security controls (TE.CL)
- [ ] HTTP request smuggling, revealing front-end request rewriting
- [ ] HTTP request smuggling, redirecting responses from an internal endpoint
- [ ] HTTP request smuggling with Huffman-encoded response
- [ ] HTTP request smuggling, web cache poisoning
- [ ] HTTP request smuggling, request tunnelling
- [ ] HTTP request smuggling with chunked request in idle connection
- [ ] HTTP request smuggling with obfuscated Transfer-Encoding header
- [ ] HTTP request smuggling, exploiting stale cache storage
- [ ] HTTP/2 request smuggling
- [ ] HTTP/2 request smuggling leading to front-end/back-end desync

---

### OS Command Injection (5)

- [ ] OS command injection, simple case 
- [ ] Blind OS command injection with time delays
- [ ] Blind OS command injection with output redirection
- [ ] Blind OS command injection with out-of-band interaction
- [ ] Blind OS command injection with out-of-band data exfiltration

---
### Server-Side Template Injection (7)

- [ ] Basic server-side template injection
- [ ] Basic server-side template injection (code context)
- [ ] Server-side template injection using documentation
- [ ] Server-side template injection in an unknown language with a documented exploit
- [ ] Server-side template injection with information disclosure via user-supplied objects
- [ ] Server-side template injection in a sandboxed environment
- [ ] Server-side template injection with a custom exploit

---

### Path Traversal (6)

- [ ] File path traversal, simple case
- [ ] File path traversal, traversal sequences blocked with absolute path bypass
- [ ] File path traversal, traversal sequences stripped non-recursively
- [ ] File path traversal, traversal sequences stripped with superfluous URL-decode
- [ ] File path traversal, validation of start of path
- [ ] File path traversal, validation of file extension with null byte bypass

---

### Access Control (13)


- [ ] Unprotected admin functionality
- [ ] Unprotected admin functionality with unpredictable URL
- [ ] User role controlled by request parameter
- [ ] User role can be modified in user profile
- [ ] User ID controlled by request parameter
- [ ] User ID controlled by request parameter with unpredictable user IDs
- [ ] User ID controlled by request parameter with data leakage in redirect
- [ ] User ID controlled by request parameter with password disclosure
- [ ] Insecure direct object references
- [ ] URL-based access control can be circumvented
- [ ] Method-based access control can be circumvented
- [ ] Multi-step process with no access control on one step
- [ ] Referer-based access control

---

### Authentication (14)

- [ ] Username enumeration via different responses
- [ ] 2FA simple bypass
- [ ] Password reset broken logic
- [ ] Username enumeration via subtly different responses
- [ ] Username enumeration via response timing
- [ ] Broken brute-force protection, IP block
- [ ] Username enumeration via account lock
- [ ] 2FA broken logic
- [ ] Brute-forcing a stay-logged-in cookie
- [ ] Offline password cracking
- [ ] Password reset poisoning via middleware
- [ ] Password brute-force via password change
- [ ] Broken brute-force protection, multiple credentials per request
- [ ] 2FA bypass using a brute-force attack

---

### WebSockets (3)

- [ ] Manipulating WebSocket messages to exploit vulnerabilities
- [ ] Cross-site WebSocket hijacking
- [ ] Manipulating the WebSocket handshake to exploit vulnerabilities

---

### Web Cache Poisoning (13)

- [ ] Web cache poisoning with an unkeyed header
- [ ] Web cache poisoning with an unkeyed cookie
- [ ] Web cache poisoning with multiple headers
- [ ] Targeted web cache poisoning using an unknown header
- [ ] Web cache poisoning via an unkeyed query string
- [ ] Web cache poisoning via an unkeyed query parameter
- [ ] Parameter cloaking
- [ ] Web cache poisoning via a fat GET request
- [ ] URL normalization
- [ ] Web cache poisoning to exploit a DOM vulnerability via a cache with strict cacheability criteria
- [ ] Combining web cache poisoning vulnerabilities
- [ ] Cache key injection
- [ ] Internal cache poisoning

---

### Insecure Deserialization (10)

- [ ] Modifying serialized objects
- [ ] Modifying serialized data types
- [ ] Using application functionality to exploit insecure deserialization
- [ ] Arbitrary object injection in PHP
- [ ] Exploiting Java deserialization with Apache Commons
- [ ] Exploiting PHP deserialization with a pre-built gadget chain
- [ ] Exploiting Ruby deserialization using a documented gadget chain
- [ ] Developing a custom gadget chain for Java deserialization
- [ ] Developing a custom gadget chain for PHP deserialization
- [ ] Using PHAR deserialization to deploy a custom gadget chai[ n

---

### Information Disclosure (5)

- [ ] Information disclosure in error messages
- [ ] Information disclosure on debug page
- [ ] Source code disclosure via backup files
- [ ] Authentication bypass via information disclosure
- [ ] Information disclosure in version control history

---

### Business Logic (12)

- [ ] Excessive trust in client-side controls
- [ ] High-level logic vulnerability
- [ ] Inconsistent security controls
- [ ] Flawed enforcement of business rules
- [ ] Low-level logic flaw
- [ ] Inconsistent handling of exceptional input
- [ ] Weak isolation on dual-use endpoint
- [ ] Insufficient workflow validation
- [ ] Authentication bypass via flawed state machine
- [ ] Infinite money logic flaw
- [ ] Authentication bypass via encryption oracle
- [ ] Bypassing access controls using email address parsing discrepancies

---

### HTTP Host Header Attacks (7)

- [ ] Basic password reset poisoning
- [ ] Host header authentication bypass
- [ ] Web cache poisoning via ambiguous requests
- [ ] Routing-based SSRF
- [ ] SSRF via flawed request parsing
- [ ] Host validation bypass via connection state attack
- [ ] Password reset poisoning via dangling markup

---

### OAuth (6)

- [ ] Authentication bypass via OAuth implicit flow
- [ ] SSRF via OpenID dynamic client registration
- [ ] Forced OAuth profile linking
- [ ] OAuth account hijacking via redirect_uri
- [ ] Stealing OAuth access tokens via an open redirect
- [ ] Stealing OAuth access tokens via a proxy page

---

### File Upload (7)

- [ ] Remote code execution via web shell upload
- [ ] Web shell upload via Content-Type restriction bypass
- [ ] Web shell upload via path traversal
- [ ] Web shell upload via extension blacklist bypass
- [ ] Web shell upload via obfuscated file extension
- [ ] Remote code execution via polyglot web shell upload
- [ ] Web shell upload via race condition

---

### JSON Web Tokens (JWT) (8)

- [ ] JWT authentication bypass via unverified signature
- [ ] JWT authentication bypass via flawed signature verification
- [ ] JWT authentication bypass via weak signing key
- [ ] JWT authentication bypass via jwk header injection
- [ ] JWT authentication bypass via jku header injection
- [ ] JWT authentication bypass via kid header path traversal
- [ ] JWT authentication bypass via algorithm confusion
- [ ] JWT authentication bypass via algorithm confusion with no exposed key

---

### Essential Skills (2)

- [ ] Discovering vulnerabilities quickly with targeted scanning
- [ ] Scanning non-standard data structures

---

### Prototype Pollution (10)

- [ ] Client-side prototype pollution via browser APIs
- [ ] DOM XSS via client-side prototype pollution
- [ ] DOM XSS via an alternative prototype pollution vector
- [ ] Client-side prototype pollution via flawed sanitization
- [ ] Client-side prototype pollution in third-party libraries
- [ ] Privilege escalation via server-side prototype pollution
- [ ] Detecting server-side prototype pollution without polluted property reflection
- [ ] Bypassing flawed input filters for server-side prototype pollution
- [ ] Remote code execution via server-side prototype pollution
- [ ] Exfiltrating sensitive data via server-side prototype pollution

---

### GraphQL (5)

- [ ] Accessing private GraphQL posts
- [ ] Accidental exposure of private GraphQL fields
- [ ] Finding a hidden GraphQL endpoint
- [ ] Bypassing GraphQL brute-force protections
- [ ] Performing CSRF exploits over GraphQL

---

### Race Conditions (6)

- [ ] Limit overrun race conditions
- [ ] Bypassing rate limits via race conditions
- [ ] Multi-endpoint race conditions
- [ ] Single-endpoint race conditions
- [ ] Exploiting time-sensitive vulnerabilities
- [ ] Partial construction race conditions

---

### NoSQL Injection (4)

- [ ] Detecting NoSQL injection
- [ ] Exploiting NoSQL operator injection to bypass authentication
- [ ] Exploiting NoSQL injection to extract data
- [ ] Exploiting NoSQL operator injection to extract unknown fields

---

### API Testing (5)

- [ ] Exploiting an API endpoint using documentation
- [ ] Exploiting server-side parameter pollution in a query string
- [ ] Finding and exploiting an unused API endpoint
- [ ] Exploiting a mass assignment vulnerability
- [ ] Exploiting server-side parameter pollution in a REST URL

---

### Web LLM Attacks (4)

- [ ] Exploiting LLM APIs with excessive agency
- [ ] Exploiting vulnerabilities in LLM APIs
- [ ] Indirect prompt injection
- [ ] Exploiting insecure output handling in LLMs

---

### Web Cache Deception (5)

- [ ] Exploiting path mapping for web cache deception
- [ ] Exploiting path delimiters for web cache deception
- [ ] Exploiting origin server normalization for web cache deception
- [ ] Exploiting cache server normalization for web cache deception
- [ ] Exploiting exact-match cache rules for web cache deception
