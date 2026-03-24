def classify(r):
    if r > 0.7:
        return 'pre-boundary'
    elif r > 0.3:
        return 'boundary-zone'
    else:
        return 'post-boundary'
