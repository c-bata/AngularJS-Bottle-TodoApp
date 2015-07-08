task_schema = {
    "name": "Tasks",
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "minLength": 1,
            "maxLength": 100
        },
        "memo": {
            "type": "string",
            "minLength": 1,
        },
        "done": {
            "type": "boolean",
        },
    },
    "required": ["title"],
}
