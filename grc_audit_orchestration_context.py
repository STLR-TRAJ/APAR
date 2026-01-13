"""
GRC AUDIT SYSTEM - MULTI-LLM ORCHESTRATION & CONTEXT MANAGEMENT (Part 6)
======================================================================
Dynamic Prompt Assembly, Token Management, LLM Routing for ChatGPT-5, Gemini-3, Claude-4.5, DeepSeek
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum
import json


# ============================================================================
# MULTI-LLM ORCHESTRATION SYSTEM
# ============================================================================

class LLMProvider(Enum):
    """Supported LLM providers"""
    CHATGPT_5 = "chatgpt_5"           # OpenAI GPT-5
    GEMINI_3 = "gemini_3"             # Google Gemini 3.0
    CLAUDE_4_5 = "claude_4_5"         # Anthropic Claude 4.5
    DEEPSEEK_V3 = "deepseek_v3"       # DeepSeek V3
    LLAMA_4 = "llama_4"               # Meta Llama 4
    MISTRAL_LARGE_2 = "mistral_large_2"  # Mistral Large 2


class UserRole(Enum):
    """User role determines prompt routing and response style"""
    BOARD_CEO_CFO = "board_ceo_cfo"   # Executive Dashboard Mode
    CISO_HEAD_IT = "ciso_head_it"      # Compliance Copilot Mode
    GRC_ANALYST = "grc_analyst"        # JSON Core Mode (detailed)
    AUDITOR = "auditor"                # Injection-Resistant Mode
    RED_TEAM = "red_team"              # Red Team Hardened Mode
    DEFAULT = "default"                # Standard Audit Mode


@dataclass
class LLMCapabilities:
    """Capabilities of each LLM"""
    provider: LLMProvider
    context_window: int               # Token limit
    supports_structured_output: bool  # JSON mode
    supports_function_calling: bool   # Tool use
    supports_vision: bool             # Image analysis
    supports_code_execution: bool     # Code interpreter
    latency_ms: int                   # Average latency
    cost_per_1k_tokens_input: float   # Cost in USD
    cost_per_1k_tokens_output: float
    strengths: List[str]              # What this LLM is best at


# LLM Capability Matrix
LLM_CAPABILITIES = {
    LLMProvider.CHATGPT_5: LLMCapabilities(
        provider=LLMProvider.CHATGPT_5,
        context_window=200000,  # 200K tokens (example)
        supports_structured_output=True,
        supports_function_calling=True,
        supports_vision=True,
        supports_code_execution=True,
        latency_ms=800,
        cost_per_1k_tokens_input=0.03,
        cost_per_1k_tokens_output=0.06,
        strengths=["Complex reasoning", "Multi-step tasks", "Code generation", "Structured output"]
    ),
    LLMProvider.GEMINI_3: LLMCapabilities(
        provider=LLMProvider.GEMINI_3,
        context_window=1000000,  # 1M tokens (example)
        supports_structured_output=True,
        supports_function_calling=True,
        supports_vision=True,
        supports_code_execution=True,
        latency_ms=600,
        cost_per_1k_tokens_input=0.02,
        cost_per_1k_tokens_output=0.04,
        strengths=["Long context", "Fast inference", "Multimodal", "Low cost"]
    ),
    LLMProvider.CLAUDE_4_5: LLMCapabilities(
        provider=LLMProvider.CLAUDE_4_5,
        context_window=200000,
        supports_structured_output=True,
        supports_function_calling=True,
        supports_vision=True,
        supports_code_execution=False,
        latency_ms=700,
        cost_per_1k_tokens_input=0.025,
        cost_per_1k_tokens_output=0.05,
        strengths=["Safety", "Instruction following", "Long-form writing", "Analysis"]
    ),
    LLMProvider.DEEPSEEK_V3: LLMCapabilities(
        provider=LLMProvider.DEEPSEEK_V3,
        context_window=64000,
        supports_structured_output=True,
        supports_function_calling=True,
        supports_vision=False,
        supports_code_execution=True,
        latency_ms=500,
        cost_per_1k_tokens_input=0.001,  # Extremely low cost
        cost_per_1k_tokens_output=0.002,
        strengths=["Cost-effective", "Code reasoning", "Math/Logic", "Fast"]
    ),
}


MULTI_LLM_ORCHESTRATION_MODULE = """
[MODULE F — MULTI-LLM ORCHESTRATION SYSTEM]

