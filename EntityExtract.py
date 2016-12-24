from watson_developer_cloud import AlchemyLanguageV1


def entity_extract_main(synopsis):
    alchemy_language = AlchemyLanguageV1(api_key='c549f5cd7c309fca1cec8e1f725a30a74f34da0f')
    keywords = []
    keywords_alchemy = alchemy_language.combined(text=synopsis, max_items=5, extract='keywords')['keywords']
    print(keywords_alchemy)
    for i in range(0, len(keywords_alchemy)):
        keywords.append(keywords_alchemy[i]['text'])
    return keywords
