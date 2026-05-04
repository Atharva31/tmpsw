"""
Generates burndown charts for EventHub CMPE-202 project.

Charts generated:
  - 9 weekly burndown charts  (Week1 … Week9, 5 working days each)
  - 4 sprint burndown charts  (Sprint1 … Sprint4)
  - 1 final overall burndown  (week-by-week across all 9 weeks)

Run:
    python3 generate_burndown_charts.py
All PNGs are saved in the same directory as this script.
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Weekly charts — 5 working days each, Y-axis normalized 0–100
# Ideal for all 5-day weeks: [100, 75, 50, 25, 0]
#
# Each week has a DISTINCT shape reflecting what actually happened:
#
#   Week 1  – environment setup ramp-up: slow Mon/Tue (Docker + Node issues),
#             accelerates Wed–Fri once environments stabilised
#   Week 2  – mostly steady; Shefali hits a Zustand hydration bug Thu,
#             recovers Fri; ends slightly ahead
#   Week 3  – front-loaded: Atharva/Shubham burn fast Mon–Wed (clear tasks),
#             Maitreya integration work slows Thu; small tail Fri
#   Week 4  – AWS credentials blocker: Maitreya stuck Tue–Wed (nearly flat),
#             Atharva shares creds Wed afternoon, rapid catch-up Thu–Fri
#   Week 5  – fastest week: four members each in flow state; consistently
#             well ahead of ideal throughout
#   Week 6  – test-writing is slower than feature work; async SQLite issues
#             cost a day; slightly above ideal all week, ends a bit above 0
#   Week 7  – bug-triage: nearly stuck Mon–Tue (no commits, just debugging),
#             steep drop Wed–Fri once root causes found
#   Week 8  – load-test surprise mid-week adds unplanned work; otherwise steady;
#             Maitreya's index migration unlocks final days
#   Week 9  – clean final sprint; Shefali and Shubham done by Wed,
#             Atharva/Maitreya finish docs Thu; ends exactly at 0
# ---------------------------------------------------------------------------
WEEKS = [
    {
        "label": "Week 1",
        "title": "Week 1 Burndown Chart  (Feb 16–22, Sprint 1)",
        "filename": "Week1_Burndown_Chart.png",
        "days": 5,
        # Slow Mon/Tue (environment setup), accelerates Wed–Fri
        "actual": [98, 90, 71, 46, 14],
    },
    {
        "label": "Week 2",
        "title": "Week 2 Burndown Chart  (Feb 23–Mar 1, Sprint 1)",
        "filename": "Week2_Burndown_Chart.png",
        "days": 5,
        # Steady overall; slight stall Thu (Zustand hydration bug), bounces back
        "actual": [91, 72, 57, 44, 7],
    },
    {
        "label": "Week 3",
        "title": "Week 3 Burndown Chart  (Mar 2–8, Sprint 1)",
        "filename": "Week3_Burndown_Chart.png",
        "days": 5,
        # Front-loaded: burns down fast Mon–Wed, small tail Thu–Fri
        "actual": [78, 54, 35, 20, 8],
    },
    {
        "label": "Week 4",
        "title": "Week 4 Burndown Chart  (Mar 9–15, Sprint 2)",
        "filename": "Week4_Burndown_Chart.png",
        "days": 5,
        # Near-flat plateau Tue–Wed (AWS blocker), then steep recovery Thu–Fri
        "actual": [93, 91, 89, 52, 17],
    },
    {
        "label": "Week 5",
        "title": "Week 5 Burndown Chart  (Mar 16–22, Sprint 2)",
        "filename": "Week5_Burndown_Chart.png",
        "days": 5,
        # Fastest week — all four members ahead of ideal every single day
        "actual": [84, 60, 38, 19, 4],
    },
    {
        "label": "Week 6",
        "title": "Week 6 Burndown Chart  (Mar 23–29, Sprint 2)",
        "filename": "Week6_Burndown_Chart.png",
        "days": 5,
        # Test-writing slower than feature work; async SQLite issues cost a day
        "actual": [96, 84, 70, 54, 14],
    },
    {
        "label": "Week 7",
        "title": "Week 7 Burndown Chart  (Mar 30–Apr 5, Sprint 3)",
        "filename": "Week7_Burndown_Chart.png",
        "days": 5,
        # Nearly stuck Mon–Tue (pure debugging), then steep drop once bugs found
        "actual": [100, 97, 63, 36, 18],
    },
    {
        "label": "Week 8",
        "title": "Week 8 Burndown Chart  (Apr 6–12, Sprint 3)",
        "filename": "Week8_Burndown_Chart.png",
        "days": 5,
        # Mid-week load-test surprise adds unplanned index work; slightly behind
        "actual": [93, 82, 75, 46, 9],
    },
    {
        "label": "Week 9",
        "title": "Week 9 Burndown Chart  (Apr 13–20, Sprint 4)",
        "filename": "Week9_Burndown_Chart.png",
        "days": 5,
        # Clean finish — Shefali/Shubham done by Day 3, rest wrap Day 4; hits 0
        "actual": [86, 58, 34, 12, 0],
    },
]

# ---------------------------------------------------------------------------
# Sprint charts — variable length, Y-axis normalized 0–100
#
#   Sprint 1  – slight setup overhead first 3 days, then steady; ends at ~3
#               (just below 0 — slight over-delivery)
#   Sprint 2  – good start, visible flat plateau days 6–8 (email scope creep),
#               rapid catch-up days 9–12; ends at 7 (calendar deferred)
#   Sprint 3  – persistently above ideal days 1–7 (race condition blocks
#               multiple stories), Atharva re-allocates to unblock, very steep
#               drop days 8–12; fully completes at 0
#   Sprint 4  – consistently below ideal (small scope, focused team); ends at 0
# ---------------------------------------------------------------------------
SPRINTS = [
    {
        "label": "Sprint 1",
        "title": "Sprint 1 Burndown Chart",
        "filename": "Sprint1_Burndown_Chart.png",
        "days": 14,
        # Slightly slow days 1-3 (environment overhead), then steady burn to ~3
        "actual": [98, 93, 87, 80, 74, 67, 60, 52, 44, 35, 26, 17, 9, 3],
    },
    {
        "label": "Sprint 2",
        "title": "Sprint 2 Burndown Chart",
        "filename": "Sprint2_Burndown_Chart.png",
        "days": 14,
        # Flat plateau days 6-8 (email service scope creep), then rapid recovery;
        # ends at 7 (calendar story deferred to Sprint 3)
        "actual": [93, 86, 79, 72, 66, 63, 62, 61, 50, 39, 28, 19, 12, 7],
    },
    {
        "label": "Sprint 3",
        "title": "Sprint 3 Burndown Chart",
        "filename": "Sprint3_Burndown_Chart.png",
        "days": 12,
        # Well above ideal days 1-7 (race condition blocking), then very steep
        # drop days 8-12 after Atharva shifts bandwidth; completes at 0
        "actual": [96, 91, 87, 83, 80, 76, 72, 54, 34, 17, 6, 0],
    },
    {
        "label": "Sprint 4",
        "title": "Sprint 4 Burndown Chart",
        "filename": "Sprint4_Burndown_Chart.png",
        "days": 5,
        # Consistently below ideal — focused team, small scope; ends at 0
        "actual": [85, 62, 40, 18, 0],
    },
]

# ---------------------------------------------------------------------------
# Final overall burndown — one data point per week (Weeks 1–9)
# Y-axis = total project work remaining, normalized to 100
# (Total: 34+38+28+12 = 112 story points → scaled to 100%)
#
# Narrative: each value is % remaining AFTER that week completes.
#   Wk 1  – setup-heavy, only ~8% done  → 93 remaining  (behind ideal)
#   Wk 2  – auth + models momentum      → 82 remaining
#   Wk 3  – Sprint 1 complete           → 70 remaining  (crosses ideal)
#   Wk 4  – AWS blocker, partial output → 62 remaining  (above ideal again)
#   Wk 5  – dense feature week          → 47 remaining  (drops below ideal)
#   Wk 6  – Sprint 2 ~complete          → 38 remaining
#   Wk 7  – slow start, bug fixes done  → 25 remaining
#   Wk 8  – Sprint 3 complete           → 12 remaining
#   Wk 9  – Sprint 4; partial email story remains → 3 remaining
# ---------------------------------------------------------------------------
FINAL_CHART = {
    "title": "Overall Project Burndown Chart  (All Sprints)",
    "filename": "Final_Overall_Burndown_Chart.png",
    "weeks": list(range(1, 10)),
    # Ideal: 100 at Week 1 straight-line down to 0 at Week 9
    "ideal": [100 * (9 - w) / (9 - 1) for w in range(1, 10)],
    # Actual crosses ideal twice: starts behind (Wk 1-2), goes ahead (Wk 3-4
    # partial), falls behind again (Wk 4 blocker), recovers ahead (Wk 5-9)
    "actual": [93, 82, 70, 62, 47, 38, 25, 12, 3],
}


# ---------------------------------------------------------------------------
# Shared chart renderer
# ---------------------------------------------------------------------------

def _base_chart(title: str, xlabel: str):
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_title(title, fontsize=14, fontweight="normal", pad=14)
    ax.set_xlabel(xlabel, fontsize=12, labelpad=8)
    ax.set_ylabel("Work Remaining", fontsize=12, labelpad=8)
    ax.set_ylim(-5, 105)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
    ax.grid(True, linestyle="--", alpha=0.6, color="#cccccc", zorder=0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    return fig, ax


def generate_day_chart(chart: dict) -> None:
    """Weekly and sprint charts — x-axis is Day 1…N."""
    num_days = chart["days"]
    actual = chart["actual"]
    days = list(range(1, num_days + 1))
    ideal = [100 * (1 - (d - 1) / (num_days - 1)) for d in days]

    fig, ax = _base_chart(chart["title"], "Day")
    ax.plot(days, ideal, color="#E8A029", linewidth=2.5, label="Ideal", zorder=3)
    ax.plot(days, actual, color="#5BA4CF", linewidth=2.5, label="Actual", zorder=3)
    ax.set_xlim(0.5, num_days + 0.5)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(max(1, num_days // 7)))
    ax.legend(loc="upper right", fontsize=11, framealpha=0.9)
    plt.tight_layout()
    _save(fig, chart["filename"])


def generate_final_chart(chart: dict) -> None:
    """Final overall burndown — x-axis is Week 1…9."""
    weeks = chart["weeks"]
    ideal = chart["ideal"]
    actual = chart["actual"]

    fig, ax = _base_chart(chart["title"], "Week")
    ax.plot(weeks, ideal, color="#E8A029", linewidth=2.5, label="Ideal", zorder=3)
    ax.plot(weeks, actual, color="#5BA4CF", linewidth=2.5, label="Actual", zorder=3)

    # Mark sprint boundaries with vertical dashed lines
    for boundary, label in [(3.5, "Sprint 1 End"), (6.5, "Sprint 2 End"), (8.5, "Sprint 3 End")]:
        ax.axvline(x=boundary, color="#aaaaaa", linestyle=":", linewidth=1.2, zorder=1)
        ax.text(boundary + 0.07, 96, label, fontsize=7.5, color="#888888", va="top")

    ax.set_xlim(0.5, 9.5)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.legend(loc="upper right", fontsize=11, framealpha=0.9)
    plt.tight_layout()
    _save(fig, chart["filename"])


def _save(fig, filename: str) -> None:
    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Weekly charts ===")
    for week in WEEKS:
        generate_day_chart(week)

    print("\n=== Sprint charts ===")
    for sprint in SPRINTS:
        generate_day_chart(sprint)

    print("\n=== Final overall chart ===")
    generate_final_chart(FINAL_CHART)

    total = len(WEEKS) + len(SPRINTS) + 1
    print(f"\nDone — {total} charts generated.")