PURPOSE:
Route audit tasks to optimal LLM based on task type, context size, cost, latency.

LLM SELECTION LOGIC:

TASK TYPE ROUTING:

1. LONG-DOCUMENT ANALYSIS (Full SOC 2 report, 100-page policy review)
   → GEMINI-3 (1M token context window)
   Reason: Can ingest entire document without chunking

2. STRUCTURED OUTPUT (Risk register, compliance matrix, JSON reports)
   → CHATGPT-5 or GEMINI-3 (both support structured output)
   Reason: Native JSON mode ensures parseable output

3. CODE ANALYSIS (Script review, Dockerfile audit, SBOM analysis)
   → DEEPSEEK-V3 or CHATGPT-5
   Reason: Strong code reasoning capabilities

4. COMPLEX REASONING (Multi-framework compliance mapping, SoD conflict resolution)
   → CHATGPT-5 or CLAUDE-4.5
   Reason: Best at multi-step reasoning and nuanced analysis

5. COST-SENSITIVE BATCH TASKS (Quarterly vulnerability report reviews)
   → DEEPSEEK-V3
   Reason: 10-50x cheaper than GPT-5 or Claude for high-volume tasks

6. SAFETY-CRITICAL TASKS (Board-level reports, regulatory submissions)
   → CLAUDE-4.5
   Reason: Strong safety guardrails, low hallucination rate

7. REAL-TIME INTERACTIVE AUDITS (Live Q&A with auditor)
   → DEEPSEEK-V3 or GEMINI-3
   Reason: Lowest latency (500-600ms vs 700-800ms)

ROLE-BASED ROUTING:

User Role: BOARD / CEO / CFO
Mode: Executive Dashboard Mode
LLM: CLAUDE-4.5 (safety, clarity, concise)
Output Style: Executive summary, risk ratings, actionable recommendations
Token Budget: 4,000 tokens max (2-page equivalent)

User Role: CISO / Head IT
Mode: Compliance Copilot Mode
LLM: CHATGPT-5 (detailed, technical, actionable)
Output Style: Technical details, control implementation guidance, code examples
Token Budget: 16,000 tokens max (8-10 pages)

User Role: GRC Analyst
Mode: JSON Core Mode
LLM: GEMINI-3 or CHATGPT-5 (structured output)
Output Style: JSON/CSV exports, compliance matrices, detailed tables
Token Budget: 32,000 tokens (full reports)

User Role: External Auditor
Mode: Injection-Resistant Mode
LLM: CLAUDE-4.5 (strong prompt injection resistance)
Output Style: Formal audit findings, no deviation from standards
Token Budget: 16,000 tokens

User Role: Red Team
Mode: Red Team Hardened Mode
LLM: CHATGPT-5 + CLAUDE-4.5 (ensemble validation)
Output Style: Attack scenarios, control weaknesses, adversarial testing
Token Budget: 32,000 tokens

CONTEXT WINDOW MANAGEMENT:

IF task context < 64K tokens:
    → Any LLM (all support 64K+)
    
IF task context 64K-200K tokens:
    → CHATGPT-5, CLAUDE-4.5, or GEMINI-3
    → Exclude DEEPSEEK-V3 (64K limit)
    
IF task context 200K-1M tokens:
    → GEMINI-3 only (1M context window)
    → Alternative: Chunk and distribute across multiple LLM calls

COST OPTIMIZATION:

Low-Cost Routing:
- Use DEEPSEEK-V3 for routine tasks (log reviews, quarterly scans)
- Use GEMINI-3 for medium-complexity tasks (policy reviews)
- Reserve CHATGPT-5/CLAUDE-4.5 for high-complexity tasks (framework mapping, board reports)

Cost Estimation:
- Input tokens × $cost_per_1k_input + Output tokens × $cost_per_1k_output
- Track cost per task, per user session, per month

Budget Alerts:
- If monthly cost > $X, route non-critical tasks to cheaper LLMs
- Notify admin if single task > $Y

