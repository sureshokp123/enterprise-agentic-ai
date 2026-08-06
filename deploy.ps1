docker build -t mcp-ai-agent .
docker tag mcp-ai-agent:latest sureshdocker-hnbwfchra7gtezhj.azurecr.io/mcp-ai-agent:v1
docker push sureshdocker-hnbwfchra7gtezhj.azurecr.io/mcp-ai-agent:v1
az webapp restart --resource-group rg-genai-learning --name mcp-ai-agent-suresh