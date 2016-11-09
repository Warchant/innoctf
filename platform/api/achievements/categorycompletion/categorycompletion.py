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
    elif category == "Reverse":
        name = "Gods of reverse"
    elif category == "PWN":
        name = "My little PWNy"
    elif category == "Forensics":
        name = "Great Detectives"
    elif category == "Web":
        name = "Pentesters"
    elif category == "Stego":
        name = "Nothing remains hidden"
    elif category == "Joy":
        name = "Enjoyable"
	elif category == "PPC":
        name = "Crazy coders"
	elif category == "Recon":
        name = "Nice googling skills"

    description = "Solved every '%s' challenge" % category
    return earned, {"name": name, "description": description}
