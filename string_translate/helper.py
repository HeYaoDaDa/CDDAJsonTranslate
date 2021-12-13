from gettext import NullTranslations


def my_gettext(translation:NullTranslations, message:str, context:str = None):
    if context:
        return translation.pgettext(context, message)
    else:
        return translation.gettext(message)


def translate_any(translation:NullTranslations, message:str, context:str = None):
    if type(message) is list:
        for i in range(len(message)):
            message[i] = translate_any(translation, message[i], context)
    elif type(message) is dict:
        if "ctxt" in message:
            context = message["ctxt"]

        if "str_pl" in message:
            message["str_pl"] = my_gettext(translation, message["str_pl"], context)

        if "str" in message:
            message["str"] = my_gettext(translation, message["str"], context)
        elif "str_sp" in message:
            message["str_sp"] = my_gettext(translation, message["str_sp"], context)
        else:
            raise Exception("ERROR: 'str' or 'str_sp' not found", message)
    elif type(message) is str:
        message = my_gettext(translation, message, context)
    elif type(message) is int:
        pass
    elif message is None:
        pass
    else:
        print("WARN: translate value is not a string, dict, list, int or None. {}".format(message))
    return message