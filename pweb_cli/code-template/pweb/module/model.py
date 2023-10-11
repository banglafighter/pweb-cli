from pweb_orm import PwebModel, pweb_orm


class ___MODEL_NAME___(PwebModel):
    name = pweb_orm.Column("name", pweb_orm.String(150), nullable=False)
