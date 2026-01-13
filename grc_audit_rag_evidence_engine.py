"""
GRC AUDIT SYSTEM - RAG INTEGRATION & EVIDENCE VALIDATION ENGINE (Part 5)
======================================================================
RAG-Compliant Source Verification, Citation Management, Evidence Validation
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import json


# ============================================================================
# RAG INTEGRATION LAYER
# ============================================================================

RAG_INTEGRATION_MODULE = """
[MODULE C — RAG INTEGRATION & SOURCE VERIFICATION]

PURPOSE:
Ensure all regulatory guidance is sourced from authoritative documents.
Prevent hallucination of clauses, circulars, control numbers.

PRINCIPLES:
1. Law > Regulation > Standard > Guidance (strict hierarchy)
2. Official sources only (government, regulators, standards bodies)
3. Version-specific citations (PCI DSS v4.0, not "PCI DSS")
4. Date-sensitive (regulations change; cite version date)
5. Never fabricate citations

RAG WORKFLOW:

STEP 1: QUERY FORMULATION
When user asks about compliance requirement:
- Identify jurisdiction (India/US/EU/Global)
- Identify framework (SEBI CSCRF/RBI/DPDP/GDPR/ISO/SOC/PCI/HIPAA)
- Identify specific topic (access control, encryption, breach notification, etc.)

STEP 2: SOURCE RETRIEVAL
Retrieve from knowledge base:
- Primary sources (laws, regulations)
- Secondary sources (circulars, guidance notes)
- Standards documents (ISO, PCI DSS, NIST)

Priority Order:
1. Statute/Act (e.g., DPDP Act 2023, SOX Section 404)
2. Regulation/Rule (e.g., GDPR Article 32, HIPAA §164.312)
3. Regulatory circular/notice (e.g., SEBI CSCRF August 2024, RBI Master Direction)
4. Standard (e.g., ISO 27001:2022 Clause 8.1, PCI DSS Requirement 8.4.2)
5. Guidance/FAQ (e.g., OCR HIPAA FAQs, PCI SSC guidance)

STEP 3: CITATION VERIFICATION
For each statement, verify:
- Source document exists
- Version matches (v4.0 vs v3.2.1 - different requirements)
- Clause/section accurately cited
- Interpretation aligns with source text

STEP 4: HALLUCINATION DETECTION
If citation cannot be verified:
- Tag: [CITATION REQUIRED]
- State: "This requires verification against [SOURCE NAME]"
- NEVER invent regulation numbers

Example:
WRONG: "RBI Circular RBI/2024-25/123 requires..."
RIGHT: "RBI Master Direction on IT Framework (updated 2021) states... [Verify specific circular number]"

STEP 5: CONFLICT RESOLUTION
If sources conflict:
- Identify conflict explicitly
- State which source takes precedence (Law > Regulation > Standard)
- Recommend legal counsel if ambiguous

Example:
"ISO 27001 recommends annual risk assessment.
SEBI CSCRF mandates quarterly Cyber Capability Index calculation.
For SEBI entities: SEBI requirement supersedes ISO recommendation."

STEP 6: VERSION CONTROL
Always specify version:
- PCI DSS v4.0 (not "PCI DSS")
- ISO 27001:2022 (not "ISO 27001")
- GDPR (no version, but cite "as amended by [regulation] if applicable")

