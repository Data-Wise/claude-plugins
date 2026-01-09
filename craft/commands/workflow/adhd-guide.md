# ADHD-Friendly Workflow Guide

Strategies for staying focused and productive with ADHD.

## Core Principle

**Externalize your memory.** Your brain is for thinking, not remembering.

---

## Essential Daily Pattern

### Morning Ritual (2 minutes)

```bash
1. cd ~/projects/my-project
2. /workflow:recap              # Restores context instantly
3. /git:sync                    # Get latest changes
4. /workflow:next               # "What should I do?"
```

**Why this works:**
- Eliminates "what was I doing?" paralysis
- Provides clear starting point
- Takes 2 minutes, saves 20

### Evening Ritual (2 minutes)

```bash
1. /workflow:done               # Captures progress
2. /git:commit                  # Saves work
3. /git:sync                    # Backs up to cloud
```

**Why this works:**
- Tomorrow-you will forget details
- Everything is saved
- No panic about lost work
- Clear stopping point

---

## During Work

### Every 30-60 Minutes

```bash
/git:commit                     # Save progress
```

**Why:**
- ADHD = forget to save
- Small commits = easier to undo
- Progress visible in git log
- Peace of mind

### When Idea Appears

```bash
/workflow:brain-dump "the idea"
```

**Immediately!** Don't think "I'll remember" - you won't.

**Why:**
- Ideas appear randomly
- Disappear just as fast
- Writing = 10 seconds
- Re-discovering = never

### When Stuck (>10 minutes)

```bash
/workflow:stuck
```

**Don't wait 30+ minutes!**

**Why:**
- Stuck ≠ lazy
- ADHD = harder to switch strategies
- AI can suggest alternatives
- 10-minute rule prevents spiraling

---

## Context Switching

**ADHD = many interruptions. Handle them:**

### Before Interruption

```bash
/workflow:brain-dump "current thought + next step"
```

**Example:**
```bash
/workflow:brain-dump "fixing login bug, next try adding debug logging to auth.js line 45"
```

### After Interruption

```bash
1. /workflow:recap              # Restore context
2. cat NOTES.md                 # Read brain dump
3. Resume work
```

**Time saved:** 5-15 minutes of "where was I?"

---

## Focus Strategies

### Enter Focus Mode

```bash
/workflow:focus
```

**What it does:**
- Closes distractions
- Sets timer
- Clear focus goal

**When to use:**
- Deep work needed
- Deadline pressure
- Too many distractions

### Pomodoro Pattern

```
1. /workflow:focus 25           # 25-minute focus
2. [work on ONE thing]
3. Timer rings → take 5-min break
4. /workflow:brain-dump "progress"
5. Repeat
```

**Why Pomodoro works for ADHD:**
- External timer (not relying on memory)
- Built-in breaks
- Finite time (less overwhelming)
- Visible progress

---

## Idea Management

### Two Types of Ideas

**Quick thoughts** (30 seconds):
```bash
/workflow:brain-dump "add dark mode to settings"
```

**Structured thinking** (5-10 minutes):
```bash
/workflow:brainstorm "dark mode implementation"
```

### When to Use Each

**Brain-dump:**
- Random idea while working
- Quick thought you'll forget
- Interruption capture
- End-of-day thoughts

**Brainstorm:**
- Planning a feature
- Problem-solving
- Generating alternatives
- Organizing accumulated ideas

### Don't Let Ideas Pile Up

**Weekly review:**
```bash
1. cat NOTES.md
2. /workflow:brainstorm "review ideas"
3. Archive old notes:
   mv NOTES.md NOTES-$(date +%Y%m).md
4. touch NOTES.md
```

---

## Common ADHD Challenges

### "I forgot to commit for 3 days"

**Solution:**
- Set 1-hour timer
- When rings: `/git:commit`
- Reset timer

**Or:** GitHub Desktop app (shows uncommitted)

### "I started 5 things, finished 0"

**Solution:**
```bash
1. /workflow:recap              # See what's in progress
2. /workflow:next               # Pick ONE
3. /workflow:focus 25           # Pomodoro on it
4. /workflow:done               # Mark complete
```

**Rule:** Finish before starting new

### "I have 47 browser tabs open"

**Solution:**
```bash
# Before closing tabs:
/workflow:brain-dump "interesting links: [paste URLs]"

# Now close all tabs
# Revisit later when relevant
```

### "I can't remember what I learned"

**Solution:**
```bash
# After learning something:
/workflow:brain-dump "learned: [key points]"

# Weekly:
grep "learned:" NOTES.md
```

