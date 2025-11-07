from typing import Any

from task.tools.users.base import BaseUserServiceTool
from task.tools.users.models.user_info import UserUpdate


class UpdateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        # TODO: Provide tool name as `update_user`
        return 'update_user'

    @property
    def description(self) -> str:
        # TODO: Provide description of this tool
        return 'Tool for user update'

    @property
    def input_schema(self) -> dict[str, Any]:
        # TODO:
        # Provide tool params Schema:
        # - id: number, required, User ID that should be updated.
        # - new_info: UserUpdate.model_json_schema()
        json_schema = UserUpdate.model_json_schema()
        print(f'UserUpdate json_schema: {json_schema}')

        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number",
                    "description": "User ID that should be updated"
                },
                'new_info': json_schema
            },
            "required": ['id']
        }

    def execute(self, arguments: dict[str, Any]) -> str:
        # TODO:
        # 1. Get user `id` from `arguments`
        # 2. Get `new_info` from `arguments` and create `UserUpdate` via pydentic `UserUpdate.model_validate`
        # 3. Call user_client update_user and return its results
        # 4. Optional: You can wrap it with `try-except` and return error as string `f"Error while creating a new user: {str(e)}"`
        try:
            user_id = arguments['id']
            new_info = arguments['new_info']
            update_model = UserUpdate.model_validate(new_info)
            return self._user_client.update_user(user_id, update_model)
        except Exception as e:
            return f"Error while creating a new user: {str(e)}"
