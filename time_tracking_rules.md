# Time Tracking Rules for HMRAH/EzyVet/Vetspire Project Analysis

## Tools to EXCLUDE (Not HMRAH Project Related)

These tools/activities should **NEVER** be counted toward the HMRAH/EzyVet/Vetspire project time:

### ❌ Customer Support Tools
- **Intercom** (app.intercom.com, mobile - io.intercom.android)
  - This is for Inventory Ally customer support, not HMRAH project

### ❌ Database Tools
- **DBeaver** (dbeaver, dbeaver community)
  - NEVER used for HMRAH

### ❌ Project Management
- **Trello** (trello.com)
  - NEVER used for HMRAH work

### ❌ General Business Tools
- **my.inventoryally.com** - Different client/project
- **analytics.inventoryally.com** - Different client/project
- **shop.vetcove.com** - Different vendor/project
- **integration.vetcove.com** - Different vendor/project
### 🟡 Slack
- **EXCLUDE**: Never used for HMRAH
---

## Tools to INCLUDE with Specific Filtering

### ✅ VS Code / Visual Studio Code
**ONLY count when associated with HMRAH-specific identifiers:**

#### Include These Contexts:
- **Codespace: effective-xylophone-p7pwqqvv9jc966j.github.dev**
  - This is the vetspire-to-ezyvet project codespace
  - ALWAYS count this time

- **Codespace: super-duper-bassoon-5vxrpp67xpfvjq7.github.dev**
  - Rescuetime analysys codespace
  - ALWAYS count this time

- **Local files when working with:**
  - `vetspire-to-ezyvet` repository
  - Files matching: `*ezyvet*.py`, `*vetspire*.py`, `*hmrah*`
  - Scripts in the hdsheena/vetspire-to-ezyvet repo
- Working on rescuetime-mcp project (like right now!)

#### Cautiously include iwth more details for the user to manually review
- Generic VS Code time without codespace/file context

#### Exclude These VS Code Sessions:

- Working on Inventory Ally codebase
- Other client projects

**Rule**: If VS Code activity shows codespace URL or specific file from vetspire-to-ezyvet repo, COUNT IT. Otherwise, EXCLUDE.

---

## Always Include (100% HMRAH Related)

### ✅ EzyVet Portals
- **hmrah.use1.ezyvet.com** - Production EzyVet instance
- **hmrah.usw2.trial.ezyvet.com** - Trial EzyVet instance
- **developers.ezyvet.com** - API documentation
- **docs.ezyvet.com** - EzyVet documentation

### ✅ Vetspire Portals
- **hopemillsroadanimalhospital.vetspire.com** - Client's Vetspire portal
- **developer.vetspire.com** - Vetspire API docs
- **vetspire.ai** - Vetspire platform

### ✅ GitHub (When HMRAH Related)
- **Github** activity when in hdsheena/vetspire-to-ezyvet repo
- **github desktop** when committing to vetspire-to-ezyvet
- Commits/PRs to vetspire-to-ezyvet repository

### ✅ API Testing
- **Postman** when testing EzyVet or Vetspire APIs
  - Look for requests to ezyvet.com or vetspire.com domains
  - Collections named with "EzyVet" or "Vetspire" or "HMRAH"

### ✅ Development Support Tools - often for hmrah, but should look at them in context of what else is goign on around then
- **Google Notebook** (google.com/notebook) - Development notes
- **Gemini AI** (gemini.google.com) - Coding assistance for HMRAH work
- **ChatGPT** (chatgpt) - Problem-solving for integration
- **epochconverter.com** - Timestamp conversions for API work

---

## Context-Dependent Tools



### 🟡 Google Meet
- **Include**: Meetings specifically about HMRAH project
- **Exclude**: everything else. most won't be. General team meetings, other client calls

### 🟡 Google Spreadsheets
- **Include**: Sheets tracking HMRAH data, migration status, pet records
- **Exclude**: General project tracking, other client data, anything referencing inventory, patterson, vetcove.

---

## Analysis Guidelines

### Codespace Time Calculation
When you see activity in **effective-xylophone-p7pwqqvv9jc966j.github.dev** or **super-duper-bassoon-5vxrpp67xpfvjq7.github.dev**:
- This is 100% HMRAH project work
- Count every second
- This is the most reliable indicator

### File-Based VS Code Time
When VS Code shows specific files:
- `justSendContactToEzy.py` ✅ Count it
- `post_appointments_batch.py` ✅ Count it  
- `fetch_visit_history.py` ✅ Count it
- `ezyvet_api.py` ✅ Count it
- Any file in vetspire-to-ezyvet repo ✅ Count it

### Portal Access Time
Any time spent in:
- EzyVet portals (hmrah.*)
- Vetspire portals (hopemillsroadanimalhospital.*)
- API documentation (developers.ezyvet.com, developer.vetspire.com)

= 100% HMRAH project time

---

## Quick Reference: Include/Exclude

| Tool | Action | Notes |
|------|--------|-------|
| effective-xylophone codespace | ✅ ALWAYS INCLUDE | 100% HMRAH |
| super-duper-bassoon codespace | ✅ ALWAYS INCLUDE | RescueTime analysis |
| rescuetime-mcp project | ✅ ALWAYS INCLUDE | RescueTime analysis |
| VS Code (generic) | 🟡 CAUTIOUS | Flag for manual review |
| VS Code (Inventory Ally) | ❌ EXCLUDE | Different client |
| hmrah.*.ezyvet.com | ✅ ALWAYS INCLUDE | Production/trial portals |
| hopemillsroadanimalhospital.vetspire.com | ✅ ALWAYS INCLUDE | Client portal |
| developers.ezyvet.com | ✅ ALWAYS INCLUDE | API docs |
| developer.vetspire.com | ✅ ALWAYS INCLUDE | API docs |
| Postman | ✅ INCLUDE | API testing |
| DBeaver | ❌ EXCLUDE | NEVER used for HMRAH |
| Intercom | ❌ EXCLUDE | Inventory Ally support |
| Trello | ❌ EXCLUDE | NEVER used for HMRAH |
| Slack | ❌ EXCLUDE | NEVER used for HMRAH |
| my.inventoryally.com | ❌ EXCLUDE | Different client |
| analytics.inventoryally.com | ❌ EXCLUDE | Different client |
| shop.vetcove.com | ❌ EXCLUDE | Different vendor |
| integration.vetcove.com | ❌ EXCLUDE | Different vendor |
| GitHub Desktop | 🟡 CONTEXT | Only if vetspire-to-ezyvet repo |
| Google Notebook | 🟡 CONTEXT | Often HMRAH, check context |
| Gemini/ChatGPT | 🟡 CONTEXT | Often HMRAH, check context |
| epochconverter.com | 🟡 CONTEXT | Often HMRAH, check context |
| Google Meet | 🟡 CONTEXT | Most excluded, rarely HMRAH |
| Google Spreadsheets | 🟡 CONTEXT | Check for inventory/patterson/vetcove refs |

---

## Notes
- **Codespace URLs are the gold standard** for identifying HMRAH work
- **Portal URLs are 100% reliable** indicators
- **Generic tool usage needs context** to be counted
- **When in doubt, exclude** to avoid inflating numbers

*Last updated: December 10, 2025*
