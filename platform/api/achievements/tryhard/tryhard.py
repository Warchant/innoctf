def process(api, data):
    submission_count = api.problem.count_submissions(tid=data["tid"], eligibility=True)
    return submission_count == 10, {}