
# Lab 1 - Breaking the Pipeline (DevSecOps in Practice)
DevSecOps Lab – Postgraduate in Cyber Offensive and Red Team Operations

->  Lab Objective

To demonstrate **DevSecOps** concepts in practice using GitHub Actions, showing how security flaws can break a CI/CD pipeline and how to remediate them effectively using automation.

This lab simulates a real-world scenario where an application is deployed with **exposed secrets** and **vulnerable dependencies**, and then properly secured following security best practices.

---

##  What Was Done

### 1. Initial Setup
- Created a GitHub repository called `lab-devsecops-fail`
- Added a Python application (`app.py`) containing an **intentionally exposed API key** (Secret Leak)
- Created a `requirements.txt` file with outdated and vulnerable dependencies

### 2. Intentionally Introduced Vulnerabilities

**Security Issues:**
- Hardcoded AWS credentials directly in the source code (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`)

**Dependency Vulnerabilities (SCA):**
- `Flask==0.12` → Vulnerable to Denial of Service (CVE-2018-1000656)
- `Jinja2==2.9` → Vulnerable to Sandbox Escape (CVE-2019-10906)
- `requests==2.20.0` → Outdated version with known vulnerabilities

### 3. DevSecOps Pipeline (GitHub Actions)

Created a workflow `.github/workflows/devsecops-audit.yml` with:

- **TruffleHog** → Secrets scanning in the codebase
- **Trivy** → Software Composition Analysis (SCA) for dependency vulnerabilities
- **SBOM Generation** (CycloneDX format)
- Upload of SBOM as pipeline artifact

### 4. Fixes Applied

**app.py:**
- Removed hardcoded credentials
- Implemented `os.getenv()` to read secrets from environment variables (security best practice)

**requirements.txt:**
- Updated to secure versions:
  - `Flask==3.0.0`
  - `requests==2.31.0`
  - `jinja2==3.1.2`

---

🔍 Security Pipeline
The pipeline runs automatically on every push. It includes two main security stages:

Secret Scanning with TruffleHog
Software Composition Analysis (SCA) with Trivy

If critical or high-severity vulnerabilities are found, the pipeline fails on purpose (exit-code: 1), enforcing security fixes before merging.

📊 Results

StageInitial StatusFinal StatusSecret LeakExposedFixedSCA VulnerabilitiesCritical/HighRemediatedSBOM Generation-GeneratedPipeline StatusBrokenPassing

🧠 Lessons Learned

Secrets should never be committed to the codebase
Outdated dependencies are one of the biggest sources of security risks
Tools like Trivy and TruffleHog are essential for Shift-Left Security
The pipeline should act as a security gatekeeper
Generating SBOMs is a recommended practice for compliance and governance

🛡️ Tools Used

GitHub Actions
TruffleHog (Secret Scanning)
Trivy (SCA + SBOM)
Python + Flask
