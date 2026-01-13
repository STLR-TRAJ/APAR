"""
GRC AUDIT SYSTEM - FINAL FRAMEWORK MODULES (Part 4)
=================================================
Covers: SOX ITGC, PCI DSS v4.0, HIPAA
"""


def get_sox_itgc_module() -> str:
    """SOX IT General Controls - Sarbanes-Oxley Act"""
    return """
[MODULE B8 — SOX ITGC AUDIT ENGINE]

SCOPE: IT General Controls supporting financial reporting
AUTHORITY: Sarbanes-Oxley Act of 2002 (US Public Companies)
ENFORCEMENT: SEC (Securities and Exchange Commission)

APPLICABILITY:
- US public companies (listed on NYSE, NASDAQ, etc.)
- Foreign companies with US listings (ADRs)
- Companies preparing for IPO (SOX readiness)

LIABILITY: CFO and CEO personally attest to effectiveness of internal controls
- Criminal penalties for false certification (up to 20 years imprisonment)
- Civil penalties (fines, disgorgement)

AUDIT TONE: "If this fails, CFO faces personal exposure. State it clearly."

SOX 404 COMPLIANCE:

Section 404(a): Management Assessment
- Management must assess and report on effectiveness of ICFR (Internal Control over Financial Reporting)

Section 404(b): Auditor Attestation
- External auditor must attest to management's assessment (for large accelerated filers)

IT GENERAL CONTROLS (ITGC) FRAMEWORK

ITGCs support application controls (which directly impact financial data)

ITGC Categories:
1. Access to Programs and Data
2. Program Development and Change Management
3. Computer Operations
4. System Software

RELATIONSHIP TO FINANCIAL REPORTING:

Financial Systems in Scope:
- ERP (SAP, Oracle, NetSuite, etc.)
- General Ledger
- Accounts Payable / Receivable
- Payroll
- Revenue Recognition Systems
- Consolidation Tools
- Any system feeding financial statements

SCOPING METHODOLOGY:

Step 1: Identify financially relevant applications
Step 2: Trace financial statement line items to source systems
Step 3: Identify ITGCs supporting those systems
Step 4: Test ITGC design and operating effectiveness

1. ACCESS TO PROGRAMS AND DATA

   Control Objective: Prevent unauthorized access to financial systems and data

   AC-1: User Access Provisioning
   
   Requirement:
   - Access to financial systems requires documented approval
   - Role-Based Access Control (RBAC)
   - Segregation of Duties (SoD)
   
   Audit Evidence (12-month period for annual audit):
   - Access request forms (sample 25-40 over year)
   - Approval by manager + IT
   - Provisioning within SLA (e.g., 48 hours)
   
   Testing Procedure:
   - Sample access requests → Verify approval before provisioning
   - Verify role assigned matches approved role
   - Check for SoD conflicts (cannot have incompatible roles)
   
   SoD Examples (CRITICAL):
   - Cannot initiate AND approve payments
   - Cannot create vendor AND process vendor payment
   - Cannot post journal entries AND approve journal entries
   - Cannot access production AND have developer rights
   
   Tool Check: SoD analysis (e.g., SAP GRC, Oracle GRC)
   - Run SoD report for all financial users
   - Flag conflicts → Require compensating controls or role change
   
   AC-2: Privileged Access Management
   
   Requirement:
   - Privileged accounts (admin, root, database admin) restricted
   - Privileged access requires approval and logging
   
   Audit Evidence:
   - Privileged account inventory
   - Privileged Access Management (PAM) solution (CyberArk, BeyondTrust)
   - Privileged access logs (who accessed, when, what was done)
   
   Testing Procedure:
   - Verify privileged accounts are named (not generic "admin")
   - Sample privileged access sessions → Verify business justification
   - Check for emergency access (break-glass) → Verify post-facto review
   
   AC-3: User Access Reviews
   
   Requirement:
   - Quarterly access reviews for financial systems
   - Managers certify user access is appropriate
   - Remediate exceptions (remove unnecessary access)
   
   Audit Evidence (Critical for SOX):
   - Access review reports (4 quarters = 4 reports for annual audit)
   - Manager sign-offs (dated, documented)
   - Remediation evidence (access removed for flagged users)
   
   Testing Procedure:
   - Verify reviews performed quarterly (no gaps)
   - Sample users from review → Verify access still appropriate
   - Check for stale accounts (no login > 90 days) → Should be flagged
   
   RED FLAG:
   If access review skipped even 1 quarter → Control deficiency
   → CFO must disclose material weakness if significant
   
   AC-4: Termination Process
   
   Requirement:
   - Access revoked on termination date (same day)
   - No delay tolerance for financial systems
   
   Audit Evidence:
   - HR termination list (all terminations over audit period)
   - Access revocation logs (cross-reference with termination dates)
   
   Testing Procedure:
   - For each terminated employee:
     - Verify ERP access disabled on termination date
     - Verify database access removed
     - Verify VPN/remote access disabled
   - Sample: 100% if < 25 terminations, otherwise 25-40
   
   CRITICAL:
   If even 1 terminated employee retained financial system access > 1 day
   → Significant deficiency (material weakness if high-risk role like Controller)

2. PROGRAM DEVELOPMENT AND CHANGE MANAGEMENT

   Control Objective: Ensure changes to financial systems are authorized, tested, and deployed correctly

   CM-1: Change Authorization
   
   Requirement:
   - Changes to production financial systems require approval
   - Business sign-off + IT management approval
   
   Audit Evidence:
   - Change tickets (sample 25-40 over audit period)
   - Approval workflow documented
   
   Testing Procedure:
   - Sample changes to ERP, GL, AR, AP → Verify approval obtained
   - Verify appropriate approvers (business owner + IT)
   - Emergency changes: Verify post-facto approval within 24 hours
   
   CM-2: Testing Before Deployment
   
   Requirement:
   - Changes tested in non-production environment
   - Test results documented and reviewed
   
   Audit Evidence:
   - Test plans and test results attached to change tickets
   - User Acceptance Testing (UAT) sign-off
   
   Testing Procedure:
   - Sample changes → Verify test evidence exists
   - Check test coverage (functional + regression testing)
   - Verify UAT sign-off from business user
   
   CM-3: Migration to Production
   
   Requirement:
   - Production migration performed by authorized personnel
   - Segregation: Developers cannot migrate to production
   
   Audit Evidence:
   - Migration logs (who migrated, when)
   - Role separation (developer role ≠ production migration role)
   
   Testing Procedure:
   - Sample production migrations → Verify performed by authorized IT ops (not developers)
   - Check for direct developer access to production (should be NONE)
   
   CRITICAL SoD:
   Developer access to production = Material weakness
   
   CM-4: Code Review
   
   Requirement:
   - Custom code changes reviewed by peer or lead developer
   - Security review for sensitive changes
   
   Audit Evidence:
   - Code review logs (GitHub pull request approvals, etc.)
   - Code review checklist (security, performance, functionality)
   
   Testing Procedure:
   - Sample code changes → Verify peer review before merge
   - Check for self-approvals (should be prohibited)
   
   CM-5: Back-Out Plan
   
   Requirement:
   - Back-out procedures documented for each change
   - Ability to rollback if change fails
   
   Audit Evidence:
   - Back-out plan documented in change ticket
   - Rollback testing (for critical changes)
   
   Testing Procedure:
   - Sample changes → Verify back-out plan documented
   - If change failed, verify rollback executed

3. COMPUTER OPERATIONS

   Control Objective: Ensure financial systems operate reliably and securely

   CO-1: Batch Job Monitoring
   
   Requirement:
   - Automated batch jobs (e.g., GL close, payroll processing) monitored for failures
   - Failures investigated and resolved
   
   Audit Evidence:
   - Batch job logs (daily monitoring over audit period)
   - Failure investigation records
   
   Testing Procedure:
   - Sample batch job logs (monthly over year → 12 samples)
   - Verify failed jobs documented and resolved
   - Check for unresolved failures (should be escalated)
   
   CO-2: Backup and Restoration
   
   Requirement:
   - Daily backups of financial data
   - Restoration testing (quarterly minimum)
   - Offsite/cloud backup storage
   
   Audit Evidence:
   - Backup logs (daily over entire audit period)
   - Restoration test results (4 tests for annual audit)
   
   Testing Procedure:
   - Verify backup success rate (target: > 99%)
   - Sample restoration tests → Verify successful and within RTO
   - Check backup encryption (data-at-rest)
   
   CO-3: Incident Management
   
   Requirement:
   - Security incidents affecting financial systems documented and resolved
   - Root cause analysis performed
   
   Audit Evidence:
   - Incident log (financial systems only)
   - Incident response documentation (investigation, resolution, lessons learned)
   
   Testing Procedure:
   - Sample incidents → Verify documented, investigated, resolved
   - Check for unresolved incidents (should be none at year-end)
   
   CO-4: Vulnerability Management
   
   Requirement:
   - Vulnerability scans of financial systems (quarterly)
   - Critical vulnerabilities remediated within SLA (e.g., 30 days)
   
   Audit Evidence:
   - Vulnerability scan reports (4 per year)
   - Remediation tracking (vulnerability aging report)
   
   Testing Procedure:
   - Verify quarterly scans performed (no gaps)
   - Sample critical vulnerabilities → Verify remediation within SLA
   - Check for long-outstanding vulnerabilities (red flag if > 90 days)
   
   CO-5: Patch Management
   
   Requirement:
   - Security patches applied to financial systems timely
   - Patch testing before production deployment
   
   Audit Evidence:
   - Patch management logs (what patches, when applied)
   - Patch testing documentation
   
   Testing Procedure:
   - Sample critical patches (OS, database, ERP) → Verify applied within SLA
   - Verify patches tested before production (no direct prod patching)

4. SYSTEM SOFTWARE (Infrastructure Controls)

   Control Objective: Ensure underlying infrastructure (OS, database, network) is secure

   SS-1: Operating System Hardening
   
   Requirement:
   - OS configurations per security baselines (CIS benchmarks)
   - Unnecessary services disabled
   
   Audit Evidence:
   - OS configuration baselines
   - Configuration compliance reports
   
   Testing Procedure:
   - Sample financial servers → Verify hardening applied
   - Check for deviations from baseline (should be documented/approved)
   
   SS-2: Database Security
   
   Requirement:
   - Database access restricted (application access only, no direct user queries)
   - Database activity monitoring (DAM)
   
   Audit Evidence:
   - Database user list (verify no end-users have direct DB access)
   - DAM logs (privileged DB access monitored)
   
   Testing Procedure:
   - Verify application service accounts only for DB access
   - Check for user accounts with direct DB access (should be exceptions only)
   - If exceptions exist (e.g., DBA), verify logging and review
   
   SS-3: Network Security
   
   Requirement:
   - Firewall rules restrict access to financial systems
   - Network segmentation (financial systems isolated)
   
   Audit Evidence:
   - Network diagram (financial system zone highlighted)
   - Firewall rule exports (restrictive rules)
   
   Testing Procedure:
   - Verify financial systems in separate VLAN/subnet
   - Sample firewall rules → Verify principle of least privilege (only necessary ports open)

COMPENSATING CONTROLS

If control cannot be implemented (e.g., SoD conflict unavoidable due to small team):

Compensating Control Requirements:
- Must reduce risk to acceptable level
- Must be documented and approved by management
- Must be tested for effectiveness

Example:
- Control Deficiency: One person creates and approves journal entries (SoD conflict)
- Compensating Control: CFO reviews all journal entries weekly (detective control)
- Evidence: Weekly review logs with CFO sign-off

Audit Challenge:
"Is compensating control truly effective, or just a paper exercise?
Show me review logs with evidence of questioning/corrections."

TESTING APPROACH (SOX 404)

Testing Phases:

Phase 1: Walkthroughs (Q1-Q2)
- Understand control design
- Identify key controls
- Document control procedures

Phase 2: Interim Testing (Q3)
- Test controls for first 9 months
- Identify control deficiencies early
- Remediate before year-end

Phase 3: Roll-Forward Testing (Q4)
- Test Q4 controls
- Update testing if control changes

Phase 4: Year-End Testing (Post-Close)
- Final testing for full 12 months
- Management assessment report
- Auditor attestation

Sample Sizes (SOX 404):

Low Risk Control: 1 sample (if automated)
Moderate Risk: 5-25 samples
High Risk: 25-40 samples

Automation Consideration:
- Automated controls (e.g., system-enforced SoD) → Test IT environment + 1 transaction
- Manual controls (e.g., access reviews) → Test full population or large sample

CONTROL DEFICIENCY CLASSIFICATION

Deficiency: Control does not operate as designed

Significant Deficiency: 
- More than remote likelihood of material misstatement not prevented/detected
- Communicated to audit committee

Material Weakness:
- Reasonable possibility of material misstatement not prevented/detected
- Must be disclosed in 10-K (public disclosure)
- CFO/CEO cannot certify controls are effective

Example Material Weaknesses:
- No access reviews for entire year
- Terminated CFO retained system access for 3 months
- Developer has production access and made unauthorized changes
- SoD conflict (treasurer can initiate and approve payments) with no compensating control

Audit Guidance:
"If control deficiency could lead to material misstatement (> $1M typical threshold),
classify as Material Weakness. CFO must disclose. Stock price impact likely."

OUTPUT FORMAT: SOX ITGC Assessment

**IN-SCOPE FINANCIAL APPLICATIONS**
| Application | Purpose | Financial Statement Impact | Risk Rating |
|-------------|---------|---------------------------|-------------|
| SAP ERP | GL, AR, AP, Inventory | All line items | HIGH |
| ADP Payroll | Payroll expense | SG&A | MEDIUM |
| Salesforce | Revenue recognition | Revenue | HIGH |
| ... | | | |

**ITGC TESTING RESULTS**

| Control # | Control Description | Test Period | Sample Size | Exceptions | Classification |
|-----------|---------------------|-------------|-------------|------------|----------------|
| AC-1 | Access provisioning requires approval | 12 months | 35 | 0 | ✓ Effective |
| AC-3 | Quarterly access reviews | Q1-Q4 | 4 quarters | 1 (Q3 delayed) | ⚠ Deficiency |
| AC-4 | Termination access removal | 12 months | 28 | 1 (3-day delay) | ⚠ Deficiency |
| CM-1 | Change authorization | 12 months | 40 | 2 (post-facto) | ⚠ Deficiency |
| CM-3 | Production migration SoD | 12 months | 40 | 0 | ✓ Effective |
| CO-2 | Backup restoration testing | 4 quarters | 4 | 0 | ✓ Effective |
| ... | | | | | |

**DEFICIENCY SUMMARY**

Deficiencies:
1. AC-3: Q3 access review delayed by 2 weeks (performed in October instead of September)
   - Impact: Low (review eventually performed, no inappropriate access identified)
   - Classification: Deficiency (not Significant Deficiency)

2. AC-4: 1 terminated employee (non-financial role) retained system access for 3 days
   - Impact: Low (read-only access, no transactions processed)
   - Classification: Deficiency

3. CM-1: 2 emergency changes deployed with post-facto approval (4 hours later instead of prior)
   - Impact: Low (changes were necessary, approval documented)
   - Classification: Deficiency

Significant Deficiencies: NONE

Material Weaknesses: NONE

**MANAGEMENT CONCLUSION**
Based on testing, ITGCs are effective with minor deficiencies that do not rise to Significant Deficiency or Material Weakness. Deficiencies have been remediated post-testing.

Management asserts that internal controls over financial reporting are effective as of December 31, 2025.

**CFO/CEO CERTIFICATION**
[Ready for SOX 404 certification]

**AUDIT FIRM ATTESTATION**
[External auditor to provide separate attestation report under AS 2201/AS 5]
"""


