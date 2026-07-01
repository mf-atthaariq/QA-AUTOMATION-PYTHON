# 🚀 QA Automation Python - Playwright & Pytest (Enterprise Full-Stack Suite)

This repository serves as a comprehensive, production-grade **Full-Stack Automation Testing Portfolio** built with **Python**, leveraging the modern **Playwright** framework and the asynchronous-capable **Pytest** engine. Heavily influenced by disciplined C# xUnit enterprise design patterns, this architecture bridges the gap between high-performance technical engineering and human-readable business logic.

---

## 🛠️ Tech Stack & Advanced Ecosystem
* **Language:** Python 3.x (Thread-Safe Compilation)
* **Web UI Core:** Playwright Python (Sync Mode with Auto-Wait Guards)
* **API Client Engine:** Requests Python
* **Test Runner:** Pytest Ecosystem
* **BDD Engine:** Pytest-BDD (Gherkin Syntax Parsing)
* **Concurrency Scaling:** Pytest-Xdist (Multi-Threading Core Workers)
* **Reporting & Telemetry:** Pytest-HTML (Self-Contained Artifacts with Native Logging)
* **Design Pattern:** Page Object Model (POM) & External Data-Driven Testing (DDT)

---

## 🏗️ Project Directory Architecture
```text
QA-AUTOMATION-PYTHON/
│
├── .github/workflows/              # Cloud DevOps Infrastructure
│   └── main.yml                    # CI/CD Cloud Pipeline Workflow (Headless Ubuntu Execution)
│
├── data/                           # Data Center & Dataset Providers (SoC Pattern)
│   └── api_negative_cases.json     # Parameterized Security & Auth Intrusion Dataset
│
├── features/                       # Behavioral Business Requirements Layer
│   └── user_login.feature          # Human-Readable Gherkin Syntax Specifications
│
├── pages/                          # Page Object Model (POM) Web Interactive Layers
│   └── login_page.py               # Decoupled Element Locators & Action Modifiers
│
├── schemas/                        # Contract Compliance Gateway (Gatekeeper Pattern)
│   └── post_schema.json            # Sealed JSON Schema Contract Validation Specs
│
├── utils/                          # Shared Corporate Constants & Constants Center
│   └── api_routes.py               # Route Utility Container (Mimicking C# Static Routing)
│
├── tests/                          # Automated Test Execution Modules
│   ├── step_defs/
│   │   └── test_login_bdd.py       # BDD Gherkin Feature-to-Code Mapping Engine
│   ├── test_api_jsonplaceholder.py # Advanced API Lifecycle Integration Suite
│   ├── test_saucedemo_pom.py       # Robust Web UI POM Regression Suite
│   └── test_buka_web.py            # Baseline Linear Web UI Functional Flow
│
├── pytest.ini                      # Global Test Config, Custom Markers Registration & Log Formatters
└── README.md                       # Project Documentation
```

---

### WEEK 1 & 2: Python Programming Foundations & OOP Architecture
- Theories: Control flows, list/dictionary JSON-like mapping structures, and core Object-Oriented Programming (OOP) pillars (Classes, Methods, State Inheritance).

### WEEK 3 & 4: Robust Web UI POM Framework & Git Control
- Theories: Playwright locator strategies, text-based selectors, conftest.py browser life-cycle orchestration, local version control management, and pytest-html integration.

### WEEK 5: Full API Lifecycle Automation & Async Decoupling
- Theories: Code-based backend validation, CRUD (POST, GET, PUT, DELETE) transaction handling, and response mapping.

### WEEK 6: Advanced Enterprise Automation Patterns (Separation of Concerns)
- Theories: Architectural migration inspired by C# enterprise systems. Created a unified Route Container to centralize paths. Implemented a Gatekeeper Contract Validation pattern via jsonschema to validate payload data types instantly, replacing manual foreach-loops. Decoupled test datasets into external data files (api_negative_cases.json).

### WEEK 7: Cloud DevSecOps Pipelines (DevOps Infrastructure)
- Theories: Built a fully automated cloud pipeline using GitHub Actions (main.yml). Orchestrated headless script execution inside a virtual Linux server (ubuntu-latest). Implemented automatic zip compilation for test report artifacts with a retention-days: 7 auto-purge storage compliance.

### WEEK 8: Grand Finale - Parallel Concurrency Scaling, Telemetry Logging, and BDD Integration
- Theories: Configured multi-threaded parallel execution via pytest-xdist to reduce pipeline durations. Established an automated telemetry infrastructure using the native Python logging module to stamp structured operational records (INFO, WARNING, ERROR) alongside strict transactional execution timestamps. Integrated Behavior-Driven Development (BDD) paradigms via pytest-bdd using Gherkin syntax to abstract code structures into business-readable features.

---
## 📊 Latest Execution Benchmark

| Environment / Runner | Total Test Items | Execution Mode | Duration | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Local Machine (Win64)** | 15 Items Collected | Parallel Workers (`-n 8`) | **7.92s** 🔥 | **PASSED** 🟢 |
| **GitHub Actions Cloud** | 14 Items Collected | Parallel Workers (`-n auto`) | **1m 20s** 🚀 | **PASSED** 🟢 |
---
## 🚀 Execution & Running Guide

1. Installation

Ensure your virtual environment (venv) is active, then install the modern dependencies:
## 🚀 Execution & Running Guide

1. Installation
Ensure your virtual environment (venv) is active, then install the modern dependencies:
```PowerShell
pip install pytest playwright requests pytest-html jsonschema pytest-xdist pytest-bdd
playwright install --with-deps
```

2. Run Commands

- Sequential run:
```PowerShell
pytest -v -s
```

- Parallel run:
```PowerShell
pytest -v -s -n auto
```
---