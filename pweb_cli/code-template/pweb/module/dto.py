from pweb import PWebRestDTO, fields


class ___DTO_NAME___DTO(PWebRestDTO):
    name = fields.String(required=True, error_messages={"required": "Please enter name"})