### "I spent 2 hours on wrong thing"

**Solution:**
- Use `/workflow:next` to verify priority
- Check `.STATUS` file regularly
- Set timer to re-check every 30 min

---

## Project Management for ADHD

### .STATUS File (Essential!)

Keep in every project:
```
project: my-project
status: active
priority: P1
progress: 40

# What I'm doing
Building user authentication

# What's done
✅ Database schema
✅ Login API

# What's next
→ Password reset flow

# Blockers
- Waiting on design review
```

**Why:**
- External memory
- `/workflow:recap` reads this
- Clear progress tracking
- No "what was I building?"

### Update .STATUS in `/workflow:done`

The command updates it automatically:
- Captures completed work
- Records next steps
- Notes blockers

**You don't have to remember to update it.**

---

## Multi-Project Context

**ADHD = often juggling projects**

### Switch Projects Cleanly

**Leaving Project A:**
```bash
/workflow:done                  # Save context A
/git:sync                       # Back up
```

**Entering Project B:**
```bash
cd ~/projects/project-b
/workflow:recap                 # Load context B
/workflow:next                  # Start working
```

**Critical:** Always `/workflow:done` before switching

---

## Medication Timing

### Before Meds Kick In (Morning)

**Low mental energy:**
```bash
/workflow:recap                 # Easy, just reading
/git:sync                       # Automated
/workflow:next                  # Get direction
```

**Don't start hard work yet**

### Peak Focus Time

**Use for:**
- Complex problems
- Deep work
- Creative thinking
- `/workflow:focus` sessions

### End of Day (Meds Wearing Off)

**Use for:**
```bash
/workflow:done                  # Just capturing
/git:commit                     # Simple action
/git:sync                       # Automated
```

**Don't try to start new things**

---

## Reducing Cognitive Load

### Use Commands, Not Memory

**DON'T:**
- Remember to commit
- Remember what you were doing
- Remember good ideas
- Track progress mentally

**DO:**
```bash
/workflow:recap     # Remember for you
/workflow:done      # Track for you
/workflow:brain-dump # Capture for you
/git:commit         # Save for you
```

### Automate Decisions

**Questions to eliminate:**
- "Should I commit?" → Yes, every 30-60 min
- "Should I save this idea?" → Yes, brain-dump it
- "Is this the right task?" → `/workflow:next` decides

### Visual Progress

```bash
# See what you did today:
git log --oneline --since="8am"

# See progress:
cat .STATUS

# See ideas captured:
cat NOTES.md
```

**Why:** ADHD needs external validation of progress

---

## Crisis Mode (Deadline, High Pressure)

```bash
1. /workflow:focus              # Close distractions
2. /workflow:next               # One clear task
3. Set 25-min timer
4. Work ONLY on that
5. /git:commit                  # Save progress
6. Repeat until done
7. /workflow:done               # Capture for later
```

**Don't:**
- Multitask
- Answer messages
- Check email
- Start new ideas

**Do:**
- ONE thing
- Timer-based
- Frequent commits
- Brain-dump other ideas for later

---

## Recovery Mode (Burnout, Low Energy)

```bash
1. /workflow:recap              # Where am I?
2. /workflow:brain-dump "feeling burned out"
3. Pick smallest possible task
4. /git:commit                  # Any progress counts
5. /workflow:done               # Capture what you did
```

**Progress ≠ Perfection**

---

## Tools Integration

### With Shell Functions

User's ADHD workflow:
```bash
work <project>      # Jumps to project + shows context
finish              # Runs /workflow:done + commits
dash                # Dashboard of all projects
```

**Combine with commands:**
```bash
work medfit         # Switch project
/workflow:recap     # Load context
/workflow:next      # Start working
```

### With Git

```bash
# Workflow → Git integration
/workflow:done      # Suggests commit message
/git:commit         # Uses suggestion
/git:sync           # Push to remote
```

### With .STATUS Files

All research/teaching projects have `.STATUS`:
```bash
/workflow:recap     # Reads .STATUS automatically
/workflow:done      # Updates .STATUS
```

---

## Quick Reference

**Start work:** `/workflow:recap` → `/workflow:next`
**During work:** `/git:commit` every 30-60 min
**Random idea:** `/workflow:brain-dump` immediately
**Stuck:** `/workflow:stuck` after 10 min
**End work:** `/workflow:done` → `/git:sync`

**Remember:**
- Commands remember for you
- External brain > mental tracking
- Progress > perfection
- Done > perfect

---

**See also:**
- `/workflow` - Workflow hub
- `/help workflows` - Command sequences
- `/help` - Getting started
