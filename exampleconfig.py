from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 3082893
    API_HASH = "5850a6f672ab5bdb1467f9c57bd1d46f"
    # the name to display in your alive message
    ALIVE_NAME = "Tabah_Rs"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://qzievucc:gJPrP4_QCBClOaN9gACwlyEdzvj2KWn6@satao.db.elephantsql.com/qzievucc"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1BVtsOKQBuw8l0clWkg__vSQG9E89tC7wcoIc13dKovfE-ReyRdoiQD7OI2-f8yznmi9ugCRyRyn6Q2w6xkh_xlYnWn3bCj7WcdNL3TDh6XuLHbujs9XDFacCxUZQDtJY5kczAVSI6QSp0g8BTKpZnx2lcaaDjIXcY7ZOWkv1mINuqveo-FMgaQKSDflyDsbyVb67QvUYtqNomTX1yTnqc3Q6nVj6hcJgZ1KEhbTrd5RF_vcxgnOyWk0nJEapB5NFhUTdgd20mZJZxmLtuwxMl_h321VEak00WVK1bvaPky9nSyAfJeGMCbOlRvKxbhmvkBZxUvv3rM3E00JM6SezSL_QQQrlhqQ="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "2140897780:AAEiqwGdxBPeOT_m_GL0tNNm0ByeeU5YJi8"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001793515147
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
