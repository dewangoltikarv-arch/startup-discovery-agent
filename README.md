# Startup Discovery Agent

An open-source tool to discover emerging Japanese and South Korean startups that are expanding to global markets. **Completely free to run** using public APIs and web scraping.

## Features

- 🌍 Discovers startups from Japan and South Korea with global market focus
- 📊 Aggregates data from multiple free sources
- 🤖 Agent-friendly JSON output
- ⚡ Runs on GitHub Actions (completely free)
- 💰 Zero cost - uses only free APIs and public data
- 🔄 Scheduled or on-demand execution

## Supported Data Sources

- **Open Unicorn API** - Global startup database
- **OpenCorporates API** - Company registration data
- **GitHub Trending** - Open source startups
- **Web Scraping** - Public startup directories (Japan/Korea)

## Quick Start

### Local Installation

```bash
git clone https://github.com/dewangoltikarv-arch/startup-discovery-agent.git
cd startup-discovery-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Discovery

```bash
python discover_startups.py \
  --country japan,south_korea \
  --industry ai,saas,fintech \
  --limit 20 \
  --market-focus global
```

### Docker

```bash
docker build -t startup-discovery .
docker run startup-discovery --country japan,south_korea --limit 20
```

## Usage with Your Agent

### Get JSON Output

```bash
python discover_startups.py --output json --country japan,south_korea --limit 20
```

### Example Output

```json
{
  "startups": [
    {
      "name": "Company Name",
      "country": "Japan",
      "industry": "AI/ML",
      "funding_stage": "Series A",
      "founded_year": 2021,
      "global_focus": true,
      "description": "...",
      "data_source": "open_unicorn"
    }
  ],
  "total_found": 20,
  "timestamp": "2026-09-11T10:30:00Z"
}
```

## Configuration

Edit `config.yaml` to customize:

```yaml
countries:
  - japan
  - south_korea

industries:
  - ai
  - saas
  - fintech
  - biotech
  - blockchain

funding_stages:
  - seed
  - series_a
  - series_b
  - series_c

market_focus: global
results_limit: 20
```

## GitHub Actions (Automated)

Set up automated discovery runs via GitHub Actions:

1. Go to `.github/workflows/discover-startups.yml`
2. Configure schedule (runs weekly by default)
3. Results are saved to `results/startups_{timestamp}.json`
4. Check "Actions" tab in your repo to see run history

## API Reference

### discover_startups.py

```python
from startup_discovery import StartupDiscovery

discovery = StartupDiscovery(
    countries=['japan', 'south_korea'],
    industries=['ai', 'saas'],
    limit=20
)

startups = discovery.find()
print(startups)
```

## Free Tier Limits

| Source | Rate Limit | Cost |
|--------|-----------|------|
| Open Unicorn API | Unlimited | Free |
| OpenCorporates | 50 req/sec | Free |
| GitHub API | 60 req/hour (unauthenticated) | Free |
| Web Scraping | Respectful rate limiting | Free |

**Total Monthly Cost: $0** ✅

## Limitations

- Data freshness depends on source updates
- Web scraping may break if websites change
- Rate limits apply to some APIs (respectfully implemented)
- No guaranteed 100% accuracy (as with all startup databases)

## Contributing

Contributions welcome! Areas to improve:
- Add more data sources
- Improve filtering criteria
- Better data normalization
- Additional country support

## License

MIT License - See LICENSE file

## Support

Issues? Questions? Open a GitHub issue or discussion.

---

**Cost: $0 | Setup Time: 5 minutes | Data Freshness: Real-time or scheduled**
