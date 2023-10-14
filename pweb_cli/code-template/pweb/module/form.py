from pweb import PWebForm, fields


class ___FORM_NAME___Form(PWebForm):
    name = fields.String(required=True, error_messages={"required": "Please enter name"})
