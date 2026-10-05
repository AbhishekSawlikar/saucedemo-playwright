<div align="center">

# 🎭 SauceDemo Playwright Automation Framework

**Production-grade UI test automation framework built with Python, Playwright, and the Page Object Model (POM).**

[![CI/CD Pipeline](https://github.com/AbhishekSawlikar/saucedemo-playwright/actions/workflows/test-pipeline.yml/badge.svg)](https://github.com/YOUR_USERNAME/saucedemo-playwright/actions/workflows/test-pipeline.yml)
[![Python Version](https://img.shields.io/badge/Python-3.11%20%7C%203.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-v1.49%2B-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/python/)
[![pytest](https://img.shields.io/badge/pytest-8.0%2B-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Architecture](#-architecture) •
[Features](#-key-features) •
[Speed Benchmarks](#-performance-benchmarks) •
[Quick Start](#-quick-start) •
[CI/CD & Docker](#-cicd--docker-pipeline)

</div>

---

## 📌 Overview

This repository demonstrates modern end-to-end web testing practices against the [SauceDemo (Swag Labs)](https://www.saucedemo.com/) ecommerce application.

Instead of writing brittle script-style tests, this framework incorporates:
- **Session-scoped authentication caching** (`storage_state`), removing redundant UI login interactions.
- **Strict branch protection enforcement** in GitHub Actions (failing PRs block merges instantly).
- **Zero-setup Dockerization** matching the official Microsoft Playwright container runtime.
- **Deep failure diagnostics** via auto-captured Playwright `.zip` traces, videos, and screenshots.

---

## ⚡ Performance Benchmarks

By eliminating repeated login roundtrips via saved storage states and executing tests across multiple worker processes with `pytest-xdist`, test run durations dropped by **over 80%**:

| Configuration | Test Scope | Workers | Runtime | Speedup |
| :--- | :--- | :---: | :---: | :---: |
| **Traditional Sequential** | 18 Tests (Chromium, Firefox, WebKit) | `1` | `61.4s` | *Baseline (1.0x)* |
| **With `storage_state`** | 18 Tests (Bypassed UI Auth) | `1` | `37.8s` | **1.6x faster** |
| **Parallel + `storage_state`** | 18 Tests (Chromium, Firefox, WebKit) | `4` | **`11.2s`** | **5.5x faster 🚀** |

> **Why the drop?** Skipping the 3-step keystroke rendering (`fill username`, `fill password`, `click login`) and the subsequent session redirect saves ~1.5s per test. Distributing the suite across 4 workers utilizes multi-core hardware efficiently.

---

## 🏗️ Architecture

```text
saucedemo-playwright/
├── .auth/
│   └── user_state.json             # Cached browser session (auto-generated; ignored by git)
├── .github/
│   └── workflows/
│       └── test-pipeline.yml       # PR validation, nightly regression, artifact retention
├── pages/
│   ├── base_page.py                # Core wrappers, URL asserts, smart waits
│   ├── login_page.py               # Authentication locators & error message validation
│   ├── inventory_page.py           # Catalog items, sorting, cart counter verification
│   ├── cart_page.py                # Item verification & checkout transitions
│   └── checkout_page.py            # Form completion, order summary, confirmation checks
├── tests/
│   ├── conftest.py                 # Storage state generator, browser contexts, page fixtures
│   ├── test_auth.py                # Smoke tests for auth flows & lockout validation
│   └── test_checkout_flow.py       # E2E purchasing flows (Smoke & Regression)
├── Dockerfile                      # Container build using [mcr.microsoft.com/playwright](https://mcr.microsoft.com/playwright)
├── pytest.ini                      # Pytest configurations, tracing flags, markers
├── requirements.txt                # Pinned framework dependencies
└── README.md
