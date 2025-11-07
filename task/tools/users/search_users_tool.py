from typing import Any

from task.tools.users.base import BaseUserServiceTool


class SearchUsersTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        # TODO: Provide tool name as `search_users`
        return 'search_users'

    @property
    def description(self) -> str:
        # TODO: Provide description of this tool
        return 'Tool for searching multiple users'

    @property
    def input_schema(self) -> dict[str, Any]:
        # TODO:
        # Provide tool params Schema:
        # - name: str
        # - surname: str
        # - email: str
        # - gender: str
        # None of them are required (see UserClient.search_users method)
        return {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "User name",
                },
                "surname": {
                    "type": "string",
                    "description": "User surname",
                },
                "email": {
                    "type": "string",
                    "description": "User email",
                },
                "gender": {
                    "type": "string",
                    "description": "User gender",
                }
            },
            "required": []
        }

    def execute(self, arguments: dict[str, Any]) -> str:
        # TODO:
        # 1. Call user_client search_users (with `**arguments`) and return its results
        # 2. Optional: You can wrap it with `try-except` and return error as string `f"Error while searching users: {str(e)}"`
        try:
            return self._user_client.search_users(**arguments)
        except Exception as e:
            return f"Error while searching users: {str(e)}"
