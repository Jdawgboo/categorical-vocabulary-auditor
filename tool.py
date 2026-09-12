def audit(values: list[str], allowed: set[str]) -> dict[str,list[str]]:
    observed=set(values)
    return {'unexpected':sorted(observed-allowed),'unused_allowed':sorted(allowed-observed)}
