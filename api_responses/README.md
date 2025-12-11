# RescueTime API Response Cache

This directory contains saved API responses to avoid re-requesting the same data.

## Stored Responses

### November 2025 Hourly Data
- **november_6_7_hourly_data.json**: Hour-by-hour activity breakdown for Nov 6-7
  - 476 rows of data
  - Shows Nov 7 @ 9:00 AM breakthrough: First production portal access (529s)
  
- **november_21_hourly_data.json**: Hour-by-hour activity breakdown for Nov 21
  - 191 rows of data
  - Shows afternoon integration work session (14:00 hour)

### November-December 2025 Daily Data
- **nov1_dec10_daily_data.json**: (TO BE CREATED) Daily resolution data for Nov 1 - Dec 10
  - 2,666 rows of daily activity totals
  - Used for initial filtering and tier-based analysis

## Data Structure

Each JSON file contains:
- `query_parameters`: The exact parameters used for the API call
- `date_retrieved`: When the data was fetched
- `description`: What the data represents
- `row_count`: Number of data rows returned
- `key_findings`: High-level summary of important HMRAH activities found
- `data`: The actual API response (or note if stored separately)

## Note on Raw Data

The actual raw API responses are very large (476+ rows per file). The JSON files above contain:
1. Metadata about the query
2. Key findings/summaries
3. Reference note that raw data was analyzed

To re-fetch any data, use the `query_parameters` stored in each file.

## Usage

When analyzing HMRAH time:
1. Check if data exists here first
2. Load the relevant JSON file
3. Review `key_findings` for summary
4. Only re-fetch if date range changes or new analysis needed

## Data Retention

These cached responses are valid as long as:
- The date range is in the past (completed days)
- No corrections were made to RescueTime tracking
- API key remains the same
