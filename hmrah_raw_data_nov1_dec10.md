# HMRAH Project Raw Time Data
**Period: November 1 - December 10, 2025**

## Filtering Rules Applied
See `time_tracking_rules.md` for complete filtering criteria.

### ✅ Always Included (100% HMRAH)
- Codespaces: effective-xylophone, super-duper-bassoon, rescuetime-mcp
- EzyVet portals: hmrah.use1.ezyvet.com, hmrah.usw2.trial.ezyvet.com
- Vetspire portals: hopemillsroadanimalhospital.vetspire.com
- API documentation: developers.ezyvet.com, developer.vetspire.com, docs.ezyvet.com

### ❌ Excluded (Never HMRAH)
- DBeaver, Trello, Intercom, Slack
- Inventory Ally tools (my.inventoryally.com, analytics.inventoryally.com)
- Vetcove tools (shop.vetcove.com, integration.vetcove.com)

### 🟡 Context-Dependent (Manually Reviewed)
- VS Code (only counted when in HMRAH codespace/repo)
- Postman (assumed HMRAH during dev sessions)
- AI tools (Gemini, ChatGPT) during HMRAH work periods
- GitHub/GitHub Desktop when working with vetspire-to-ezyvet repo

---

## Raw Time Data by Category

### **Codespaces (100% HMRAH)**
| Activity | Seconds | Hours | Category |
|----------|---------|-------|----------|
| effective-xylophone-p7pwqqvv9jc966j.github.dev | 32,723 | 9.09 | Cloud Dev |
| super-duper-bassoon-5vxrpp67xpfvjq7.github.dev | 1,117 | 0.31 | RescueTime Analysis |
| **TOTAL CODESPACES** | **33,840** | **9.40** | |

### **EzyVet Portals (100% HMRAH)**
| Activity | Seconds | Hours | Category |
|----------|---------|-------|----------|
| hmrah.use1.ezyvet.com | 6,924 | 1.92 | Production Portal |
| hmrah.usw2.trial.ezyvet.com | 3,091 | 0.86 | Trial Portal |
| developers.ezyvet.com | 1,802 | 0.50 | API Docs |
| docs.ezyvet.com | 590 | 0.16 | Documentation |
| support.ezyvet.com | 33 | 0.01 | Support |
| ezyvet.com | 171 | 0.05 | Main Site |
| **TOTAL EZYVET PORTALS** | **12,611** | **3.50** | |

### **Vetspire Portals (100% HMRAH)**
| Activity | Seconds | Hours | Category |
|----------|---------|-------|----------|
| hopemillsroadanimalhospital.vetspire.com | 2,488 | 0.69 | Client Portal |
| developer.vetspire.com | 300 | 0.08 | API Docs |
| vetspire.ai | 10 | 0.00 | Platform |
| link.vetspire.com | 7 | 0.00 | Links |
| vetintegrations.vetspire.com | 7 | 0.00 | Integrations |
| sandbox.vetspire.com | 12 | 0.00 | Sandbox |
| vetspire.com | 2 | 0.00 | Main Site |
| **TOTAL VETSPIRE PORTALS** | **2,826** | **0.78** | |

### **Development Tools (Context-Based)**
| Activity | Seconds | Hours | Notes |
|----------|---------|-------|-------|
| Visual Studio Code | 150,871 | 41.91 | ⚠️ MULTI-PROJECT - need codespace filtering |
| postman | 19,885 | 5.52 | ✅ Likely HMRAH during Dec 4-10 |
| Github | 8,154 | 2.26 | 🟡 Only vetspire-to-ezyvet commits |
| github desktop | 4,259 | 1.18 | 🟡 Only vetspire-to-ezyvet commits |
| Cursor | 1,879 | 0.52 | ✅ Used Dec 6 for HMRAH |

**VS Code Note**: Of the 150,871 seconds, only count sessions that:
- Occurred in effective-xylophone or super-duper-bassoon codespaces (already counted above)
- Worked on rescuetime-mcp project (super-duper-bassoon time)
- Exclude all other VS Code time as multi-project

**Postman**: Primarily used Dec 4-10 during intensive HMRAH development. Earlier Postman use may be other projects.

### **AI Assistance Tools (Context-Based)**
| Activity | Seconds | Hours | Notes |
|----------|---------|-------|-------|
| gemini.google.com | 22,383 | 6.22 | 🟡 Used during HMRAH dev sessions |
| chatgpt | 7,458 | 2.07 | 🟡 Used during HMRAH dev sessions |
| google.com/notebook | 4,410 | 1.23 | 🟡 Development notes |
| mobile - com.openai.chatgpt | 3,363 | 0.93 | 🟡 Mobile assistance |

