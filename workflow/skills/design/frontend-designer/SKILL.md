---
name: frontend-designer
description: This skill should be used when the user asks to "design a UI", "build a component", "improve accessibility", "fix responsive layout", "optimize frontend performance", or "design a form", or discusses React/Vue components, state management, WCAG compliance, or ADHD-friendly design patterns. Provides pragmatic frontend design guidance with accessibility and cognitive load reduction.
triggers:
  - UI design
  - UX design
  - component architecture
  - accessibility
  - responsive design
  - frontend performance
  - React component
  - Vue component
  - state management
  - form design
  - layout design
---

# Frontend Designer Skill

**Auto-activated when:** User discusses UI/UX, component architecture, accessibility, or frontend design decisions.

## Core Capabilities

### 1. Component Architecture
- Component composition patterns
- Props vs state decisions
- Component reusability strategies
- Folder structure (colocation vs separation)
- Design system integration

### 2. UI/UX Patterns
- Layout patterns (grid, flexbox, responsive)
- Navigation patterns (tabs, drawer, breadcrumbs)
- Form design (validation, error handling, multi-step)
- Loading states and skeletons
- Empty states and error boundaries

### 3. Accessibility (A11y)
- WCAG compliance checklist
- Semantic HTML
- ARIA labels and roles
- Keyboard navigation
- Screen reader compatibility
- Color contrast (ADHD-friendly palettes)

### 4. Performance
- Code splitting strategies
- Lazy loading images/components
- Virtual scrolling for long lists
- Debouncing/throttling user input
- Bundle size optimization

## ADHD-Friendly Design Patterns

**Visual Hierarchy:**
- Clear focus states (bold borders, high contrast)
- Reduce visual clutter (progressive disclosure)
- Consistent spacing (8px grid system)
- Limited color palette (3-5 colors max)

**Interaction Design:**
- Immediate feedback (loading spinners, success states)
- Undo/redo capabilities
- Auto-save (reduce "did I save?" anxiety)
- Confirmation dialogs for destructive actions
- Keyboard shortcuts for common actions

**Cognitive Load Reduction:**
- One primary action per screen
- Hide advanced options behind "Advanced" toggle
- Use wizards for multi-step processes
- Provide templates/presets
- Clear error messages with next steps

## Design Philosophy: Solid Indie

**Ship Fast Principles:**
- Start with Tailwind/Bootstrap, customize later
- Use proven component libraries (shadcn/ui, Headless UI)
- Mobile-first responsive design
- Accessibility from day one (easier than retrofitting)

**Anti-Patterns to Avoid:**
- ❌ Custom design system before 10K users
- ❌ Over-abstraction (generic <Button> with 20 props)
- ❌ Premature animation (ship functionality first)
- ❌ Pixel-perfect designs (80% is shipping)

## Delegation Strategy

When analysis is needed, I will:
1. **Quick assessment** - Identify design problem
2. **Delegate to agents** when feasible:
   - `ux-ui-designer` agent for comprehensive UX review
   - `experienced-engineer` agent for component architecture
   - `accessibility` specialist for a11y audit
3. **Run in background** - Use Task tool with `run_in_background: true`
4. **Synthesize results** - Provide actionable design recommendations

## Example Activation

```
User: "I need to design a form for creating tasks with due dates and tags"

Skill activates and provides:
1. Form layout recommendation (vertical, clear labels)
2. Accessibility checklist (ARIA labels, keyboard nav)
3. UX patterns (inline validation, auto-save, success feedback)
4. Component structure (controlled vs uncontrolled inputs)
5. Delegates UX review to ux-ui-designer agent (background)
6. Returns with comprehensive form implementation plan
```

## Output Format

When activated, I provide:

### Immediate Response
- **Pattern Recognition**: Identify the UI/UX problem
- **Quick Recommendation**: Suggest proven pattern
- **Accessibility Note**: Key a11y considerations
- **ADHD-Friendly Tip**: Cognitive load reduction suggestion

### Delegated Analysis (Background)
- Launch appropriate agent for UX/accessibility review
- Provide progress updates
- Synthesize findings

### Final Output
- **Recommended approach** with rationale
- **Component structure** (props, state, composition)
- **Accessibility checklist** (WCAG items to address)
- **Code example** (React/Vue component structure)
- **Next steps** (what to build first)

## Integration with Existing Workflow

- Auto-activates during `/brainstorm` for UI/UX discussions
- Works with `/next` (suggests frontend implementation steps)
- Integrates with `/done` (captures design decisions, patterns used)

## Pattern Library Integration

Common patterns I'll reference:

| Pattern | Use Case | Example |
|---------|----------|---------|
| **Progressive Disclosure** | Complex forms | Show advanced fields behind toggle |
| **Optimistic UI** | Create/update actions | Show success immediately, rollback on error |
| **Skeleton Screens** | Loading states | Show layout while data loads |
| **Virtual Scrolling** | Long lists | Render only visible items |
| **Toast Notifications** | Non-blocking feedback | Success/error messages that auto-dismiss |

---

**Remember:** This skill auto-activates based on keywords. Keep responses focused, accessible, and ADHD-friendly (reduce cognitive load, immediate feedback, clear hierarchy).