LATENCY OPTIMIZATION:

For interactive sessions (chatbot-style):
- Prioritize DEEPSEEK-V3 (500ms) or GEMINI-3 (600ms)
- Avoid CHATGPT-5 (800ms) unless complexity requires it

For batch processing (overnight reports):
- Latency irrelevant; optimize for cost or quality

ENSEMBLE MODE (High-Stakes Tasks):

For critical outputs (regulatory submissions, board reports):
1. Generate output with LLM A (e.g., CHATGPT-5)
2. Validate output with LLM B (e.g., CLAUDE-4.5)
3. If disagreement: Flag for human review
4. If agreement: Proceed with confidence

Example:
Task: Generate SOX 404 Management Assertion Letter
LLM A (CHATGPT-5): Drafts letter
LLM B (CLAUDE-4.5): Reviews for accuracy, compliance, tone
Human: Final review and sign-off

FAILOVER STRATEGY:

IF primary LLM unavailable (rate limit, downtime):
1. Route to secondary LLM with similar capabilities
2. Log failover event
3. Notify user of LLM switch (transparency)

Failover Pairs:
- CHATGPT-5 → CLAUDE-4.5
- GEMINI-3 → CHATGPT-5
- DEEPSEEK-V3 → GEMINI-3
"""


class LLMRouter:
    """Routes audit tasks to optimal LLM"""
    
    def __init__(self):
        self.llm_capabilities = LLM_CAPABILITIES
        self.cost_tracker: Dict[LLMProvider, float] = {}
        self.latency_tracker: Dict[LLMProvider, List[int]] = {}
    
    def select_llm(self, 
                   task_type: str,
                   user_role: UserRole,
                   context_size_tokens: int,
                   priority: str = "balanced") -> LLMProvider:
        """
        Select optimal LLM for task.
        priority: "cost" | "latency" | "quality" | "balanced"
        """
        
        # Filter by context window requirement
        compatible_llms = [
            provider for provider, cap in self.llm_capabilities.items()
            if cap.context_window >= context_size_tokens
        ]
        
        if not compatible_llms:
            raise ValueError(f"No LLM supports context size {context_size_tokens}")
        
        # Role-based routing overrides
        if user_role == UserRole.BOARD_CEO_CFO:
            return LLMProvider.CLAUDE_4_5  # Safety, clarity
        elif user_role == UserRole.AUDITOR:
            return LLMProvider.CLAUDE_4_5  # Injection-resistant
        
        # Task-type routing
        if task_type == "long_document_analysis" and context_size_tokens > 200000:
            return LLMProvider.GEMINI_3  # Only one with 1M context
        elif task_type == "code_analysis":
            return LLMProvider.DEEPSEEK_V3  # Best for code
        elif task_type == "structured_output":
            return LLMProvider.CHATGPT_5  # Best structured output
        
        # Priority-based routing
        if priority == "cost":
            return LLMProvider.DEEPSEEK_V3  # Cheapest
        elif priority == "latency":
            return LLMProvider.DEEPSEEK_V3  # Fastest
        elif priority == "quality":
            return LLMProvider.CHATGPT_5    # Highest quality
        
        # Balanced default
        return LLMProvider.GEMINI_3  # Good balance of cost, speed, quality
    
    def estimate_cost(self, 
                     provider: LLMProvider,
                     input_tokens: int,
                     output_tokens: int) -> float:
        """Estimate cost for LLM call"""
        cap = self.llm_capabilities[provider]
        cost = (input_tokens / 1000 * cap.cost_per_1k_tokens_input +
                output_tokens / 1000 * cap.cost_per_1k_tokens_output)
        return cost
    
    def track_usage(self, provider: LLMProvider, cost: float, latency_ms: int):
        """Track LLM usage for monitoring and optimization"""
        if provider not in self.cost_tracker:
            self.cost_tracker[provider] = 0.0
            self.latency_tracker[provider] = []
        
        self.cost_tracker[provider] += cost
        self.latency_tracker[provider].append(latency_ms)


# ============================================================================
# DYNAMIC PROMPT ASSEMBLY & CHUNKING
# ============================================================================

CONTEXT_MANAGEMENT_MODULE = """
[MODULE G — DYNAMIC PROMPT ASSEMBLY & TOKEN MANAGEMENT]

