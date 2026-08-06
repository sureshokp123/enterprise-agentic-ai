from mcp.server.mcpserver import MCPServer

server = MCPServer("demo")

print(type(server))
print("\nAvailable methods:\n")

for name in dir(server):
    if not name.startswith("_"):
        print(name)