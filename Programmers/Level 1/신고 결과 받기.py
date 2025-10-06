def solution(ids, reports, k):
    reported_counts = {id: 0 for id in ids}
    report_ids = {id: set() for id in ids}

    for report in reports:
        reporter_id, reported_id = report.split()

        if reported_id not in report_ids[reporter_id]:
            reported_counts[reported_id] += 1
            report_ids[reporter_id].add(reported_id)

    suspended_ids = set(id for id, count in reported_counts.items() if count >= k)
    answer = [len(suspended_ids) - len(suspended_ids - ids) for ids in report_ids.values()]

    return answer