**Note**: AI tools likely used for HMRAH during Dec 4-10 intensive dev period. Earlier usage unknown.

### **Supporting Tools (Context-Based)**
| Activity | Seconds | Hours | Notes |
|----------|---------|-------|----------|
| epochconverter.com | 131 | 0.04 | ✅ Timestamp conversion for APIs |
| rescuetime.com | 993 | 0.28 | ✅ This analysis project |
| heapanalytics.com | 319 | 0.09 | ✅ Analytics Dec 10 |
| survey3.medallia.com | 182 | 0.05 | 🟡 Feedback survey |

### **Excluded Tools (Not HMRAH)**
| Activity | Seconds | Hours | Reason |
|----------|---------|-------|--------|
| dbeaver | 70,031 | 19.45 | ❌ NEVER used for HMRAH |
| app.intercom.com | 15,914 | 4.42 | ❌ Inventory Ally support |
| my.inventoryally.com | 13,218 | 3.67 | ❌ Different client |
| trello.com | 5,080 | 1.41 | ❌ NEVER used for HMRAH |
| Slack | 30,545 | 8.48 | ❌ NEVER used for HMRAH |
| shop.vetcove.com | 538 | 0.15 | ❌ Different vendor |
| integration.vetcove.com | 48 | 0.01 | ❌ Different vendor |
| analytics.inventoryally.com | 504 | 0.14 | ❌ Different client |

---

## Conservative Time Estimate (High Confidence)

### **Tier 1: Absolute HMRAH Time**
| Category | Seconds | Hours |
|----------|---------|-------|
| Codespaces (effective-xylophone + super-duper-bassoon) | 33,840 | 9.40 |
| EzyVet Portals | 12,611 | 3.50 |
| Vetspire Portals | 2,826 | 0.78 |
| **TIER 1 TOTAL** | **49,277** | **13.69** |

### **Tier 2: High Probability HMRAH (Dec 4-10 Dev Period)**
| Category | Seconds | Hours | Confidence |
|----------|---------|-------|------------|
| Postman (Dec 4-10) | ~15,000 | ~4.17 | 90% |
| Gemini AI (Dec 4-10) | ~12,000 | ~3.33 | 85% |
| ChatGPT (Dec 4-10) | ~4,000 | ~1.11 | 85% |
| Cursor IDE (Dec 6) | 1,879 | 0.52 | 95% |
| Google Notebook (Dec 4-10) | ~2,500 | ~0.69 | 80% |
| RescueTime setup (Dec 10) | 993 | 0.28 | 100% |
| GitHub activity (Dec 4-10) | ~3,000 | ~0.83 | 90% |
| **TIER 2 TOTAL (ESTIMATED)** | **~39,372** | **~10.93** | |

### **Tier 3: Uncertain / Needs Review**
| Category | Note |
|----------|------|
| VS Code (generic) | Cannot separate HMRAH from other projects without codespace context |
| Postman (Nov 1 - Dec 3) | Mixed with other projects, unclear allocation |
| AI tools (Nov 1 - Dec 3) | Used for multiple projects |
| Google Spreadsheets | Cannot identify which sheets are HMRAH vs Inventory Ally |

---

## Summary

### **Conservative Minimum (Tier 1 Only)**
- **Total: 13.69 hours** over 40 days
- **Average: 0.34 hours/day**
- **Confidence: 100%** - All activities definitively HMRAH

### **Likely Total (Tier 1 + Tier 2)**
- **Total: ~24.62 hours** over 40 days  
- **Average: ~0.62 hours/day**
- **Confidence: 85-95%** - Strong evidence these activities were HMRAH

### **Peak Development Period (Dec 4-10)**
- **Most activities concentrated in 7 days**
- **Codespace usage: Dec 5-10 (6 days)**
- **Portal testing: Throughout December**

---

## Notes for Manual Review

1. **VS Code Generic Time**: 150,871 seconds (41.91 hours) cannot be accurately split without file-level context. RescueTime doesn't track which files were open in generic VS Code sessions.

2. **November Activity**: Very minimal HMRAH work in November. Most November time was other projects (Inventory Ally, Vetcove integrations).

3. **December Ramp-Up**: Clear spike in activity starting Dec 4, with Dec 7-8 being marathon weekend development sessions.

4. **Postman Allocation**: Postman used extensively Dec 4-10. Earlier Postman use likely other APIs.

5. **AI Tool Usage**: Gemini and ChatGPT heavily used Dec 5-10, aligned with intensive development period.

---

*Generated: December 10, 2025*
*Analysis based on time_tracking_rules.md filtering criteria*