If user references old version:
"Note: You mentioned PCI DSS v3.2.1. Current version is v4.0 (mandatory March 31, 2025).
v4.0 includes new requirements: Requirement 6.4.3 (script inventory), Requirement 11.6.1 (IDS/IPS).
Guidance based on v4.0. Confirm version applicability."
"""


class SourceType(Enum):
    """Classification of regulatory sources"""
    STATUTE = "statute"  # Acts, Laws (highest authority)
    REGULATION = "regulation"  # CFR, Rules
    CIRCULAR = "circular"  # Regulatory notices, master directions
    STANDARD = "standard"  # ISO, PCI DSS, NIST
    GUIDANCE = "guidance"  # FAQs, white papers (lowest authority)


class RegulatoryDomain(Enum):
    """Regulatory domain classification"""
    SEBI = "sebi"
    RBI = "rbi"
    DPDP = "dpdp"
    GDPR = "gdpr"
    ISO_27001 = "iso_27001"
    ISO_42001 = "iso_42001"
    SOC2 = "soc2"
    SOX = "sox"
    PCI_DSS = "pci_dss"
    HIPAA = "hipaa"


@dataclass
class RegulatorySource:
    """Represents an authoritative source"""
    source_type: SourceType
    domain: RegulatoryDomain
    title: str
    version: Optional[str]
    date_published: str
    url: Optional[str]
    clause_reference: Optional[str]
    content_excerpt: str
    authority_level: int  # 1 (highest) to 5 (lowest)


class RAGEngine:
    """RAG engine for regulatory compliance"""
    
    def __init__(self):
        self.knowledge_base: List[RegulatorySource] = []
        self.citation_cache: Dict[str, RegulatorySource] = {}
    
    def query_sources(self, 
                     query: str, 
                     domain: RegulatoryDomain,
                     source_types: Optional[List[SourceType]] = None) -> List[RegulatorySource]:
        """
        Query knowledge base for relevant sources.
        Returns sources ordered by authority level.
        """
        # Placeholder for actual RAG implementation
        # In production: Vector search across indexed regulatory documents
        pass
    
    def verify_citation(self, 
                       claim: str, 
                       citation: str, 
                       domain: RegulatoryDomain) -> Tuple[bool, Optional[str]]:
        """
        Verify a compliance claim against cited source.
        Returns (is_valid, explanation)
        """
        # Placeholder for citation verification
        # In production: Retrieve source, compare claim text, validate accuracy
        pass
    
    def detect_hallucination(self, statement: str, domain: RegulatoryDomain) -> bool:
        """
        Detect potential hallucinated citations.
        Returns True if hallucination suspected.
        """
        # Red flags:
        # - Specific circular numbers without verification (e.g., "RBI/2024-25/123")
        # - Non-existent clause references
        # - Claims without any source
        pass


# ============================================================================
# EVIDENCE VALIDATION ENGINE
# ============================================================================

EVIDENCE_VALIDATION_MODULE = """
[MODULE D — EVIDENCE AUDITOR & PROFESSIONAL SKEPTICISM]

PRINCIPLE: "Trust must be earned through evidence."

EVIDENCE HIERARCHY (Quality Levels):

Level 1: PRIMARY EVIDENCE (Highest Quality)
- Time-stamped system logs (immutable, tamper-evident)
- Cryptographically signed documents
- Third-party audit reports (SOC 2, penetration tests)
- Regulatory submissions (acknowledged by regulator)

Level 2: SECONDARY EVIDENCE (High Quality)
- System-generated reports (SIEM, vulnerability scans)
- Database exports with metadata
- Configuration files with version control
- Backup logs with success confirmation

Level 3: TERTIARY EVIDENCE (Moderate Quality)
- Manual documentation (policies, procedures)
- Screenshots with timestamps
- Email communications
- Meeting minutes

Level 4: TESTIMONIAL EVIDENCE (Low Quality)
- Verbal claims
- Self-attestations without supporting docs
- "We do this" without proof

EVIDENCE REQUIREMENTS:

Time-Stamped:
- Date/time must be verifiable
- Reject: "Latest" or "Current" (too vague)
- Require: "Dated January 15, 2026, 14:35 UTC"

Traceable:
- Source system identifiable
- Audit trail exists
- Chain of custody documented

Period-Appropriate:
- For annual audit: Evidence spans 12 months
- For quarterly compliance: Evidence from that quarter
- No single point-in-time evidence for continuous controls

Verifiable:
- Can be independently confirmed
- Not solely in control of auditee
- Third-party validation preferred

EVIDENCE INTERROGATION FRAMEWORK:

NEVER ASK: "Do you have backups?"
ALWAYS ASK: "Provide restoration test logs for [Critical Database] from Q4 2025 verifying RTO = 4 hours. Include: timestamp, data integrity check results, downtime duration."

NEVER ASK: "Do you have antivirus?"
ALWAYS ASK: "Show centralized EDR console screenshot dated within 7 days. Verify: 100% endpoint coverage, signature update lag < 24 hours, quarantine actions for any detections."

NEVER ASK: "Do you review access?"
ALWAYS ASK: "Provide access review reports for Q1, Q2, Q3, Q4 2025. For each: reviewer name, review completion date, exceptions identified, remediation evidence for exceptions."

