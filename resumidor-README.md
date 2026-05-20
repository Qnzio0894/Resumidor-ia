# Resumidor con IA

A Python script that uses the Anthropic API to summarize any text from the command line.

## What it does

You paste or type any text into the terminal, press Enter twice, and the script returns a clear and concise summary powered by Claude AI.

## Demo

```
=== RESUMIDOR CON IA ===
Pegá o escribí el texto que querés resumir.
Cuando termines, presioná Enter dos veces.

> La inteligencia artificial está transformando la manera en que trabajamos...

Generando resumen...

RESUMEN:
La IA está revolucionando múltiples sectores, pero plantea desafíos sobre
empleo y privacidad que requieren regulación responsable.
```

## Tech stack

- Python 3.10+
- [Anthropic API](https://www.anthropic.com) — Claude AI model
- `python-dotenv` — for secure API key management

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/Qnzio0894/resumidor-ia.git
cd resumidor-ia
```

**2. Install dependencies**
```bash
pip3 install anthropic python-dotenv
```

**3. Create a `.env` file in the root folder**
```
ANTHROPIC_API_KEY=your_api_key_here
```

You can get an API key at [console.anthropic.com](https://console.anthropic.com)

**4. Run the script**
```bash
python3 resumidor.py
```

## Project structure

```
resumidor-ia/
├── resumidor.py      # Main script
├── .gitignore        # Excludes .env from version control
└── README.md         # This file
```

## About

Built by [Diego González Caselli](https://github.com/Qnzio0894) as part of a dev portfolio.
This project demonstrates Python scripting, REST API integration, prompt engineering,
and secure credential management.
