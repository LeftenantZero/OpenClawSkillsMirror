---
name: web-artifacts-builder
version: 1.0.0
description: "Build elaborate multi-component HTML artifacts using React, Tailwind CSS, and shadcn/ui"
tags: [testing, frontend, visual, browser, api-integration]
license: Complete terms in LICENSE.txt
dependencies:
  node:
    - react: ^18
    - react-dom: ^18
    - typescript: ^5
    - vite: ^5
    - tailwindcss: ^3.4
    - parcel: ^2
    - "@parcel/config-default": ^2
    - parcel-resolver-tspaths: ^1
    - html-inline: ^1
  system:
    - Node.js >= 18
---

# Web Artifacts Builder

Build powerful frontend artifacts with React + TypeScript + Tailwind CSS + shadcn/ui.

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

This creates a fully configured project with:
- �?React + TypeScript (via Vite)
- �?Tailwind CSS 3.4.1 with shadcn/ui theming system
- �?Path aliases (`@/`) configured
- �?40+ shadcn/ui components pre-installed
- �?All Radix UI dependencies included
- �?Parcel configured for bundling (via .parcelrc)
- �?Node 18+ compatibility (auto-detects and pins Vite version)

### Step 2: Develop Your Artifact

Edit the generated files to build your artifact. See **Common Development Tasks** below for guidance.

### Step 3: Bundle to Single HTML File

Bundle the React app into a single HTML artifact:
```bash
bash scripts/bundle-artifact.sh
```

This creates `bundle.html` - a self-contained artifact with all JavaScript, CSS, and dependencies inlined.

**Requirements**: Your project must have an `index.html` in the root directory.

**What the script does**:
- Installs bundling dependencies (parcel, @parcel/config-default, parcel-resolver-tspaths, html-inline)
- Creates `.parcelrc` config with path alias support
- Builds with Parcel (no source maps)
- Inlines all assets into single HTML using html-inline

### Step 4: Share Artifact with User

Share the bundled HTML file with the user so they can view it as an artifact.

### Step 5: Testing/Visualizing (Optional)

Only perform if necessary or requested. Use available tools (Playwright, Puppeteer, or browser). Test after presenting the artifact if issues arise.

## Design & Style Guidelines

**IMPORTANT**: To avoid "AI slop", avoid using:
- Excessive centered layouts
- Purple gradients on white
- Uniform rounded corners
- Inter font as display font

## Error Handling

### Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| `npm install` fails | Node version mismatch | Ensure Node.js >= 18, check `node -v` |
| Vite version conflict | Node 18+ auto-detection issue | Script auto-pins compatible Vite version |
| Parcel build fails | Path alias misconfiguration | Check `tsconfig.json` paths and `.parcelrc` |
| Bundle too large | External dependencies not tree-shaken | Use dynamic imports, check bundle size |
| shadcn components not rendering | Missing Radix UI peer dependencies | Run `npx shadcn-ui@latest add <component>` |
| Tailwind styles not applying | CSS not being processed | Check `tailwind.config.js` content paths |
| `html-inline` fails | Missing assets or circular references | Ensure all assets exist, check for circular imports |

### Dependency Check

```bash
# Verify Node.js version
node -v  # Should be >= 18

# Check if all dependencies are installed
npm ls --depth=0

# Reinstall if needed
rm -rf node_modules package-lock.json
npm install
```

### Graceful Degradation

```
If bundling fails:
1. Try serving development version: npm run dev
2. Share development URL if localhost accessible
3. Share source files as fallback
4. Provide setup instructions for user to run locally
```

## Reference

- **shadcn/ui components**: https://ui.shadcn.com/docs/components
- **Tailwind CSS**: https://tailwindcss.com/docs
- **Radix UI primitives**: https://www.radix-ui.com/themes/docs/overview/introduction