PURPOSE:
Solve "Sorry, the response hit the length limit" by chunking prompts intelligently.

PROBLEM:
- Full GRC audit system prompt = 150K+ tokens (core + all frameworks)
- Single LLM call limited by context window (64K-1M depending on model)
- Output limited by max_tokens setting (typically 4K-16K)

SOLUTION: Modular, On-Demand Prompt Assembly

ARCHITECTURE:

CORE PROMPT (Always Loaded):
- System Identity (5K tokens)
- Vibe Directives (3K tokens)
- Do Not Touch Constraints (2K tokens)
- Regulatory Triage Module (5K tokens)
- RAG Integration Module (4K tokens)
- Evidence Validation Module (4K tokens)
Total: ~23K tokens (always in context)

FRAMEWORK MODULES (Load on Demand):
- SEBI CSCRF Module: 12K tokens
- RBI CSITE Module: 10K tokens
- DPDP Act Module: 9K tokens
- GDPR Module: 11K tokens
- ISO 27001 Module: 14K tokens
- ISO 42001 Module: 13K tokens
- SOC 2 Module: 15K tokens
- SOX ITGC Module: 12K tokens
- PCI DSS v4.0 Module: 16K tokens
- HIPAA Module: 14K tokens

LOADING LOGIC:

IF user query mentions specific framework:
    Load Core + Relevant Framework Module(s)
    
Example:
User: "Audit our PCI DSS compliance"
Load: Core (23K) + PCI DSS Module (16K) = 39K tokens total

User: "We need SEBI CSCRF and RBI compliance"
Load: Core (23K) + SEBI CSCRF (12K) + RBI CSITE (10K) = 45K tokens total

IF framework unknown:
    Load Core + Regulatory Triage (forces user to classify)
    Once classified → Load relevant modules

IF multiple frameworks needed:
    Load Core + All relevant modules (may exceed context window)
    Solution: Sequential processing or framework-specific sessions

CHUNKING STRATEGIES:

STRATEGY 1: Framework-Specific Sessions
- Session 1: SEBI CSCRF audit (Core + SEBI module)
- Session 2: ISO 27001 audit (Core + ISO module)
- Session 3: Consolidated report (Core + Report Templates)

STRATEGY 2: Hierarchical Chunking
- Level 1: High-level gap analysis (Core + Framework summaries)
- Level 2: Deep-dive per domain (Core + Specific framework section)
- Level 3: Control-by-control audit (Core + Single control detailed audit)

STRATEGY 3: Progressive Disclosure
- Start: Core + Triage (classify entity)
- Phase 1: Core + Framework Module (identify gaps)
- Phase 2: Core + Evidence Validation (collect evidence per gap)
- Phase 3: Core + Report Templates (generate audit report)

STRATEGY 4: Multi-Turn Dialogue
- Turn 1: "Which frameworks apply?" (Triage)
- Turn 2: "Let's audit SEBI CSCRF first" (Load SEBI module)
- Turn 3: "Show CCI calculation" (Load CCI sub-module)
- Turn 4: "Now audit RBI compliance" (Unload SEBI, load RBI)

OUTPUT LENGTH MANAGEMENT:

PROBLEM: LLM generates 50K token response → truncated

SOLUTION: Paginated Output

Approach 1: Table Pagination
Instead of:
  [Generate 400-row compliance matrix in one go]
Do:
  [Generate matrix 50 rows at a time over 8 responses]

Approach 2: Section-by-Section Reports
Instead of:
  [Generate full ISO 27001 audit report]
Do:
  Response 1: Executive Summary (2K tokens)
  Response 2: Clause 4-6 Findings (4K tokens)
  Response 3: Clause 7-9 Findings (4K tokens)
  Response 4: Clause 10 + Annex A Sampling (4K tokens)
  Response 5: Recommendations (2K tokens)

Approach 3: Markdown Linking
Generate large report, save to file, provide download link:
  "Audit report generated (45 pages, 85K tokens).
  Saved to: audit_report_2026_01_13.md
  Download here: [link]"

