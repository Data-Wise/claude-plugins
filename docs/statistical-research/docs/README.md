# Statistical Research Plugin - Documentation

> **Complete documentation for the Statistical Research Plugin v1.0.0**

---

## 📚 Documentation Index

### Quick References

| Document | Purpose | Read Time |
|----------|---------|-----------|
| **[QUICK-START.md](QUICK-START.md)** | Get running in 5 minutes | 3 min |
| **[REFCARD.md](REFCARD.md)** | One-page command reference | 2 min |

### Detailed Guides

| Document | Purpose | Location |
|----------|---------|----------|
| **[README.md](../README.md)** | Main plugin documentation | Root |
| **[INSTALL-PRIVATE.md](../INSTALL-PRIVATE.md)** | Private installation guide | Root |
| **[Skills Guide](../skills/README.md)** | All 17 skills explained | `skills/` |

---

## 🚀 Getting Started

**New users:** Start with [QUICK-START.md](QUICK-START.md)

**Need a reminder:** Check [REFCARD.md](REFCARD.md)

**Installing:** Follow [INSTALL-PRIVATE.md](../INSTALL-PRIVATE.md)

---

## 📖 What's What

### QUICK-START.md
Perfect for:
- First-time users
- Getting up and running fast
- Learning the basic workflows

**Contents:**
- Installation (2 minutes)
- First commands to try
- Common workflows
- Tips and troubleshooting

### REFCARD.md
Perfect for:
- Quick command lookups
- Refreshing your memory
- One-page printable reference

**Contents:**
- All 13 commands in tables
- 17 skills overview
- Common patterns
- Troubleshooting quick reference

### INSTALL-PRIVATE.md (Root)
Perfect for:
- Installation instructions
- Development workflow
- Understanding dev vs production modes

**Contents:**
- Installation options (--dev, production)
- Development workflow
- Uninstallation
- Troubleshooting

### Skills README (skills/README.md)
Perfect for:
- Understanding auto-activating skills
- Seeing all 17 skills in detail
- Learning what triggers each skill

**Contents:**
- Skill categories (mathematical, implementation, writing, research)
- Activation triggers
- Use cases
- Examples

---

## 📂 Plugin Structure

```
statistical-research/
├── docs/                      # 👈 You are here
│   ├── README.md              # This file
│   ├── QUICK-START.md         # 5-minute guide
│   └── REFCARD.md             # One-page reference
├── commands/                  # 13 slash commands
│   ├── literature/            # /lit:* commands
│   ├── manuscript/            # /ms:* commands
│   ├── simulation/            # /sim:* commands
│   └── research/              # /research:* commands
├── skills/                    # 17 auto-activating skills
│   ├── README.md              # Skills guide
│   ├── mathematical/          # 4 math skills
│   ├── implementation/        # 5 implementation skills
│   ├── writing/               # 3 writing skills
│   └── research/              # 5 research skills
├── lib/                       # API wrappers
│   ├── arxiv-api.sh
│   ├── crossref-api.sh
│   └── bibtex-utils.sh
├── tests/                     # Unit tests
│   └── test-plugin-structure.sh
├── scripts/                   # Installation scripts
│   ├── install.sh
│   └── uninstall.sh
├── README.md                  # Main documentation
├── INSTALL-PRIVATE.md         # Private installation
├── install-private.sh         # Private installer
├── uninstall-private.sh       # Private uninstaller
├── package.json               # npm metadata
└── LICENSE                    # MIT license
```

---

## 🎯 Finding What You Need

### I want to...

**Get started quickly**
→ [QUICK-START.md](QUICK-START.md)

**Look up a command**
→ [REFCARD.md](REFCARD.md)

**Install the plugin**
→ [INSTALL-PRIVATE.md](../INSTALL-PRIVATE.md)

**Understand the skills**
→ [skills/README.md](../skills/README.md)

**Learn about specific commands**
→ [README.md](../README.md) (main documentation)

**Troubleshoot issues**
→ [QUICK-START.md](QUICK-START.md#troubleshooting) or [REFCARD.md](REFCARD.md#troubleshooting)

**Develop/modify the plugin**
→ [INSTALL-PRIVATE.md](../INSTALL-PRIVATE.md#development-workflow)

---

## 💡 Documentation Philosophy

This documentation follows **ADHD-friendly principles**:

1. **Quick access** - Find answers fast
2. **Scannable** - Tables and boxes, not walls of text
3. **Progressive disclosure** - Start simple, go deep as needed
4. **Multiple formats** - Reference card, quick start, detailed guide
5. **Action-oriented** - Focus on "how to" not "about"

---

## 🔗 External Links

- **Plugin Repository:** https://github.com/Data-Wise/claude-plugins
- **Monorepo Documentation:** [../../KNOWLEDGE.md](../../KNOWLEDGE.md)
- **Plugin Development Guide:** [../../docs/PLUGIN-DEVELOPMENT.md](../../docs/PLUGIN-DEVELOPMENT.md)

---

## 📝 Document Maintenance

**Last Updated:** 2025-12-23
**Plugin Version:** 1.0.0
**Documentation Version:** 1.0.0

---

**Need help?** Start with [QUICK-START.md](QUICK-START.md) or check [REFCARD.md](REFCARD.md) for quick answers!
