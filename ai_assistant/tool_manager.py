from google.genai import types

#this function is used to convert MCP tools into Gemini Function Declarations
def convert_mcp_tools(mcp_tools):
    """
    Convert MCP tools into Gemini Function Declarations.
    """

    gemini_tools = []

    for tool in mcp_tools:
        gemini_tools.append(
            types.FunctionDeclaration(
                name=tool.name,
                description=tool.description or "",
                parameters=tool.inputSchema,
            )
        )

    return gemini_tools