NEVER ASK: "Do you have MFA?"
ALWAYS ASK: "Extract from IAM system: All user accounts with [Critical System] access. For each: MFA enabled (Y/N), MFA method, last login with MFA timestamp. If any user lacks MFA: Justify exception OR remediate."

EVIDENCE REJECTION CRITERIA:

Reject if:
1. Undated or date unverifiable
2. Generic (template, not entity-specific)
3. Incomplete (partial data, redacted critical info)
4. Stale (> 12 months old for annual controls, > 3 months for quarterly)
5. Single screenshot for continuous control (need longitudinal evidence)
6. "In progress" without completion evidence
7. Self-signed without third-party validation (for critical controls)

SAMPLING METHODOLOGY:

Population-Based Sampling:
- Population < 25: Test 100%
- Population 25-250: Sample 25-40
- Population > 250: Sample 40-60

Risk-Based Adjustments:
- High-risk controls: Increase sample size or test 100%
- Automated controls: Test IT environment + 1 transaction
- Manual controls: Larger sample required

Sampling Selection:
- Random sampling (avoid bias)
- Include edge cases (beginning/end of period, high-value transactions, privileged users)

EVIDENCE DOCUMENTATION:

For each piece of evidence, document:
1. Evidence Type (log, report, screenshot, document)
2. Source System (from which system obtained)
3. Date/Timestamp (when evidence created)
4. Retrieval Method (how obtained - direct export, API, manual)
5. Verification Performed (what checks conducted)
6. Sufficiency Assessment (adequate or additional evidence needed)
"""


class EvidenceType(Enum):
    """Type of audit evidence"""
    SYSTEM_LOG = "system_log"
    SYSTEM_REPORT = "system_report"
    CONFIGURATION_FILE = "configuration_file"
    DOCUMENT = "document"
    SCREENSHOT = "screenshot"
    EMAIL = "email"
    THIRD_PARTY_REPORT = "third_party_report"
    TESTIMONIAL = "testimonial"


class EvidenceQuality(Enum):
    """Quality rating of evidence"""
    PRIMARY = 1      # Highest quality (system logs, third-party reports)
    SECONDARY = 2    # High quality (system-generated reports)
    TERTIARY = 3     # Moderate quality (manual documentation, screenshots)
    TESTIMONIAL = 4  # Low quality (verbal claims)


@dataclass
class AuditEvidence:
    """Represents a piece of audit evidence"""
    evidence_id: str
    control_reference: str  # Which control this evidences
    evidence_type: EvidenceType
    quality_level: EvidenceQuality
    description: str
    source_system: Optional[str]
    timestamp: str
    retrieval_method: str
    verification_notes: str
    sufficiency: str  # "Sufficient", "Insufficient", "Partial"
    retention_period: str  # How long to retain (e.g., "7 years for SOX")


class EvidenceValidator:
    """Validates audit evidence quality and sufficiency"""
    
    def validate_evidence(self, evidence: AuditEvidence) -> Tuple[bool, List[str]]:
        """
        Validate evidence against APAR-GRC standards.
        Returns (is_valid, list_of_issues)
        """
        issues = []
        
        # Check timestamp
        if not evidence.timestamp or evidence.timestamp == "unknown":
            issues.append("Evidence lacks timestamp or date verification")
        
        # Check quality for control type
        if evidence.control_reference.startswith("SOX") and evidence.quality_level == EvidenceQuality.TESTIMONIAL:
            issues.append("SOX controls require higher-quality evidence than testimonial")
        
        # Check source system for system-generated evidence
        if evidence.evidence_type in [EvidenceType.SYSTEM_LOG, EvidenceType.SYSTEM_REPORT]:
            if not evidence.source_system:
                issues.append("System-generated evidence must identify source system")
        
        # Sufficiency check
        if evidence.sufficiency == "Insufficient":
            issues.append("Evidence marked as insufficient - additional evidence required")
        
        is_valid = len(issues) == 0
        return is_valid, issues
    
    def assess_control_evidence(self, 
                               control_id: str, 
                               evidence_list: List[AuditEvidence],
                               control_type: str) -> str:
        """
        Assess whether evidence is sufficient for control.
        control_type: "automated", "manual_continuous", "manual_periodic"
        Returns: "Sufficient", "Insufficient", "Partial"
        """
        if not evidence_list:
            return "Insufficient"
        
        # Automated controls: Need IT environment evidence + 1 transaction
        if control_type == "automated":
            has_config = any(e.evidence_type == EvidenceType.CONFIGURATION_FILE for e in evidence_list)
            has_transaction = any(e.evidence_type in [EvidenceType.SYSTEM_LOG, EvidenceType.SYSTEM_REPORT] for e in evidence_list)
            if has_config and has_transaction:
                return "Sufficient"
            else:
                return "Partial"
        
        # Manual continuous controls: Need longitudinal evidence (multiple points in time)
        if control_type == "manual_continuous":
            if len(evidence_list) < 4:  # Quarterly minimum for annual audit
                return "Insufficient"
            return "Sufficient"
        
        # Manual periodic controls: Need evidence for each occurrence
        if control_type == "manual_periodic":
            return "Sufficient" if evidence_list else "Insufficient"
        
        return "Partial"


class ProfessionalSkepticismEngine:
    """Applies professional skepticism to claims and evidence"""
    
    def challenge_claim(self, claim: str, domain: RegulatoryDomain) -> List[str]:
        """
        Generate skeptical challenge questions for a compliance claim.
        Returns list of questions to ask.
        """
        questions = []
        
        # Generic challenges
        questions.append("What evidence supports this claim? (Require specific, dated artifacts)")
        questions.append("Is this control operating as designed, or just documented? (Test operating effectiveness)")
        questions.append("Who performs this control? How often? Where is the record? (Verify execution)")
        
        # Domain-specific challenges
        if "access review" in claim.lower():
            questions.append("Show access review reports for last 4 quarters. For each: Reviewer, date, exceptions, remediation.")
            questions.append("Sample 5 users from last review. Are their current access levels appropriate?")
        
        if "mfa" in claim.lower() or "multi-factor" in claim.lower():
            questions.append("Show IAM system report: % users with MFA enabled. Target: 100%. Any below 100%: Justify.")
            questions.append("Attempt login without MFA. Result should be: Access denied.")
        
        if "backup" in claim.lower():
            questions.append("Show backup logs: Last 90 days, success rate %. Target: >99%.")
            questions.append("Show restoration test: Last test date, system restored, time taken, RTO met (Y/N).")
        
        if "encryption" in claim.lower():
            questions.append("Show encryption configuration: Algorithm (AES-256?), key length, key storage location.")
            questions.append("Access database directly. Verify data is encrypted (not plaintext).")
        
        if "policy" in claim.lower() or "procedure" in claim.lower():
            questions.append("Policy approval date? (If >12 months, requires review.)")
            questions.append("Policy communication evidence? (Training logs, acknowledgments.)")
            questions.append("Is this generic template or entity-specific? (Generic = insufficient.)")
        
        return questions
    
    def detect_red_flags(self, evidence: AuditEvidence) -> List[str]:
        """
        Identify red flags in evidence that suggest fabrication or weakness.
        Returns list of red flags.
        """
        red_flags = []
        
        # Timestamp red flags
        if "screenshot" in evidence.evidence_type.value:
            if "timestamp" not in evidence.description.lower():
                red_flags.append("Screenshot lacks visible timestamp")
        
        # Generic language red flags
        generic_phrases = ["best practice", "industry standard", "generally", "typically", "usually"]
        if any(phrase in evidence.description.lower() for phrase in generic_phrases):
            red_flags.append("Evidence contains generic language instead of specific facts")
        
        # Incomplete evidence red flags
        if evidence.sufficiency == "Partial":
            red_flags.append("Evidence marked as partial - may be insufficient for control assurance")
        
        # Quality red flags
        if evidence.quality_level == EvidenceQuality.TESTIMONIAL:
            red_flags.append("Low-quality evidence (testimonial) - requires corroboration")
        
        return red_flags


# ============================================================================
# ANTI-HALLUCINATION CONTROLS
# ============================================================================

ANTI_HALLUCINATION_PROTOCOL = """
[MODULE E — ANTI-HALLUCINATION CONTROLS]

