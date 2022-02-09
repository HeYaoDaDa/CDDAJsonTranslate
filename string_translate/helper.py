from gettext import NullTranslations

def my_gettext(translation:NullTranslations, context, single, plural=None):
    if context:
        if not plural:
            text = translation.pgettext(context, single)
        if plural or text == single:
            text = translation.npgettext(context, single, plural, 1)
    else:
        if not single:
            return ''
        if not plural:
            text = translation.gettext(single)
        if plural or text == single:
            text = translation.ngettext(single, plural, 1)
    return text

def translate_any(translation:NullTranslations, message:any, context:str = None):
    if type(message) is list:
        for i in range(len(message)):
            message[i] = translate_any(translation, message[i], context)
    elif type(message) is dict:
        if "ctxt" in message:
            context = message["ctxt"]

        if "str_pl" in message:
            message["str_pl"] = my_gettext(translation, context, message["str_pl"], message["str_pl"])

        if "str" in message:
            message["str"] = my_gettext(translation, context, message["str"])
        elif "str_sp" in message:
            message["str_sp"] = my_gettext(translation, context, message["str_sp"], message["str_sp"])
        else:
            raise Exception("ERROR: 'str' or 'str_sp' not found", message)
    elif type(message) is str:
        message = my_gettext(translation, context, message)
    elif type(message) is int:
        pass
    elif message is None:
        pass
    else:
        print("WARN: translate value is not a string, dict, list, int or None. {}".format(message))
    return message