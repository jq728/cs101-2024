def count_entities(sentences):
    entity_count = 0
    for sentence in sentences:
        words = sentence.split()
        i = 0
        while i < len(words):
            if words[i].startswith("###") and words[i].endswith("###"):
                entity_count += 1
                while i < len(words) and words[i].startswith("###") and words[i].endswith("###"):
                    i += 1
            else:
                i += 1
    return entity_count
N = int(input())
sentences = [input() for _ in range(N)]
print(count_entities(sentences))