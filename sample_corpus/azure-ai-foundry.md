# Azure AI Foundry — Getting Started

Topic: Azure AI Foundry
Tags: azure, foundry, agents, openai

## Key points
- Azure AI Foundry is the hub for building, evaluating, and deploying generative AI apps and agents.
- Projects group models, prompts, evaluations, and connections (OpenAI, search, storage).
- Prefer managed identity + Key Vault for secrets; never embed keys in prompts or notebooks.
- Use prompt flow / evaluations early: faithfulness, groundedness, and safety filters.
- Model catalog lets you compare GPT, Phi, Llama and route by latency/cost.

## Clip notes
Reel covered: creating a Foundry project, deploying a chat model, and running a simple eval set.
Common mistake: treating Foundry as "just ChatGPT in Azure" — it's an ops + eval surface.
