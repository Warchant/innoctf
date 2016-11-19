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
        image = "categorycompletion-crypto.png"

    elif category == "Reverse":
        name = "Gods of reverse"
        image = "categorycompletion-reverse.png"

    elif category == "PWN":
        name = "My little PWNy"
        image = "categorycompletion-pwn.png"

    elif category == "Forensics":
        name = "Great Detectives"
        image = "categorycompletion-forensics.jpeg"

    elif category == "Web":
        name = "Pentesters"
        image = "categorycompletion-web.png"

    elif category == "Steganography":
        name = "Nothing remains hidden"
        image = "categorycompletion-stegano.png"

    elif category == "Joy":
        name = "Enjoyable"
        image = "categorycompletion-joy.png"

    elif category == "PPC":
        name = "Crazy coders"
        image = "categorycompletion-ppc.jpg"

    elif category == "Recon":
        name = "Nice googling skills"
        image = "categorycompletion-recon.png"

    elif category == "Misc":
        name = "Anykeyteam"
        image = "categorycompletion-misc.png"

    big = "/img/achievements/" + image
    description = "Вы решили каждое задание в категории '%s'" % category
    return earned, {"name": name, "description": description, "image": big}
