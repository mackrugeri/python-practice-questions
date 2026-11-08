
from collections import defaultdict

def deployment_order(services, dependencies):
    graph = defaultdict(list)
    indegree = {s: 0 for s in services}

    for service, dependency in set(dependencies):
        graph[dependency].append(service)
        indegree[service] += 1

    queue = [s for s in services if indegree[s] == 0]
    result = []
    index = 0

    while index < len(queue):
        service = queue[index]
        index += 1

        result.append(service)

        for next_service in graph[service]:
            indegree[next_service] -= 1

            if indegree[next_service] == 0:
                queue.append(next_service)

    if len(result) != len(services):
        return {"possible": False, "order": []}

    return {"possible": True, "order": result}


services = ["auth", "database", "payment", "notification", "api", "frontend"]

dependencies = [
    ("auth", "database"),
    ("payment", "auth"),
    ("payment", "database"),
    ("notification", "database"),
    ("api", "payment"),
    ("api", "notification"),
    ("frontend", "api")
]

print(deployment_order(services, dependencies))
