# Scrum Report Commit Schedule

Commit each report at the **end of the corresponding week** using the backdated git commands below.
Run commands from the **root of the repository** (`project-local/`).

---

## How Backdating Works

Git commit dates are controlled by two environment variables:
- `GIT_AUTHOR_DATE` — the date shown in `git log`
- `GIT_COMMITTER_DATE` — the internal commit timestamp

Set both to the same value to produce a clean, consistent backdated commit.

**Format:** `"YYYY-MM-DDTHH:MM:SS"`

---

## Commit Commands by Week

### Week 1 — Feb 22, 2026 (Sprint 1 Kickoff)

```bash
git add ScrumReports/Week1_Scrum_Report_Sprint1_Backlog.md
GIT_AUTHOR_DATE="2026-02-22T23:00:00" GIT_COMMITTER_DATE="2026-02-22T23:00:00" \
git commit -m "Add Week 1 Scrum Report and Sprint 1 Backlog"
```

---

### Week 2 — Mar 1, 2026 (Sprint 1)

```bash
git add ScrumReports/Week2_Scrum_Report.md
GIT_AUTHOR_DATE="2026-03-01T23:00:00" GIT_COMMITTER_DATE="2026-03-01T23:00:00" \
git commit -m "Add Week 2 Scrum Report"
```

---

### Week 3 — Mar 8, 2026 (Sprint 1)

```bash
git add ScrumReports/Week3_Scrum_Report.md
GIT_AUTHOR_DATE="2026-03-08T23:00:00" GIT_COMMITTER_DATE="2026-03-08T23:00:00" \
git commit -m "Add Week 3 Scrum Report"
```

---

### Week 4 — Mar 15, 2026 (Sprint 2 Kickoff)

```bash
git add ScrumReports/Week4_Scrum_Report_Sprint2_Backlog.md
GIT_AUTHOR_DATE="2026-03-15T23:00:00" GIT_COMMITTER_DATE="2026-03-15T23:00:00" \
git commit -m "Add Week 4 Scrum Report and Sprint 2 Backlog"
```

---

### Week 5 — Mar 22, 2026 (Sprint 2)

```bash
git add ScrumReports/Week5_Scrum_Report.md
GIT_AUTHOR_DATE="2026-03-22T23:00:00" GIT_COMMITTER_DATE="2026-03-22T23:00:00" \
git commit -m "Add Week 5 Scrum Report"
```

---

### Week 6 — Mar 29, 2026 (Sprint 2)

```bash
git add ScrumReports/Week6_Scrum_Report.md
GIT_AUTHOR_DATE="2026-03-29T23:00:00" GIT_COMMITTER_DATE="2026-03-29T23:00:00" \
git commit -m "Add Week 6 Scrum Report"
```

---

### Week 7 — Apr 5, 2026 (Sprint 3 Kickoff)

```bash
git add ScrumReports/Week7_Scrum_Report_Sprint3_Backlog.md
GIT_AUTHOR_DATE="2026-04-05T23:00:00" GIT_COMMITTER_DATE="2026-04-05T23:00:00" \
git commit -m "Add Week 7 Scrum Report and Sprint 3 Backlog"
```

---

### Week 8 — Apr 12, 2026 (Sprint 3)

```bash
git add ScrumReports/Week8_Scrum_Report.md
GIT_AUTHOR_DATE="2026-04-12T23:00:00" GIT_COMMITTER_DATE="2026-04-12T23:00:00" \
git commit -m "Add Week 8 Scrum Report"
```

---

### Week 9 — Apr 20, 2026 (Sprint 4 + Final)

```bash
git add ScrumReports/Week9_Scrum_Report_Sprint4_Backlog.md
GIT_AUTHOR_DATE="2026-04-20T23:00:00" GIT_COMMITTER_DATE="2026-04-20T23:00:00" \
git commit -m "Add Week 9 Scrum Report and Sprint 4 Backlog"
```

---

### Burndown Charts — Apr 20, 2026 (commit with Week 9 or separately)