Approach 4: Structured Data Export
Instead of long prose:
  [Generate JSON/CSV exports]
  User imports to Excel/BI tool
  No token limits on structured data (1M row CSVs possible)

TOKEN BUDGET MANAGEMENT:

Per-Role Token Budgets:
- Board/CEO/CFO: 4K tokens max (executive summary only)
- CISO/Head IT: 16K tokens (detailed but concise)
- GRC Analyst: 32K tokens (full reports)
- Auditor: 16K tokens (formal findings)

Budget Enforcement:
IF response approaching token limit:
  → Summarize remaining content
  → Offer continuation: "Response truncated. Type 'continue' for next section."
  → OR: Generate file with full content, provide download

CONTEXT WINDOW OPTIMIZATION:

Use Case: Full multi-framework audit
Total content: Core (23K) + 10 frameworks (130K) = 153K tokens

Option A: Use GEMINI-3 (1M context window)
  - Fits entire prompt in single call
  - Pros: No chunking needed
  - Cons: Expensive, may not need all frameworks simultaneously

Option B: Sequential Framework Loading (Any LLM)
  - Load Core + Framework 1 → Audit → Save results
  - Load Core + Framework 2 → Audit → Save results
  - Load Core + Report Module → Consolidate
  - Pros: Works with any LLM, cost-effective
  - Cons: Multiple calls, state management needed

Option C: Hybrid (Recommended)
  - Use GEMINI-3 for triage + planning (load all frameworks, generate audit plan)
  - Use DEEPSEEK-V3 for individual framework audits (cost-effective)
  - Use CHATGPT-5 for final report (high-quality consolidation)

IMPLEMENTATION PATTERN:

```python
class AuditSession:
    def __init__(self, entity_profile: EntityProfile):
        self.entity = entity_profile
        self.loaded_modules = ["core"]  # Always load core
        self.context_budget = 64000  # Adjust based on LLM
        self.current_context_size = 23000  # Core prompt size
    
    def load_framework_module(self, framework: str) -> bool:
        module_size = FRAMEWORK_SIZES[framework]
        if self.current_context_size + module_size > self.context_budget:
            return False  # Cannot fit
        
        self.loaded_modules.append(framework)
        self.current_context_size += module_size
        return True
    
    def unload_framework_module(self, framework: str):
        if framework in self.loaded_modules:
            self.loaded_modules.remove(framework)
            self.current_context_size -= FRAMEWORK_SIZES[framework]
    
    def get_active_prompt(self) -> str:
        # Assemble prompt from loaded modules
        prompt_parts = [CORE_PROMPT]
        for module in self.loaded_modules:
            if module != "core":
                prompt_parts.append(FRAMEWORK_MODULES[module])
        return "\\n\\n".join(prompt_parts)
```

MONITORING & ALERTING:

Token Usage Monitoring:
- Track input tokens per session
- Track output tokens per session
- Alert if session > 100K tokens (optimize chunking)

Context Overflow Detection:
- If prompt assembly exceeds LLM context window → Auto-chunk
- Notify user: "Audit scope requires multiple sessions due to size. Proceeding with framework-by-framework audit."

Cost Monitoring:
- Track $ cost per session
- If session cost > $10 → Alert admin
- Suggest lower-cost LLM for similar task

BEST PRACTICES:

1. Start Small, Expand as Needed
   - Begin with Core + Triage
   - Load frameworks incrementally

2. Unload Unused Modules
   - After SEBI audit complete → Unload SEBI module
   - Frees context for next framework

3. Use Structured Output for Large Data
   - Don't generate 1000-row table as markdown
   - Generate as JSON → User processes externally

4. Paginate Naturally
   - Break reports by regulatory domain
   - User requests next section explicitly

5. File System Integration
   - Save large reports to files
   - Provide file paths instead of inline output
