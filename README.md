<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-blueviolet?style=for-the-badge&logo=openai&logoColor=white" alt="AI Powered"/>
  <img src="https://img.shields.io/badge/100%25-Free-brightgreen?style=for-the-badge" alt="100% Free"/>
  <img src="https://img.shields.io/badge/No%20Signup-Required-orange?style=for-the-badge" alt="No Signup Required"/>
  <img src="https://img.shields.io/badge/7%20Tools-Live-blue?style=for-the-badge" alt="7 Tools Live"/>
</p>

<h1 align="center">Free AI Tools Suite</h1>

<p align="center">
  <strong>7 free AI-powered web tools, all running on n8n webhooks with GPT-4o-mini. No login required.</strong>
</p>

<p align="center">
  Built by a 17-year-old developer during a 24-hour challenge.
</p>

<p align="center">
  <a href="https://crazeemedia.app.n8n.cloud/webhook/ai-tools"><img src="https://img.shields.io/badge/TRY%20IT%20NOW-Launch%20Tools%20Hub-blue?style=for-the-badge&logo=rocket&logoColor=white" alt="Launch Tools Hub"/></a>
</p>

---

## What Is This?

A collection of **7 free AI-powered tools** that you can use right now in your browser. No accounts, no API keys, no limits. Just paste your input and get professional AI-generated output in seconds.

Each tool has:
- A **beautiful landing page** (dark theme, responsive, mobile-friendly)
- A **REST API** you can call programmatically
- An **n8n workflow template** you can import into your own instance

---

## The Tools