PURPOSE:
Prevent fabrication of regulatory requirements, control numbers, clauses.

HALLUCINATION PATTERNS TO DETECT:

Pattern 1: Specific Circular/Notification Numbers Without Source
Example: "RBI Circular RBI/2024-25/123 requires quarterly audits"
Detection: If specific number cited, verify in knowledge base. If not found → [CITATION REQUIRED]

Pattern 2: Non-Existent Clauses
Example: "ISO 27001 Clause 10.5.7 mandates blockchain for audit logs"
Detection: ISO 27001 has no Clause 10.5.7. Verify clause exists before citing.

Pattern 3: Misattributed Requirements
Example: "GDPR requires MFA for all user access"
Reality: GDPR requires "appropriate security" but doesn't mandate MFA specifically
Detection: Verify requirement actually states what's claimed

Pattern 4: Version Confusion
Example: Citing PCI DSS v3.2.1 requirement as v4.0 requirement (they differ)
Detection: Always verify version-specific requirements

Pattern 5: Jurisdiction Blending
Example: Claiming DPDP Act applies in EU or GDPR applies in India (without specific trigger)
Detection: Verify jurisdictional applicability

SAFEGUARDS:

Safeguard 1: Citation Verification
Before stating "Regulation X requires Y":
- Retrieve Regulation X from knowledge base
- Verify text actually says Y
- If uncertain → Tag [CITATION REQUIRED] or "Requires verification against [source]"

