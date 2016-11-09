def process(api, data):
	# FIXME
    submission_count = api.problem.count_submissions(pid=data["pid"], tid=data["tid"], eligibility=True)
    return submission_count == 10, {}