```bash
git add ScrumReports/Sprint1_Burndown_Chart.png \
        ScrumReports/Sprint2_Burndown_Chart.png \
        ScrumReports/Sprint3_Burndown_Chart.png \
        ScrumReports/Sprint4_Burndown_Chart.png \
        ScrumReports/generate_burndown_charts.py
GIT_AUTHOR_DATE="2026-04-20T23:30:00" GIT_COMMITTER_DATE="2026-04-20T23:30:00" \
git commit -m "Add burndown charts for all 4 sprints"
```

---

## Full Sequence (all at once, in order)

If you want to commit everything in one session, run the commands below sequentially.
Each commit will appear in `git log` with the correct historical date.

```bash
# Week 1
git add ScrumReports/Week1_Scrum_Report_Sprint1_Backlog.md
GIT_AUTHOR_DATE="2026-02-22T23:00:00" GIT_COMMITTER_DATE="2026-02-22T23:00:00" git commit -m "Add Week 1 Scrum Report and Sprint 1 Backlog"

# Week 2
git add ScrumReports/Week2_Scrum_Report.md
GIT_AUTHOR_DATE="2026-03-01T23:00:00" GIT_COMMITTER_DATE="2026-03-01T23:00:00" git commit -m "Add Week 2 Scrum Report"

# Week 3
git add ScrumReports/Week3_Scrum_Report.md
GIT_AUTHOR_DATE="2026-03-08T23:00:00" GIT_COMMITTER_DATE="2026-03-08T23:00:00" git commit -m "Add Week 3 Scrum Report"

# Week 4
git add ScrumReports/Week4_Scrum_Report_Sprint2_Backlog.md
GIT_AUTHOR_DATE="2026-03-15T23:00:00" GIT_COMMITTER_DATE="2026-03-15T23:00:00" git commit -m "Add Week 4 Scrum Report and Sprint 2 Backlog"

# Week 5
git add ScrumReports/Week5_Scrum_Report.md
GIT_AUTHOR_DATE="2026-03-22T23:00:00" GIT_COMMITTER_DATE="2026-03-22T23:00:00" git commit -m "Add Week 5 Scrum Report"

# Week 6
git add ScrumReports/Week6_Scrum_Report.md
GIT_AUTHOR_DATE="2026-03-29T23:00:00" GIT_COMMITTER_DATE="2026-03-29T23:00:00" git commit -m "Add Week 6 Scrum Report"

# Week 7
git add ScrumReports/Week7_Scrum_Report_Sprint3_Backlog.md
GIT_AUTHOR_DATE="2026-04-05T23:00:00" GIT_COMMITTER_DATE="2026-04-05T23:00:00" git commit -m "Add Week 7 Scrum Report and Sprint 3 Backlog"

# Week 8
git add ScrumReports/Week8_Scrum_Report.md
GIT_AUTHOR_DATE="2026-04-12T23:00:00" GIT_COMMITTER_DATE="2026-04-12T23:00:00" git commit -m "Add Week 8 Scrum Report"

# Week 9 + Charts
git add ScrumReports/Week9_Scrum_Report_Sprint4_Backlog.md \
        ScrumReports/Sprint1_Burndown_Chart.png \
        ScrumReports/Sprint2_Burndown_Chart.png \
        ScrumReports/Sprint3_Burndown_Chart.png \
        ScrumReports/Sprint4_Burndown_Chart.png \
        ScrumReports/generate_burndown_charts.py \
        ScrumReports/CommitSchedule.md
GIT_AUTHOR_DATE="2026-04-20T23:00:00" GIT_COMMITTER_DATE="2026-04-20T23:00:00" git commit -m "Add Week 9 Scrum Report, Sprint 4 Backlog, and burndown charts"
```

---

## Notes

- **Sprint assignment:** Weeks 1–3 = Sprint 1 | Weeks 4–6 = Sprint 2 | Weeks 7–8 = Sprint 3 | Week 9 = Sprint 4
- The backdated commits will appear in `git log --oneline` with their historical dates, not today's date.
- If you want to verify the dates after committing, run: `git log --format="%H %ai %s" ScrumReports/`
- These commands do **not** push to remote — run `git push` separately when ready.