def get_pci_dss_v4_module() -> str:
    """PCI DSS v4.0 - Payment Card Industry Data Security Standard"""
    return """
[MODULE B9 — PCI DSS v4.0 AUDIT ENGINE]

SCOPE: Payment Card Data Security
VERSION: PCI DSS v4.0 (Effective March 31, 2024; mandatory March 31, 2025)
AUTHORITY: PCI Security Standards Council (PCI SSC)

APPLICABILITY:
- ALL entities that store, process, or transmit cardholder data
- Merchants (all sizes)
- Service providers (payment processors, gateways, hosting providers)
- Even 1 transaction = PCI DSS applies

ENFORCEMENT:
- Card brands (Visa, Mastercard, Amex, Discover) via acquiring banks
- Non-compliance penalties: Fines ($5K-$100K/month), increased transaction fees, loss of ability to process cards

CARDHOLDER DATA ENVIRONMENT (CDE):

CDE Includes:
- Systems that store, process, or transmit cardholder data (CHD)
- Systems that provide security services to CDE (firewalls, IDS, authentication)
- Systems that can impact security of CDE (same network segment)

Cardholder Data (CHD):
- Primary Account Number (PAN) [16-digit card number] - MUST PROTECT
- Cardholder Name
- Expiration Date
- Service Code

Sensitive Authentication Data (SAD): CANNOT STORE AFTER AUTHORIZATION
- Full magnetic stripe data
- CAV2/CVC2/CVV2/CID [3/4-digit security code]
- PINs / PIN blocks

VALIDATION LEVELS (Merchants):

Level 1: > 6 million transactions/year → Annual onsite audit by QSA (Qualified Security Assessor)
Level 2: 1-6 million transactions/year → Annual Self-Assessment Questionnaire (SAQ) + Quarterly ASV scans
Level 3: 20K-1M e-commerce transactions/year → Annual SAQ + Quarterly scans
Level 4: < 20K e-commerce OR < 1M total → Annual SAQ (may vary by acquirer)

SELF-ASSESSMENT QUESTIONNAIRES (SAQ):

SAQ A: Card-not-present (e-commerce), outsourced payment page (redirect to PSP)
- Easiest (22 requirements out of 400+)
- No CHD stored/processed/transmitted by merchant

SAQ A-EP: E-commerce with outsourced processing BUT website impacts payment security
- Moderate (~200 requirements)

SAQ D: All other merchants (full PCI DSS scope)
- Hardest (all 400+ requirements)
- Includes merchants with POS terminals, call centers, etc.

Audit Guidance:
"Which SAQ type applies? If unsure → Likely SAQ D (full scope). 
Verify with acquirer or QSA. Misclassification = non-compliance risk."

PCI DSS v4.0 STRUCTURE:

12 Requirements across 6 Goals:

GOAL 1: Build and Maintain a Secure Network and Systems
- Requirement 1: Install and maintain network security controls
- Requirement 2: Apply secure configurations to all system components

GOAL 2: Protect Account Data
- Requirement 3: Protect stored account data
- Requirement 4: Protect cardholder data with strong cryptography during transmission

GOAL 3: Maintain a Vulnerability Management Program
- Requirement 5: Protect all systems and networks from malicious software
- Requirement 6: Develop and maintain secure systems and software

GOAL 4: Implement Strong Access Control Measures
- Requirement 7: Restrict access to system components and cardholder data by business need to know
- Requirement 8: Identify users and authenticate access to system components
- Requirement 9: Restrict physical access to cardholder data

GOAL 5: Regularly Monitor and Test Networks
- Requirement 10: Log and monitor all access to system components and cardholder data
- Requirement 11: Test security of systems and networks regularly

GOAL 6: Maintain an Information Security Policy
- Requirement 12: Support information security with organizational policies and programs

KEY CHANGES IN v4.0 (vs v3.2.1):

New Requirements:
- Requirement 6.4.3: Inventory of bespoke and custom software (scripts, change history)
- Requirement 11.6.1: Intrusion detection/prevention systems (IDS/IPS) mandatory
- Requirement 12.3.1-12.3.2: Targeted Risk Analysis (TRA) for Customized Approach
- Multi-Factor Authentication (MFA) expanded to all CDE access (Requirement 8.4.2)

Customized Approach:
- Alternative to Defined Approach (prescriptive controls)
- Allows entity to define custom controls IF they achieve stated objective
- Requires Targeted Risk Analysis (TRA) documentation
- QSA must validate control meets objective

Audit Guidance:
"If claiming Customized Approach, demand TRA documentation.
No TRA = Non-compliant. Revert to Defined Approach."

DETAILED AUDIT PROCEDURES (Select High-Risk Requirements):

REQUIREMENT 1: Network Security Controls (Firewalls)

1.2.1: Configuration standards for network security controls
- Firewall rules documented and reviewed at least every 6 months
- Deny-all, permit-by-exception

Audit Evidence:
- Firewall rule documentation (current rules export)
- Review logs (bi-annual reviews → need 2 for annual audit)
- Rule justification (business need for each rule)

Testing Procedure:
- Sample firewall rules → Verify business justification documented
- Verify bi-annual review performed (check dates)
- Test: Verify inbound traffic to CDE restricted (only necessary ports)

1.3.1: Inbound traffic to CDE restricted
- Only essential traffic allowed
- Default deny

Audit Test:
- Attempt connection from untrusted network to CDE (should be blocked)
- Verify DMZ exists (internet-facing zone separate from CDE)

1.4.2: Outbound traffic from CDE authorized
- Monitor outbound traffic (prevent data exfiltration)

Audit Evidence:
- Outbound firewall rules
- Data Loss Prevention (DLP) solution

REQUIREMENT 3: Protect Stored Account Data

3.1.1: CHD storage minimized
- Retention policy (only store if business need)
- Delete CHD when no longer needed

Audit Evidence:
- Data retention policy (defines retention period per business need)
- Automated deletion jobs (purge after retention period)

Audit Challenge:
"Why are you storing PAN? Is it necessary? Can you tokenize instead?"

3.2.1: Account data storage does not exceed business justification

Audit Test:
- Query databases for CHD (PAN search using regex: 4[0-9]{15} for Visa)
- Verify only approved storage locations (no rogue databases/files)

3.3.1-3.3.3: PAN Masking

Requirements:
- PAN masked when displayed (show last 4 digits only)
- Exceptions: Business need (e.g., call center with authentication)

Audit Test:
- View application screens → Verify PAN masked (e.g., 411111******1111)
- Verify unmasking requires authentication + logging

3.4.1: PAN Unreadable Anywhere Stored

Cryptographic Requirements:
- Encrypt PAN using strong cryptography (AES-256, RSA-2048)
- OR tokenize (replace PAN with non-sensitive token)
- OR one-way hash (if no need to retrieve original PAN)

Audit Evidence:
- Encryption key management (keys stored separately from data)
- Database encryption configuration (TDE: Transparent Data Encryption)
- Tokenization solution (PCI-compliant token vault)

Audit Test:
- Access database directly → Verify PAN encrypted (not plaintext)
- Attempt to decrypt → Verify keys are access-controlled

3.5.1: Cryptographic Keys Protected

Requirements:
- Keys stored securely (HSM: Hardware Security Module preferred)
- Key access restricted (dual control, split knowledge)
- Key rotation (annual or per policy)

Audit Evidence:
- Key management policy
- HSM configuration (FIPS 140-2 Level 2+ certified)
- Key custodian list (who has access to keys)
- Key ceremony records (key generation, rotation)

Audit Challenge:
"Show me key ceremony log. Who were the witnesses? 
Where are keys stored? Can one person decrypt data alone? (Should be NO)"

3.6.1: Key Management Procedures

Requirements:
- Key generation (strong entropy, per algorithm standards)
- Key distribution (secure channels)
- Key storage (encrypted, access-controlled)
- Key change (compromised keys replaced, routine rotation)
- Key destruction (secure deletion when no longer needed)

REQUIREMENT 4: Protect CHD During Transmission

4.1.1: Strong Cryptography for Transmission

Requirements:
- TLS 1.2 or TLS 1.3 (SSL, TLS 1.0, TLS 1.1 prohibited)
- Strong ciphers (AES-GCM, ChaCha20-Poly1305)
- No weak ciphers (RC4, DES, 3DES, MD5)

Audit Evidence:
- SSL/TLS configuration (web servers, APIs)
- Vulnerability scan results (verify no weak ciphers)

Audit Test:
- Use sslyze or testssl.sh → Verify TLS 1.2+ only
- Verify certificate validity (not expired, trusted CA)

4.2.1: Never Send PAN via End-User Messaging

Prohibited:
- Email (even encrypted)
- SMS
- Chat/IM

Audit Evidence:
- DLP policies (block PAN in emails/messages)
- User training (awareness of prohibition)

Audit Test:
- Send test email with fake PAN → Verify blocked by DLP

REQUIREMENT 6: Secure Systems and Software

6.2.4: Vulnerability Management

Requirements:
- Vulnerability scans (internal quarterly, external quarterly)
- Critical vulnerabilities patched within 30 days (was within 1 month in v3.2.1)

Audit Evidence:
- Vulnerability scan reports (quarterly → 4 for annual audit)
- Patch management logs (critical patches applied within 30 days)

Audit Test:
- Sample critical vulnerabilities → Verify remediation within 30 days
- Verify quarterly scans performed (no gaps)

6.3.1: Secure Software Development Lifecycle (SDLC)

Requirements:
- Security requirements in design
- Code review (manual or automated SAST: Static Application Security Testing)
- Security testing before deployment

Audit Evidence:
- SDLC policy (security gates defined)
- Code review logs (peer review or tool-based)
- Security testing reports (SAST, DAST: Dynamic Application Security Testing)

6.4.3: Bespoke and Custom Software Inventory (NEW in v4.0)

Requirements:
- Inventory of all custom code and scripts
- Change history maintained
- Review for unauthorized changes

Audit Evidence:
- Software inventory (all custom applications, scripts)
- Version control logs (Git commits, change history)

Audit Challenge:
"Show me all custom scripts with access to CHD. 
Are they version-controlled? Who approved each change?"

REQUIREMENT 8: Identification and Authentication

8.3.1: MFA for ALL Access to CDE (Enhanced in v4.0)

Requirements:
- MFA required for:
  - All remote access to CDE
  - All access to CDE from within internal network (NEW in v4.0 - applies after March 31, 2025)
  - All administrative access

MFA Types (at least 2 of 3):
- Something you know (password)
- Something you have (token, smart card)
- Something you are (biometric)

Audit Evidence:
- MFA solution (Duo, Okta, RSA SecurID, etc.)
- MFA coverage report (% users with MFA enabled)

Audit Test:
- Attempt login to CDE system without MFA → Should be blocked
- Verify 100% coverage (no exceptions unless documented with compensating control)

8.4.2: MFA for All Personnel with Administrative Access (CRITICAL)

Requirement: Admins MUST use MFA (no exceptions)

Audit Test:
- Sample admin accounts → Verify MFA enforced
- Attempt admin login without MFA → Must fail

RED FLAG:
If even 1 admin account without MFA → Non-compliant (Requirement 8.4.2 failure)

8.6.1-8.6.3: Password Requirements

Requirements:
- Minimum length: 12 characters (or 8 if MFA used)
- Complexity (mix of uppercase, lowercase, numbers, special characters)
- No common passwords (password, 123456, etc.)
- Password change: At least every 90 days (if passwords sole authentication factor)

Audit Evidence:
- Password policy configuration (Active Directory, IAM)
- Password compliance reports (weak passwords flagged)

Audit Test:
- Attempt to set weak password (e.g., "Password123") → Should be rejected

REQUIREMENT 10: Logging and Monitoring

10.2.1: Audit Logs Implemented

Events to Log:
- User access to CHD
- Actions by privileged users (root, admin)
- Access to audit logs
- Invalid login attempts
- Changes to authentication credentials
- System component changes (new software, config changes)

Audit Evidence:
- SIEM configuration (log sources, retention)
- Log review reports (monthly minimum → 12 for annual audit)

Audit Test:
- Simulate logged event (e.g., admin login) → Verify logged in SIEM
- Review sample log entries → Verify completeness (timestamp, user ID, event type, result)

10.3.1: Audit Logs Retention (90 days online, 1 year total)

Requirements:
- 90 days online (readily available for analysis)
- 1 year total (archived, retrievable if needed)

Audit Test:
- Query SIEM for logs from 80 days ago → Should be available
- Query for logs from 11 months ago → Should be retrievable (even if offline)

10.4.1: Log Review (Daily for Critical Systems)

Requirements:
- Daily review of logs for CDE components
- Automated alerting for critical events (failed logins, privilege escalation)

Audit Evidence:
- Daily log review reports (365 for annual audit - typically sampled)
- SIEM alert rules (critical events defined)
- Alert investigation logs (how alerts were handled)

Audit Test:
- Sample log review reports (daily over 1 month = 30 reports)
- Verify reviews performed daily (no gaps)
- Verify findings documented and investigated

REQUIREMENT 11: Security Testing

11.3.1: Penetration Testing (Annual + After Significant Changes)

Requirements:
- Annual penetration test (external and internal)
- After significant changes (new systems, network changes)
- Methodology: Industry-accepted (OWASP, PTES, etc.)

Audit Evidence:
- Penetration test report (dated within 12 months)
- Remediation evidence (critical/high findings fixed)

Audit Test:
- Review pentest report → Verify scope includes CDE
- Verify findings addressed (show remediation evidence)

11.3.2: Network Segmentation Testing (Annual)

Requirements:
- If using segmentation to reduce PCI scope, test effectiveness annually

Audit Evidence:
- Network segmentation testing report (penetration test or vulnerability scan from out-of-scope network)

Audit Test:
- Verify segmentation tested (attempt to access CDE from out-of-scope network → should fail)

11.6.1: Intrusion Detection/Prevention (IDS/IPS) (NEW/Enhanced in v4.0)

Requirements:
- IDS/IPS deployed at CDE perimeter
- Critical traffic monitored
- Alerts reviewed and responded to

Audit Evidence:
- IDS/IPS deployment (Snort, Suricata, commercial NGFW)
- Alert rules (signatures updated)
- Alert review logs (how alerts investigated)

REQUIREMENT 12: Information Security Policy

12.3.1-12.3.2: Targeted Risk Analysis for Customized Approach (NEW in v4.0)

Requirements:
- If using Customized Approach (alternative controls), must conduct TRA
- TRA documents: Threat scenarios, risk assessment, control objectives, custom control, validation

Audit Evidence:
- TRA document per customized control
- QSA validation (auditor confirms control meets objective)

Audit Challenge:
"You claim customized approach for [Requirement X]. Show TRA.
Does your custom control truly achieve the stated objective? Prove it."

12.5.1-12.5.2: PCI DSS Scope Confirmation (Annual)

Requirements:
- Annual scope confirmation (document all CDE components)
- Verify segmentation effectiveness

Audit Evidence:
- Scope document (network diagram, system inventory, data flows)
- Dated within 12 months

Audit Test:
- Verify scope document completeness (all CHD locations identified)
- Verify segmentation documented (if claimed)

12.10.1: Incident Response Plan

Requirements:
- IR plan specific to payment card breaches
- Tested annually (tabletop or simulation)

Audit Evidence:
- IR plan document
- IR drill report (dated within 12 months)

Audit Test:
- Review IR plan → Verify covers card breach scenarios (PAN compromise)
- Verify drill conducted (participants, lessons learned)

QUARTERLY ASV SCANS (Requirement 11.3.2)

Requirements:
- Quarterly vulnerability scans by Approved Scanning Vendor (ASV)
- Must achieve "passing" result (no critical/high vulnerabilities)

Audit Evidence:
- 4 quarterly ASV scan reports (Q1, Q2, Q3, Q4)
- All scans must be passing

Audit Challenge:
"Show me 4 consecutive quarters of passing scans. 
If any scan failed, show rescans until passing achieved."

OUTPUT FORMAT: PCI DSS v4.0 Assessment

**SCOPE DEFINITION**
- Merchant Level: [ ] 1 [ ] 2 [ ] 3 [ ] 4
- Validation Method: [ ] QSA Onsite Audit [ ] SAQ (Type: ___)
- CDE Components: [List all systems storing/processing/transmitting CHD]
- Segmentation: [ ] Yes [ ] No (If Yes, attach network diagram)

**REQUIREMENT TESTING RESULTS**

| Req # | Requirement | Status | Evidence | Findings |
|-------|-------------|--------|----------|----------|
| 1.2.1 | Firewall rule review (bi-annual) | ✓ | 2 reviews (Jan, Jul 2025) | - |
| 3.4.1 | PAN encrypted in storage | ✓ | TDE enabled, AES-256 | - |
| 6.2.4 | Quarterly vulnerability scans | ⚠ | Q3 scan failed, rescanned | Q3 required rescan |
| 8.4.2 | MFA for all admin access | ❌ | 2/30 admin accounts lack MFA | CRITICAL |
| 10.4.1 | Daily log review | ✓ | 365 reviews sampled (30 tested) | - |
| 11.3.1 | Annual penetration test | ✓ | Pentest dated March 2025 | Findings remediated |
| ... | | | | |

**NON-COMPLIANCE SUMMARY**

CRITICAL:
1. Requirement 8.4.2: MFA not enforced for 2 admin accounts (Database Admins)
   - Impact: HIGH (admin accounts can access encrypted CHD, retrieve keys)
   - Remediation: Enable MFA for all admin accounts within 7 days
   - Penalty Risk: If breach occurs, card brand fines + forensic investigation ($$$)

Moderate:
1. Requirement 6.2.4: Q3 vulnerability scan initially failed (high-risk vulnerability on web server)
   - Remediation: Patched, rescanned, passed in Q3 (within quarter)
   - Impact: LOW (remediated within quarter)

**COMPLIANCE STATUS**
- Overall: ❌ NON-COMPLIANT (due to Requirement 8.4.2 failure)
- Action Required: Remediate Requirement 8.4.2 within 7 days, provide evidence, request re-assessment

**ATTESTATION OF COMPLIANCE (AOC)**
[Cannot be issued until all critical findings resolved]

**NEXT STEPS**
1. Remediate MFA for all admin accounts (Timeline: 7 days)
2. Re-test Requirement 8.4.2 (verify 100% MFA coverage)
3. Issue AOC upon full compliance
4. Submit AOC to acquirer + card brands (annual requirement)
"""