| # | Tool | Description | Try It |
|---|------|-------------|--------|
| 1 | **AI Email Writer** | Generate professional emails in any tone | [Launch](https://crazeemedia.app.n8n.cloud/webhook/email-writer) |
| 2 | **AI LinkedIn Post Generator** | Create engaging LinkedIn content with hooks and hashtags | [Launch](https://crazeemedia.app.n8n.cloud/webhook/linkedin-writer) |
| 3 | **AI Code Reviewer** | Get detailed, senior-level code reviews with ratings | [Launch](https://crazeemedia.app.n8n.cloud/webhook/code-review) |
| 4 | **Roast My Code** | Get your code hilariously roasted (but learn real tips) | [Launch](https://crazeemedia.app.n8n.cloud/webhook/roast-my-code) |
| 5 | **Roast My Website** | Enter any URL for a hilarious design and UX roast | [Launch](https://crazeemedia.app.n8n.cloud/webhook/roast-my-website) |
| 6 | **AI Regex Generator** | Describe what to match in plain English, get working regex | [Launch](https://crazeemedia.app.n8n.cloud/webhook/regex-generator) |
| 7 | **AI Tools Hub** | Central directory page linking to all tools | [Launch](https://crazeemedia.app.n8n.cloud/webhook/ai-tools) |

---

## Tool Details

### 1. AI Email Writer
> Turn rough ideas into polished, professional emails in seconds.

**[Launch Email Writer](https://crazeemedia.app.n8n.cloud/webhook/email-writer)**

- 8 email types: follow-up, cold outreach, thank you, apology, introduction, request, announcement, and more
- 6 tones: professional, casual, friendly, formal, persuasive, empathetic
- Optional recipient field for personalization
- Saves 10+ minutes per email

**Example:** *"Tell my professor I need an extension on my paper because I was sick"* --> Gets you a polished, respectful email ready to send.

---

### 2. AI LinkedIn Post Generator
> Create scroll-stopping LinkedIn posts that actually get impressions.

**[Launch LinkedIn Post Generator](https://crazeemedia.app.n8n.cloud/webhook/linkedin-writer)**

- 5 tone options: professional, storytelling, thought leadership, casual, inspirational
- 3 length options: short, medium, long
- Auto-generates hooks, CTAs, formatting, and hashtags
- Great for founders, job seekers, and anyone building their personal brand

**Example:** *"I just launched my first SaaS product after 6 months of building"* --> Gets you a viral-worthy LinkedIn post.

---

### 3. AI Code Reviewer
> Get instant, senior-engineer-level code reviews powered by AI.

**[Launch Code Reviewer](https://crazeemedia.app.n8n.cloud/webhook/code-review)**

- Supports 16+ programming languages (Python, JavaScript, TypeScript, Go, Rust, Java, C++, and more)
- Structured feedback: Critical Issues, Warnings, Suggestions, Improved Code, Key Takeaways
- Identifies security issues, anti-patterns, and optimization opportunities
- Like having a senior developer review your PRs 24/7

---

### 4. Roast My Code
> Learn from your mistakes -- with laughs.

**[Launch Code Roast](https://crazeemedia.app.n8n.cloud/webhook/roast-my-code)**

- Paste any code and get a savage, funny, but educational roast
- Sections: First Impressions, The Good, The Bad, The Ugly, Roast Score (0-10)
- Actually helpful -- real feedback disguised as comedy
- Supports 15+ programming languages

**Example:** Paste a basic function --> *"Ah yes, the classic add function -- the culinary equivalent of boiling water and calling yourself a chef."*

---

### 5. Roast My Website
> Your website called. It wants a redesign.

**[Launch Website Roast](https://crazeemedia.app.n8n.cloud/webhook/roast-my-website)**

- Enter any URL and get a hilarious design and UX roast
- AI visits your site, analyzes the design, layout, typography, and UX
- Covers: layout, color scheme, accessibility, mobile responsiveness
- Brutally honest but genuinely useful feedback
- Great for getting a fresh perspective on your site's design

---

### 6. AI Regex Generator
> Stop Googling regex. Just describe what you want to match.

**[Launch Regex Generator](https://crazeemedia.app.n8n.cloud/webhook/regex-generator)**

- Describe your pattern in plain English (e.g., "match email addresses" or "extract phone numbers")
- Get a working regex pattern with detailed explanation
- Includes test examples showing what matches and what doesn't
- Supports common regex flavors (JavaScript, Python, PCRE)
- Never write regex from scratch again

---

## How It Works

Each tool follows the same architecture pattern using [n8n](https://n8n.io) workflow automation:

```
                    Landing Page Workflow
                    +------------------+
User Browser  --->  | Webhook (GET)    |  ---> Returns HTML page
                    +------------------+

                    When user submits form:

                    API Workflow
                    +------------------+     +---------------------+
Form POST     --->  | Webhook (POST)   | --> | AI Agent + OpenAI   |
                    +------------------+     +---------------------+
                                                      |
                    +------------------+     +------------------+
              <---  | Respond Webhook  | <-- | Format Response  |
                    +------------------+     +------------------+
```

**Key details:**
- All tools use **GPT-4o-mini** via n8n's built-in OpenAI integration
- Landing pages are server-rendered HTML returned by webhook GET requests
- API endpoints accept POST requests and return JSON or HTML responses
- No external hosting needed -- everything runs on n8n Cloud
- Each tool is a pair of workflows: one for the landing page, one for the API

---

## API Reference

All API endpoints accept `POST` requests with form data or JSON body. No authentication required.

### AI Email Writer API
**Endpoint:** `https://crazeemedia.app.n8n.cloud/webhook/ai-email-api`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `context` | string | Yes | What the email should say |
| `tone` | string | No | `professional`, `casual`, `friendly`, `formal`, `persuasive`, `empathetic` (default: `professional`) |
| `emailType` | string | No | `follow-up`, `cold-outreach`, `thank-you`, `apology`, `introduction`, `request`, `announcement` |
| `recipient` | string | No | Who the email is addressed to |

```bash
curl -X POST https://crazeemedia.app.n8n.cloud/webhook/ai-email-api \
  -d "context=Follow up on job interview at Google last week" \
  -d "tone=professional" \
  -d "emailType=follow-up"
```

---

### AI LinkedIn Post Generator API
**Endpoint:** `https://crazeemedia.app.n8n.cloud/webhook/linkedin-api`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `topic` | string | Yes | What the post should be about |
| `tone` | string | No | `professional`, `storytelling`, `thought-leadership`, `casual`, `inspirational` |
| `length` | string | No | `short`, `medium`, `long` |

```bash
curl -X POST https://crazeemedia.app.n8n.cloud/webhook/linkedin-api \
  -d "topic=Why remote work is the future of tech" \
  -d "tone=thought-leadership" \
  -d "length=medium"
```

---

### AI Code Reviewer API
**Endpoint:** `https://crazeemedia.app.n8n.cloud/webhook/code-review-api`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | The source code to review |
| `language` | string | No | Programming language (default: auto-detect) |

```bash
curl -X POST https://crazeemedia.app.n8n.cloud/webhook/code-review-api \
  -H "Content-Type: application/json" \
  -d '{"code": "def fib(n):\n  if n <= 1: return n\n  return fib(n-1) + fib(n-2)", "language": "python"}'
```

---

### Roast My Code API
**Endpoint:** `https://crazeemedia.app.n8n.cloud/webhook/roast-code-api`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `code` | string | Yes | The source code to roast |
| `language` | string | No | Programming language (default: auto-detect) |

```bash
curl -X POST https://crazeemedia.app.n8n.cloud/webhook/roast-code-api \
  -d "code=var x = new Array(); for(var i=0;i<10;i++){x.push(i);}" \
  -d "language=javascript"
```

---

### Roast My Website API
**Endpoint:** `https://crazeemedia.app.n8n.cloud/webhook/roast-my-website`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | The URL of the website to roast |

```bash
curl -X POST https://crazeemedia.app.n8n.cloud/webhook/roast-my-website \
  -d "url=https://example.com"
```

---

### AI Regex Generator API
**Endpoint:** `https://crazeemedia.app.n8n.cloud/webhook/regex-generator`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `description` | string | Yes | Plain English description of the pattern to match |

```bash
curl -X POST https://crazeemedia.app.n8n.cloud/webhook/regex-generator \
  -d "description=Match all valid email addresses"
```

---

## Get the n8n Workflow Templates

Want to run these tools on your own n8n instance? All 13 workflow JSON files are included in the [`/workflows`](./workflows) directory.

### What's Included

| # | File | Description |
|---|------|-------------|
| 1 | `ai-email-writer-landing-page.json` | Email Writer web interface |
| 2 | `ai-email-writer-api.json` | Email Writer API backend |
| 3 | `ai-linkedin-post-generator-landing-page.json` | LinkedIn Post Generator web interface |
| 4 | `ai-linkedin-post-generator-api.json` | LinkedIn Post Generator API backend |
| 5 | `ai-code-reviewer-landing-page.json` | Code Reviewer web interface |
| 6 | `ai-code-reviewer-api.json` | Code Reviewer API backend |
| 7 | `roast-my-code-landing-page.json` | Code Roast web interface |
| 8 | `roast-my-code-api.json` | Code Roast API backend |
| 9 | `roast-my-website-landing-page.json` | Website Roast web interface |
| 10 | `roast-my-website-api.json` | Website Roast API backend |
| 11 | `ai-regex-generator-landing-page.json` | Regex Generator web interface |
| 12 | `ai-regex-generator-api.json` | Regex Generator API backend |
| 13 | `ai-tools-hub.json` | Central hub/directory page |

### Quick Start

1. **Import** the workflow JSON files into your n8n instance (Workflows > Import from File)
2. **Connect** your OpenAI API credentials in each API workflow
3. **Update** the API URLs in each landing page workflow to point to your new webhook URLs
4. **Activate** both the API and landing page workflows
5. **Visit** the landing page webhook URL in your browser

> Full setup guide available in the [n8n AI Templates documentation](./workflows/).

---

## Use Programmatically

Python example scripts are available in the [`/examples`](./examples) directory:

```python
import requests

# AI Email Writer
response = requests.post(
    "https://crazeemedia.app.n8n.cloud/webhook/ai-email-api",
    data={
        "context": "Follow up on my internship application",
        "tone": "professional",
        "emailType": "follow-up"
    }
)
print(response.text)

# AI Code Reviewer
response = requests.post(
    "https://crazeemedia.app.n8n.cloud/webhook/code-review-api",
    data={
        "code": "def add(a, b): return a + b",
        "language": "python"
    }
)
print(response.text)

# AI Regex Generator
response = requests.post(
    "https://crazeemedia.app.n8n.cloud/webhook/regex-generator",
    data={"description": "Match US phone numbers in any format"}
)
print(response.text)
```

See the [`/examples`](./examples) directory for complete scripts for each tool.

---

## Get the Premium Templates

Want the full n8n workflow bundle with setup guide?

| Product | Description | Link |
|---------|-------------|------|
| **n8n AI Templates Bundle** | All 13 workflow JSONs + detailed setup guide | [Get on Payhip](https://payhip.com/b/sCTo9) |
| **Prompt Engineering Cheat Sheet** | 50+ tested prompts for developers | [Get on Payhip](https://payhip.com/b/hTs2L) |

Visit the [Payhip Store](https://payhip.com/ArmanisDevTools) for all products.

---

## Why I Built This

I'm Armani, a 17-year-old developer. I built these tools during a 24-hour challenge to create useful things that people can actually use -- for free. Too many AI tools are locked behind paywalls and signups. I wanted to change that.

These tools run on **n8n Cloud** with OpenAI's GPT-4o-mini, so they're fast, reliable, and always available.

---

## Tech Stack

- **Backend:** [n8n Cloud](https://n8n.io) -- workflow automation platform
- **AI Model:** GPT-4o-mini via n8n's built-in OpenAI nodes
- **Frontend:** Server-rendered HTML via n8n webhook responses (dark theme, responsive)
- **Hosting:** n8n Cloud (always on, no cold starts, no external servers)
- **Architecture:** Each tool = 2 workflows (landing page + API), all using the same 4-node pattern

---

## Support This Project

If these tools saved you time or helped you out, consider supporting the project:

### Star This Repo
<a href="https://github.com/acunningham-ship-it/free-ai-tools">
  <img src="https://img.shields.io/github/stars/acunningham-ship-it/free-ai-tools?style=social" alt="GitHub Stars"/>
</a>

### Ko-fi
<a href="https://ko-fi.com/armanidev">
  <img src="https://img.shields.io/badge/Ko--fi-Support%20Armani-ff5e5b?style=for-the-badge&logo=ko-fi&logoColor=white" alt="Ko-fi"/>
</a>

Your support helps me:
- Keep these tools free and running
- Build more useful AI tools
- Cover hosting and API costs
- Keep learning and building as a young developer

---

## Roadmap

- [x] AI Email Writer
- [x] AI LinkedIn Post Generator
- [x] AI Code Reviewer
- [x] Roast My Code
- [x] Roast My Website
- [x] AI Regex Generator
- [x] AI Tools Hub (central directory)
- [ ] AI Resume Bullet Point Generator
- [ ] AI Twitter/X Thread Writer
- [ ] AI Blog Post Outliner
- [ ] API rate limiting and usage dashboard
- [ ] Shareable result links

Want a specific tool? [Open an issue](https://github.com/acunningham-ship-it/free-ai-tools/issues) and let me know!

---

## Contributing

Got ideas? Found a bug? Want to add a tool?

1. Fork this repo
2. Open an issue describing what you want to build
3. Submit a PR

The n8n workflow pattern is simple and repeatable:
1. Create a **Webhook node** (GET for landing page, POST for API)
2. Add an **AI Agent + OpenAI Chat Model** node with your system prompt
3. Add a **Code node** to format the response
4. Add a **Respond to Webhook node** to return the result

All contributions are welcome!

---

## License

MIT License -- Use these tools however you want. See [LICENSE](./LICENSE) for details.

---

<p align="center">
  <strong>Built with determination by <a href="https://github.com/acunningham-ship-it">Armani</a>, a 17-year-old developer</strong>
  <br/>
  <sub>Part of a 24-hour coding challenge. Ship fast, help people, make cool things.</sub>
</p>

<p align="center">
  <a href="https://crazeemedia.app.n8n.cloud/webhook/ai-tools"><strong>Try the tools now</strong></a>
  &nbsp;|&nbsp;
  <a href="https://ko-fi.com/armanidev"><strong>Support me</strong></a>
  &nbsp;|&nbsp;
  <a href="https://github.com/acunningham-ship-it/free-ai-tools/issues"><strong>Request a tool</strong></a>
</p>
