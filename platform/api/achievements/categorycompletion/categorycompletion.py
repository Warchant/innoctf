def process(api, data):
    pid = data["pid"]
    pid_map = api.stats.get_pid_categories()
    category = pid_map[pid]
    category_pids = api.stats.get_pids_by_category()[category]
    solved_pids = api.problem.get_solved_pids(tid=data['tid'])

    earned = True
    for pid in category_pids:
        if pid not in solved_pids:
            earned = False

    name = "Category Master"
    if category == "Crypto":
        name = "Sons of Bruce Schneier"
        image = "/img/achievements/categorycompletion-crypto.png"
    elif category == "Reverse":
        name = "Gods of reverse"
        image = "/img/achievements/categorycompletion-reverse.png"
    elif category == "PWN":
        name = "My little PWNy"
        image = "/img/achievements/categorycompletion-pwn.png"
    elif category == "Forensics":
        name = "Great Detectives"
        image = "/img/achievements/categorycompletion-forensics.jpeg"
    elif category == "Web":
        name = "Pentesters"
        image = "/img/achievements/categorycompletion-web.png"
    elif category == "Steganography":
        name = "Nothing remains hidden"
        image = "/img/achievements/categorycompletion-stegano.png"
    elif category == "Joy":
        name = "Enjoyable"
        image = "/img/achievements/categorycompletion-joy.png"
    elif category == "PPC":
        name = "Crazy coders"
        image = "/img/achievements/categorycompletion-ppc.jpg"
    elif category == "Recon":
        name = "Nice googling skills"
        image = "/img/achievements/categorycompletion-recon.png"
    elif category == "Admin":
        name = "Beardyteam"
        image = "/img/achievements/categorycompletion-admin.png"
    elif category == "Misc":
        name = "Anykeyteam"
        image = "/img/achievements/categorycompletion-misc.png"

    '''
    Categories:
    Admin
    Recon
    Joy
    PPC
    Crypto
    Steganography
    PWN
    Web
    Forensics
    Misc
    Reverse
    '''

    description = "Вы решили каждое задание в категории '%s'" % category
    return earned, {"name": name, "description": description, "image": image}