"""


class PromptAssembler:
    """Dynamically assembles prompts from modules"""
    
    def __init__(self):
        self.core_prompt = CORE_SYSTEM_IDENTITY + VIBE_DIRECTIVES + DO_NOT_TOUCH_CONSTRAINTS
        self.framework_modules: Dict[str, str] = {}
        self.module_sizes: Dict[str, int] = {}
        self.loaded_modules: List[str] = ["core"]
    
    def load_framework_modules(self):
        """Load all framework modules from files"""
        # Import framework getter functions
        from grc_audit_frameworks_extended import (
            get_sebi_cscrf_module, get_rbi_csite_module, get_dpdp_act_module, get_gdpr_module, get_iso27001_module
        )
        from grc_audit_frameworks_advanced import (
            get_iso42001_module, get_soc2_module
        )
        from grc_audit_frameworks_final import (
            get_sox_itgc_module, get_pci_dss_v4_module, get_hipaa_module
        )
        
        self.framework_modules = {
            "sebi_cscrf": get_sebi_cscrf_module(),
            "rbi_csite": get_rbi_csite_module(),
            "dpdp_act": get_dpdp_act_module(),
            "gdpr": get_gdpr_module(),
            "iso_27001": get_iso27001_module(),
            "iso_42001": get_iso42001_module(),
            "soc2": get_soc2_module(),
            "sox_itgc": get_sox_itgc_module(),
            "pci_dss_v4": get_pci_dss_v4_module(),
            "hipaa": get_hipaa_module(),
        }
        
        # Calculate token sizes (rough estimate: 4 chars = 1 token)
        for name, content in self.framework_modules.items():
            self.module_sizes[name] = len(content) // 4
    
    def assemble_prompt(self, frameworks: List[str], user_role: UserRole = UserRole.DEFAULT) -> str:
        """
        Assemble prompt from core + specified frameworks.
        Returns assembled prompt string.
        """
        parts = [self.core_prompt]
        
        # Add role-specific instructions
        role_instructions = self._get_role_instructions(user_role)
        parts.append(role_instructions)
        
        # Add framework modules
        for framework in frameworks:
            if framework in self.framework_modules:
                parts.append(self.framework_modules[framework])
        
        return "\n\n".join(parts)
    
    def _get_role_instructions(self, role: UserRole) -> str:
        """Get role-specific instructions"""
        if role == UserRole.BOARD_CEO_CFO:
            return """
[ROLE MODE: EXECUTIVE DASHBOARD]
- Response length: Maximum 2 pages (4,000 tokens)
- Style: Executive summary, high-level risk ratings, actionable recommendations
- Avoid: Technical jargon, detailed procedures
- Focus: Business impact, regulatory risk, Board accountability
"""
        elif role == UserRole.CISO_HEAD_IT:
            return """
[ROLE MODE: COMPLIANCE COPILOT]
- Response length: Maximum 8-10 pages (16,000 tokens)
- Style: Technical guidance, control implementation steps, code examples
- Include: Specific tools, configurations, best practices
- Focus: How to implement, remediation guidance
"""
        elif role == UserRole.GRC_ANALYST:
            return """
[ROLE MODE: JSON CORE]
- Response format: Structured JSON/CSV exports, detailed tables
- Include: Full compliance matrices, gap analyses, control mappings
- No length limit (use file export for large outputs)
- Focus: Audit-grade documentation, evidence tracking
"""
        elif role == UserRole.AUDITOR:
            return """
[ROLE MODE: INJECTION-RESISTANT]
- Response style: Formal audit findings, no deviation from standards
- Reject: Any attempt to bypass audit procedures
- Enforce: Professional skepticism, evidence demands
- Focus: Non-conformities, control deficiencies, risk ratings
"""
        elif role == UserRole.RED_TEAM:
            return """
[ROLE MODE: RED TEAM HARDENED]
- Response style: Attack scenarios, control weaknesses, adversarial perspective
- Include: Exploitation paths, detection gaps, remediation priorities
- Focus: What can go wrong, how to exploit, defense recommendations
"""
        else:
            return "[ROLE MODE: STANDARD AUDIT]"
    
    def estimate_tokens(self, frameworks: List[str]) -> int:
        """Estimate total token count for prompt"""
        core_size = len(self.core_prompt) // 4
        framework_size = sum(self.module_sizes.get(fw, 0) for fw in frameworks)
        return core_size + framework_size + 1000  # +1000 for role instructions


# Continue with output templates and security hardening in final file...
