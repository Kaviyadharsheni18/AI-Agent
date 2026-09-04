from tools import tool_mapping


class Agent:

    def __init__(self):
        self.tools = tool_mapping

    def llm_decide(self, user_query):

        query = user_query.lower()

        if "columns" in query:
            return {
                "name": "get_columns",
                "arguments": {
                    "file_path": "data.csv"
                }
            }

        elif "average salary" in query:
            return {
                "name": "get_average_salary",
                "arguments": {
                    "file_path": "data.csv"
                }
            }

        elif "summary" in query:
            return {
                "name": "get_summary",
                "arguments": {
                    "file_path": "data.csv"
                }
            }

        elif "read" in query:
            return {
                "name": "read_csv",
                "arguments": {
                    "file_path": "data.csv"
                }
            }

        return None

    def execute_tool(self, tool_call):

        tool_name = tool_call["name"]
        arguments = tool_call["arguments"]

        if tool_name not in self.tools:
            return "Tool not found"

        function = self.tools[tool_name]

        result = function(**arguments)

        return result

    def generate_answer(self, user_query, result):

        return f"Analysis result:\n{result}"

    def run(self, user_query):

        tool_call = self.llm_decide(user_query)

        if tool_call is None:
            return "I don't know which tool to use."

        print("\nTool selected:", tool_call["name"])

        result = self.execute_tool(tool_call)

        print("Tool result:", result)

        answer = self.generate_answer(
            user_query,
            result
        )

        return answer