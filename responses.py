def msg_hndler(input_msg) ->str:
    input_msg= str(input_msg).lower()
    if input_msg in ("hello","hi","wassup") :

        return "hello ,how's it going"
    elif input_msg in ("good morning","gm"):
        return "good morning "
    elif input_msg in ("goodnight","gn"):
        return "good night..sleep tight"

    else:
        return "idk"