Safeguard 2: Version Checking
Always specify version:
- "ISO 27001:2022" not "ISO 27001"
- "PCI DSS v4.0" not "PCI DSS"
If user references old version → Flag version delta

Safeguard 3: Jurisdiction Clarity
Explicitly state jurisdiction:
- "Under DPDP Act 2023 (India privacy law)..."
- "For entities subject to GDPR (EU/EEA)..."

Safeguard 4: Confidence Tagging
If confidence low (<80%):
- State: "This interpretation requires verification with [legal counsel / regulator / authoritative source]"
- Never present low-confidence claims as fact

Safeguard 5: Source Attribution
Every claim must trace to source:
- "SEBI CSCRF (August 2024) mandates quarterly CCI calculation (Annexure B)"
- NOT: "SEBI requires cyber audits" (too vague)

HALLUCINATION REJECTION EXAMPLES:

User: "What does RBI Circular RBI/2025-26/45 say about AI governance?"
Agent: "I cannot verify a circular with that specific number. Please provide the circular title or dated reference for verification. I can discuss RBI's guidance on IT risk management if relevant."

User: "ISO 27001 Clause 15.3 requires penetration testing monthly."
Agent: "ISO 27001:2022 does not contain a Clause 15.3. (Clauses go up to 10, with Annex A controls.) 
Penetration testing is addressed in Annex A Control 5.7 (Threat Intelligence) and organizational policy. 
Can you clarify which requirement you're referencing?"

User: "GDPR says we need ISO 27001 certification."
Agent: "GDPR does not mandate ISO 27001 certification. GDPR Article 32 requires 'appropriate technical and organizational measures' which ISO 27001 can help demonstrate, but certification is not explicitly required. Would you like guidance on GDPR Article 32 compliance?"
"""


class HallucinationDetector:
    """Detects and prevents hallucinated compliance claims"""
    
    def __init__(self, rag_engine: RAGEngine):
        self.rag_engine = rag_engine
        self.known_regulations: Dict[str, List[str]] = {}  # Domain -> List of clauses/requirements
    
    def check_claim(self, claim: str, domain: RegulatoryDomain) -> Tuple[bool, Optional[str]]:
        """
        Check if claim is likely hallucinated.
        Returns (is_valid, explanation)
        """
        # Extract citation patterns (e.g., "RBI/2024-25/123", "ISO 27001 Clause 10.5")
        citations = self._extract_citations(claim)
        
        for citation in citations:
            # Verify citation exists in knowledge base
            is_valid, explanation = self.rag_engine.verify_citation(claim, citation, domain)
            if not is_valid:
                return False, f"Citation '{citation}' could not be verified: {explanation}"
        
        return True, None
    
    def _extract_citations(self, text: str) -> List[str]:
        """Extract regulatory citations from text"""
        # Placeholder for citation extraction logic
        # In production: Regex patterns for RBI/YYYY-YY/NNN, ISO XXXXX:YYYY Clause X.X, etc.
        return []
    
    def suggest_correction(self, invalid_claim: str, domain: RegulatoryDomain) -> str:
        """Suggest corrected phrasing for invalid claim"""
        # Query knowledge base for relevant actual requirements
        # Return suggested corrected phrasing with proper citation
        return "[Corrected claim with verified citation]"


# Continue with multi-LLM orchestration in next file...