def get_hipaa_module() -> str:
    """HIPAA - Health Insurance Portability and Accountability Act"""
    return """
[MODULE B10 — HIPAA AUDIT ENGINE]

SCOPE: Protected Health Information (PHI) Security and Privacy
AUTHORITY: US Department of Health and Human Services (HHS) Office for Civil Rights (OCR)
REGULATIONS: HIPAA Security Rule (45 CFR Part 164 Subpart C), Privacy Rule (45 CFR Part 164 Subpart E)

APPLICABILITY:
- Covered Entities: Healthcare providers, health plans, healthcare clearinghouses
- Business Associates: Service providers handling PHI on behalf of covered entities (IT vendors, billing companies, etc.)

ENFORCEMENT:
- OCR investigations and audits
- Penalties: Tiered ($100 - $50,000 per violation, up to $1.5M per year per violation category)
- Criminal penalties: Up to $250K fine + 10 years imprisonment (for intentional misuse)

PROTECTED HEALTH INFORMATION (PHI):

PHI = Individually identifiable health information

Includes:
- Medical records (diagnoses, treatments, prescriptions)
- Billing information (claims, payment data)
- Demographic data (name, address, DOB, SSN) + health info

Electronic PHI (ePHI): PHI in electronic form (focus of Security Rule)

NOT PHI (De-identified Data):
- 18 identifiers removed (per Safe Harbor method) OR
- Statistical de-identification (expert determination)

HIPAA STRUCTURE:

1. Privacy Rule: Governs use and disclosure of PHI
2. Security Rule: Governs ePHI security (our focus for audit)
3. Breach Notification Rule: Breach reporting requirements

SECURITY RULE STRUCTURE:

3 Safeguard Categories:
- Administrative Safeguards (9 standards)
- Physical Safeguards (4 standards)
- Technical Safeguards (5 standards)

Implementation Specifications: Required vs Addressable
- Required: MUST implement
- Addressable: Implement IF reasonable and appropriate OR document why not + alternative measure

Audit Philosophy:
"For Addressable specs, do NOT accept 'not applicable' without rigorous justification.
Default: It applies. Prove otherwise with risk assessment."

ADMINISTRATIVE SAFEGUARDS (§164.308)

AS-1: Security Management Process (REQUIRED)

§164.308(a)(1)(ii)(A): Risk Analysis (REQUIRED)

Requirements:
- Conduct accurate and thorough assessment of risks to ePHI
- Consider: Threats, vulnerabilities, likelihood, impact

Audit Evidence:
- Risk assessment document (comprehensive, not checklist)
- Methodology (qualitative or quantitative)
- Asset inventory (all systems with ePHI)
- Threat and vulnerability identification
- Risk ratings (likelihood × impact)

Audit Challenge:
"Show me your risk analysis. When was it last conducted? (Must be current)
Are all ePHI systems included? (Sample and verify)
Is this generic or specific to your organization? (Generic = insufficient)"

§164.308(a)(1)(ii)(B): Risk Management (REQUIRED)

Requirements:
- Implement security measures to reduce risks to reasonable and appropriate level

Audit Evidence:
- Risk treatment plan (mitigation strategies per identified risk)
- Control implementation (verify controls from risk analysis are in place)

§164.308(a)(1)(ii)(C): Sanction Policy (REQUIRED)

Requirements:
- Sanctions for workforce members who violate security policies

Audit Evidence:
- Sanction policy (disciplinary actions defined)
- Enforcement examples (at least 1-2 cases in last 2 years for mature organizations)

Audit Challenge:
"Has anyone ever been sanctioned for HIPAA violation? (If NO for 5+ years → is policy real or paper?)"

§164.308(a)(1)(ii)(D): Information System Activity Review (REQUIRED)

Requirements:
- Regularly review audit logs, access reports, security incident tracking

Audit Evidence:
- Log review procedures (frequency: monthly minimum)
- Log review reports (dated, findings documented)
- Incident reports (security incidents logged and investigated)

Audit Test:
- Sample log review reports (last 12 months → verify monthly reviews)
- Verify findings escalated and acted upon

AS-2: Assigned Security Responsibility (REQUIRED)

Requirements:
- Designate a Security Official responsible for HIPAA security

Audit Evidence:
- Appointment letter (Security Officer designated)
- Job description (HIPAA responsibilities included)

Audit Challenge:
"Who is your HIPAA Security Officer? (Interview them - do they know their responsibilities?)"

AS-3: Workforce Security (REQUIRED)

§164.308(a)(3)(ii)(A): Authorization and/or Supervision (ADDRESSABLE)

Requirements:
- Implement procedures for authorization/supervision of workforce accessing ePHI

Audit Evidence:
- Access authorization procedures (who approves ePHI access)
- Access request forms (documented approvals)

§164.308(a)(3)(ii)(B): Workforce Clearance Procedure (ADDRESSABLE)

Requirements:
- Procedures to determine appropriate ePHI access (background checks, role-based access)

Audit Evidence:
- Background check policy (for employees with ePHI access)
- Background check records (verify conducted for sampled employees)

§164.308(a)(3)(ii)(C): Termination Procedures (ADDRESSABLE)

Requirements:
- Procedures for terminating ePHI access upon employment termination

Audit Evidence:
- Termination checklist (ePHI access revocation included)
- Termination logs (verify access removed on termination date)

Audit Test (CRITICAL):
- Sample terminated employees (last 12 months) → Verify ePHI access revoked on/before termination
- If any delay > 24 hours → Document as control gap

AS-4: Information Access Management (REQUIRED)

§164.308(a)(4)(ii)(B): Access Authorization (ADDRESSABLE)

Requirements:
- Implement policies for granting ePHI access (least privilege, need-to-know)

Audit Evidence:
- Access control policy (role-based access)
- Access matrix (roles and permissions)

§164.308(a)(4)(ii)(C): Access Establishment and Modification (ADDRESSABLE)

Requirements:
- Procedures for establishing/modifying/terminating ePHI access

Audit Evidence:
- Access request procedures
- Access modification logs (role changes documented)
- Periodic access reviews (quarterly/annual)

Audit Test:
- Sample access requests → Verify appropriate approval and provisioning
- Sample access reviews → Verify performed and documented

AS-5: Security Awareness and Training (REQUIRED)

§164.308(a)(5)(ii)(A): Security Reminders (ADDRESSABLE)

Requirements:
- Periodic security updates (newsletters, alerts)

Audit Evidence:
- Security awareness communications (emails, posters, training sessions)

§164.308(a)(5)(ii)(B): Protection from Malicious Software (ADDRESSABLE)

Requirements:
- Procedures for detecting/reporting/guarding against malware

Audit Evidence:
- Antivirus/EDR deployment (coverage %)
- Malware incident log

§164.308(a)(5)(ii)(C): Log-in Monitoring (ADDRESSABLE)

Requirements:
- Procedures for monitoring login attempts (failed logins, anomalies)

Audit Evidence:
- Login monitoring (SIEM alerts on failed logins, unusual times/locations)
- Incident investigation logs (login anomalies investigated)

§164.308(a)(5)(ii)(D): Password Management (ADDRESSABLE)

Requirements:
- Procedures for creating, changing, safeguarding passwords

Audit Evidence:
- Password policy (complexity, rotation, prohibition on sharing)
- Password compliance reports (weak passwords flagged)

AS-6: Security Incident Procedures (REQUIRED)

§164.308(a)(6)(ii): Response and Reporting (REQUIRED)

Requirements:
- Identify and respond to security incidents
- Document incidents

Audit Evidence:
- Incident response plan (specific to ePHI breaches)
- Incident log (all security incidents over audit period)
- Incident investigation reports (root cause, remediation)

Audit Test:
- Sample incidents → Verify documented, investigated, resolved
- Verify breach notification (if PHI breach > 500 individuals → OCR notified within 60 days)

AS-7: Contingency Plan (REQUIRED)

§164.308(a)(7)(ii)(A): Data Backup Plan (REQUIRED)

Requirements:
- Backup procedures for ePHI
- Restore capability

Audit Evidence:
- Backup policy (frequency: daily recommended)
- Backup logs (verify backups performed)
- Restoration test logs (at least annual)

Audit Test:
- Verify backup logs (last 90 days)
- Verify restoration test (dated within 12 months, successful)

§164.308(a)(7)(ii)(B): Disaster Recovery Plan (REQUIRED)

Requirements:
- Procedures to restore ePHI after emergency

Audit Evidence:
- Disaster recovery plan (RTO, RPO defined)
- DR test results (annual minimum)

§164.308(a)(7)(ii)(C): Emergency Mode Operation Plan (REQUIRED)

Requirements:
- Procedures to enable continuation of critical business processes while operating in emergency mode

Audit Evidence:
- Business continuity plan (critical processes identified)
- Emergency contacts and procedures

§164.308(a)(7)(ii)(D): Testing and Revision Procedures (ADDRESSABLE)

Requirements:
- Test BCP/DR and revise as needed

Audit Evidence:
- BCP/DR test reports (annual)
- Lessons learned (revisions based on tests)

AS-8: Evaluation (REQUIRED)

Requirements:
- Periodic technical and non-technical evaluation of security controls

Audit Evidence:
- Internal audit program (annual HIPAA audit recommended)
- External audit/assessment (if conducted)
- Evaluation reports (findings and remediation)

Audit Challenge:
"When was last HIPAA evaluation? (If > 2 years → insufficient)
Was it comprehensive or checklist-based? (Demand sample findings)"

AS-9: Business Associate Contracts (REQUIRED) - CRITICAL

Requirements:
- Written contract (Business Associate Agreement - BAA) with each BA handling PHI
- Contract must include specific safeguards (per §164.314(a)(2))

BAA Must Include:
- BA will not use/disclose PHI except as permitted
- BA will implement administrative, physical, technical safeguards
- BA will report security incidents/breaches to Covered Entity
- BA will ensure subcontractors sign BAAs (chain of responsibility)
- BA will return or destroy PHI upon contract termination

Audit Evidence:
- Vendor inventory (all vendors/BAs handling PHI)
- BAA documents (signed, dated)
- Cross-check: Vendor inventory vs BAA list (any vendor without BAA = violation)

Audit Test (CRITICAL):
- Obtain vendor inventory (IT vendors, billing, hosting, cloud)
- Obtain all BAAs
- Identify gaps: Vendors with PHI access BUT no BAA
- RED FLAG: Missing BAA = HIPAA violation (OCR penalty risk)

Audit Challenge:
"Show me list of all vendors with PHI access.
Show me signed BAAs for each.
If mismatch → immediate remediation required (get BAA signed within 30 days)."

PHYSICAL SAFEGUARDS (§164.310)

PS-1: Facility Access Controls (REQUIRED)

§164.310(a)(1): Facility Access Controls (REQUIRED)

Requirements:
- Limit physical access to ePHI systems/facilities

Audit Evidence:
- Physical access control system (badge readers, biometric)
- Access logs (who entered facility/data center)

§164.310(a)(2)(ii): Facility Security Plan (ADDRESSABLE)

Requirements:
- Safeguards to protect facility from unauthorized access

Audit Evidence:
- Security plan (cameras, guards, alarms)
- Incident logs (unauthorized access attempts)

§164.310(a)(2)(iii): Access Control and Validation Procedures (ADDRESSABLE)

Requirements:
- Procedures to control/validate physical access

Audit Evidence:
- Visitor logs (sign-in/sign-out)
- Escort procedures (visitors accompanied)

§164.310(a)(2)(iv): Maintenance Records (ADDRESSABLE)

Requirements:
- Document repairs/modifications to physical security (locks, cameras)

Audit Evidence:
- Maintenance logs (physical security systems)

PS-2: Workstation Use (REQUIRED)

Requirements:
- Specify proper functions/physical attributes of workstations accessing ePHI

Audit Evidence:
- Workstation use policy (where ePHI can be accessed, physical protections)
- Privacy screens (prevent shoulder surfing)

PS-3: Workstation Security (REQUIRED)

Requirements:
- Physical safeguards for workstations accessing ePHI

Audit Evidence:
- Workstation security controls (cable locks, secure locations)
- Auto-lock policy (screen locks after inactivity)

PS-4: Device and Media Controls (REQUIRED)

§164.310(d)(1): Disposal (REQUIRED)

Requirements:
- Securely dispose of ePHI and hardware containing ePHI

Audit Evidence:
- Disposal policy (secure wipe, degaussing, shredding)
- Certificates of destruction (for disposed hardware)

Audit Test:
- Sample disposed devices (laptops, hard drives) → Verify certificates of destruction exist

§164.310(d)(2)(ii): Media Re-use (REQUIRED)

Requirements:
- Remove ePHI before re-using media

Audit Evidence:
- Media sanitization procedures (secure wipe before reuse)
- Sanitization logs

§164.310(d)(2)(iii): Accountability (ADDRESSABLE)

Requirements:
- Track hardware/media containing ePHI

Audit Evidence:
- Asset inventory (all devices with ePHI access)
- Asset tracking system (location, custodian)

§164.310(d)(2)(iv): Data Backup and Storage (ADDRESSABLE)

Requirements:
- Backup copies of ePHI before movement

Audit Evidence:
- Backup procedures (before hardware movement/disposal)

TECHNICAL SAFEGUARDS (§164.312)

TS-1: Access Control (REQUIRED)

§164.312(a)(1): Access Control (REQUIRED)

Requirements:
- Implement technical policies/procedures allowing only authorized access to ePHI

§164.312(a)(2)(i): Unique User Identification (REQUIRED)

Requirements:
- Assign unique identifier to each user (no shared accounts)

Audit Test:
- Review user accounts → Verify no generic accounts (admin, guest, shared)
- If shared accounts exist → Document as violation

§164.312(a)(2)(ii): Emergency Access Procedure (REQUIRED)

Requirements:
- Establish procedures for ePHI access during emergency (break-glass)

Audit Evidence:
- Emergency access procedure (when used, how approved, how audited)
- Emergency access logs (any usage → verify justified and reviewed)

§164.312(a)(2)(iii): Automatic Logoff (ADDRESSABLE)

Requirements:
- Terminate session after inactivity period

Audit Evidence:
- Auto-logoff configuration (15-minute timeout typical)

Audit Test:
- Test workstation → Verify auto-lock after inactivity

§164.312(a)(2)(iv): Encryption and Decryption (ADDRESSABLE)

Requirements:
- Encrypt and decrypt ePHI (ADDRESSABLE but strongly recommended)

Audit Evidence:
- Encryption policy (ePHI encrypted at-rest and in-transit)
- Encryption configuration (AES-256 at-rest, TLS 1.2+ in-transit)

Audit Challenge:
"If you claim encryption is NOT reasonable/appropriate (addressable opt-out),
provide documented risk analysis justifying decision. (Most entities cannot justify opt-out.)"

TS-2: Audit Controls (REQUIRED)

§164.312(b): Audit Controls (REQUIRED)

Requirements:
- Implement hardware/software to record/examine ePHI access and activity

Audit Evidence:
- Audit logging enabled (all ePHI systems)
- SIEM or log aggregation (centralized logs)
- Log retention (6 years recommended for HIPAA)

Audit Test:
- Verify ePHI access logged (user ID, timestamp, action, result)
- Sample logs → Verify completeness

TS-3: Integrity (REQUIRED)

§164.312(c)(1): Integrity (REQUIRED)

Requirements:
- Protect ePHI from improper alteration/destruction

§164.312(c)(2): Mechanism to Authenticate ePHI (ADDRESSABLE)

Requirements:
- Ensure ePHI has not been altered/destroyed in unauthorized manner

Audit Evidence:
- Integrity controls (checksums, digital signatures, version control)

TS-4: Person or Entity Authentication (REQUIRED)

§164.312(d): Person or Entity Authentication (REQUIRED)

Requirements:
- Verify person/entity seeking ePHI access is who they claim

Audit Evidence:
- Authentication mechanisms (passwords, MFA, biometrics)
- MFA deployment (coverage %)

Audit Test:
- Verify authentication required for all ePHI access
- Check for MFA (not required by HIPAA but best practice)

TS-5: Transmission Security (REQUIRED)

§164.312(e)(1): Transmission Security (REQUIRED)

Requirements:
- Protect ePHI during transmission over electronic networks

§164.312(e)(2)(i): Integrity Controls (ADDRESSABLE)

Requirements:
- Ensure ePHI not improperly modified during transmission

Audit Evidence:
- Encryption in transit (TLS 1.2+)
- VPN for remote access

§164.312(e)(2)(ii): Encryption (ADDRESSABLE)

Requirements:
- Encrypt ePHI during transmission

Audit Evidence:
- Encryption configuration (TLS for web, VPN for remote, encrypted email for PHI)

Audit Test:
- Test PHI transmission (email, web portal) → Verify encrypted
- Vulnerability scan → Verify no weak ciphers

BREACH NOTIFICATION RULE (§164.400-414)

Breach Definition: Unauthorized acquisition, access, use, or disclosure of PHI compromising security/privacy

Breach Notification Requirements:

To Individuals (§164.404):
- Within 60 days of discovery
- Written notice (letter or email)

To HHS/OCR (§164.408):
- If breach affects > 500 individuals: Within 60 days of discovery
- If breach affects < 500 individuals: Annual report (within 60 days of year-end)

To Media (§164.406):
- If breach affects > 500 individuals in a state/jurisdiction: Notify prominent media outlets

Audit Evidence:
- Breach log (all breaches over audit period)
- Breach notifications (copies of letters sent, OCR portal submissions)
- Timeliness verification (notification within 60 days)

Audit Test:
- If breach occurred: Verify notifications sent (individuals, OCR, media if applicable)
- Verify timelines (60-day requirement met)

RED FLAG:
If breach > 500 individuals AND no OCR notification → MAJOR VIOLATION (OCR penalty + potential public disclosure)

OUTPUT FORMAT: HIPAA Assessment

**SCOPE**
- Entity Type: [ ] Covered Entity [ ] Business Associate
- ePHI Systems: [List all applications, databases, servers with ePHI]

**SAFEGUARD COMPLIANCE**

| Standard | Specification | Type | Status | Evidence | Gap |
|----------|---------------|------|--------|----------|-----|
| AS-1 | Risk Analysis | Required | ✓ | Risk assessment dated Jan 2025 | - |
| AS-3(ii)(C) | Termination Procedures | Addressable | ⚠ | 1 termination delayed by 3 days | Control gap |
| AS-9 | Business Associate Contracts | Required | ❌ | 2 vendors lack BAA | CRITICAL |
| TS-1(a)(2)(iv) | Encryption | Addressable | ✓ | AES-256 at-rest, TLS 1.2+ in-transit | - |
| TS-2 | Audit Controls | Required | ✓ | SIEM logs all ePHI access | - |
| ... | | | | | |

**CRITICAL FINDINGS**

1. AS-9: Business Associate Agreements Missing
   - Vendors: [Cloud Hosting Provider X], [Billing Service Y]
   - Impact: CRITICAL (PHI shared without BAA = HIPAA violation)
   - Penalty Risk: OCR investigation if breach occurs → $100-$50K per violation
   - Remediation: Obtain signed BAAs within 30 days OR cease PHI sharing

2. AS-3(ii)(C): Delayed Termination Access Removal
   - Impact: MODERATE (1 ex-employee retained ePHI access for 3 days post-termination)
   - Remediation: Strengthen termination checklist, automate access revocation

**COMPLIANCE STATUS**
- Overall: ❌ NON-COMPLIANT (due to missing BAAs)
- Action Required: Obtain BAAs within 30 days, re-assess

**BREACH NOTIFICATION REVIEW**
- Breaches in last 12 months: [0 / X]
- If breaches occurred: [Verify notifications sent, timelines met, OCR submissions]

**RECOMMENDATIONS**
1. Immediate: Obtain missing BAAs (AS-9)
2. Short-term: Implement MFA for all ePHI access (best practice)
3. Long-term: Annual HIPAA risk analysis and internal audit program
"""


# Continue with integration layer in next file...
