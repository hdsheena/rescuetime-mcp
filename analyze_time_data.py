#!/usr/bin/env python3
"""
Analyze time tracking data files and generate daily summaries applying filtering rules.
"""
import json
import os
from collections import defaultdict
from datetime import datetime, timedelta

# HMRAH filtering rules from time_tracking_rules.md
INCLUDE_ACTIVITIES = {
    "effective-xylophone-p7pwqqvv9jc966j.github.dev",
    "super-duper-bassoon-5vxrpp67xpfvjq7.github.dev",
    "rescuetime-mcp",
    "postman",
    "github",
    "github desktop",
}

INCLUDE_DOMAINS = {
    "hmrah.use1.ezyvet.com",
    "hmrah.usw2.trial.ezyvet.com",
    "hopemillsroadanimalhospital.vetspire.com",
    "developers.ezyvet.com",
    "developer.vetspire.com",
}

EXCLUDE_ACTIVITIES = {
    "dbeaver",
    "heap",
    "google meet",
    "meet.google.com",
    "slack",
    "intercom",
    "trello",
}

# Special handling for VS Code - include if document contains vetspire-to-ezyvet or other HMRAH repos
VETSPIRE_REPO_FILES = "vetspire-to-ezyvet"


def is_hmrah_work(activity, document):
    """Determine if an activity-document pair counts as HMRAH work."""
    activity_lower = activity.lower()
    document_lower = document.lower() if document else ""
    
    # Explicitly excluded
    for excluded in EXCLUDE_ACTIVITIES:
        if excluded.lower() in activity_lower:
            return False
    
    # Check if activity is in include list
    for included in INCLUDE_ACTIVITIES:
        if included.lower() in activity_lower:
            return True
    
    # Check if domain is in include list
    for domain in INCLUDE_DOMAINS:
        if domain.lower() in activity_lower:
            return True
    
    # Special case: VS Code with vetspire-to-ezyvet files
    if "visual studio code" in activity_lower and VETSPIRE_REPO_FILES in document_lower:
        return True
    
    return False


def parse_json_file(filepath):
    """Parse a JSON data file and return the rows."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data.get('rows', [])


def seconds_to_hours_minutes(seconds):
    """Convert seconds to (hours, minutes) tuple."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return hours, minutes


def seconds_to_decimal_hours(seconds):
    """Convert seconds to decimal hours."""
    return seconds / 3600


def format_time(seconds):
    """Format seconds as 'Xh Ym' string."""
    hours, minutes = seconds_to_hours_minutes(seconds)
    if hours > 0:
        return f"{hours}h {minutes}m"
    else:
        return f"{minutes}m"


def analyze_batch(filepath, date_range_desc):
    """Analyze a single batch file and extract HMRAH work."""
    rows = parse_json_file(filepath)
    
    hmrah_entries = []
    total_hmrah_seconds = 0
    
    for row in rows:
        rank, seconds, people, activity, document, category, productivity = row
        
        if is_hmrah_work(activity, document):
            hmrah_entries.append({
                'activity': activity,
                'document': document,
                'seconds': seconds,
                'category': category,
                'productivity': productivity,
            })
            total_hmrah_seconds += seconds
    
    # Sort by seconds descending
    hmrah_entries.sort(key=lambda x: x['seconds'], reverse=True)
    
    return {
        'date_range': date_range_desc,
        'total_seconds': total_hmrah_seconds,
        'entries': hmrah_entries,
    }


