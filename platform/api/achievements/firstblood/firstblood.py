def process(api, data):
    submission_count = api.problem.count_submissions(correctness=True, eligibility=True)
    return submission_count == 1, {}