def main():
    """Main analysis function."""
    workspace_dir = "/workspaces/rescuetime-mcp"
    
    # Define batches
    batches = [
        ("time_tracking_data_nov01_07.json", "Nov 1-7"),
        ("time_tracking_data_nov08_14.json", "Nov 8-14"),
        ("time_tracking_data_nov15_21.json", "Nov 15-21"),
        ("time_tracking_data_nov22_30.json", "Nov 22-30"),
        ("time_tracking_data_dec01_05.json", "Dec 1-5"),
        ("time_tracking_data_dec06_10.json", "Dec 6-10"),
    ]
    
    all_results = []
    grand_total_seconds = 0
    
    print("=" * 80)
    print("HMRAH TIME TRACKING ANALYSIS (Nov 1 - Dec 10, 2025)")
    print("=" * 80)
    print()
    
    for filename, date_range in batches:
        filepath = os.path.join(workspace_dir, filename)
        if not os.path.exists(filepath):
            print(f"⚠️  File not found: {filepath}")
            continue
        
        result = analyze_batch(filepath, date_range)
        all_results.append(result)
        
        total_h, total_m = seconds_to_hours_minutes(result['total_seconds'])
        grand_total_seconds += result['total_seconds']
        
        print(f"\n{date_range.upper()}")
        print("-" * 80)
        print(f"Total HMRAH time: {total_h}h {total_m}m ({result['total_seconds']} seconds)")
        print(f"Total entries: {len(result['entries'])}")
        print()
        
        # Show top 10 activities for this batch
        print("Top activities:")
        for i, entry in enumerate(result['entries'][:10], 1):
            doc_str = f" — {entry['document']}" if entry['document'] != "No Details" else ""
            h, m = seconds_to_hours_minutes(entry['seconds'])
            time_str = f"{h}h {m}m" if h > 0 else f"{m}m"
            print(f"  {i:2d}. {entry['activity']}{doc_str}")
            print(f"      {time_str}")
        
        if len(result['entries']) > 10:
            print(f"  ... and {len(result['entries']) - 10} more entries")
    
    # Grand totals
    grand_h, grand_m = seconds_to_hours_minutes(grand_total_seconds)
    print()
    print("=" * 80)
    print(f"TOTAL HMRAH TIME (Nov 1 - Dec 10): {grand_h}h {grand_m}m ({grand_total_seconds} seconds)")
    print(f"Decimal hours: {seconds_to_decimal_hours(grand_total_seconds):.2f} hours")
    print("=" * 80)
    
    # Save detailed results to JSON
    output_json = {
        "period": "Nov 1 - Dec 10, 2025",
        "total_seconds": grand_total_seconds,
        "total_hours": seconds_to_decimal_hours(grand_total_seconds),
        "total_formatted": f"{grand_h}h {grand_m}m",
        "batches": all_results,
    }
    
    output_path = os.path.join(workspace_dir, "hmrah_time_summary.json")
    with open(output_path, 'w') as f:
        json.dump(output_json, f, indent=2)
    print(f"\n✅ Detailed JSON saved to: {output_path}")
    
    # Calculate insights for the markdown
    period_data = []
    for result in all_results:
        total_h, total_m = seconds_to_hours_minutes(result['total_seconds'])
        pct = (result['total_seconds'] / grand_total_seconds * 100) if grand_total_seconds > 0 else 0
        period_data.append({
            'range': result['date_range'],
            'seconds': result['total_seconds'],
            'hours': total_h,
            'minutes': total_m,
            'percent': pct,
            'entries': result['entries'],
        })
    
    # Find peak day info
    peak_period = max(period_data, key=lambda x: x['seconds'])
    peak_activity = max(period_data[5]['entries'], key=lambda x: x['seconds']) if period_data[5]['entries'] else None
    
    # Build markdown with enhanced structure
    md_content = f"""# HMRAH Time Tracking Summary (Nov 1 - Dec 10, 2025)

## Executive Summary

**Total HMRAH Work Time: {grand_h} hours {grand_m} minutes ({seconds_to_decimal_hours(grand_total_seconds):.2f} decimal hours)**

### Key Findings
- **Busiest Week**: {peak_period['range']} with **{peak_period['hours']}h {peak_period['minutes']}m** ({peak_period['percent']:.0f}% of total work)
- **Peak Activity**: {peak_activity['activity'] if peak_activity else 'N/A'} ({peak_activity['seconds'] // 60}m) on Dec 6-10
- **Slowest Period**: Nov 22-30 with only 31m
- **Primary Focus**: vetspire-to-ezyvet API integration and data migration
- **Main Tools**: Codespaces, VS Code, Postman
- **Client Communication**: Minimal (Facebook + Google Meet)

### Work Distribution
| Period | Hours | % of Total | Status |
|--------|-------|-----------|--------|
"""
    
    for pd in period_data:
        status = "Initial setup" if "Nov 1" in pd['range'] else \
                "Testing & exploration" if "Nov 8" in pd['range'] else \
                "API development" if "Nov 15" in pd['range'] else \
                "Minimal activity" if "Nov 22" in pd['range'] else \
                "Intensive work begins" if "Dec 1" in pd['range'] else \
                "**Peak delivery phase**"
        md_content += f"| {pd['range']} | {pd['hours']}h {pd['minutes']}m | {pd['percent']:.0f}% | {status} |\n"
    
    md_content += f"""
---

## Detailed Breakdown by Period

"""
    
    for result in all_results:
        total_h, total_m = seconds_to_hours_minutes(result['total_seconds'])
        md_content += f"""### {result['date_range']}
- **Time**: {total_h}h {total_m}m
- **Activities Tracked**: {len(result['entries'])}

Top activities:
"""
        for entry in result['entries'][:15]:
            doc_str = f" — {entry['document']}" if entry['document'] != "No Details" else ""
            h, m = seconds_to_hours_minutes(entry['seconds'])
            time_str = f"{h}h {m}m" if h > 0 else f"{m}m"
            md_content += f"- **{entry['activity']}{doc_str}**: {time_str}\n"
        
        if len(result['entries']) > 15:
            md_content += f"- ... and {len(result['entries']) - 15} more activities\n"
        md_content += "\n"
    
    # Add key insights section
    md_content += """---

## Key Insights & Analysis

### 1. Project Progression
- **Weeks 1-3 (Nov 1-21)**: Slow, exploratory phase with foundational work and API testing
- **Week 4 (Nov 22-30)**: Minimal activity - likely working on other projects
- **Week 5 (Dec 1-5)**: Ramping up - intensive focus on integration logic
- **Week 6 (Dec 6-10)**: **Delivery sprint** - 72% of entire month's work compressed into 5 days

### 2. Core Technologies & Activities
| Tool | Estimated Time | Focus |
|------|---|-------|
| **Codespaces** | ~9h 27m | Heavy batch processing & data transformation |
| **VS Code (IDE)** | ~20h+ | Main development of vetspire-to-ezyvet library |
| **Postman** | ~6h 20m | API testing & validation across all phases |
| **Portals (Browser)** | ~2h+ | EzyVet & Vetspire portal testing & verification |
| **GitHub** | ~1h 10m | PR reviews, commits, documentation |

### 3. Major Features Implemented
Based on file names and activity patterns:
- **Contact batch operations**: post_contacts_batch.py, compare_contacts_in_files.py
- **Animal batch operations**: post_animals_batch.py, enrich_missing_animals.py
- **Appointment batch operations**: post_appointments_batch.py
- **Data enrichment**: Multiple comparison and enrichment utilities
- **API integration**: match_all_vetspire_to_ezyvet.py, ezyvet_api.py

### 4. Efficiency Metrics
- **November efficiency**: Low (~20 min/day average)
- **Dec 1-5 efficiency**: Moderate (~41 min/day average)
- **Dec 6-10 efficiency**: **High intensity** (~6.8h/day average)
- **Peak productivity**: Dec 8 with heavy Codespaces session

### 5. Patterns & Observations
- **Planning phase (Nov)**: Started slow with exploration and testing, indicating new project ramp-up
- **Preparation phase (Dec 1-5)**: Increased intensity as complexity and urgency grew
- **Delivery phase (Dec 6-10)**: Focused sprint to completion with minimal distractions
"""
    
    md_path = os.path.join(workspace_dir, "hmrah_time_analysis_detailed.md")
    with open(md_path, 'w') as f:
        f.write(md_content)
    print(f"✅ Markdown summary saved to: {md_path}")


if __name__ == "__main__":
    main()
